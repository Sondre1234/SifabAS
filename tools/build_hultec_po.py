#!/usr/bin/env python3
"""
Hultec Purchase Order Generator — Sifab AS
Builds a Zigma-style "Bestilling" (PO) PDF for Hultec EMEA orders.
Works around the Zigma limitation of single-currency (NOK) projects.

Usage:
    python tools/build_hultec_po.py
"""

import os
from pathlib import Path

from reportlab.lib import colors
from reportlab.lib.pagesizes import A4
from reportlab.lib.units import mm
from reportlab.lib.styles import getSampleStyleSheet, ParagraphStyle
from reportlab.lib.enums import TA_LEFT, TA_RIGHT
from reportlab.platypus import (
    SimpleDocTemplate, Table, TableStyle, Paragraph, Spacer, Image, KeepTogether,
)

# Sifab / Zigma style
SIFAB_GREEN = colors.HexColor("#5BA84F")
GRID_GREY = colors.HexColor("#BDBDBD")
ROW_HEAD = colors.HexColor("#E8E8E8")
TEXT_DARK = colors.HexColor("#1A1A1A")
TEXT_MED = colors.HexColor("#555555")

REPO = Path(__file__).resolve().parent.parent
LOGO = REPO / "temp_logo.jpeg"
SHARED = Path(os.environ["USERPROFILE"]) / "OneDrive - Sifab AS" / "Dokumenter - Felles"


def styles_setup():
    s = getSampleStyleSheet()
    s.add(ParagraphStyle("POTitle", fontName="Helvetica-Bold", fontSize=22,
                         textColor=TEXT_DARK, alignment=TA_LEFT))
    s.add(ParagraphStyle("Label", fontName="Helvetica-Bold", fontSize=9,
                         textColor=TEXT_DARK, leading=12))
    s.add(ParagraphStyle("Value", fontName="Helvetica", fontSize=9,
                         textColor=TEXT_DARK, leading=12))
    s.add(ParagraphStyle("Small", fontName="Helvetica", fontSize=8,
                         textColor=TEXT_MED, leading=10))
    s.add(ParagraphStyle("SmallR", fontName="Helvetica", fontSize=8,
                         textColor=TEXT_MED, leading=10, alignment=TA_RIGHT))
    s.add(ParagraphStyle("Cell", fontName="Helvetica", fontSize=9,
                         textColor=TEXT_DARK, leading=11))
    s.add(ParagraphStyle("CellR", fontName="Helvetica", fontSize=9,
                         textColor=TEXT_DARK, leading=11, alignment=TA_RIGHT))
    s.add(ParagraphStyle("CellB", fontName="Helvetica-Bold", fontSize=9,
                         textColor=TEXT_DARK, leading=11),)
    s.add(ParagraphStyle("CellBR", fontName="Helvetica-Bold", fontSize=9,
                         textColor=TEXT_DARK, leading=11, alignment=TA_RIGHT))
    return s


