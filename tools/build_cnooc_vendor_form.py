"""
Generate CNOOC Vendor Registration Form on Sifab AS letterhead.
Output: PDF in the correct SP project folder on shared drive.
"""

from pathlib import Path
from reportlab.lib.pagesizes import A4
from reportlab.lib.units import mm
from reportlab.lib import colors
from reportlab.platypus import SimpleDocTemplate, Table, TableStyle, Spacer, Paragraph, Image
from reportlab.lib.styles import getSampleStyleSheet, ParagraphStyle
import os

# Paths
SHARED_DRIVE = Path(os.environ['USERPROFILE']) / 'OneDrive - Sifab AS' / 'Dokumenter - Felles'
LOGO_PATH = Path(__file__).parent.parent / 'temp_logo.jpeg'
OUTPUT_DIR = Path(os.environ['USERPROFILE']) / 'OneDrive - Sifab AS' / 'Dokumenter - Felles'
OUTPUT_FILE = OUTPUT_DIR / 'CNOOC_Vendor_Registration_Sifab_AS.pdf'

# Company details
COMPANY = {
    'name': 'Sifab AS',
    'street': 'Bedriftsveien 20',
    'city': 'Sandnes',
    'region': 'Rogaland',
    'postal_code': '4313',
    'country': 'Norway',
    'remittance_email': 'post@sifab.no',
    'reg_no': '886803222',
    'vat': 'NO886803222MVA',
    'contact_name': 'Sondre Falch',
    'contact_phone': '+47 900 29 588',
    'contact_email': 'sondre.falch@sifab.no',
    'type': 'Sales',
    'government': 'No',
}

BANK = {
    'holder': 'Sifab AS',
    'bank_name': 'Rogaland Sparebank',
    'bank_address': 'Rådhusgata 3, 4306 Sandnes, Norway',
    'currency': 'EUR (GBP payments can also be accommodated — please contact us)',
    'iban': 'NO20 3260 9001 452',
    'swift': 'SASKNO22XXX',
}

SEQUAL = 'No'
SEQUAL_REG = ''
CNOOC_TC = 'Yes'

SIGNER = {
    'name': 'Sondre Falch',
    'title': 'Manager',
    'date': '2026-04-09',
}


