# SP-01415 — Project Execution Plan (Post-PO)

| Field | Value |
|---|---|
| **PO Number** | 4500998501 |
| **PO Created** | 2026-04-29 |
| **PO Received** | 2026-04-30 |
| **PO Acknowledged by** | Sifab — pending (OC due ~2026-05-07) |
| **Project Code** | SP-01415 |
| **Customer** | Measurement Solutions Norway AS (Guidant) |
| **End Client** | Equinor — Snorre A platform |
| **Customer Project** | GM-5341 Snorre A Oil Metering |
| **PO Total** | **USD 1,608,262.36** (FCA Sandnes, 30 days net) |
| **Delivery Date** | **2027-04-15** |
| **Warranty** | 28 months after installation at platform |
| **Governing T&C** | PP-PS-13 Rev 00 |

---

## 1. Commercial summary

### 1.1 Price reconciliation — quote vs PO

| # | Quote Pos | Description | Quote (USD) | Notes |
|---|---|---|---|---|
| 1 | 1 | O85 Small Volume Prover (Honeywell) | 1,515,869.01 | **11.2% discount applied → 1,346,091.69** |
| 2 | 2 | Seraphine Can (Pemberton) | 75,054.92 | |
| 3 | 3 | Shipment TruStop (US) → Sifab | 58,798.32 | |
| 4 | 4 | Onshore disassembly + reinstallation Snorre A | 0.00 | Budget estimate ~USD 110,000 (hourly) — **NOT in PO line** |
| 5 | 5 | Spare parts incl. seal kit | 16,679.03 | |
| 6 | 6 | Travel/accommodation Tempe (kick-off + FAT) | 30,104.74 | |
| 7 | 7 | Project Management + Documentation | 81,533.67 | |
| 8 | 8 | Terms and conditions (admin) | 0.25 | |
| | | **Quote Sum** | **1,778,039.94** | |
| | | **− 11.2% on Pos 1** | **−169,777.32** | |
| | | **PO Net Value** | **1,608,262.62** | matches PO 1,608,262.36 ✓ |

**Discount note on PO:** "Pricing as agreed during meeting April 30th 2026. -11.2% discount on line item 10 in Sifab's quotation SP-01415." (PO refers to Sifab Pos 1 prover line.)

### 1.2 Milestones

| # | Milestone | % | Amount (USD) | Trigger | Sifab notes |
|---|---|---|---|---|---|
| M1 | Clarified PO + bank guarantee 1 yr | 30% | 482,478.71 | OC submitted, deviations resolved, BG issued | BG to be arranged with bank. **Cash positive only after Honeywell 30% downpayment paid out.** |
| M2 | FAT accepted at Tempe, Arizona | 50% | 804,131.18 | Witnessed FAT pass | Trigger after flow test in US; Honeywell milestone |
| M3 | Re-assembly + testing complete at Snorre A | 10% | 160,826.24 | SAT pass offshore | Sifab-controlled phase |
| M4 | Documentation accepted, package close-out | 10% | 160,826.24 | MDCC sign-off | Sifab-controlled phase |
| | **Total** | 100% | 1,608,262.36 | | |

Each milestone requires Vendor Milestone Completion Certificate (template in `05 Dokumentasjon/01.Dokumentmaler/`).

### 1.3 Cash-flow / back-to-back exposure

- Honeywell requires **30% non-refundable down payment** at order acceptance (DEV-018).
- Honeywell SVP cost: USD 584,819 → 30% = **USD 175,446** payable by Sifab to Honeywell.
- Guidant M1 = USD 482,479. Net positive ≈ USD 307,000 after BG cost — provided BG is issued and clarified PO signed before M1 invoice.
- **Pre-financing risk:** if BG/clarification delays M1 beyond Honeywell PO acceptance, Sifab carries the gap.

---

## 2. Open commercial / contractual items requiring action

