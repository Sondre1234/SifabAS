# RFQ Compliance Matrix — SP-01415 Snorre A Small Volume Prover

| Field | Value |
|-------|-------|
| **RFQ No.** | GM-8501-1447 Rev. A |
| **Sifab Project** | SP-01415 |
| **Client** | Guidant (Measurement Solutions Norway AS) |
| **End Client** | Equinor — Snorre A |
| **Honeywell Proposal** | 10465986-O-1010834 R0 |
| **Date** | 2026-03-23 |
| **Revision** | 0 |

**Legend:**
- **C** = Comply
- **PC** = Partially Comply
- **D** = Deviate (see Deviation List)
- **CR** = Clarification Required
- **N/A** = Not applicable to this party

**Responsible Party:**
- **HW** = Honeywell (prover manufacturer)
- **SF** = Sifab AS (system integrator / fabrication)
- **GU** = Guidant / Equinor (customer)

---

## §1 — Scope of Supply

| # | RFQ Requirement | Status | Resp. | DEV | Remarks |
|---|----------------|--------|-------|-----|---------|
| 1.0-1 | Supply one (1) SVP including SVP controller for proving crude oil USMs | **C** | HW | — | SVP085 model quoted. Controller included. |
| 1.0-2 | Supply one (1) certified Seraphin can for water draw calibration | **C** | SF | — | Sifab sourcing from Pemberton. |
| 1.0-3 | Seraphin can certification by Justervesenet | **CR** | SF | DEV-017 | Lead time to be confirmed with Justervesenet. |
| 1.0-4 | Seraphin can in SS316 cabinet for protection, transport, storage offshore | **C** | SF | — | SS316 cabinet confirmed (Tom, 21 Mar). Forklift lifting arrangement included. |
| 1.0-5 | Water draw kit including solenoid valve and manual instrument valves | **PC** | HW/SF | — | Honeywell quotes "KIT WATER DRAW SVP CONTROLLER, DC" ($7,363). Full kit scope (solenoid + manual valves) to be confirmed. Water draw kit also sourced from Flowtec by Sifab. |
| 1.0-6 | Split SVP into modules per §1.7 envelope requirements | **D** | HW/SF | DEV-007 | Two-piece frame. Modules exceed stated envelope. Verbally accepted by Guidant (18 Mar) — formal deviation needed. |
| 1.0-7 | Vendor disassembly and packing at onshore facility in Norway | **C** | HW/SF | — | Included in scope. Honeywell supervision required. |
| 1.0-8 | Re-assembly of SVP on Snorre A platform | **C** | HW/SF | DEV-008 | Included in scope. Honeywell supervisor rates pending (DEV-008). |
| 1.0-9 | Warranty valid from date vendor has assembled and released SVP on site | **D** | HW | DEV-005 | Honeywell standard: 24m from delivery. RFQ: from site release. Back-to-back required. |
| 1.0-10 | Warranty min. 28 months after installation | **D** | HW | DEV-005 | Honeywell standard is 24 months. Extended warranty needed. |
| 1.0-11 | CE marking per PED and ATEX | **C** | HW | — | PED 2014/68/EU and ATEX 2014/34/EU included. |

---

## §1.1 — Standards & Requirements

