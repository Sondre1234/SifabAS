#!/usr/bin/env python3
"""
Maloney Quote Generator — Sifab AS
Generates professional PDF quotes for Maloney prover sphere sales.
"""

import os
import sys
from pathlib import Path

from reportlab.lib import colors
from reportlab.lib.pagesizes import A4
from reportlab.lib.units import mm
from reportlab.lib.styles import getSampleStyleSheet, ParagraphStyle
from reportlab.lib.enums import TA_LEFT, TA_CENTER, TA_RIGHT
from reportlab.platypus import (
    SimpleDocTemplate, Table, TableStyle, Paragraph, Spacer, Image,
    HRFlowable,
)

# --- Sifab branding colours ---
SIFAB_GREEN = colors.HexColor("#2E7D32")
SIFAB_DARK = colors.HexColor("#1B5E20")
LIGHT_GREEN = colors.HexColor("#E8F5E9")
LIGHT_GREY = colors.HexColor("#F5F5F5")
BORDER_GREY = colors.HexColor("#BDBDBD")
TEXT_DARK = colors.HexColor("#212121")
TEXT_MED = colors.HexColor("#616161")

REPO = Path(__file__).resolve().parent.parent
LOGO_PATH = REPO / "temp_logo.jpeg"
SHARED_DRIVE = Path(os.environ.get("USERPROFILE", "")) / "OneDrive - Sifab AS" / "Dokumenter - Felles"


def build_styles():
    styles = getSampleStyleSheet()
    styles.add(ParagraphStyle(
        "QuoteTitleLeft", parent=styles["Heading1"],
        fontSize=22, textColor=SIFAB_GREEN, spaceAfter=0,
        fontName="Helvetica-Bold", alignment=TA_LEFT,
    ))
    styles.add(ParagraphStyle(
        "SectionHead", parent=styles["Heading2"],
        fontSize=11, textColor=SIFAB_DARK, spaceBefore=4 * mm, spaceAfter=2 * mm,
        fontName="Helvetica-Bold",
    ))
    styles.add(ParagraphStyle(
        "BodySmall", parent=styles["Normal"],
        fontSize=9, textColor=TEXT_DARK, leading=12, fontName="Helvetica",
    ))
    styles.add(ParagraphStyle(
        "BodySmallBold", parent=styles["Normal"],
        fontSize=9, textColor=TEXT_DARK, leading=12, fontName="Helvetica-Bold",
    ))
    styles.add(ParagraphStyle(
        "Footer", parent=styles["Normal"],
        fontSize=7, textColor=TEXT_MED, alignment=TA_CENTER, fontName="Helvetica",
    ))
    styles.add(ParagraphStyle(
        "RightAlign", parent=styles["Normal"],
        fontSize=9, textColor=TEXT_DARK, alignment=TA_RIGHT, fontName="Helvetica",
    ))
    styles.add(ParagraphStyle(
        "RightAlignBold", parent=styles["Normal"],
        fontSize=9, textColor=TEXT_DARK, alignment=TA_RIGHT, fontName="Helvetica-Bold",
    ))
    styles.add(ParagraphStyle(
        "CellDesc", parent=styles["Normal"],
        fontSize=8.5, textColor=TEXT_DARK, leading=11, fontName="Helvetica",
    ))
    return styles