| # | Item | Owner | Required by | Status |
|---|---|---|---|---|
| C1 | **Order Confirmation issued to Anne Krotseng** | Tom | 2026-05-07 (5 business days) | Open |
| C2 | **Deviation list issued to Guidant at PO acceptance** | Sondre/Tom | 2026-05-07 | Existing list `SP-01415_Deviation_List_Rev0` — needs PO context update before issue |
| C3 | **Bank guarantee 1-year valid** | Tom (bank) | Before M1 invoice | Sondre confirmed acceptance to Anne 2026-04-30 |
| C4 | **First Monthly Progress Report** | Sondre | **2026-05-08** | Template in `05 Dokumentasjon/01.Dokumentmaler/Supplier Progress Report - Template - Guidant Measurement.doc` |
| C5 | **Ship-to address** | Anne Krotseng (Guidant) | Before any shipment | PO shows "TBC" — need to clarify |
| C6 | **Sifab address** on PO/quote | Tom → Anne | Before next revision | PO has Bedriftsveien 24, should be **Bedriftsveien 20** (per 2026-02-26 move). Tom's signature also still wrong. |
| C7 | **Pos 4 dis/re-assembly mechanism** | Tom | Before VOR window opens | PO bundles Pos 4 budget into single line. ~USD 110k of hourly work has no separate VOR cap. **Confirm in OC reply that hourly Pos 4 work will be a future VOR per PP-PS-13.** |
| C8 | **Honeywell back-to-back PO** | Tom | Before M1 issued | Match terms: warranty 28 mo from platform install, milestone-aligned payments, NORSOK supervision rates, 30% down. |
| C9 | **Kick-off meeting + pre-production meeting** | Sifab + Guidant | Date TBD | PO requires this — propose week 19/20 |
| C10 | **Hold/witness notification (14-day)** | Sifab QC | Each test | Send to beritdahl.hystad@guidantmeasurement.com |

---

## 3. Technical scope mapping (Quote → Supplier → Deliverable)

### 3.1 Pos 1 — SVP085 (Honeywell)
| Item | Source | Status |
|---|---|---|
| SVP085 prover, displaced volume 75 USG (283.9 L) | Honeywell Enraf (Tempe, AZ + flow tube India) | Quoted |
| Model: SVP085-O-E8C06N5A-2A-000-112-211-YYY-01 | Confirmed in quote | Confirmed |
| Process flange: 12" ANSI B16.5 CL600 RTJ | Per BD20X (lower DP than CL600 due to 316SS) | Open — DEV-009 |
| Drain/vent: 1" 600# RTJ | Per quote | Confirmed |
| Wetted parts: SS316 / hard chrome lined bore | Per quote | NACE compliance per DEV-009 |
| NORSOK M-501 System 6C coating | Sifab to source locally after flow test (DEV-004) | Open — Sifab scope |
| Motor 220/240 VAC 50 Hz | Quote shows 50 Hz; Sidney verbally confirmed 60 Hz at no cost (DEV-002) | **Open — needs formal update** |
| ATEX IIB T4 / Ex d ia | Quote confirms | OK |
| IP65 transmitters / IP56 motor | RFQ requires IP66 (DEV-001) | **HIGH — open** |
| Two-piece main frame, ~5,258 mm total | Modular split engineering | **HIGH — DEV-007** |
| PED + PMI on welds | Per quote | DEV-010 — clarify "less hardware" |
| Sifab free-issue: 3 transmitters, B&B valve, RTDs, thermowells | Per quote note | Sifab to procure |
| Insulation | Sifab scope | Per DEV-015 |

### 3.2 Pos 2 — Seraphin Can
| Item | Detail |
|---|---|
| Pemberton EMSS0283.9L-30-3, 283.9 L, 316 SS, NIST + NVLAP cal | Per quote |
| Cabinet | Quote: aluminum transport box. **RFQ requires SS316 cabinet** — open gap |
| Justervesenet 3rd-party certification | Quote: not included; Sifab can organise (DEV-017) — confirm with Guidant |

### 3.3 Pos 3 — Shipment TruStop → Sifab
- Honeywell standard skid → wooden crate, 10t fork lift / crane lifting
- Air freight planned (sea freight option for cost)

### 3.4 Pos 4 — Disassembly + reinstallation (BUDGET)
- HE supervisor 120 h onshore + 180–240 h offshore
- Intertek prover expert 36 h onshore + 180–240 h offshore
- Rates: USD 140 onshore / USD 180 offshore + KPI adjustment (confirmed 2026-04-23)
- Estimate ~USD 110,000 — **NOT in PO sum**; future VOR
- Blu Electro for cabling re-connect (subcontract)

