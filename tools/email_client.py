"""
E-postverktøy for Sifab — Microsoft 365 via Graph API

Bruk:
    py tools/email_client.py login          — Logg inn (første gang)
    py tools/email_client.py inbox          — Vis siste 10 e-poster
    py tools/email_client.py inbox 20       — Vis siste 20 e-poster
    py tools/email_client.py read <id>      — Les en bestemt e-post
    py tools/email_client.py send <til> <emne> <melding>  — Send e-post
    py tools/email_client.py search <søkeord>             — Søk i e-post
"""

import sys
import os
import json
import msal
import requests
from pathlib import Path
from dotenv import load_dotenv

sys.stdout.reconfigure(encoding='utf-8', errors='replace')

# Load config
load_dotenv(Path(__file__).parent.parent / '.env')
CLIENT_ID = os.getenv('AZURE_CLIENT_ID')
TENANT_ID = os.getenv('AZURE_TENANT_ID')
EMAIL = os.getenv('EMAIL_ADDRESS')

AUTHORITY = f"https://login.microsoftonline.com/{TENANT_ID}"
SCOPES = ["Mail.Read", "Mail.Send"]
TOKEN_CACHE_FILE = Path(__file__).parent.parent / '.token_cache.json'
GRAPH_URL = "https://graph.microsoft.com/v1.0"


def get_cache():
    cache = msal.SerializableTokenCache()
    if TOKEN_CACHE_FILE.exists():
        cache.deserialize(TOKEN_CACHE_FILE.read_text())
    return cache


def save_cache(cache):
    if cache.has_state_changed:
        TOKEN_CACHE_FILE.write_text(cache.serialize())


def get_app(cache=None):
    return msal.PublicClientApplication(
        CLIENT_ID,
        authority=AUTHORITY,
        token_cache=cache
    )


def get_token():
    cache = get_cache()
    app = get_app(cache)

    accounts = app.get_accounts()
    if accounts:
        result = app.acquire_token_silent(SCOPES, account=accounts[0])
        if result and 'access_token' in result:
            save_cache(cache)
            return result['access_token']

    # Device code flow
    flow = app.initiate_device_flow(scopes=SCOPES)
    if 'user_code' not in flow:
        print(f"Feil: {flow.get('error_description', 'Ukjent feil')}")
        sys.exit(1)

    print(f"\n{'='*60}")
    print(f"  Åpne: {flow['verification_uri']}")
    print(f"  Skriv inn kode: {flow['user_code']}")
    print(f"{'='*60}\n")

    result = app.acquire_token_by_device_flow(flow)
    if 'access_token' in result:
        save_cache(cache)
        print(f"Logget inn som {result.get('id_token_claims', {}).get('preferred_username', EMAIL)}")
        return result['access_token']
    else:
        print(f"Innlogging feilet: {result.get('error_description', 'Ukjent feil')}")
        sys.exit(1)


def api_get(endpoint, token, params=None):
    headers = {"Authorization": f"Bearer {token}"}
    r = requests.get(f"{GRAPH_URL}{endpoint}", headers=headers, params=params)
    if r.status_code == 401:
        print("Token utløpt — kjør 'login' på nytt.")
        sys.exit(1)
    r.raise_for_status()
    return r.json()


def api_post(endpoint, token, data):
    headers = {
        "Authorization": f"Bearer {token}",
        "Content-Type": "application/json"
    }
    r = requests.post(f"{GRAPH_URL}{endpoint}", headers=headers, json=data)
    if r.status_code == 401:
        print("Token utløpt — kjør 'login' på nytt.")
        sys.exit(1)
    r.raise_for_status()
    return r


def cmd_login():
    get_token()
    print("Innlogging vellykket!")


def cmd_inbox(count=10):
    token = get_token()
    data = api_get("/me/messages", token, params={
        "$top": count,
        "$orderby": "receivedDateTime desc",
        "$select": "id,subject,from,receivedDateTime,isRead,bodyPreview"
    })

    msgs = data.get('value', [])
    if not msgs:
        print("Ingen e-poster funnet.")
        return

    print(f"\n{'#':>3}  {'Dato':10}  {'Fra':30}  {'Emne'}")
    print("-" * 90)
    for i, m in enumerate(msgs, 1):
        date = m['receivedDateTime'][:10]
        sender = m.get('from', {}).get('emailAddress', {}).get('name', 'Ukjent')[:30]
        subj = m.get('subject', '(ingen emne)')[:50]
        read_mark = " " if m.get('isRead') else "*"
        print(f"{i:>3}{read_mark} {date}  {sender:30}  {subj}")

    print(f"\nBruk 'read <nr>' for å lese en e-post (f.eks. 'read 1')")

    # Store message IDs for easy reference
    id_map = {str(i): m['id'] for i, m in enumerate(msgs, 1)}
    (Path(__file__).parent.parent / '.last_inbox.json').write_text(json.dumps(id_map))


