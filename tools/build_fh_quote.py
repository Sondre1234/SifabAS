#!/usr/bin/env python3
"""
Faure Herman UK Quote Generator — Sifab AS

Generates professional PDF quotes for FH trading house / spares jobs.
For larger jobs, quotes are registered in Zigma instead.

Usage:
    python tools/build_fh_quote.py                  # Generate from default data below
    python tools/build_fh_quote.py --output FILE    # Specify output path
"""

import os
import sys
import argparse
from pathlib import Path
from datetime import datetime

from reportlab.lib import colors
from reportlab.lib.pagesizes import A4
from reportlab.lib.units import mm, cm
from reportlab.lib.styles import getSampleStyleSheet, ParagraphStyle
from reportlab.lib.enums import TA_LEFT, TA_CENTER, TA_RIGHT
from reportlab.platypus import (
    SimpleDocTemplate, Table, TableStyle, Paragraph, Spacer, Image,
    HRFlowable, KeepTogether
)
from reportlab.pdfbase import pdfmetrics
from reportlab.pdfbase.ttfonts import TTFont


# --- Sifab branding colours ---
SIFAB_GREEN = colors.HexColor("#2E7D32")
SIFAB_DARK = colors.HexColor("#1B5E20")
LIGHT_GREEN = colors.HexColor("#E8F5E9")
LIGHT_GREY = colors.HexColor("#F5F5F5")
BORDER_GREY = colors.HexColor("#BDBDBD")
TEXT_DARK = colors.HexColor("#212121")
TEXT_MED = colors.HexColor("#616161")

# --- Paths ---
REPO = Path(__file__).resolve().parent.parent
LOGO_PATH = REPO / "temp_logo.jpeg"
SHARED_DRIVE = Path(os.environ.get("USERPROFILE", "")) / "OneDrive - Sifab AS" / "Dokumenter - Felles"


def build_styles():
    styles = getSampleStyleSheet()

    styles.add(ParagraphStyle(
        "QuoteTitle", parent=styles["Heading1"],
        fontSize=22, textColor=SIFAB_GREEN, spaceAfter=2 * mm,
        fontName="Helvetica-Bold"
    ))
    styles.add(ParagraphStyle(
        "SectionHead", parent=styles["Heading2"],
        fontSize=11, textColor=SIFAB_DARK, spaceBefore=4 * mm, spaceAfter=2 * mm,
        fontName="Helvetica-Bold", borderWidth=0,
        borderPadding=0, borderColor=None,
    ))
    styles.add(ParagraphStyle(
        "BodySmall", parent=styles["Normal"],
        fontSize=9, textColor=TEXT_DARK, leading=12,
        fontName="Helvetica"
    ))
    styles.add(ParagraphStyle(
        "BodySmallBold", parent=styles["Normal"],
        fontSize=9, textColor=TEXT_DARK, leading=12,
        fontName="Helvetica-Bold"
    ))
    styles.add(ParagraphStyle(
        "Footer", parent=styles["Normal"],
        fontSize=7, textColor=TEXT_MED, alignment=TA_CENTER,
        fontName="Helvetica"
    ))
    styles.add(ParagraphStyle(
        "RightAlign", parent=styles["Normal"],
        fontSize=9, textColor=TEXT_DARK, alignment=TA_RIGHT,
        fontName="Helvetica"
    ))
    styles.add(ParagraphStyle(
        "RightAlignBold", parent=styles["Normal"],
        fontSize=9, textColor=TEXT_DARK, alignment=TA_RIGHT,
        fontName="Helvetica-Bold"
    ))
    styles.add(ParagraphStyle(
        "CellDesc", parent=styles["Normal"],
        fontSize=8.5, textColor=TEXT_DARK, leading=11,
        fontName="Helvetica"
    ))
    return styles