| # | RFQ Requirement | Status | Resp. | DEV | Remarks |
|---|----------------|--------|-------|-----|---------|
| 1.1-1 | API MPMS Chapter 4.2 (Displacement Provers) | **C** | HW | — | Honeywell designs per API MPMS 4.2. |
| 1.1-2 | Måleforskriften (Norwegian fiscal measurement regulations) | **CR** | HW/SF | — | Honeywell does not reference Måleforskriften. Sifab/Guidant to confirm compliance during engineering. |
| 1.1-3 | PED 2014/68/EU | **C** | HW | — | PED certification included. |
| 1.1-4 | ATEX 2014/34/EU | **C** | HW | — | ATEX certification included. |
| 1.1-5 | Machinery Directive 2006/42/EC | **CR** | HW | — | Not explicitly referenced in Honeywell proposal. |
| 1.1-6 | EMC Directive 2014/30/EU | **CR** | HW | — | Not explicitly referenced in Honeywell proposal. |
| 1.1-7 | TR2000 (PCS BD20X, Plant SNA) | **D** | HW | DEV-009 | Honeywell states 316/316L but does not reference TR2000 BD20X. |
| 1.1-8 | TR0042 (Surface preparation and coating) | **PC** | SF | DEV-004 | Sifab scope — painting in Norway. Motor/gearbox deviation pending. |
| 1.1-9 | TR1427 (PMI) | **PC** | HW | DEV-010 | "PMI on pressurized wetted parts (less hardware)" — scope ambiguous. |
| 1.1-10 | TR1824/TR1826 (Welding and inspection) | **D** | HW | DEV-003 | Honeywell welds per ASME IX, not TR1826/NORSOK. Deviation request needed. |
| 1.1-11 | TR3023 (E&I installations offshore) | **D** | SF | DEV-011 | Not addressed by Honeywell. Sifab free-issue scope. |
| 1.1-12 | TR3032 (Field instrumentation) | **CR** | HW/SF | — | Not addressed in Honeywell proposal. |
| 1.1-13 | NORSOK E-001 (Electrical systems) | **D** | SF | DEV-011 | Not addressed by Honeywell. |
| 1.1-14 | NORSOK L-004 (Piping fabrication) | **D** | HW | DEV-003 | See welding deviation. |
| 1.1-15 | NORSOK M-101 (Structural steel fabrication) | **CR** | SF | — | Applies to Sifab structural work (frame modifications, lifting). |
| 1.1-16 | NORSOK M-501 (Surface preparation and coating) | **PC** | SF | DEV-004 | Sifab scope. |
| 1.1-17 | NORSOK M-601 (Welding and inspection of piping) | **D** | HW | DEV-003 | See welding deviation. |
| 1.1-18 | NORSOK M-630 (Piping Material Data Sheets) | **CR** | HW | DEV-009 | Flow tube to be min SS316 per MDS in NORSOK M-630. Honeywell to confirm MDS. |
| 1.1-19 | NORSOK R-002 (Lifting equipment) | **D** | SF | DEV-014 | Not addressed by Honeywell. Sifab engineering scope. |

---

## §1.2 — Area Classification

| # | RFQ Requirement | Status | Resp. | DEV | Remarks |
|---|----------------|--------|-------|-----|---------|
| 1.2-1 | ATEX Certified for Zone 1, IIA T3 minimum | **C** | HW | — | "ATEX certification considered." |
| 1.2-2 | Ingress Protection: min. IP66 | **D** | HW | DEV-001 | IP65 transmitters/JB, IP56 motor. Both below IP66. |

---

## §1.3 — Process & Design Data

| # | RFQ Requirement | Status | Resp. | DEV | Remarks |
|---|----------------|--------|-------|-----|---------|
| 1.3-1 | SVP sized for 67–750 m³/h | **C** | HW | — | SVP085 model covers this range. |
| 1.3-2 | Min. stroke time 1 second between switches | **CR** | HW | — | Not explicitly confirmed. To be verified in Honeywell datasheet. |
| 1.3-3 | Design pressure 49 barg | **C** | HW | — | CL600 rating exceeds 49 barg. |
| 1.3-4 | Design temperature -8°C to 106°C | **D** | HW | DEV-006 | Standard prover rated 60°C. High-temp option status unclear. |
| 1.3-5 | Repeatability ≤ 0.020% per API MPMS 4.2 | **C** | HW | — | "Repeatability 0.02%" confirmed. |
| 1.3-6 | Vendor to confirm noise, sizing, pressure drop report | **CR** | HW | — | Not mentioned in proposal. Standard deliverable to be confirmed. |

---

## §1.4 — Ambient Conditions

| # | RFQ Requirement | Status | Resp. | DEV | Remarks |
|---|----------------|--------|-------|-----|---------|
| 1.4-1 | Extreme max ambient: 25°C | **C** | HW | — | Within standard range. |
| 1.4-2 | Extreme min ambient: -7°C | **CR** | HW | — | May require nitrogen purge system (Honeywell option §6.6) to prevent shaft icing. To be confirmed. |
| 1.4-3 | Humidity 100%, highly saline/corrosive | **PC** | HW | DEV-001 | IP66 deviation affects protection against saline environment. |

---

## §1.5 — Motor

| # | RFQ Requirement | Status | Resp. | DEV | Remarks |
|---|----------------|--------|-------|-----|---------|
| 1.5-1 | Power: 230 VAC, 3-phase, 60 Hz | **PC** | HW | DEV-002 | 60 Hz verbally confirmed (23 Mar). Formal quote update pending. |
| 1.5-2 | ATEX Ex de or Ex e, entry to motor | **C** | HW | — | Explosion-proof motor included. |

---

## §1.6 — Connections