### 3.5 Pos 5 — Spare parts
| Qty | Item | P/N |
|---|---|---|
| 1 | KIT OPTICAL SWITCH (3 ea) | 44110148 |
| 1 | (TBD — line item 5 incomplete in quote) | — |
| 1 | Motor stop switch — O models | 44107515 |
| 1 | Seal Kit CSK S85 150/300/600# CRB | 44105627 |

**Action C-SP1:** confirm missing line 5 with Honeywell and update SPIR.

### 3.6 Pos 6 — Travel Tempe (Kick-off + FAT)
- 1 day kick-off + 2 days FAT/calibration in Tempe, AZ
- Sifab arranges trips and accommodation

### 3.7 Pos 7 — Project Management + Documentation
- Sifab PM appointed; full document package per quote Pos 8 list

### 3.8 Pos 8 — Document deliverables (timeline)

| WAO | Documents |
|---|---|
| **2 WAO (by 2026-05-14)** | Production plan & progress report; Quality & Inspection plan; Vendor document schedule |
| **4 WAO (by 2026-05-28)** | All GA + split-module drawings + 3D model + interface list; GA water draw panel; GA Seraphin can incl. cabinet; Surface treatment procedure; NORSOK datasheets (prover, thermowells, motor, switches); Wake frequency calcs; Wiring diagram; NDE operator certs; Monthly progress reports |
| **8 WAO (by 2026-06-25)** | NDE procedure; FAT/Calibration procedure; SAT/Water draw procedure; Pressure test procedure; ATEX certs (mech + elec); Welder certs; WPS/WPQ; Weld record sheet; SPIR with prices + cross-refs |
| **WD (with delivery)** | Operating manual; Maintenance manual; EC Declaration of Conformity; EN 10204 3.1 material certs; PMI report; NDE reports; FAT/Cal report (factory); SAT/Water draw report (Snorre A); Pressure test report; Surface treatment + coating report; Weighing report; Preservation report |

All documentation routed to **MDCC@guidantmeasurement.com**.

---

## 4. Deviation register status (Rev 0, 2026-03-23)

18 deviations logged before PO. **None resolved before PO acceptance.** Must be re-issued as **Rev 1 with PO 4500998501 reference** and submitted with OC per PO clause: "any deviation to this Purchase Order (technical/commercial) must be made in a separate document and issued to Guidant upon receipt of this order."

| # | Deviation | Severity | Action at PO acceptance |
|---|---|---|---|
| DEV-001 | IP65/IP56 vs IP66 | HIGH | Re-issue; Honeywell to confirm IP66 alt or Sifab to add IP66 enclosure scope |
| DEV-002 | Motor 50→60 Hz | MED | Get Sidney's written confirmation; close |
| DEV-003 | Welding ASME vs NORSOK M-601 | HIGH | Project deviation request (Aker BP precedent) |
| DEV-004 | NORSOK painting excluded — Sifab scope | MED | Confirm in OC; price-locked |
| DEV-005 | Warranty 24m delivery vs 28m install | HIGH | **Critical — must close before M1**. Need Honeywell EWA or written extension |
| DEV-006 | Std 60°C vs design 106°C | HIGH | Honeywell to confirm hi-temp option included |
| DEV-007 | Modules exceed 1.4×2.56×2.2 m | HIGH | Submit formal deviation with split drawings |
| DEV-008 | SAT/commissioning/3rd party not included | HIGH | HE supervision rates locked; SAT scope to clarify |
| DEV-009 | TR2000 BD20X / 6Mo tubing | HIGH | Honeywell to confirm material chain to BD20X |
| DEV-010 | PMI "less hardware" ambiguous | MED | Clarify per TR1427 |
| DEV-011 | NORSOK E-001 / TR3023 / BFOU cables | MED | Sifab free-issue scope (Aker BP precedent) |
| DEV-012 | Standard doc package vs RFQ list | MED | Map gap, price gap items |
| DEV-013 | Procedure approval before fabrication | MED | Include in HE PO |
| DEV-014 | Lifting per NORSOK R-002 | MED | Clarify in engineering |
| DEV-015 | 100 mm insulation clearance | LOW | Engineering review |
| DEV-016 | Hydro test 1.5× BD20X | LOW | Honeywell confirm |
| DEV-017 | Seraphin Justervesenet cert | LOW | Sifab to arrange (lead time) |
| DEV-018 | 30% Honeywell down vs Guidant milestones | HIGH | Cash-flow alignment per §1.3 above |