def build_quote(quote_data: dict, output_path: str):
    """Generate a PDF quote from quote_data dict."""

    styles = build_styles()
    page_w, page_h = A4
    margin = 18 * mm

    doc = SimpleDocTemplate(
        output_path, pagesize=A4,
        leftMargin=margin, rightMargin=margin,
        topMargin=margin, bottomMargin=20 * mm,
    )

    elements = []

    # --- HEADER: Logo + Company info + Quote title ---
    # Logo — preserve native aspect ratio
    if LOGO_PATH.exists():
        from PIL import Image as PILImage
        pil_img = PILImage.open(str(LOGO_PATH))
        img_w, img_h = pil_img.size
        logo_w = 50 * mm
        logo_h = logo_w * (img_h / img_w)  # preserve aspect ratio
        logo = Image(str(LOGO_PATH), width=logo_w, height=logo_h)
    else:
        logo = Paragraph("SIFAB AS", styles["QuoteTitle"])

    company_info = Paragraph(
        "Sifab AS<br/>"
        "Bedriftsveien 20, 4313 Sandnes, Norway<br/>"
        "Tel: +47 51 97 45 00 &nbsp;|&nbsp; www.sifab.no",
        styles["BodySmall"]
    )

    quote_title = Paragraph("QUOTATION", styles["QuoteTitle"])

    header_table = Table(
        [[logo, company_info, quote_title]],
        colWidths=[55 * mm, 60 * mm, 55 * mm],
    )
    header_table.setStyle(TableStyle([
        ("VALIGN", (0, 0), (-1, -1), "MIDDLE"),
        ("ALIGN", (2, 0), (2, 0), "RIGHT"),
    ]))
    elements.append(header_table)
    elements.append(Spacer(1, 3 * mm))
    elements.append(HRFlowable(width="100%", thickness=1.5, color=SIFAB_GREEN))
    elements.append(Spacer(1, 4 * mm))

    # --- QUOTE META: two-column ---
    q = quote_data
    meta_left = [
        ["To:", q.get("client_name", "")],
        ["Attn:", q.get("client_contact", "")],
        ["", q.get("client_address", "")],
    ]
    meta_right = [
        ["Quote Ref:", q.get("quote_ref", "")],
        ["Date:", q.get("date", datetime.now().strftime("%d %B %Y"))],
        ["Your Ref:", q.get("client_ref", "")],
        ["Valid Until:", q.get("valid_until", "")],
    ]

    left_table = Table(meta_left, colWidths=[18 * mm, 65 * mm])
    left_table.setStyle(TableStyle([
        ("FONTNAME", (0, 0), (0, -1), "Helvetica-Bold"),
        ("FONTNAME", (1, 0), (1, -1), "Helvetica"),
        ("FONTSIZE", (0, 0), (-1, -1), 9),
        ("TEXTCOLOR", (0, 0), (-1, -1), TEXT_DARK),
        ("VALIGN", (0, 0), (-1, -1), "TOP"),
        ("TOPPADDING", (0, 0), (-1, -1), 1),
        ("BOTTOMPADDING", (0, 0), (-1, -1), 1),
    ]))

    right_table = Table(meta_right, colWidths=[22 * mm, 55 * mm])
    right_table.setStyle(TableStyle([
        ("FONTNAME", (0, 0), (0, -1), "Helvetica-Bold"),
        ("FONTNAME", (1, 0), (1, -1), "Helvetica"),
        ("FONTSIZE", (0, 0), (-1, -1), 9),
        ("TEXTCOLOR", (0, 0), (-1, -1), TEXT_DARK),
        ("VALIGN", (0, 0), (-1, -1), "TOP"),
        ("TOPPADDING", (0, 0), (-1, -1), 1),
        ("BOTTOMPADDING", (0, 0), (-1, -1), 1),
        ("BACKGROUND", (0, 0), (-1, -1), LIGHT_GREEN),
        ("BOX", (0, 0), (-1, -1), 0.5, SIFAB_GREEN),
        ("LEFTPADDING", (0, 0), (-1, -1), 4),
        ("RIGHTPADDING", (0, 0), (-1, -1), 4),
    ]))

    meta_table = Table(
        [[left_table, right_table]],
        colWidths=[90 * mm, 80 * mm],
    )
    meta_table.setStyle(TableStyle([
        ("VALIGN", (0, 0), (-1, -1), "TOP"),
    ]))
    elements.append(meta_table)
    elements.append(Spacer(1, 5 * mm))

    # --- SUBJECT LINE ---
    subject = q.get("subject", "")
    if subject:
        elements.append(Paragraph(f"<b>Re: {subject}</b>", styles["BodySmall"]))
        elements.append(Spacer(1, 3 * mm))

    # --- INTRO TEXT ---
    intro = q.get("intro_text", "")
    if intro:
        elements.append(Paragraph(intro, styles["BodySmall"]))
        elements.append(Spacer(1, 4 * mm))

    # --- LINE ITEMS TABLE ---
    elements.append(Paragraph("Scope of Supply", styles["SectionHead"]))

    # Header row
    col_widths = [12 * mm, 90 * mm, 12 * mm, 28 * mm, 28 * mm]
    header_row = [
        Paragraph("<b>Item</b>", styles["BodySmallBold"]),
        Paragraph("<b>Description</b>", styles["BodySmallBold"]),
        Paragraph("<b>Qty</b>", styles["BodySmallBold"]),
        Paragraph("<b>Unit Price</b>", styles["RightAlignBold"]),
        Paragraph("<b>Total</b>", styles["RightAlignBold"]),
    ]

    table_data = [header_row]
    currency = q.get("currency", "EUR")

    for item in q.get("line_items", []):
        row = [
            Paragraph(str(item["item"]), styles["BodySmall"]),
            Paragraph(item["description"], styles["CellDesc"]),
            Paragraph(str(item["qty"]), styles["BodySmall"]),
            Paragraph(f"{currency} {item['unit_price']:,.2f}", styles["RightAlign"]),
            Paragraph(f"{currency} {item['total']:,.2f}", styles["RightAlign"]),
        ]
        table_data.append(row)

    # Total row
    grand_total = q.get("grand_total", sum(i["total"] for i in q.get("line_items", [])))
    total_row = [
        "", "",
        Paragraph("", styles["BodySmall"]),
        Paragraph(f"<b>Total {q.get('incoterm', 'EXW')}:</b>", styles["RightAlignBold"]),
        Paragraph(f"<b>{currency} {grand_total:,.2f}</b>", styles["RightAlignBold"]),
    ]
    table_data.append(total_row)

    items_table = Table(table_data, colWidths=col_widths, repeatRows=1)
    items_table.setStyle(TableStyle([
        # Header
        ("BACKGROUND", (0, 0), (-1, 0), SIFAB_GREEN),
        ("TEXTCOLOR", (0, 0), (-1, 0), colors.white),
        ("FONTNAME", (0, 0), (-1, 0), "Helvetica-Bold"),
        # Alternating rows
        *[("BACKGROUND", (0, i), (-1, i), LIGHT_GREY if i % 2 == 0 else colors.white)
          for i in range(1, len(table_data) - 1)],
        # Total row
        ("BACKGROUND", (0, -1), (-1, -1), LIGHT_GREEN),
        ("LINEABOVE", (0, -1), (-1, -1), 1.2, SIFAB_GREEN),
        # Grid
        ("GRID", (0, 0), (-1, -2), 0.4, BORDER_GREY),
        ("BOX", (0, 0), (-1, -1), 0.8, SIFAB_GREEN),
        # Padding
        ("TOPPADDING", (0, 0), (-1, -1), 4),
        ("BOTTOMPADDING", (0, 0), (-1, -1), 4),
        ("LEFTPADDING", (0, 0), (-1, -1), 4),
        ("RIGHTPADDING", (0, 0), (-1, -1), 4),
        ("VALIGN", (0, 0), (-1, -1), "TOP"),
    ]))
    elements.append(items_table)
    elements.append(Spacer(1, 6 * mm))

    # --- COMMERCIAL TERMS ---
    elements.append(Paragraph("Commercial Terms", styles["SectionHead"]))

    terms = q.get("terms", [])
    terms_data = [[Paragraph(f"<b>{t[0]}</b>", styles["BodySmallBold"]),
                    Paragraph(t[1], styles["BodySmall"])] for t in terms]

    terms_table = Table(terms_data, colWidths=[35 * mm, 130 * mm])
    terms_table.setStyle(TableStyle([
        ("VALIGN", (0, 0), (-1, -1), "TOP"),
        ("TOPPADDING", (0, 0), (-1, -1), 2),
        ("BOTTOMPADDING", (0, 0), (-1, -1), 2),
        ("LINEBELOW", (0, 0), (-1, -2), 0.3, BORDER_GREY),
        ("BOX", (0, 0), (-1, -1), 0.5, BORDER_GREY),
        ("LEFTPADDING", (0, 0), (-1, -1), 4),
        ("BACKGROUND", (0, 0), (0, -1), LIGHT_GREEN),
    ]))
    elements.append(terms_table)
    elements.append(Spacer(1, 6 * mm))

    # --- PAYMENT SCHEDULE (if provided) ---
    payments = q.get("payment_schedule", [])
    if payments:
        elements.append(Paragraph("Payment Schedule", styles["SectionHead"]))
        pay_header = [
            Paragraph("<b>Payment</b>", styles["BodySmallBold"]),
            Paragraph("<b>Timing</b>", styles["BodySmallBold"]),
            Paragraph("<b>Amount</b>", styles["RightAlignBold"]),
        ]
        pay_data = [pay_header]
        for p in payments:
            pay_data.append([
                Paragraph(p[0], styles["BodySmall"]),
                Paragraph(p[1], styles["BodySmall"]),
                Paragraph(f"{currency} {p[2]:,.2f}", styles["RightAlign"]),
            ])
        # Total
        pay_data.append([
            "", Paragraph("<b>Total</b>", styles["RightAlignBold"]),
            Paragraph(f"<b>{currency} {grand_total:,.2f}</b>", styles["RightAlignBold"]),
        ])

        pay_table = Table(pay_data, colWidths=[40 * mm, 75 * mm, 45 * mm])
        pay_table.setStyle(TableStyle([
            ("BACKGROUND", (0, 0), (-1, 0), SIFAB_GREEN),
            ("TEXTCOLOR", (0, 0), (-1, 0), colors.white),
            ("GRID", (0, 0), (-1, -2), 0.4, BORDER_GREY),
            ("BOX", (0, 0), (-1, -1), 0.8, SIFAB_GREEN),
            ("BACKGROUND", (0, -1), (-1, -1), LIGHT_GREEN),
            ("LINEABOVE", (0, -1), (-1, -1), 1.2, SIFAB_GREEN),
            ("TOPPADDING", (0, 0), (-1, -1), 4),
            ("BOTTOMPADDING", (0, 0), (-1, -1), 4),
            ("LEFTPADDING", (0, 0), (-1, -1), 4),
            ("RIGHTPADDING", (0, 0), (-1, -1), 4),
            ("VALIGN", (0, 0), (-1, -1), "MIDDLE"),
        ]))
        elements.append(pay_table)
        elements.append(Spacer(1, 6 * mm))

    # --- CLOSING ---
    closing = q.get("closing_text", "")
    if closing:
        elements.append(Paragraph(closing, styles["BodySmall"]))
        elements.append(Spacer(1, 4 * mm))

    # --- SIGNATURE BLOCK ---
    sig = q.get("signature", {})
    sig_text = (
        f"<b>{sig.get('name', 'Sondre Falch')}</b><br/>"
        f"{sig.get('title', 'Manager')}<br/>"
        f"Sifab AS<br/>"
        f"Tel: {sig.get('phone', '+47 900 29 588')}<br/>"
        f"Email: {sig.get('email', 'sondre.falch@sifab.no')}"
    )
    elements.append(Paragraph(sig_text, styles["BodySmall"]))
    elements.append(Spacer(1, 8 * mm))

    # --- FOOTER ---
    elements.append(HRFlowable(width="100%", thickness=0.5, color=SIFAB_GREEN))
    elements.append(Spacer(1, 2 * mm))
    elements.append(Paragraph(
        "Sifab AS &nbsp;|&nbsp; Bedriftsveien 20, 4313 Sandnes, Norway &nbsp;|&nbsp; "
        "Org.nr: 912 408 346 &nbsp;|&nbsp; www.sifab.no<br/>"
        "Authorised Faure Herman Channel Partner — Norway &amp; UK (FHNS)",
        styles["Footer"]
    ))

    doc.build(elements)
    return output_path