| # | RFQ Requirement | Status | Resp. | DEV | Remarks |
|---|----------------|--------|-------|-----|---------|
| 1.6-1 | Inlet/outlet: 12" ANSI B16.5 CL600 RTJ, Sch. 40S | **C** | HW | — | CL600 RTJ included. Schedule to be confirmed on GA. |
| 1.6-2 | Drain/vent: 1" ANSI B16.5 CL600 RTJ, Sch. 160 | **CR** | HW | — | Not specifically addressed. Standard for SVP085 to be confirmed. |
| 1.6-3 | Orientation: Upward/Upward | **CR** | HW | — | To be confirmed on GA drawing. |
| 1.6-4 | Tubing/fittings: Metric, VTA mm, Hoke Gyrolok | **CR** | HW/SF | — | Not addressed. May be Sifab free-issue scope. |
| 1.6-5 | 3× process thermowells: ½" NPTF, bore 6.5mm, TR2000 BD20X | **CR** | SF | — | Guidant free-issues temperature elements. Thermowells to be supplied — by whom? TR2000 material. |
| 1.6-6 | 1× rod thermowell: ½" NPTF, bore 6.5mm | **CR** | HW/SF | — | Scope assignment to be confirmed. |
| 1.6-7 | 1× process pressure take-off: ½" DB&B per VDS-MHBD102R, TR2000 BD20X | **CR** | SF | — | B&B valve listed as Sifab-supplied item. TR2000 compliance required. |
| 1.6-8 | Prover delivered without pressure transmitters | **C** | HW | — | "No Transmitters" confirmed. |
| 1.6-9 | Guidant free-issues temperature elements — vendor to install | **CR** | HW/SF | — | Installation responsibility to be confirmed (Honeywell at factory or Sifab in Norway). |

---

## §1.7 — Envelope

| # | RFQ Requirement | Status | Resp. | DEV | Remarks |
|---|----------------|--------|-------|-----|---------|
| 1.7-1 | Max module: W 1.4m × L 2.56m × H 2.2m | **D** | HW/SF | DEV-007 | Modules exceed limits. Transport plan developed. Formal deviation needed. |
| 1.7-2 | Lifting points and handling description per module | **D** | SF | DEV-014 | Not yet developed. NORSOK R-002 compliance needed. |
| 1.7-3 | Drawing showing size/weight of biggest/heaviest module | **PC** | HW | — | Honeywell provided frame drawing (44200419.PDF). Detailed split-module drawings pending. |

---

## §1.8 — Material

| # | RFQ Requirement | Status | Resp. | DEV | Remarks |
|---|----------------|--------|-------|-----|---------|
| 1.8-1 | Wetted/pressure parts per TR2000 BD20X | **D** | HW | DEV-009 | Honeywell states 316/316L. TR2000 compliance unconfirmed. |
| 1.8-2 | Flow tube min SS316 per NORSOK M-630 MDS | **C** | HW | — | 316 SST confirmed. MDS reference to be provided. |
| 1.8-3 | Sour service per NACE MR0175 / ISO 15156-3 | **C** | HW | — | "NACE" stated in proposal. |
| 1.8-4 | Atmospheric parts min SS316 | **C** | HW | — | "316 SST Offshore" throughout. |
| 1.8-5 | Structural frame SS316L | **C** | HW | — | Confirmed by Sidney (frame is 316SS). |
| 1.8-6 | Controller/interface box SS316 | **CR** | HW | — | Not explicitly stated. Standard for SVP085 to be confirmed. |
| 1.8-7 | Dissimilar metals separated with PTFE | **CR** | HW | — | Not addressed. |
| 1.8-8 | Cable glands SS316 or nickel-plated brass | **CR** | HW/SF | DEV-011 | Not addressed. |
| 1.8-9 | Tubing/fittings 6Mo per TR2000 MDS ST701/SF712 | **D** | SF | DEV-009 | Not in Honeywell scope. Sifab to supply as free-issue. |
| 1.8-10 | Instrument valves SS316 | **CR** | SF | — | Sifab scope (B&B valve). |
| 1.8-11 | PMI per TR1427 (10% SS316, 100% duplex/6Mo) | **PC** | HW | DEV-010 | "PMI on pressurized wetted parts (less hardware)" — ambiguous. |

---

## §1.9 — Painting