---

## 5. Schedule (high-level)

| Date | Milestone |
|---|---|
| 2026-04-29 | PO 4500998501 issued |
| 2026-04-30 | PO received by Sifab |
| **2026-05-07** | **OC due (5 business days)** |
| **2026-05-07** | **Deviation list Rev 1 issued with OC** |
| **2026-05-08** | **First monthly progress report** |
| Week 19 / 20 | Kick-off + pre-production meeting (Tempe) |
| 2026-05-14 | 2 WAO documents due |
| 2026-05-28 | 4 WAO documents due |
| 2026-06-25 | 8 WAO documents due |
| Q4 2026 | FAT at Tempe, Arizona (M2) |
| Q1 2027 | Disassembly at Norwegian fab yard, NORSOK painting |
| Q1 2027 | Sea transport to Snorre A |
| Q1–Q2 2027 | Re-assembly + SAT on Snorre A (M3) |
| **2027-04-15** | **Delivery date per PO** |
| Q2 2027 | Documentation close-out (M4) |
| 2027-04-15 + 28 mo | Warranty expiry (≈ 2029-08-15) |

Honeywell delivery time stated as 50–52 weeks → from order ≈ Q2 2027. Aligns with PO 2027-04-15.

---

## 6. Project parties

### 6.1 Customer (Guidant)

| Role | Name | E-mail |
|---|---|---|
| Commercial (primary) | Anne Josefine Torsvik Krotseng | anne.krotseng@guidantmeasurement.com |
| Technical | Feraz Mohammed | feraz.mohammed@guidantmeasurement.com |
| Project Manager | Martin Carlsson | martin.carlsson@guidantmeasurement.com |
| Quality | Berit Dahl Hystad | beritdahl.hystad@guidantmeasurement.com |
| Senior Tender Engineer | Torleif Espegard | torleif.espegard@guidantmeasurement.com |
| Document Control | MDCC inbox | MDCC@guidantmeasurement.com |
| Accounts Payable | — | Accounts.Payable_NO28@guidantmeasurement.com |

Anne Krotseng must be copied on **all** PO-related correspondence.

### 6.2 Sifab team

| Role | Name |
|---|---|
| Project responsible / Sales Manager | Sondre Falch |
| General Manager / Commercial lead | Tom Sverre Falch |
| Project Engineer (proposed) | Oliver Vetland |
| Service Engineer | Sayed M. Mortazavi |

### 6.3 Honeywell Enraf (supplier)

| Role | Name |
|---|---|
| Lead | Sidney Swart |
| Prover specialist | Samir Sakota |
| Support | Mark Price, Eric van der Made |

### 6.4 Sub-suppliers

| Item | Supplier |
|---|---|
| Seraphin can | Pemberton (US) |
| Water draw kit (parts) | Flowtec |
| NORSOK painting | TBD — local Norwegian workshop |
| Cabling subcontract | Blu Electro |
| Freight forwarder (Norway side) | Håkull AS (Even Hansen) |
| 3rd-party witness | Intertek |

---

## 7. Project file inventory (reference)

### 7.1 OneDrive — `Zigma360/Projects/SP-01415 Small Volume Prover Snorre A/`

