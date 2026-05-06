# Deviation List — SP-01415 Snorre A Small Volume Prover

| Field | Value |
|-------|-------|
| **RFQ No.** | GM-8501-1447 |
| **Sifab Project** | SP-01415 |
| **Client** | Guidant (Measurement Solutions Norway AS) |
| **End Client** | Equinor — Snorre A |
| **Honeywell Proposal** | 10465986-O-1010834 R0, dated 20 March 2026 |
| **Prepared by** | Sifab AS |
| **Date** | 2026-03-23 |
| **Revision** | 0 |

> **Note:** Sifab AS acts as system integrator and intermediary between Guidant and Honeywell. Deviations are documented to ensure full transparency. Sifab does not accept technical risk for items outside its scope — risk sits with the party responsible for the deliverable.

---

## DEV-001: Ingress Protection — IP65/IP56 vs. IP66

| Field | Detail |
|-------|--------|
| **RFQ Ref** | §1.2 Area Classification |
| **RFQ Requirement** | Ingress Protection: min. IP66 |
| **Honeywell Offer** | IP65 for transmitters and junction boxes; IP56 for motor |
| **Deviation** | IP65 and IP56 are both below the required IP66. IP65 lacks protection against powerful water jets; IP56 lacks full dust protection. |
| **Risk** | Non-compliance with Equinor/Norsok requirements for Zone 1 offshore environment. Highly saline and corrosive ambient (RFQ §1.4). |
| **Risk Owner** | Honeywell (prover manufacturer) |
| **Proposed Resolution** | Honeywell to confirm if IP66-rated alternatives are available for motor and junction boxes, with any price/schedule impact. If not possible, a formal deviation request must be submitted to Guidant/Equinor for acceptance. **Sifab does not accept risk on this item.** |

---

## DEV-002: Motor Frequency — 50 Hz vs. 60 Hz

| Field | Detail |
|-------|--------|
| **RFQ Ref** | §1.5 Motor |
| **RFQ Requirement** | 230 VAC, 3-phase, 60 Hz |
| **Honeywell Offer** | Initially quoted 50 Hz |
| **Status (23 Mar)** | Sidney Swart confirmed 60 Hz is possible with "no USD impact" (e-mail 23 Mar 09:03). Earlier message said "small price change." Formal confirmation and updated spec pending. |
| **Deviation** | Quote and technical spec still show 50 Hz. Needs formal update. |
| **Risk Owner** | Honeywell |
| **Proposed Resolution** | Honeywell to issue updated proposal confirming 60 Hz motor with final pricing. Sifab to pass through any adder to Guidant. |

---

## DEV-003: Welding Standards — ASME vs. NORSOK/TR

| Field | Detail |
|-------|--------|
| **RFQ Ref** | §1.11 Fabrication |
| **RFQ Requirement** | Welding per TR1826, NORSOK M-601 (Welding and inspection of piping), NORSOK L-004 (Piping fabrication). |
| **Honeywell Offer** | "Pressure containing welds are welded by a certified welder as per ASME BPV code section IX." (Proposal §9, Deviations) |
| **Deviation** | Honeywell welds per ASME IX, not NORSOK M-601 / TR1826. This is a known deviation — same approach was used on previous Aker BP provers (SP-00525/SP-00577) via project deviation request. |
| **Risk Owner** | To be accepted by Guidant/Equinor via formal deviation request |
| **Proposed Resolution** | Submit project deviation request to Guidant for flow tube welding, referencing Aker BP precedent. Honeywell to provide ASME IX WPS/WPQ documentation for Guidant/Equinor review and acceptance. **Sifab does not carry welding risk — Honeywell is the welder of record for the flow tube.** |

---

## DEV-004: NORSOK Painting — Excluded from Honeywell Scope