| # | RFQ Requirement | Status | Resp. | DEV | Remarks |
|---|----------------|--------|-------|-----|---------|
| 1.9-1 | Surface prep per TR0042 and NORSOK M-501 | **PC** | SF | DEV-004 | Sifab scope — painting in Norway after flow test. |
| 1.9-2 | Flow tube and process-wetted parts: System 6C | **PC** | SF | DEV-004 | Flow tube painting by Sifab in Norway. |
| 1.9-3 | SS structure: N/A | **C** | — | — | No painting required on SS structure per RFQ. |
| 1.9-4 | Approved coating brands per TR0042 | **CR** | SF | — | Sifab to select approved brand. |
| 1.9-5 | All parts under insulation to be painted | **C** | SF | — | Confirmed by Tom (23 Mar), including thermowells. |

---

## §1.10 — Electrical Requirements

| # | RFQ Requirement | Status | Resp. | DEV | Remarks |
|---|----------------|--------|-------|-----|---------|
| 1.10-1 | Cable glands per NORSOK E-001 and TR3023 | **D** | SF | DEV-011 | Sifab free-issue / Norwegian installation scope. |
| 1.10-2 | Cables BFOU type, halogen-free | **D** | SF | DEV-011 | Sifab free-issue scope. Lessons learned from Aker BP. |

---

## §1.11 — Fabrication

| # | RFQ Requirement | Status | Resp. | DEV | Remarks |
|---|----------------|--------|-------|-----|---------|
| 1.11-1 | Welding per TR1826 and NORSOK M-601 | **D** | HW | DEV-003 | ASME IX deviation. |
| 1.11-2 | Piping per NORSOK L-004 | **D** | HW | DEV-003 | See above. |
| 1.11-3 | Structural per NORSOK M-101 | **CR** | SF | — | Applies to Sifab structural work. |
| 1.11-4 | Procedures approved by Guidant before fabrication | **D** | HW | DEV-013 | Not addressed by Honeywell. Must be in PO. |
| 1.11-5 | SVP prepared for min 100mm insulation | **CR** | HW | DEV-015 | 100mm insulation around flow tube is confirmed requirement. Clearance for 12" flanges and vent/drain nozzles still unconfirmed. Frame dimensions must account for insulation thickness. |
| 1.11-6 | E&I per TR3023, NORSOK I-001, NORSOK E-001 | **D** | SF | DEV-011 | Sifab scope. |

---

## §1.12 — Testing Prover

| # | RFQ Requirement | Status | Resp. | DEV | Remarks |
|---|----------------|--------|-------|-----|---------|
| 1.12-1 | Gravimetric calibration at vendor factory | **C** | HW | — | FAT at Tempe, AZ included. |
| 1.12-2 | Test witnessed by Buyer, Contractor, End Client, Norwegian Authorities | **PC** | HW | DEV-008 | FAT can be witnessed (4 weeks notice). Norwegian Authority witnessing not addressed. |
| 1.12-3 | Water draw test at factory with Seraphin can | **C** | HW/SF | — | Confirmed — Seraphin can to be sent to TruStop (Tom, 23 Mar). |
| 1.12-4 | Repeatability ≤ 0.020% per API MPMS 4.2 | **C** | HW | — | Confirmed. |
| 1.12-5 | Water draw test after re-assembly on Snorre A | **D** | HW/SF | DEV-008 | SAT not included in Honeywell scope. Must be scoped/priced. |
| 1.12-6 | Hydrostatic 1.5× max design pressure BD20X | **CR** | HW | DEV-016 | Test pressure to be confirmed against BD20X. |

---

## §1.13 — Lifting

| # | RFQ Requirement | Status | Resp. | DEV | Remarks |
|---|----------------|--------|-------|-----|---------|
| 1.13-1 | Lifting lugs/points per NORSOK R-002 | **CR** | SF | DEV-014 | To be clarified. |

---

## §1.14 — Instrument Tagging

| # | RFQ Requirement | Status | Resp. | DEV | Remarks |
|---|----------------|--------|-------|-----|---------|
| 1.14-1 | SS316 nameplate with CE marking and tag | **CR** | HW | — | Not explicitly addressed. Standard for Honeywell to be confirmed. |
| 1.14-2 | Individual instruments with separate SS316 tag signs | **CR** | HW/SF | — | To be confirmed. |

---

## §1.15 — Spare Parts

| # | RFQ Requirement | Status | Resp. | DEV | Remarks |
|---|----------------|--------|-------|-----|---------|
| 1.15-1 | Option: commissioning and 2-year operation spares | **C** | HW | — | Recommended 2-year spares kit included (optical switches, motor stop switch, relay, seal kit). Pricing in distributor proposal. |

---

## §1.16 — Document Deliverables