def build_pdf():
    doc = SimpleDocTemplate(
        str(OUTPUT_FILE),
        pagesize=A4,
        leftMargin=20 * mm,
        rightMargin=20 * mm,
        topMargin=15 * mm,
        bottomMargin=15 * mm,
    )

    styles = getSampleStyleSheet()
    title_style = ParagraphStyle('FormTitle', parent=styles['Heading1'], fontSize=13,
                                  alignment=1, spaceAfter=4 * mm)
    subtitle_style = ParagraphStyle('FormSubtitle', parent=styles['Normal'], fontSize=9,
                                     alignment=1, textColor=colors.red, spaceAfter=6 * mm,
                                     fontName='Helvetica-BoldOblique')
    section_style = ParagraphStyle('Section', parent=styles['Heading2'], fontSize=10,
                                    spaceAfter=2 * mm, spaceBefore=4 * mm,
                                    underlineProportion=1)
    normal = ParagraphStyle('Normal2', parent=styles['Normal'], fontSize=9, leading=12)
    small = ParagraphStyle('Small', parent=styles['Normal'], fontSize=8, leading=10,
                           textColor=colors.HexColor('#333333'))
    footer_style = ParagraphStyle('Footer', parent=styles['Normal'], fontSize=7,
                                   alignment=1, textColor=colors.grey)
    bold_style = ParagraphStyle('Bold', parent=normal, fontName='Helvetica-Bold')
    check_yes = '[X]'
    check_no = '[  ]'

    elements = []

    # Logo
    if LOGO_PATH.exists():
        logo = Image(str(LOGO_PATH), width=45 * mm, height=18 * mm)
        logo.hAlign = 'RIGHT'
        elements.append(logo)
        elements.append(Spacer(1, 4 * mm))

    # Title
    elements.append(Paragraph('New Vendor Information Form – CNOOC Petroleum Europe Limited', title_style))
    elements.append(Paragraph('To be completed by vendor and submitted on company headed paper', subtitle_style))

    # Section A
    elements.append(Paragraph('<u>Section A: General Company Information</u>', section_style))

    section_a_data = [
        ['Vendor/Company Name (as per invoice)', COMPANY['name']],
        ['c/o (if applicable)', ''],
        ['Street', COMPANY['street']],
        ['PO Box (if applicable)', ''],
        ['City', COMPANY['city']],
        ['Region', COMPANY['region']],
        ['Postal Code', COMPANY['postal_code']],
        ['Country', COMPANY['country']],
        ['Remittance E-mail address', COMPANY['remittance_email']],
        ['Registration No.', COMPANY['reg_no']],
        ['Tax ID: GST / TIN / VAT', COMPANY['vat']],
        ['Designated Contact Name', COMPANY['contact_name']],
        ['Designated Contact Direct Telephone No.', COMPANY['contact_phone']],
        ['Designated Contact E-mail Address', COMPANY['contact_email']],
        ['Type of Company', f"Manufacturing {check_no}       Sales {check_yes}       Service {check_no}"],
    ]

    t = Table(section_a_data, colWidths=[75 * mm, 95 * mm])
    t.setStyle(TableStyle([
        ('GRID', (0, 0), (-1, -1), 0.5, colors.black),
        ('FONTNAME', (0, 0), (0, -1), 'Helvetica-Bold'),
        ('FONTNAME', (1, 0), (1, -1), 'Helvetica'),
        ('FONTSIZE', (0, 0), (-1, -1), 9),
        ('VALIGN', (0, 0), (-1, -1), 'MIDDLE'),
        ('LEFTPADDING', (0, 0), (-1, -1), 4),
        ('RIGHTPADDING', (0, 0), (-1, -1), 4),
        ('TOPPADDING', (0, 0), (-1, -1), 3),
        ('BOTTOMPADDING', (0, 0), (-1, -1), 3),
    ]))
    elements.append(t)

    # Government question
    elements.append(Spacer(1, 3 * mm))
    gov_text = (
        'CNOOC Petroleum Europe Limited ("CNOOC International") is subject to reporting under the '
        'Reports on Payments to Government Regulations 2014 directive. As such payments made to '
        'Government agencies need to be identified. Please indicate if you are a Government in the U.K '
        'or abroad, body established by two or more governments, or any trust, board, commission, '
        'corporate, body or authority that exercises a function, power or duty of any government in the '
        'U.K. or abroad.'
    )
    elements.append(Paragraph(gov_text, small))
    elements.append(Spacer(1, 2 * mm))
    elements.append(Paragraph(
        f'Does the above description apply to your company?&nbsp;&nbsp;&nbsp;'
        f'Yes {check_no}&nbsp;&nbsp;&nbsp;No {check_yes}', normal))

    # Section B
    elements.append(Spacer(1, 4 * mm))
    elements.append(Paragraph('<u>Section B: Banking Instructions</u>', section_style))
    elements.append(Paragraph(
        "CNOOC International's preference is to make payments electronically due to the lower cost "
        "and lower risk of fraud.", small))
    elements.append(Spacer(1, 2 * mm))

    section_b_data = [
        ['Name of Bank Account Holder', BANK['holder']],
        ['Bank Name', BANK['bank_name']],
        ['Bank Address', BANK['bank_address']],
        ['Currency', BANK['currency']],
        ['IBAN', BANK['iban']],
        ['SWIFT / BIC', BANK['swift']],
    ]
    t2 = Table(section_b_data, colWidths=[75 * mm, 95 * mm])
    t2.setStyle(TableStyle([
        ('GRID', (0, 0), (-1, -1), 0.5, colors.black),
        ('FONTNAME', (0, 0), (0, -1), 'Helvetica-Bold'),
        ('FONTNAME', (1, 0), (1, -1), 'Helvetica'),
        ('FONTSIZE', (0, 0), (-1, -1), 9),
        ('VALIGN', (0, 0), (-1, -1), 'MIDDLE'),
        ('LEFTPADDING', (0, 0), (-1, -1), 4),
        ('RIGHTPADDING', (0, 0), (-1, -1), 4),
        ('TOPPADDING', (0, 0), (-1, -1), 3),
        ('BOTTOMPADDING', (0, 0), (-1, -1), 3),
    ]))
    elements.append(t2)

    elements.append(Spacer(1, 2 * mm))
    elements.append(Paragraph(
        '<b>Please attach <u>one</u> of the following mandatory banking documents for back up:</b>', small))
    elements.append(Paragraph(
        '• an original pre-printed void cheque<br/>'
        '• a copy of an invoice that includes pre-printed banking details<br/>'
        '• a formal letter of banking instructions on company letterhead ← <b>ATTACHED</b><br/>'
        '• a letter, form or statement from your financial institution', small))

    # Section C
    elements.append(Spacer(1, 4 * mm))
    elements.append(Paragraph('<u>Section C: SEQUAL / CNOOC Terms &amp; Conditions</u>', section_style))

    section_c_data = [
        ['Are you SEQUAL registered?', f'Yes {check_no}    No {check_yes}'],
        ['If yes, provide your SEQUAL Reg. No.', SEQUAL_REG],
        ['CNOOC Terms & Conditions Accepted?', f'Yes {check_yes}    No {check_no}'],
    ]
    t3 = Table(section_c_data, colWidths=[75 * mm, 95 * mm])
    t3.setStyle(TableStyle([
        ('GRID', (0, 0), (-1, -1), 0.5, colors.black),
        ('FONTNAME', (0, 0), (0, -1), 'Helvetica-Bold'),
        ('FONTNAME', (1, 0), (1, -1), 'Helvetica'),
        ('FONTSIZE', (0, 0), (-1, -1), 9),
        ('VALIGN', (0, 0), (-1, -1), 'MIDDLE'),
        ('LEFTPADDING', (0, 0), (-1, -1), 4),
        ('RIGHTPADDING', (0, 0), (-1, -1), 4),
        ('TOPPADDING', (0, 0), (-1, -1), 3),
        ('BOTTOMPADDING', (0, 0), (-1, -1), 3),
    ]))
    elements.append(t3)

    # Section D
    elements.append(Spacer(1, 4 * mm))
    elements.append(Paragraph('<u>Section D: Data Collection</u>', section_style))
    dc_text = (
        'By completing this form, you consent and agree to CNOOC International and its affiliates '
        'collecting, processing, holding, storing, accessing, using, disclosing, or possessing the '
        'personal information and/or confidential information for the purposes of establishing you as '
        'a Supplier or Contractor. This information will be used as part of the Approved Supplier '
        'Status process and for payment of invoices. This information will be input into CNOOC '
        'International systems and access to the information will be limited to those who need the '
        'information to perform business functions.'
    )
    elements.append(Paragraph(dc_text, small))
    elements.append(Spacer(1, 2 * mm))
    dc_text2 = (
        'I understand that I may, at any time, request access to the information that CNOOC possesses '
        'and that I may request that this information is updated, corrected or deleted. This request '
        'must be made in writing and sent to vendoruk@intl.cnoocltd.com.'
    )
    elements.append(Paragraph(dc_text2, small))

    # Section E
    elements.append(Spacer(1, 6 * mm))
    elements.append(Paragraph('<u>Section E: Signature of Authorized Representative</u>', section_style))

    section_e_data = [
        ['Name', SIGNER['name']],
        ['Title', SIGNER['title']],
        ['Signature', ''],
        ['Date', SIGNER['date']],
    ]
    t4 = Table(section_e_data, colWidths=[75 * mm, 95 * mm])
    t4.setStyle(TableStyle([
        ('GRID', (0, 0), (-1, -1), 0.5, colors.black),
        ('FONTNAME', (0, 0), (0, -1), 'Helvetica-Bold'),
        ('FONTNAME', (1, 0), (1, -1), 'Helvetica'),
        ('FONTSIZE', (0, 0), (-1, -1), 9),
        ('VALIGN', (0, 0), (-1, -1), 'MIDDLE'),
        ('LEFTPADDING', (0, 0), (-1, -1), 4),
        ('RIGHTPADDING', (0, 0), (-1, -1), 4),
        ('TOPPADDING', (0, 0), (-1, -1), 3),
        ('BOTTOMPADDING', (0, 0), (-1, -1), 3),
    ]))
    elements.append(t4)

    # Footer
    elements.append(Spacer(1, 10 * mm))
    elements.append(Paragraph(
        'Sifab AS | Bedriftsveien 20, 4313 Sandnes, Norway | Org.nr: 886 803 222 | www.sifab.no',
        footer_style))

    doc.build(elements)
    print(f'PDF generated: {OUTPUT_FILE}')


if __name__ == '__main__':
    build_pdf()