def cmd_read(msg_ref):
    token = get_token()

    # Check if it's a number reference from inbox
    id_map_file = Path(__file__).parent.parent / '.last_inbox.json'
    if msg_ref.isdigit() and id_map_file.exists():
        id_map = json.loads(id_map_file.read_text())
        msg_id = id_map.get(msg_ref, msg_ref)
    else:
        msg_id = msg_ref

    data = api_get(f"/me/messages/{msg_id}", token, params={
        "$select": "subject,from,toRecipients,ccRecipients,receivedDateTime,body,hasAttachments"
    })

    print(f"\n{'='*70}")
    print(f"  Emne:  {data.get('subject', '(ingen emne)')}")
    sender = data.get('from', {}).get('emailAddress', {})
    print(f"  Fra:   {sender.get('name', '')} <{sender.get('address', '')}>")

    to_list = [r['emailAddress']['address'] for r in data.get('toRecipients', [])]
    print(f"  Til:   {', '.join(to_list)}")

    cc_list = [r['emailAddress']['address'] for r in data.get('ccRecipients', [])]
    if cc_list:
        print(f"  Kopi:  {', '.join(cc_list)}")

    print(f"  Dato:  {data.get('receivedDateTime', '')[:19].replace('T', ' ')}")
    if data.get('hasAttachments'):
        print(f"  Vedlegg: Ja")
    print(f"{'='*70}\n")

    # Extract text from HTML body
    body = data.get('body', {})
    if body.get('contentType') == 'html':
        import re
        text = re.sub(r'<[^>]+>', '', body.get('content', ''))
        text = re.sub(r'\n\s*\n', '\n\n', text).strip()
        print(text[:3000])
    else:
        print(body.get('content', '(tom)')[:3000])


def cmd_send(to, subject, body, cc=None, attachments=None):
    import base64
    token = get_token()

    html_body = text_to_html(body)

    message = {
        "message": {
            "subject": subject,
            "body": {
                "contentType": "HTML",
                "content": html_body
            },
            "toRecipients": [
                {"emailAddress": {"address": addr.strip()}} for addr in to.split(",")
            ]
        },
        "saveToSentItems": True
    }

    if cc:
        message["message"]["ccRecipients"] = [
            {"emailAddress": {"address": addr.strip()}} for addr in cc.split(",")
        ]

    if attachments:
        att_list = []
        for filepath in attachments:
            p = Path(filepath)
            if not p.exists():
                print(f"Vedlegg ikke funnet: {filepath}")
                continue
            content = base64.b64encode(p.read_bytes()).decode('utf-8')
            att_list.append({
                "@odata.type": "#microsoft.graph.fileAttachment",
                "name": p.name,
                "contentBytes": content
            })
        if att_list:
            message["message"]["attachments"] = att_list

    api_post("/me/sendMail", token, message)
    print(f"E-post sendt til {to}: \"{subject}\"")


def cmd_search(query, count=20):
    token = get_token()

    # Search inbox
    data = api_get("/me/messages", token, params={
        "$search": f'"{query}"',
        "$top": count,
        "$select": "id,subject,from,receivedDateTime,bodyPreview"
    })
    msgs = data.get('value', [])

    # Also search deleted items
    try:
        deleted = api_get("/me/mailFolders/deleteditems/messages", token, params={
            "$search": f'"{query}"',
            "$top": count,
            "$select": "id,subject,from,receivedDateTime,bodyPreview"
        })
        deleted_msgs = deleted.get('value', [])
        for m in deleted_msgs:
            m['_deleted'] = True
        msgs.extend(deleted_msgs)
    except Exception:
        pass  # Deleted items search may not be available

    if not msgs:
        print(f"Ingen treff for \"{query}\".")
        return

    # Sort by date descending
    msgs.sort(key=lambda m: m.get('receivedDateTime', ''), reverse=True)

    print(f"\nSøk: \"{query}\" — {len(msgs)} treff (inkl. slettede)\n")
    print(f"{'#':>3}  {'Dato':10}  {'Fra':30}  {'Emne'}")
    print("-" * 90)
    for i, m in enumerate(msgs, 1):
        date = m['receivedDateTime'][:10]
        sender = m.get('from', {}).get('emailAddress', {}).get('name', 'Ukjent')[:30]
        deleted_tag = " [SLETTET]" if m.get('_deleted') else ""
        subj = m.get('subject', '(ingen emne)')[:50 - len(deleted_tag)] + deleted_tag
        print(f"{i:>3}  {date}  {sender:30}  {subj}")

    id_map = {str(i): m['id'] for i, m in enumerate(msgs, 1)}
    (Path(__file__).parent.parent / '.last_inbox.json').write_text(json.dumps(id_map))