# ============================================================
# DEFAULT QUOTE DATA — JCH Marine Ref 69725
# ============================================================
JCH_QUOTE = {
    "quote_ref": "FHNS-2026-001",
    "date": "26 March 2026",
    "valid_until": "25 April 2026",
    "currency": "EUR",
    "incoterm": "EXW Sandnes, Norway",

    "client_name": "JCH Marine & Offshore Supplies Ltd",
    "client_contact": "Mark Hanson, Head of Sales",
    "client_address": "JCH House, Highgate Trade Park, Stoke-on-Trent, ST6 4JZ, UK",
    "client_ref": "69725",

    "subject": "Internal Calibrated Cartridges — Turbine Meter SN 100052883 / Tag 664-FT-2104-11",

    "intro_text": (
        "Thank you for your enquiry. Sifab AS is the authorised Faure Herman channel partner "
        "for Norway and the UK. Please find below our quotation for the supply of turbine meter "
        "internals as requested."
    ),

    "line_items": [
        {
            "item": 1,
            "description": (
                "Internal calibrated cartridge for TZN 400-4000 (16\") turbine flowmeter<br/>"
                "Titanium rotor / Stainless steel internals<br/>"
                "Factory calibration at 2 viscosities (6 cSt and 11 cSt)<br/>"
                "Flow range: 500 — 3,600 m\u00b3/h<br/>"
                "Accuracy: \u00b10.15% &nbsp;|&nbsp; Repeatability: 0.04%"
            ),
            "qty": "2 pc",
            "unit_price": 87_260.00,
            "total": 174_520.00,
        },
        {
            "item": 2,
            "description": (
                "Documentation package:<br/>"
                "Certificate of Conformity, Calibration Certificates,<br/>"
                "Technical Manuals, EU Compliance Statement (if applicable)"
            ),
            "qty": "1 lot",
            "unit_price": 950.00,
            "total": 950.00,
        },
    ],

    "grand_total": 175_470.00,

    "terms": [
        ("Incoterms", "EXW Sandnes, Norway"),
        ("Delivery", "17 weeks from receipt of PO and advance payment"),
        ("Payment", "Pro forma with PO (see payment schedule below), balance 2 weeks prior to despatch"),
        ("Validity", "25 April 2026"),
        ("Warranty", "24 months from delivery (FCA)"),
        ("Currency", "EUR"),
    ],

    "payment_schedule": [
        ("Pro forma", "With Purchase Order", 147_913.00),
        ("Balance", "2 weeks prior to despatch", 27_557.00),
    ],

    "closing_text": (
        "We look forward to working with you. Please do not hesitate to contact us "
        "if you have any questions or require further information."
    ),

    "signature": {
        "name": "Sondre Falch",
        "title": "Manager",
        "phone": "+47 900 29 588",
        "email": "sondre.falch@sifab.no",
    },
}