| Field | Detail |
|-------|--------|
| **RFQ Ref** | §1.9 Painting |
| **RFQ Requirement** | All surface preparation and protection per TR0042 and NORSOK M-501. Flow tube and process-wetted parts: System 6C. |
| **Honeywell Offer** | "NORSOK Painting not included in this proposal: Sifab does agree to source this locally." |
| **Deviation** | Honeywell delivers prover without NORSOK M-501 coating. Sifab will source painting locally in Norway after flow test. Motor and gearbox delivered with Honeywell offshore paint — Tom has requested exemption from NORSOK remaling for these items (mounted under protective cover). |
| **Risk Owner** | Sifab (for local painting execution), Guidant/Equinor (for motor/gearbox paint exemption acceptance) |
| **Proposed Resolution** | (a) Sifab to arrange NORSOK M-501 System 6C painting of flow tube and wetted parts at Norwegian workshop after flow test. Cost included in Sifab quote. (b) Motor/gearbox: Honeywell to provide painting certificates/procedures. Formal deviation request to Guidant if Equinor acceptance is needed. (c) All parts under insulation to be painted — confirmed by Tom (23 Mar), including thermowells. |

---

## DEV-005: Warranty — 24 Months vs. 28 Months After Installation

| Field | Detail |
|-------|--------|
| **RFQ Ref** | §1 Scope of Supply |
| **RFQ Requirement** | "Warranty of the SVP shall be valid from the date that the vendor of the SVP has fully assembled and released the SVP for use on site." + Guidant requirement: min. 28 months after installation at platform. |
| **Honeywell Offer** | "Our standard warranty on Small Volume Provers of 24 months after delivery applies." + "Warranty only covers parts, excluded are wearable parts and labor." + "Commissioning by persons not approved by Honeywell will result in limited warranty." |
| **Deviation** | (a) Honeywell warranty starts at delivery, not platform installation. (b) Honeywell standard is 24 months, not 28 months. (c) Honeywell excludes labor and wearable parts. |
| **Risk Owner** | Sifab warranty to Guidant must match RFQ terms. Gap between Honeywell's 24m from delivery and Guidant's 28m from installation creates risk exposure for Sifab. |
| **Proposed Resolution** | Tom confirmed warranty is included "as long as Honeywell Enraf supervisor is present for disassembly/reassembly." This must be formalized: (a) Honeywell to confirm in writing extended warranty terms aligned with project timeline. (b) Alternatively, explore Honeywell Extended Warranty Agreement (EWA) as referenced in their proposal. (c) **Sifab must not accept warranty responsibility beyond what Honeywell provides — back-to-back warranty terms required.** |

---

## DEV-006: Temperature Rating — Standard 60°C vs. Design 106°C

| Field | Detail |
|-------|--------|
| **RFQ Ref** | §1.3 Process Data / PDS S1-AA-PDE-0219 |
| **RFQ Requirement** | Design temperature: -8°C to 106°C. Operating temperature: 55–57°C. |
| **Honeywell Offer** | "Honeywell Standard approved up to 60°C. Honeywell has +60°C." High Temperature Insulation option listed (§6.5): insulation plate between drive unit and flow tube + insulation jacket. |
| **Deviation** | Standard prover is rated to 60°C. Design temperature of 106°C requires the high-temperature option. It is unclear whether this option is included in the quoted price or is an adder. |
| **Risk Owner** | Honeywell (to confirm inclusion) |
| **Proposed Resolution** | Honeywell to confirm that high-temperature option (insulation plate + jacket) is included in the quoted SVP085 price. If it is an adder, provide pricing. **This is critical — operating at 55–57°C is within standard range, but design temperature of 106°C is not.** |

---

## DEV-007: Modular Split — Module Dimensions Exceed RFQ Envelope

| Field | Detail |
|-------|--------|
| **RFQ Ref** | §1.7 Envelope |
| **RFQ Requirement** | Max module size: W 1.4m × L 2.56m × H 2.2m |
| **Honeywell Offer** | Two-piece main frame. Total frame length: 5,258mm (~2.7m per half). Frame width: ~1.6m. Flow tube: 2.6–2.7m without end flanges. Flow tube weight: ~3,500 kg. |
| **Deviation** | (a) Frame half-length (~2.7m) exceeds L limit of 2.56m. (b) Frame width (1.6m) exceeds W limit of 1.4m. (c) Flow tube length (~2.6m) exceeds L limit. The transport plan relies on rotating modules 90° to reduce effective width to ~30cm, and accepting the ~14cm length overrun. |
| **Risk Owner** | Guidant/Equinor (must accept transport plan), Sifab (execution), Honeywell (frame design) |
| **Proposed Resolution** | Guidant/Equinor have verbally acknowledged the split concept and said "dette med splitt av ramme må gå fint" (18 Mar). However, formal acceptance is needed: (a) Honeywell/Sifab to provide detailed split-module drawings showing dimensions and weights per module. (b) Formal deviation request for modules exceeding the stated envelope. (c) Transport method documentation (trolley, handling procedure) to be developed. |