def build_jci_quote(output_path: str):
    styles = build_styles()
    margin = 18 * mm

    doc = SimpleDocTemplate(
        output_path, pagesize=A4,
        leftMargin=margin, rightMargin=margin,
        topMargin=margin, bottomMargin=20 * mm,
    )

    elements = []

    # --- HEADER: QUOTATION left, Logo right ---
    quote_title = Paragraph("QUOTATION", styles["QuoteTitleLeft"])

    if LOGO_PATH.exists():
        from PIL import Image as PILImage
        pil_img = PILImage.open(str(LOGO_PATH))
        img_w, img_h = pil_img.size
        logo_w = 50 * mm
        logo_h = logo_w * (img_h / img_w)
        logo = Image(str(LOGO_PATH), width=logo_w, height=logo_h)
    else:
        logo = Paragraph("SIFAB AS", styles["QuoteTitleLeft"])

    header_table = Table(
        [[quote_title, logo]],
        colWidths=[110 * mm, 60 * mm],
    )
    header_table.setStyle(TableStyle([
        ("VALIGN", (0, 0), (-1, -1), "MIDDLE"),
        ("ALIGN", (1, 0), (1, 0), "RIGHT"),
    ]))
    elements.append(header_table)
    elements.append(Spacer(1, 2 * mm))
    elements.append(HRFlowable(width="100%", thickness=1.5, color=SIFAB_GREEN))
    elements.append(Spacer(1, 4 * mm))

    # --- QUOTE META: both sides in green boxes ---
    box_style = TableStyle([
        ("FONTNAME", (0, 0), (0, -1), "Helvetica-Bold"),
        ("FONTNAME", (1, 0), (1, -1), "Helvetica"),
        ("FONTSIZE", (0, 0), (-1, -1), 9),
        ("TEXTCOLOR", (0, 0), (-1, -1), TEXT_DARK),
        ("VALIGN", (0, 0), (-1, -1), "TOP"),
        ("TOPPADDING", (0, 0), (-1, -1), 2),
        ("BOTTOMPADDING", (0, 0), (-1, -1), 2),
        ("BACKGROUND", (0, 0), (-1, -1), LIGHT_GREEN),
        ("BOX", (0, 0), (-1, -1), 0.5, SIFAB_GREEN),
        ("LEFTPADDING", (0, 0), (-1, -1), 4),
        ("RIGHTPADDING", (0, 0), (-1, -1), 4),
    ])

    meta_left_data = [
        [Paragraph("<b>To:</b>", styles["BodySmallBold"]),
         Paragraph("Johnson Controls", styles["BodySmall"])],
        [Paragraph("<b>Attn:</b>", styles["BodySmallBold"]),
         Paragraph("Susan Ritchie, Service Manager \u2014 Oil and Gas", styles["BodySmall"])],
        [Paragraph("", styles["BodySmall"]),
         Paragraph("Pavilion 3, Craigshaw Business Park, Craigshaw Road, "
                    "West Tullos Industrial Estate, Aberdeen, AB12 3QH, UK", styles["BodySmall"])],
    ]
    left_table = Table(meta_left_data, colWidths=[15 * mm, 70 * mm])
    left_table.setStyle(box_style)

    meta_right_data = [
        [Paragraph("<b>Quote Ref:</b>", styles["BodySmallBold"]),
         Paragraph("MAL-2026-001", styles["BodySmall"])],
        [Paragraph("<b>Date:</b>", styles["BodySmallBold"]),
         Paragraph("07 April 2026", styles["BodySmall"])],
        [Paragraph("<b>Your Ref:</b>", styles["BodySmallBold"]),
         Paragraph("Sphere (Eddie Schrader / PX Limited)", styles["BodySmall"])],
        [Paragraph("<b>Valid Until:</b>", styles["BodySmallBold"]),
         Paragraph("07 May 2026", styles["BodySmall"])],
    ]
    right_table = Table(meta_right_data, colWidths=[24 * mm, 56 * mm])
    right_table.setStyle(box_style)

    meta_table = Table([[left_table, right_table]], colWidths=[90 * mm, 84 * mm])
    meta_table.setStyle(TableStyle([("VALIGN", (0, 0), (-1, -1), "TOP")]))
    elements.append(meta_table)
    elements.append(Spacer(1, 5 * mm))

    # --- SUBJECT ---
    elements.append(Paragraph(
        '<b>Re: Maloney 4" Inflatable Prover Spheres</b>', styles["BodySmall"]
    ))
    elements.append(Spacer(1, 3 * mm))

    # --- INTRO ---
    elements.append(Paragraph(
        "Thank you for your enquiry. Sifab AS is an authorised distributor for Maloney Technical "
        "Products, with distribution in Norway and the UK. Please find below our quotation for the "
        "supply of inflatable prover spheres as requested.",
        styles["BodySmall"],
    ))
    elements.append(Spacer(1, 4 * mm))

    # --- LINE ITEMS ---
    elements.append(Paragraph("Scope of Supply", styles["SectionHead"]))

    col_widths = [12 * mm, 90 * mm, 12 * mm, 28 * mm, 28 * mm]
    header_row = [
        Paragraph("<b>Item</b>", styles["BodySmallBold"]),
        Paragraph("<b>Description</b>", styles["BodySmallBold"]),
        Paragraph("<b>Qty</b>", styles["BodySmallBold"]),
        Paragraph("<b>Unit Price</b>", styles["RightAlignBold"]),
        Paragraph("<b>Total</b>", styles["RightAlignBold"]),
    ]

    table_data = [header_row]

    # Item 1: Spheres incl. shipping
    table_data.append([
        Paragraph("1", styles["BodySmall"]),
        Paragraph(
            'Maloney 4" Inflatable Sphere, Polyurethane, U-53 (yellow)<br/>'
            "P/N: +200-0400U-53<br/>"
            "Weight (unfilled): 1.3 LBS<br/>"
            'Diameter (uninflated): 3.9"<br/>'
            "Country of Origin: USA<br/>"
            "Manufacturer: Maloney Technical Products<br/><br/>"
            "<i>Price includes freight from USA to Aberdeen, UK</i>",
            styles["CellDesc"],
        ),
        Paragraph("2 pcs", styles["BodySmall"]),
        Paragraph("USD 850.00", styles["RightAlign"]),
        Paragraph("USD 1,700.00", styles["RightAlign"]),
    ])

    # Total row
    table_data.append([
        "", "",
        Paragraph("", styles["BodySmall"]),
        Paragraph("<b>Total DDP:</b>", styles["RightAlignBold"]),
        Paragraph("<b>USD 1,700.00</b>", styles["RightAlignBold"]),
    ])

    items_table = Table(table_data, colWidths=col_widths, repeatRows=1)
    items_table.setStyle(TableStyle([
        ("BACKGROUND", (0, 0), (-1, 0), SIFAB_GREEN),
        ("TEXTCOLOR", (0, 0), (-1, 0), colors.white),
        ("FONTNAME", (0, 0), (-1, 0), "Helvetica-Bold"),
        ("BACKGROUND", (0, 2), (-1, 2), LIGHT_GREY),
        ("BACKGROUND", (0, -1), (-1, -1), LIGHT_GREEN),
        ("LINEABOVE", (0, -1), (-1, -1), 1.2, SIFAB_GREEN),
        ("GRID", (0, 0), (-1, -2), 0.4, BORDER_GREY),
        ("BOX", (0, 0), (-1, -1), 0.8, SIFAB_GREEN),
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

    terms_data = [
        [Paragraph("<b>Incoterms</b>", styles["BodySmallBold"]),
         Paragraph("DDP Johnson Controls/Tyco, Unit 7-9 Hareness Park, "
                    "Hareness Circle, Altens Industrial Estate, Aberdeen, AB12 3QY, UK",
                    styles["BodySmall"])],
        [Paragraph("<b>Delivery</b>", styles["BodySmallBold"]),
         Paragraph("10\u201312 weeks from receipt of Purchase Order", styles["BodySmall"])],
        [Paragraph("<b>Payment</b>", styles["BodySmallBold"]),
         Paragraph("Net 30 days", styles["BodySmall"])],
        [Paragraph("<b>Validity</b>", styles["BodySmallBold"]),
         Paragraph("07 May 2026", styles["BodySmall"])],
        [Paragraph("<b>Currency</b>", styles["BodySmallBold"]),
         Paragraph("USD", styles["BodySmall"])],
        [Paragraph("<b>Certificates</b>", styles["BodySmallBold"]),
         Paragraph("Certificate of Conformity and Manufacturer's Certificate of Origin "
                    "included at no additional charge", styles["BodySmall"])],
    ]

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

    # --- CLOSING ---
    elements.append(Paragraph(
        "Sifab AS is an authorised channel partner for Maloney Technical Products, Faure Herman, "
        "Honeywell, McCrometer, and Emerson. As a supply house for all types of products to the oil "
        "and gas industry, we welcome any further enquiries you may have.<br/><br/>"
        "We look forward to working with you and Johnson Controls.",
        styles["BodySmall"],
    ))
    elements.append(Spacer(1, 4 * mm))

    # --- SIGNATURE ---
    elements.append(Paragraph(
        "<b>Sondre Falch</b><br/>"
        "Manager<br/>"
        "Sifab AS<br/>"
        "Tel: +47 900 29 588<br/>"
        "Email: sondre.falch@sifab.no",
        styles["BodySmall"],
    ))
    elements.append(Spacer(1, 8 * mm))

    # --- FOOTER ---
    elements.append(HRFlowable(width="100%", thickness=0.5, color=SIFAB_GREEN))
    elements.append(Spacer(1, 2 * mm))
    elements.append(Paragraph(
        "Sifab AS &nbsp;|&nbsp; Bedriftsveien 20, 4313 Sandnes, Norway &nbsp;|&nbsp; "
        "Org.nr: 912 408 346 &nbsp;|&nbsp; www.sifab.no<br/>"
        "Authorised Channel Partner \u2014 Maloney Technical Products, Faure Herman, "
        "Honeywell, McCrometer, Emerson",
        styles["Footer"],
    ))

    doc.build(elements)
    return output_path


if __name__ == "__main__":
    import argparse
    parser = argparse.ArgumentParser()
    parser.add_argument("--output", "-o", default=None)
    args = parser.parse_args()
    out = args.output or str(SHARED_DRIVE / "Zigma360" / "Projects" / "MAL-2026-001_Quote_JCI.pdf")
    build_jci_quote(out)
    print(f"Quote generated: {out}")