def build_po(output_path: Path):
    S = styles_setup()

    # --- Data ---
    po_number = "PO-00670"
    project_no = "SP-01484"
    po_date = "21.04.2026"
    lev_date = "TBC"  # confirmed by supplier in order acknowledgement
    lev_bet = "FCA Enschede (Incoterms 2020)"
    sendes_pr = "Road freight (Haakull)"
    bet_bet = "Net 30 days"
    currency = "USD"

    supplier_lines = [
        "Hultec EMEA & Asia Pacific B.V.",
        "Attn: Gerben de Jonge",
        "The Gallery, Hengelosestraat 500 (office 079A)",
        "7521 AN Enschede",
        "The Netherlands",
    ]

    delivery_lines = [
        "Sifab AS",
        "Bedriftsveien 20",
        "4313 Sandnes",
        "Norway",
    ]

    invoice_lines = delivery_lines  # same for Sifab

    vaar_ref = "Sondre Falch"
    deres_ref = "Gerben de Jonge"
    best_nr = "SP-01484 / MAL-2026-001 Rev 1"
    beskrivelse = 'Maloney 4" Inflatable Sphere, Polyurethane, U-53'

    # Line items
    qty = 2
    unit_price = 414.29
    line_total = qty * unit_price
    total = line_total

    # --- Build document ---
    doc = SimpleDocTemplate(
        str(output_path), pagesize=A4,
        leftMargin=18 * mm, rightMargin=18 * mm,
        topMargin=12 * mm, bottomMargin=14 * mm,
    )

    flow = []

    # Top row: Logo (left) | Bestilling + right-side fields
    logo = Image(str(LOGO), width=55 * mm, height=16 * mm)
    logo.hAlign = "LEFT"

    right_info = Table(
        [
            [Paragraph("Prosjektnr:", S["Label"]), Paragraph(project_no, S["Value"])],
            [Paragraph("Dato:", S["Label"]), Paragraph(po_date, S["Value"])],
            [Paragraph("Lev.dato:", S["Label"]), Paragraph(lev_date, S["Value"])],
            [Paragraph("Lev.bet.:", S["Label"]), Paragraph(lev_bet, S["Value"])],
            [Paragraph("Sendes pr:", S["Label"]), Paragraph(sendes_pr, S["Value"])],
            [Paragraph("Bet.betingelser:", S["Label"]), Paragraph(bet_bet, S["Value"])],
        ],
        colWidths=[30 * mm, 60 * mm],
    )
    right_info.setStyle(TableStyle([
        ("VALIGN", (0, 0), (-1, -1), "TOP"),
        ("LEFTPADDING", (0, 0), (-1, -1), 0),
        ("RIGHTPADDING", (0, 0), (-1, -1), 0),
        ("TOPPADDING", (0, 0), (-1, -1), 1),
        ("BOTTOMPADDING", (0, 0), (-1, -1), 1),
    ]))

    header_row = Table(
        [[logo, Paragraph("Bestilling", S["POTitle"])]],
        colWidths=[84 * mm, 90 * mm],
        rowHeights=[18 * mm],
    )
    header_row.setStyle(TableStyle([
        ("VALIGN", (0, 0), (0, 0), "TOP"),
        ("VALIGN", (1, 0), (1, 0), "BOTTOM"),
        ("LEFTPADDING", (0, 0), (-1, -1), 0),
        ("RIGHTPADDING", (0, 0), (-1, -1), 0),
    ]))
    flow.append(header_row)
    flow.append(Spacer(1, 4 * mm))

    info_row = Table(
        [[Spacer(1, 1 * mm), right_info]],
        colWidths=[84 * mm, 90 * mm],
    )
    info_row.setStyle(TableStyle([
        ("VALIGN", (0, 0), (-1, -1), "TOP"),
        ("LEFTPADDING", (0, 0), (-1, -1), 0),
        ("RIGHTPADDING", (0, 0), (-1, -1), 0),
    ]))
    flow.append(info_row)
    flow.append(Spacer(1, 8 * mm))

    # Supplier + delivery/invoice addresses side by side
    supplier_para = [Paragraph("<b>Bestilt til:</b>", S["Value"])]
    supplier_para += [Paragraph("", S["Value"])]
    supplier_para += [Paragraph(f"<b>{supplier_lines[0]}</b>", S["Value"])]
    for line in supplier_lines[1:]:
        supplier_para.append(Paragraph(line, S["Value"]))

    del_para = [Paragraph("<i>Leveringsadresse:</i>", S["Value"])]
    for line in delivery_lines:
        del_para.append(Paragraph(line, S["Value"]))
    del_para.append(Spacer(1, 3 * mm))
    del_para.append(Paragraph("<i>Fakturaadresse:</i>", S["Value"]))
    for line in invoice_lines:
        del_para.append(Paragraph(line, S["Value"]))

    addr_row = Table(
        [[supplier_para, del_para]],
        colWidths=[84 * mm, 90 * mm],
    )
    addr_row.setStyle(TableStyle([
        ("VALIGN", (0, 0), (-1, -1), "TOP"),
        ("LEFTPADDING", (0, 0), (-1, -1), 0),
        ("RIGHTPADDING", (0, 0), (-1, -1), 0),
    ]))
    flow.append(addr_row)
    flow.append(Spacer(1, 6 * mm))

    # Ref block
    ref_rows = [
        [Paragraph("Vår ref.:", S["Label"]), Paragraph(vaar_ref, S["Value"])],
        [Paragraph("Deres ref.:", S["Label"]), Paragraph(deres_ref, S["Value"])],
        [Paragraph("Best.nr:", S["Label"]), Paragraph(best_nr, S["Value"])],
        [Spacer(1, 2 * mm), Spacer(1, 2 * mm)],
        [Paragraph("Beskrivelse:", S["Label"]), Paragraph(f"<b>{beskrivelse}</b>", S["Value"])],
    ]
    ref_tbl = Table(ref_rows, colWidths=[30 * mm, 144 * mm])
    ref_tbl.setStyle(TableStyle([
        ("VALIGN", (0, 0), (-1, -1), "TOP"),
        ("LEFTPADDING", (0, 0), (-1, -1), 0),
        ("RIGHTPADDING", (0, 0), (-1, -1), 0),
        ("TOPPADDING", (0, 0), (-1, -1), 1),
        ("BOTTOMPADDING", (0, 0), (-1, -1), 1),
    ]))
    flow.append(ref_tbl)
    flow.append(Spacer(1, 6 * mm))

    # Line item table: Pos, Art.nr, Beskrivelse, Mengde, Enhet, USD, Rab., Sum
    line_desc = (
        'Maloney 4" Inflatable Sphere, Polyurethane, U-53 (yellow)<br/>'
        'P/N: +200-0400U-53<br/>'
        'Weight (unfilled): 1.3 LBS — Diameter (uninflated): 3.9"<br/>'
        'Schedule B: 3926.90.7500 — Country of Origin: USA'
    )

    header = [
        Paragraph("<b>Pos</b>", S["Cell"]),
        Paragraph("<b>Art.nr</b>", S["Cell"]),
        Paragraph("<b>Beskrivelse</b>", S["Cell"]),
        Paragraph("<b>Mengde</b>", S["CellR"]),
        Paragraph("<b>Enhet</b>", S["Cell"]),
        Paragraph(f"<b>{currency}</b>", S["CellR"]),
        Paragraph("<b>Rab.</b>", S["CellR"]),
        Paragraph("<b>Sum</b>", S["CellR"]),
    ]
    row1 = [
        Paragraph("1", S["Cell"]),
        Paragraph("+200-0400U-53", S["Cell"]),
        Paragraph(line_desc, S["Cell"]),
        Paragraph(f"{qty},00", S["CellR"]),
        Paragraph("pcs", S["Cell"]),
        Paragraph(f"{unit_price:,.2f}".replace(",", " "), S["CellR"]),
        Paragraph("0", S["CellR"]),
        Paragraph(f"{line_total:,.2f}".replace(",", " "), S["CellR"]),
    ]

    tbl = Table(
        [header, row1],
        colWidths=[10 * mm, 26 * mm, 66 * mm, 16 * mm, 12 * mm, 16 * mm, 12 * mm, 16 * mm],
    )
    tbl.setStyle(TableStyle([
        ("BACKGROUND", (0, 0), (-1, 0), ROW_HEAD),
        ("LINEBELOW", (0, 0), (-1, 0), 0.5, GRID_GREY),
        ("LINEBELOW", (0, 1), (-1, 1), 0.5, GRID_GREY),
        ("VALIGN", (0, 0), (-1, -1), "TOP"),
        ("LEFTPADDING", (0, 0), (-1, -1), 3),
        ("RIGHTPADDING", (0, 0), (-1, -1), 3),
        ("TOPPADDING", (0, 0), (-1, -1), 4),
        ("BOTTOMPADDING", (0, 0), (-1, -1), 4),
    ]))
    flow.append(tbl)

    # Spacer then totals bar toward the bottom of page
    flow.append(Spacer(1, 25 * mm))

    totals = Table(
        [[
            Paragraph("<b>Sum:</b>", S["CellR"]),
            Paragraph(f"<b>{total:,.2f}</b>".replace(",", " "), S["CellR"]),
            Paragraph("<b>MVA</b>", S["CellR"]),
            Paragraph("", S["CellR"]),
            Paragraph("<b>Sum inkl. MVA</b>", S["CellR"]),
            Paragraph(f"<b>{total:,.2f}</b>".replace(",", " "), S["CellR"]),
            Paragraph(f"<b>{currency}</b>", S["Cell"]),
        ]],
        colWidths=[26 * mm, 28 * mm, 20 * mm, 22 * mm, 30 * mm, 30 * mm, 18 * mm],
    )
    totals.setStyle(TableStyle([
        ("BACKGROUND", (0, 0), (-1, -1), ROW_HEAD),
        ("VALIGN", (0, 0), (-1, -1), "MIDDLE"),
        ("LEFTPADDING", (0, 0), (-1, -1), 3),
        ("RIGHTPADDING", (0, 0), (-1, -1), 3),
        ("TOPPADDING", (0, 0), (-1, -1), 5),
        ("BOTTOMPADDING", (0, 0), (-1, -1), 5),
    ]))
    flow.append(totals)
    flow.append(Spacer(1, 8 * mm))

    # Footer (mimics Zigma's bottom bar)
    foot = Table(
        [
            [
                Paragraph("<b>Navn:</b><br/>SIFAB AS", S["Small"]),
                Paragraph("<b>Postadresse:</b><br/>Bedriftsveien 20<br/>4313 Sandnes", S["Small"]),
                Paragraph("<b>Telefon:</b><br/>(+47) 984 97 000", S["Small"]),
                Paragraph("<b>E-post:</b><br/>post@sifab.no", S["Small"]),
            ],
            [
                Paragraph("<b>Org.nr:</b><br/>NO 912 408 346 MVA", S["Small"]),
                Paragraph("<b>Web:</b><br/>www.sifab.no", S["Small"]),
                Paragraph("<b>Bankkonto:</b><br/>3260 65 40549", S["Small"]),
                Paragraph("", S["Small"]),
            ],
        ],
        colWidths=[44 * mm, 44 * mm, 42 * mm, 44 * mm],
    )
    foot.setStyle(TableStyle([
        ("VALIGN", (0, 0), (-1, -1), "TOP"),
        ("LINEABOVE", (0, 0), (-1, 0), 0.5, GRID_GREY),
        ("LEFTPADDING", (0, 0), (-1, -1), 0),
        ("RIGHTPADDING", (0, 0), (-1, -1), 3),
        ("TOPPADDING", (0, 0), (-1, -1), 3),
        ("BOTTOMPADDING", (0, 0), (-1, -1), 3),
    ]))
    flow.append(foot)

    doc.build(flow)
    return output_path


def main():
    out_dir = (
        SHARED
        / "Zigma360" / "Projects"
        / "SP-01484 Johnson Controls - Maloney 4in U-53 Spheres"
        / "01.Bestillinger & Ordrebekreftelser"
    )
    out_dir.mkdir(parents=True, exist_ok=True)
    out_path = out_dir / "PO-00670_SP-01484_Hultec_Maloney_4in_U-53.pdf"
    build_po(out_path)
    print(f"Generated: {out_path}")


if __name__ == "__main__":
    main()