---

## DEV-008: SAT / Commissioning / Third-Party Inspection — Not Included

| Field | Detail |
|-------|--------|
| **RFQ Ref** | §1.12 Testing Prover |
| **RFQ Requirement** | Gravimetric calibration witnessed by Buyer, Contractor, End Client, Norwegian Authorities. Water draw test at factory with Seraphin can. Repeatability ≤ 0.020%. Water draw test after re-assembly on Snorre A. |
| **Honeywell Offer** | "SAT, commissioning and third-party inspection were not included." FAT at Tempe, AZ is included. |
| **Deviation** | (a) No SAT included. (b) No commissioning support included. (c) Third-party inspection not included. (d) Witnessed tests by Norwegian Authorities not addressed. (e) Re-assembly water draw test on Snorre A not included. |
| **Risk Owner** | Must be scoped and priced — either by Honeywell (supervision) or Sifab/third party |
| **Proposed Resolution** | (a) Honeywell supervision for re-assembly and SAT on Snorre A to be quoted separately (Tom has requested rates from Sidney — pending). (b) Justervesenet / Norwegian Authority witnessing arrangements to be coordinated. (c) Flow test in Norway (Guidant's requirement) to be coordinated and scoped. **Sifab must not accept responsibility for test results — Honeywell supervisor must be present.** |

---

## DEV-009: Materials — TR2000 BD20X Compliance Unconfirmed

| Field | Detail |
|-------|--------|
| **RFQ Ref** | §1.8 Material |
| **RFQ Requirement** | Wetted/pressure-containing parts per Equinor TR2000 PCS BD20X (Plant SNA). Sour service per NACE MR0175 / ISO 15156-3. Tubing/fittings: 6Mo per TR2000 MDS ST701/SF712. |
| **Honeywell Offer** | "MOC: Process Fluid Wetted Parts: AISI 316/316L (UNS31600/UNS31603)." ATEX and NACE compliance stated. No reference to TR2000 BD20X or 6Mo tubing. |
| **Deviation** | (a) Honeywell does not reference TR2000 BD20X — unclear if their 316/316L meets Equinor's specific MDS requirements. (b) 6Mo tubing/fittings not addressed. (c) Sour service (NACE MR0175) stated but not linked to TR2000 requirements. |
| **Risk Owner** | Honeywell (material compliance) |
| **Proposed Resolution** | (a) Honeywell to confirm that their SS316/316L meets or exceeds TR2000 BD20X MDS requirements, or identify specific gaps. (b) 6Mo tubing and fittings: clarify if Sifab will supply these as free-issue items (similar to Aker BP provers). (c) If deviations exist, submit formal deviation request to Guidant/Equinor. |

---

## DEV-010: PMI Scope — "Less Hardware" Ambiguity

| Field | Detail |
|-------|--------|
| **RFQ Ref** | §1.8 Material (PMI per TR1427) |
| **RFQ Requirement** | PMI per TR1427: min. 10% for SS316 wetted/pressure parts; 100% for duplex and 6Mo. |
| **Honeywell Offer** | "PMI on pressurized wetted parts (less hardware)" |
| **Deviation** | "Less hardware" is ambiguous — unclear what is excluded from PMI. TR1427 requires 10% minimum on SS316. |
| **Risk Owner** | Honeywell |
| **Proposed Resolution** | Honeywell to clarify PMI scope and confirm compliance with TR1427 requirements. |

---

## DEV-011: Electrical — NORSOK E-001 / TR3023 / Cable Type Not Addressed

| Field | Detail |
|-------|--------|
| **RFQ Ref** | §1.10 Electrical Requirements |
| **RFQ Requirement** | Cable glands per NORSOK E-001 and TR3023. Cables to be BFOU type, halogen-free. |
| **Honeywell Offer** | Not addressed in proposal. |
| **Deviation** | No mention of NORSOK E-001, TR3023, BFOU cables, or halogen-free requirements. Lessons learned from Aker BP provers showed cabling and connections had to be re-done in Norway. |
| **Risk Owner** | Sifab (if supplying cables/glands as free-issue), Honeywell (if included in their scope) |
| **Proposed Resolution** | Based on Aker BP experience, Sifab will likely supply NORSOK-compliant cables, glands, and cable trays as free-issue items for Honeywell installation or Sifab installation in Norway. This must be explicitly scoped and priced. |

---

## DEV-012: Document Deliverables — Standard Package vs. RFQ Requirements

| Field | Detail |
|-------|--------|
| **RFQ Ref** | §1.16 Documents Required |
| **RFQ Requirement** | Extensive list of 30+ documents with specific delivery timelines (2 WAO, 4 WAO, 8 WAO, With Delivery). |
| **Honeywell Offer** | "Standard documentation package shipped within 2 weeks of SVP shipment." + "If additional documents are required that are not part of the Standard Document Package there will be a charge." |
| **Deviation** | RFQ requires many documents that are likely outside Honeywell's standard package (surface treatment procedure, NORSOK datasheets, wake frequency calcs, NDE certs, weld records, SPIR, SAT report, coating report, weighing report, preservation report). Delivery timeline requirements (2/4/8 WAO) may not align with Honeywell's standard schedule. |
| **Risk Owner** | Honeywell (for their standard documents), Sifab (for Norsok-specific additions) |
| **Proposed Resolution** | (a) Map Honeywell's standard doc package against RFQ §1.16 to identify gaps. (b) Request Honeywell pricing for additional documentation if required. (c) Sifab to produce Norsok-specific documents (NORSOK datasheets, surface treatment procedures, etc.) for items in their scope. |

---

## DEV-013: Fabrication Procedures — Guidant Approval Not Addressed

| Field | Detail |
|-------|--------|
| **RFQ Ref** | §1.11 Fabrication |
| **RFQ Requirement** | "Procedures and qualifications to be approved by Guidant prior to fabrication." |
| **Honeywell Offer** | Not addressed. Honeywell proposal states "Customer reference standards must be part of RFQ, otherwise Honeywell standard built is applicable!" |
| **Deviation** | Honeywell does not commit to submitting procedures for Guidant approval before starting fabrication. |
| **Risk Owner** | Schedule risk if Guidant review delays production start |
| **Proposed Resolution** | Include in PO to Honeywell: all welding, NDE, and fabrication procedures to be submitted to Guidant via Sifab for approval before manufacturing clearance. Allow adequate review time in schedule. |

---

## DEV-014: Lifting Lugs — NORSOK R-002 Not Addressed

| Field | Detail |
|-------|--------|
| **RFQ Ref** | §1.13 Lifting |
| **RFQ Requirement** | Lifting lugs/points shall comply with NORSOK R-002. |
| **Honeywell Offer** | Not addressed. |
| **Deviation** | To be clarified. |
| **Risk Owner** | To be clarified |
| **Proposed Resolution** | To be clarified during engineering phase. |

---

## DEV-015: 100mm Insulation Clearance — Unconfirmed

| Field | Detail |
|-------|--------|
| **RFQ Ref** | §1.11 Fabrication |
| **RFQ Requirement** | "The SVP shall be prepared for min. 100mm insulation." The flow tube shall have 100mm insulation. |
| **Status** | Tom confirmed this does not affect price but is "a bit uncertain regarding the 12" in/out flanges and length of vent/drain flanges." To be resolved in engineering. Confirmed: 100mm insulation around flow tube is required. |
| **Deviation** | Not confirmed whether prover layout allows 100mm insulation around all components, particularly 12" RTJ flanges and vent/drain nozzles. The flow tube must accommodate 100mm insulation — frame and structural clearances must account for this. |
| **Risk Owner** | Honeywell (prover design), Sifab (frame/structural design) |
| **Proposed Resolution** | Engineering review required — Honeywell to confirm in GA drawings that all process connections and flow tube allow 100mm insulation clearance. Frame design must account for 100mm insulation thickness around the flow tube when determining overall module dimensions. |

---

## DEV-016: Hydrostatic Test Pressure — BD20X Reference

| Field | Detail |
|-------|--------|
| **RFQ Ref** | §1.12 Testing Prover |
| **RFQ Requirement** | "Hydrostatic: 1.5 times the max design pressure of PCS BD20X" |
| **Honeywell Offer** | Not specifically addressed. Standard Honeywell testing per API MPMS 4.2 and PED. |
| **Deviation** | The max design pressure per BD20X for CL600 may differ from Honeywell's standard test pressure. PDS shows 49 barg design pressure → hydro test would be 73.5 barg. |
| **Risk Owner** | Honeywell |
| **Proposed Resolution** | Honeywell to confirm hydrotest pressure and that it meets 1.5× BD20X max design pressure. If Honeywell tests at CL600 rating (which is higher), this should be sufficient — but must be documented. |

---

## DEV-017: Seraphin Can — Justervesenet Certification

| Field | Detail |
|-------|--------|
| **RFQ Ref** | §1 Scope of Supply |
| **RFQ Requirement** | "Certification shall be performed by Justervesenet. The Seraphin shall be delivered inside a suitable SS316 cabinet." |
| **Honeywell Offer** | Not in Honeywell scope — Sifab to source from Pemberton. |
| **Deviation** | N/A (Sifab scope, not a Honeywell deviation). But: Justervesenet certification lead time must be managed. |
| **Risk Owner** | Sifab (procurement and certification) |
| **Proposed Resolution** | Sifab to source Seraphin can from Pemberton and arrange Justervesenet certification. SS316 cabinet to be fabricated by Sifab in Norway with forklift lifting arrangement (confirmed by Tom). Lead time to be confirmed. |

---

## DEV-018: Payment Terms — 30% Down Payment vs. Guidant T&C

| Field | Detail |
|-------|--------|
| **RFQ Ref** | Guidant T&C (PP-PS-13) |
| **RFQ Requirement** | Per Guidant General Terms & Conditions |
| **Honeywell Offer** | 30% non-refundable down payment required for order acceptance. 30 days net from invoice. |
| **Deviation** | Honeywell requires 30% upfront before production starts. Guidant T&C may have different payment milestones. |
| **Risk Owner** | Sifab (cash flow risk if Guidant pays later than Honeywell requires) |
| **Proposed Resolution** | **Sifab must align payment terms: Guidant milestone payments should cover or precede Honeywell's 30% down payment.** Do not pre-finance Honeywell on Sifab's own account. Back-to-back payment structure required. |

---

## Summary

| # | Deviation | Severity | Status |
|---|-----------|----------|--------|
| DEV-001 | IP65/IP56 vs IP66 | **HIGH** | Open — needs Honeywell response |
| DEV-002 | Motor 50 Hz vs 60 Hz | MEDIUM | Verbally resolved — needs formal update |
| DEV-003 | Welding ASME vs NORSOK | **HIGH** | Deviation request needed (Aker BP precedent) |
| DEV-004 | NORSOK painting excluded | MEDIUM | Sifab scope — accepted |
| DEV-005 | Warranty 24m delivery vs 28m installation | **HIGH** | Needs back-to-back warranty agreement |
| DEV-006 | Temperature 60°C std vs 106°C design | **HIGH** | Needs Honeywell confirmation |
| DEV-007 | Module size exceeds envelope | **HIGH** | Verbally accepted — needs formal deviation |
| DEV-008 | SAT/commissioning not included | **HIGH** | Needs scoping and pricing |
| DEV-009 | TR2000 BD20X compliance unconfirmed | **HIGH** | Needs Honeywell confirmation |
| DEV-010 | PMI scope ambiguous | MEDIUM | Needs clarification |
| DEV-011 | Electrical NORSOK not addressed | MEDIUM | Sifab free-issue scope |
| DEV-012 | Document package incomplete | MEDIUM | Needs gap analysis |
| DEV-013 | Fabrication procedure approval | MEDIUM | Include in PO |
| DEV-014 | Lifting NORSOK R-002 | MEDIUM | To be clarified |
| DEV-015 | 100mm insulation clearance | LOW | Engineering phase |
| DEV-016 | Hydrotest pressure | LOW | Needs confirmation |
| DEV-017 | Seraphin can Justervesenet | LOW | Sifab scope — on track |
| DEV-018 | Payment terms 30% down | **HIGH** | Back-to-back required |

**HIGH severity items: 8 | MEDIUM: 7 | LOW: 3**