# ============================================================
# STORM PROCUREMENT — RFQ 439464 (same meter SN 100052883)
# ============================================================
STORM_QUOTE = {
    **JCH_QUOTE,
    "quote_ref": "FHNS-2026-002",
    "client_name": "Storm Procurement",
    "client_contact": "Isabelle Tittanegro",
    "client_address": "",
    "client_ref": "RFQ 439464",

    "intro_text": (
        "Thank you for your enquiry. Sifab AS is the authorised Faure Herman channel partner "
        "for Norway and the UK. Please find below our quotation for the supply of turbine meter "
        "internals as requested."
    ),
}


# ============================================================
# UTSL — UTS Limited UK — RFQ 26Y841-NAS (B)
# 4 × FH71 preamplifiers, freight France→Sandnes baked into unit price
# ============================================================
UTSL_QUOTE = {
    "quote_ref": "FHNS-2026-003",
    "date": "27 April 2026",
    "valid_until": "27 May 2026",
    "currency": "GBP",
    "incoterm": "EXW Sandnes, Norway",

    "client_name": "UTSL — UTS Limited",
    "client_contact": "Sales Team",
    "client_address": "United Kingdom",
    "client_ref": "RFQ 26Y841-NAS (B)",

    "subject": "Faure Herman FH71 Preamplifiers — 4 off",

    "intro_text": (
        "Thank you for your enquiry. Sifab AS is the authorised Faure Herman channel partner "
        "for Norway and the United Kingdom (FHNS). Please find below our quotation for the "
        "supply of FH71 preamplifiers as requested."
    ),

    "line_items": [
        {
            "item": 1,
            "description": (
                "Faure Herman FH71 Preamplifier — Standard 2-wire version<br/>"
                "Faure Herman P/N 500090 (drawing 73 99 252)<br/>"
                "Condition: New, factory original<br/>"
                "Including: Certificate of Conformity, EU Compliance Statement, "
                "technical manuals"
            ),
            "qty": "4 pc",
            "unit_price": 550.00,
            "total": 2_200.00,
        },
    ],

    "grand_total": 2_200.00,

    "terms": [
        ("Incoterms", "EXW Sandnes, Norway"),
        ("Delivery", "6 weeks from receipt of clean Purchase Order"),
        ("Payment", "50% with Purchase Order, 50% on delivery"),
        ("Validity", "27 May 2026"),
        ("Warranty", "24 months from delivery"),
        ("Currency", "GBP"),
    ],

    "payment_schedule": [
        ("50% Advance", "With Purchase Order", 1_100.00),
        ("50% Balance", "On delivery", 1_100.00),
    ],

    "closing_text": (
        "We look forward to working with you. Please do not hesitate to contact us "
        "if you have any questions or require further information."
    ),

    "signature": {
        "name": "Sondre Falch",
        "title": "Manager",
        "phone": "+47 900 29 588",
        "email": "sondre.falch@sifab.no",
    },
}


QUOTES = {
    "jch": JCH_QUOTE,
    "storm": STORM_QUOTE,
    "utsl": UTSL_QUOTE,
}


def main():
    parser = argparse.ArgumentParser(description="Generate FH UK quote PDF")
    parser.add_argument("--output", "-o", default=None, help="Output PDF path")
    parser.add_argument("--quote", "-q", default="jch", choices=QUOTES.keys(),
                        help="Which quote to generate (default: jch)")
    parser.add_argument("--all", action="store_true", help="Generate all quotes")
    args = parser.parse_args()

    if args.all:
        for name, quote in QUOTES.items():
            ref = quote["quote_ref"]
            client_short = name.upper()
            out = str(REPO / f"{ref}_Quote_{client_short}.pdf")
            build_quote(quote, out)
            print(f"Quote generated: {out}")
    else:
        quote = QUOTES[args.quote]
        if args.output:
            out = args.output
        else:
            ref = quote["quote_ref"]
            out = str(REPO / f"{ref}_Quote_{args.quote.upper()}.pdf")
        build_quote(quote, out)
        print(f"Quote generated: {out}")


if __name__ == "__main__":
    main()