def cmd_attachments(msg_ref, download_dir=None):
    """List and download attachments from an email."""
    token = get_token()

    # Resolve message ID
    id_map_file = Path(__file__).parent.parent / '.last_inbox.json'
    if msg_ref.isdigit() and id_map_file.exists():
        id_map = json.loads(id_map_file.read_text())
        msg_id = id_map.get(msg_ref, msg_ref)
    else:
        msg_id = msg_ref

    data = api_get(f"/me/messages/{msg_id}/attachments", token)
    attachments = data.get('value', [])

    if not attachments:
        print("Ingen vedlegg funnet.")
        return

    if download_dir is None:
        download_dir = Path(__file__).parent.parent / 'downloads'
    else:
        download_dir = Path(download_dir)
    download_dir.mkdir(parents=True, exist_ok=True)

    import base64
    for att in attachments:
        name = att.get('name', 'ukjent')
        size = att.get('size', 0)
        print(f"  Vedlegg: {name} ({size:,} bytes)")

        if att.get('@odata.type') == '#microsoft.graph.fileAttachment':
            content = base64.b64decode(att['contentBytes'])
            filepath = download_dir / name
            filepath.write_bytes(content)
            print(f"  -> Lagret: {filepath}")


def text_to_html(text):
    """Convert plain text to clean HTML email body."""
    import html as html_mod
    paragraphs = text.strip().split('\n\n')
    html_parts = []
    for para in paragraphs:
        lines = para.strip().split('\n')
        escaped = [html_mod.escape(line) for line in lines]
        html_parts.append('<p style="margin:0 0 10px 0;font-family:Calibri,Arial,sans-serif;font-size:11pt;">' + '<br>'.join(escaped) + '</p>')
    return ''.join(html_parts)


def cmd_forward(msg_ref, to, comment):
    """Forward an email (with attachments) to a new recipient."""
    token = get_token()

    # Resolve message ID
    id_map_file = Path(__file__).parent.parent / '.last_inbox.json'
    if msg_ref.isdigit() and id_map_file.exists():
        id_map = json.loads(id_map_file.read_text())
        msg_id = id_map.get(msg_ref, msg_ref)
    else:
        msg_id = msg_ref

    html_comment = text_to_html(comment)

    data = {
        "comment": html_comment,
        "toRecipients": [
            {"emailAddress": {"address": to}}
        ]
    }

    api_post(f"/me/messages/{msg_id}/forward", token, data)
    print(f"E-post videresendt til {to}")


if __name__ == "__main__":
    if len(sys.argv) < 2:
        print(__doc__)
        sys.exit(0)

    cmd = sys.argv[1].lower()

    if cmd == "login":
        cmd_login()
    elif cmd == "inbox":
        count = int(sys.argv[2]) if len(sys.argv) > 2 else 10
        cmd_inbox(count)
    elif cmd == "read":
        if len(sys.argv) < 3:
            print("Bruk: read <nr eller id>")
            sys.exit(1)
        cmd_read(sys.argv[2])
    elif cmd == "send":
        if len(sys.argv) < 5:
            print("Bruk: send <til> <emne> <melding> [--attachment <fil>]...")
            sys.exit(1)
        # Parse --attachment flags
        args = sys.argv[2:]
        att_files = []
        remaining = []
        i = 0
        while i < len(args):
            if args[i] == "--attachment" and i + 1 < len(args):
                att_files.append(args[i + 1])
                i += 2
            else:
                remaining.append(args[i])
                i += 1
        to_addr = remaining[0]
        subj = remaining[1]
        msg_body = " ".join(remaining[2:])
        cmd_send(to_addr, subj, msg_body, attachments=att_files if att_files else None)
    elif cmd == "attachments":
        if len(sys.argv) < 3:
            print("Bruk: attachments <nr eller id>")
            sys.exit(1)
        cmd_attachments(sys.argv[2])
    elif cmd == "forward":
        if len(sys.argv) < 5:
            print("Bruk: forward <nr eller id> <til> <kommentar>")
            sys.exit(1)
        cmd_forward(sys.argv[2], sys.argv[3], " ".join(sys.argv[4:]))
    elif cmd == "search":
        if len(sys.argv) < 3:
            print("Bruk: search <søkeord>")
            sys.exit(1)
        cmd_search(" ".join(sys.argv[2:]))
    else:
        print(f"Ukjent kommando: {cmd}")
        print(__doc__)