```
01.Bestillinger & Ordrebekreftelser/
   PO 4500998501.pdf                                        — issued PO
   PP-PS-13 GTC for Goods and Ancillary Services.pdf        — governing T&C
02 Tilbud/
   Tilbud SP-01415.pdf                                       — Zigma quote (pre-discount sum)
   Tilbudsskriv SP-01415 Rev 1 Guidant Snorre A.doc          — quote letter Rev 1
   Fra Honeywell/Tegning fra Samir.docx                      — supplier drawings
   Fra Honeywell/Tegning fra Samir med kommentarer.docx
   RFQ_Pemberton_Seraphin_Can_Snorre_A (002).docx
03 Underlag fra Kunde/
   Technical Specification Honeywell SVP.pdf (SPC_0000043_A_004) — applies to PO
   Snorre A_RFQ Compact Prover.msg
   Drive end and prover barrel.JPG
04 E-mail/                                                    — to populate
05 Dokumentasjon/
   01.Dokumentmaler/
     Vendor Milestone Completion Certificate Template.doc
     Supplier Progress Report - Template.doc
     Vendor Sub Supplied Items - Status.xlsx
   02.Dok fra Leverandør/        03.Dok sendt leverandør for oppdatering/
   04.Dok sendt til kunde/       05.Dok Kode 1/
   Transmittel/
   Dokument status og oppfølging.xlsx
06 Møtereferat/                                              — to populate (kick-off MOM)
07 Clarifications/                                           — to populate
08 Underlag fra Leverandører/                                — Honeywell scope, Pemberton, etc.
09 VOR/                                                      — Variation Orders (e.g. Pos 4 hourly work)
10 Bilder/
11 Punch lists/
ARKIV/
BID FOR HONEYWELL ENRAF FLOW PROVER TECHNICAL ISSUES.docx
Modular_Split_Execution_Plan_SVP085_Rev3.docx
QCF524_Snorre_A_FILLED Datasheet.docx
SVP O85 Scope disassembly and reinstallation Snorre A.docx
```

### 7.2 Git repo — `projects/snorre-a-compact-prover/`

```
PROJECT.md                                                  — technical scope (pre-PO)
rfq/
   RFQ Small volume prover, Rev. A.pdf
   08 -- S1-AA-PDE-0219_02S.pdf                             — process datasheet
   PP-PS-13 GTC for Goods and Ancillary Services (1).pdf
honeywell/
   QCF524_Specification Worksheet Rev V19.docx
   Prover Checklist Example Punch List.xlsx
   Prover Checklist Template SNORRE Punchlist Example.xlsx
engineering/
   SP-01415_Deviation_List_Rev0.md / .docx                  — 18 deviations, 8 HIGH
   SP-01415_RFQ_Compliance_Matrix_Rev0.md / .docx
   Modular_Split_Execution_Plan_SVP085_Rev2.docx
   QCF524_Snorre_A_FILLED.docx
   Norsok_Compliance_Matrix_Snorre_A_SVP.md
   INTERNAL_NOTE_Project_Cautions_Snorre_A.md
   Lessons_Learned_NOA_Valhall_Provers.md
   Sifab_Quote_Request_Honeywell_Snorre_A.md / .pdf
   RFQ_Flowtec_Water_Draw_Kit_Snorre_A.md / .docx / .pdf
   RFQ_Pemberton_Seraphin_Can_Snorre_A.md / .docx / .pdf
   Free_Issued_Parts_NOA_Valhall_Reference.xlsx
   Snorre_A_Punchlist_FILLED.xlsx
handoffs/
   SP-01415_Project_Execution_Plan_PO_Received.md           — this document
```

---

## 8. Immediate actions (next 5 business days)

1. **OC reply to Anne Krotseng** with deviation list Rev 1 attached, ship-to address request, address-correction note (Bedriftsveien 20).
2. **Deviation List Rev 1** — update header to reference PO 4500998501; add new section for PO commercial deviations (warranty back-to-back, Pos 4 hourly mechanism, ship-to).
3. **First Progress Report** drafted using Guidant template — even if minimal content, deadline is 2026-05-08.
4. **Bank guarantee** — initiate with bank (1-year validity, M1 trigger).
5. **Honeywell back-to-back PO** — issue PO from Sifab to Honeywell mirroring the 28-month warranty, milestone-aligned payments, NORSOK painting Sifab scope, supervision rates, free-issue parts list.
6. **Kick-off meeting proposal** — propose dates to Anne + Martin.
7. **MDCC distribution** — set up document distribution list to MDCC@guidantmeasurement.com with Anne and Martin in CC.

---

*Document prepared 2026-05-05 for project hand-over from sales to execution. Owner: project-manager agent. Distribute to: Tom, Sondre, Oliver Vetland.*