| # | Document | Due | Status | Resp. | Remarks |
|---|----------|-----|--------|-------|---------|
| 1.16-1 | Production plan and progress report | 2 WAO | **CR** | HW | In standard package? |
| 1.16-2 | Quality & Inspection Plan | 2 WAO | **CR** | HW | In standard package? |
| 1.16-3 | Vendor document schedule | 2 WAO | **CR** | HW | In standard package? |
| 1.16-4 | GA drawings, split-module drawings, 3D model, interface list | 4 WAO | **PC** | HW | GA available. Split-module drawings pending. |
| 1.16-5 | GA water draw panel | 4 WAO | **CR** | SF | Sifab/Flowtec scope. |
| 1.16-6 | GA Seraphin can + cabinet | 4 WAO | **CR** | SF | Sifab/Pemberton scope. |
| 1.16-7 | Surface treatment procedure | 4 WAO | **CR** | SF | Sifab scope (NORSOK M-501). |
| 1.16-8 | NORSOK datasheets (prover, thermowells, motor, switches) | 4 WAO | **CR** | HW/SF | Likely not in Honeywell standard package. |
| 1.16-9 | Wake frequency calcs (thermowells) | 4 WAO | **CR** | SF | Thermowell supplier to provide. |
| 1.16-10 | Wiring diagram | 4 WAO | **CR** | HW | In standard package? |
| 1.16-11 | NDE operator certs | 4 WAO | **CR** | HW | In standard package? |
| 1.16-12 | Monthly progress report | 4 WAO | **CR** | HW | To be included in PO. |
| 1.16-13 | NDE procedure | 8 WAO | **CR** | HW | In standard package? |
| 1.16-14 | FAT/calibration procedure | 8 WAO | **C** | HW | FAT included. |
| 1.16-15 | SAT/water draw procedure | 8 WAO | **D** | HW/SF | DEV-008 — SAT not included. |
| 1.16-16 | Pressure test procedure | 8 WAO | **CR** | HW | Standard deliverable. |
| 1.16-17 | ATEX certificates (mech + elec) | 8 WAO | **C** | HW | ATEX included. |
| 1.16-18 | Welder certs, WPS, WPQ | 8 WAO | **CR** | HW | In standard package? |
| 1.16-19 | Weld record sheet | 8 WAO | **CR** | HW | In standard package? |
| 1.16-20 | SPIR w/prices and GA cross-refs | 8 WAO | **CR** | HW | In standard package? |
| 1.16-21 | Operating manual | WD | **C** | HW | Available online + shipped. |
| 1.16-22 | Maintenance manual | WD | **C** | HW | Available online + shipped. |
| 1.16-23 | EC Declaration of Conformity | WD | **C** | HW | PED/ATEX CE marking included. |
| 1.16-24 | EN 10204:2004 3.1 material certs | WD | **C** | HW | "Material certifications from suppliers in as-received condition." |
| 1.16-25 | PMI report | WD | **PC** | HW | DEV-010 — scope ambiguous. |
| 1.16-26 | NDE reports | WD | **CR** | HW | In standard package? |
| 1.16-27 | FAT/calibration test report | WD | **C** | HW | Included with FAT. |
| 1.16-28 | SAT/water draw report (Snorre A) | WD | **D** | HW/SF | DEV-008 — SAT not included. |
| 1.16-29 | Pressure test report | WD | **CR** | HW | Standard deliverable. |
| 1.16-30 | Surface treatment/coating report | WD | **CR** | SF | Sifab scope. |
| 1.16-31 | Weighing report | WD | **CR** | HW | In standard package? |
| 1.16-32 | Preservation report | WD | **CR** | SF | Sifab scope. |

---

## Compliance Summary

| Status | Count | % |
|--------|-------|---|
| **Comply (C)** | 23 | 28% |
| **Partially Comply (PC)** | 11 | 13% |
| **Deviate (D)** | 18 | 22% |
| **Clarification Required (CR)** | 31 | 37% |
| **Total requirements** | 83 | 100% |

### Key Actions Required

1. **Honeywell must respond to 8 HIGH deviations** (IP66, warranty, temperature, welding, materials, SAT, modules, payment)
2. **37% of requirements need clarification** — most relate to Honeywell's standard package vs. RFQ-specific needs
3. **Sifab scope items** (painting, electrical, lifting, Seraphin can, documents) are understood but need formal scoping
4. **Back-to-back terms** must be established before PO to Honeywell — warranty, payment, liability
5. **Formal deviation requests** needed for welding (ASME vs NORSOK) and module envelope before contract award
