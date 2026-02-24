# INTERNAL NOTE — Snorre A SVP085 Project Cautions
# Lessons from SP-00525 (Hugin A / SVP050) & SP-00577 (Valhall Fenris / SVP015)

**Classification:** Internal — Sifab AS only
**Prepared by:** Sifab Engineering Team
**Date:** 2026-02-24
**Purpose:** Ensure a smooth project execution by documenting every issue from the two previous prover projects and defining preventive actions for Snorre A.

---

## EXECUTIVE SUMMARY

The NOA/Valhall projects (total value USD 1.57M) were delivered successfully but experienced:
- **USD 57k in variation orders** (3.8% cost growth)
- **20 months total duration** (vs. ~12 months planned)
- **6 months of documentation tail** after physical completion
- **23–25 punch list items per prover** at factory inspection
- **14 quality concerns** requiring rework after delivery to Norway
- **50–60 documents stuck in client approval queue** for months
- **Cash flow gap of ~USD 500k** for 6+ months due to milestone structure

The Snorre A project adds new complexity: **modular split** (max 1.4×2.56×2.2m modules), **offshore re-assembly**, **higher pressure class** (CL 600 vs CL 300), and a **different client chain** (Guidant/Equinor vs FMC/Aker BP).

---

## 1. PROJECT MANAGEMENT — Schedule & Coordination

### 1.1 Critical Path Warning
| Phase | NOA/Valhall Duration | Snorre A Estimate | Risk |
|-------|---------------------|-------------------|------|
| PO to FAT | 10 months | 12+ months (larger prover) | SVP085 has longer manufacturing lead |
| FAT to delivery | 2 months | 3+ months (modular split disassembly) | New scope: split + pack in Norway |
| Delivery to closeout | 6 months (documentation) | 6+ months | Always the long tail |
| **Total** | **~20 months** | **~22+ months** | Budget accordingly |

### 1.2 Caution Items

**C-PM-01: Document approval bottleneck.**
On NOA/Valhall, 50–60 Sifab-submitted documents sat unapproved at FMC for months. This blocked the final milestone payment (10%) and delayed closeout by 6 months.
- **Action:** Establish a document tracker with Guidant from Week 1. Agree on maximum 2-week review cycle. Escalation procedure after 3 weeks.

**C-PM-02: "Need dates" for free-issue parts were undefined.**
The Honeywell RAIL tracker showed most delivery dates as "TBD" months after kick-off. This caused parts arriving late and factory production holds.
- **Action:** Issue a complete free-issue parts schedule at kick-off with firm need-dates. Lock down all dates within 2 weeks of PO.

**C-PM-03: Tagging IDs arrived 14 months late.**
FMC was asked for tagging IDs in Feb 2023 — not delivered until April 2024. This blocked GA drawing approvals and name plate production.
- **Action:** Request tag numbers from Guidant as a condition of PO acknowledgment. Do not start detailed engineering without confirmed tags.

**C-PM-04: Wiring diagram responsibility was unclear.**
Originally assigned to Sifab, then shifted to FMC, then back. The diagram was still incomplete at 10 months into the project.
- **Action:** Define in the contract who produces the wiring diagram. If Honeywell, get it within 4 WAO.

**C-PM-05: Buyer entity may change mid-project.**
On NOA/Valhall, the buyer changed from FMC Kongsberg to Measurement Solutions Norway AS mid-project, requiring new POs and administrative rework.
- **Action:** Confirm Guidant's legal entity and ensure the contract allows PO transfer without delay.

---

## 2. COMMERCIAL & FINANCIAL

### 2.1 Pricing Reference

| Item | Hugin A (SVP050) | Valhall (SVP015) | Snorre A (SVP085) Est. |
|------|-------------------|-------------------|------------------------|
| Prover unit | USD 718,333 | USD 436,521 | USD 900k–1.1M (larger, CL 600, Duplex) |
| Spare parts (2yr) | USD 13,691 | USD 13,039 | ~USD 15k |
| Seraphin can | USD 34,303 | USD 30,023 | ~USD 40k (larger volume) |
| Water draw kit | USD 18,054 | USD 17,308 | ~USD 20k (use 1" from start) |
| PM + documentation | USD 28,034 | USD 28,034 | ~USD 35k |
| Shipping (air, AZ→NO) | USD 40,000 | USD 30,000 | ~USD 45k (larger crate) |
| Painting (M-501 6C) | USD 10,500 | USD 9,250 | ~USD 15k |
| Extended warranty | USD 66,000 | USD 44,000 | ~USD 70k |
| **Modular split engineering** | N/A | N/A | **USD 50–100k (NEW)** |
| **Offshore re-assembly** | N/A | N/A | **USD 80–150k (NEW)** |
| **VOR contingency** | USD 31,438 | USD 25,408 | **USD 40k minimum** |

### 2.2 Caution Items

**C-FIN-01: Gross margin was 19% at quote, dropped to ~14.5% after negotiation.**
The client negotiated a 5.5% discount from the original quote. Then VOR costs eroded margin further.
- **Action:** Build VOR contingency into the quote (min 5% of total). Protect margin on high-uncertainty items (shipping, painting, modular split).

**C-FIN-02: Cash flow gap of ~USD 500k for 6 months.**
The 40/50/10 milestone structure left Sifab carrying significant unbilled work from Q3 2023 to Q1 2024.
- **Action:** Negotiate a more granular milestone structure: 30/20/20/20/10 or similar. Monthly progress invoicing if possible.

**C-FIN-03: Bank financing was required.**
The bid review flagged that bank financing needed to be arranged for projects over 1 MNOK.
- **Action:** Arrange credit facility before PO acceptance. SVP085 project value likely exceeds NOK 15M.

**C-FIN-04: "Quotation = PO specification" clause.**
The cover page stated that the supplier quotation becomes the PO specification. Every word in the bid letter is contractually binding.
- **Action:** Ensure the quote is precise with no TBA/TBD items. Every deviation must be explicitly stated. Include a limitations/exclusions section.

**C-FIN-05: Liquidated damages exposure.**
NOA/Valhall had LD exposure (reduced by negotiation). Snorre A likely will too.
- **Action:** Negotiate LD cap (e.g., max 10% of contract value). Define clear force majeure and client-delay relief provisions.

**C-FIN-06: US tariff risk.**
The SP-01415 bid notes flag potential US tariffs affecting Honeywell's pricing.
- **Action:** Get Honeywell's quote with tariff exposure clearly allocated. Include tariff escalation clause in our quote to Guidant.

**C-FIN-07: Shipping cost uncertainty.**
Air freight from Arizona to Norway was USD 30–40k but highly variable. NOA/Valhall even proposed cost-plus-5% as alternative.
- **Action:** Get firm shipping quote from Honeywell. Consider sea freight (6–8 weeks, significantly cheaper) if schedule permits.

---

## 3. COATING & SURFACE TREATMENT

### 3.1 The Single Most Important Technical Lesson

**TSA (System 2A/2C) MUST NOT be applied to the prover flow tube.**

Honeywell formally wrote (2 Feb 2023) that the molten aluminium spray reaches +2000°C and will:
- Deform the roundness of the precision-machined flow tube
- Damage the hard chrome internal surface
- Cause piston seal failure and calibration failure

**The correct system is 6C** per NORSOK M-501 — applicable for insulated stainless steel vessels below 150°C.

### 3.2 Caution Items

**C-COAT-01: Desert Coating in Arizona had no NORSOK experience.**
At the PPM (Jan 2024), it was discovered that the painting contractor had never done NORSOK-compliant work before. Operator qualification testing per M-501 §10.2.3 was required.
- **Action:** Verify Desert Coating's NORSOK qualification status before committing. If expired, allow time for re-qualification.

**C-COAT-02: Painting procedure approval chain is the longest bottleneck.**
On NOA/Valhall, the painting procedure had to go from Desert Coating → Sifab → FMC → Aker BP. This delay froze motor supply and caused potential Honeywell factory charges.
- **Action:** Submit painting procedure (6C) to Guidant/Equinor within 2 WAO. Get pre-approval before FAT scheduling.

**C-COAT-03: The coating spec for the skid frame is separate from the flow tube.**
The RFQ requires TR0042 / M-501 for all surfaces. Confirm the frame (SS 316L) uses 6A or 6C — not 2A.
- **Action:** Define coating system for each component (flow tube, skid frame, thermowells, adapters) in the initial technical submission.

**C-COAT-04: Polyurethane-based paints are forbidden by Equinor.**
Aker BP's additional requirements (53-000778) explicitly prohibit isocyanate-based paints.
- **Action:** Verify all paint products are polyurethane-free. Obtain SDS sheets for Guidant/Equinor review.

---

## 4. ELECTRICAL & INSTRUMENTATION

### 4.1 Factory Workmanship — The Biggest Quality Risk

The Honeywell/TruStop factory in Tempe, Arizona produced **systematic electrical workmanship failures** on both NOA/Valhall provers. Sifab's inspection found 14 quality issues, and the formal electrical report (BluElectro) confirmed the extent.

### 4.2 Caution Items

**C-EI-01: TruStop does not understand NORSOK offshore electrical standards.**
They had never handled cable braid armour before, used wrong ferrule sizes, wrong material grades (SS 304 vs 316), wrong bolt types in cable trays, and wrong wiring polarity.
- **Action:** Prepare a **Factory Instruction Package** with step-by-step visual instructions for:
  - Cable braid splitting and grounding
  - Ferrule selection chart (color-coded by wire size)
  - SS 316 specification for all hardware
  - Round-head bolts only inside cable trays
  - Cable routing standards (max 10D unsupported length)
  - Blue sleeve marking requirements

**C-EI-02: Cable tray sizing was inadequate.**
Trays were too small for the number of cables, forcing 4-wide stacking instead of 2×2, causing damage at bends.
- **Action:** Specify cable tray dimensions with 30% margin in the GA review. Require Honeywell to submit cable tray layout drawing for approval.

**C-EI-03: Heat shrink inside cable glands creates water ingress path.**
Found on "many of the cables." On an offshore platform this leads to corrosion and instrument failure.
- **Action:** Include in Factory Instruction Package: NO heat shrink between cable and gland gasket.

**C-EI-04: 3 cables per prover could not be megger tested.**
Due to inability to disconnect, 3 cables on each unit were not verified for insulation resistance.
- **Action:** Design all cable terminations to allow individual disconnection for megger testing.

**C-EI-05: "Volvo list" (edge protection) term was unknown to TruStop.**
The factory didn't understand Scandinavian electrical terminology.
- **Action:** Use generic terms in all specifications. Replace "Volvo list" with "SS 316 cable tray edge protection strip" and provide photos.

**C-EI-06: ATEX JB type confusion (Ex d vs Ex e vs Ex i).**
Initially specified as Exe, corrected to Exi 8 months later. The February kick-off said Exe; the September meeting said Exi.
- **Action:** Lock down ATEX certification approach at the quote stage. For Snorre A, Honeywell proposes standard Ex D controller — confirm this eliminates the JB type issue.

**C-EI-07: Cable transport damage from Arizona.**
One optical switch cable was damaged during sea/air transit from the US due to insufficient securing in cable tray.
- **Action:** Require Honeywell to secure all cables with SS 316 clamps at 300mm intervals before shipping. Add cable protection inspection to packing checklist.

**C-EI-08: Motor frequency confusion (50Hz vs 60Hz).**
NOA was 50Hz, Valhall was 60Hz. The prover config code "W" meant 60Hz but the PO specified 50Hz for NOA — resolved under "YYY special."
- **Action:** Resolve TQ-001 (60Hz confirmation) with Guidant BEFORE submitting to Honeywell. This affects motor, gear, and controller sizing.

---

## 5. METERING & CALIBRATION

### 5.1 Caution Items

**C-MET-01: Seal degradation during storage.**
If a prover sits 4+ years without operation, piston seals develop "flat spots" causing calibration failure. All seals must be replaced before commissioning.
- **Action:** Include seal replacement kit in spare parts. If commissioning is delayed >2 years after FAT, budget for pre-commissioning seal replacement and re-calibration.

**C-MET-02: Reference calibration temperature was undefined at PO.**
On NOA/Valhall, the calibration reference temperature was marked "TBA" at the time of ordering. This affects the calibration certificate.
- **Action:** Define reference temperature (likely 15°C per API MPMS) in the quote request. Get confirmation from Guidant/Equinor.

**C-MET-03: Seraphin can FAT verification was a VOR.**
Including the Seraphin can in the FAT (checking fill volume against prover) was not in the original scope — added as VOR 001 (USD 4,970 per prover).
- **Action:** Include Seraphin can verification during FAT in the base scope. Not a VOR item.

**C-MET-04: Water draw kit orifice size change at FAT.**
The solenoid valve orifice needed to be smaller than originally specified — discovered at FAT (VOR 004).
- **Action:** Confirm orifice size with Honeywell during engineering phase, not at FAT. Get prover-specific recommendation.

**C-MET-05: Repeatability after re-assembly is unproven.**
The Snorre A RFQ requires ≤0.020% repeatability after offshore re-assembly. This has never been done on the previous projects (no modular split).
- **Action:** This is TQ-003 to Honeywell. Get a written confirmation of the re-calibration procedure. Consider requiring a water draw test on site (SAT) as contractual proof.

---

## 6. STRUCTURAL & MODULAR SPLIT

### 6.1 Caution Items (NEW scope — no precedent from NOA/Valhall)

**C-STR-01: Modular split has never been done before on these projects.**
The max module size of W 1.4 × L 2.56 × H 2.2m is a constraint driven by the Snorre A platform access routes. The SVP085 is significantly larger than SVP050.
- **Action:** This is the single biggest engineering risk. Get Honeywell's split concept drawing before committing to a price. Verify weight of heaviest module against Snorre A crane capacity.

**C-STR-02: Flow tube ships without end flanges to fit 2.5m limit.**
From the SP-01415 bid notes — the flow tube must be shipped without end flanges, with flanges attached during re-assembly offshore.
- **Action:** Confirm Honeywell's procedure for re-attaching flanges and what this means for calibration integrity.

**C-STR-03: Lifting points per Norsok R-002 on each module.**
Each split module needs certified lifting lugs with calculations.
- **Action:** Include R-002 lifting engineering in Honeywell's deliverable scope. Get lifting calculations reviewed by a certified lifting engineer.

**C-STR-04: Insulation clearance discrepancy (65mm vs 80mm).**
On NOA/Valhall, the specification said 80mm insulation but the punch list referenced 65mm. The Snorre A RFQ says "min 100mm insulation."
- **Action:** Design for 100mm insulation from the start. Ensure GA drawings show insulation envelope and verify tool access clearance.

**C-STR-05: Re-assembly man-hours estimation.**
Offshore labor on Snorre A is extremely expensive. The bid notes suggest partnering with Intertek for re-assembly.
- **Action:** Get Honeywell's estimated re-assembly man-hours. Add 50% contingency for offshore conditions. Consider Intertek partnership.

---

## 7. HSE & ATEX

### 7.1 Caution Items

**C-HSE-01: ATEX approach is different from NOA/Valhall.**
NOA/Valhall removed the Honeywell controller and used individual ATEX certs on each component (costly, complex). Snorre A uses the standard Honeywell controller with standard Ex D certification.
- **Action:** Confirm with Honeywell that standard Ex D covers Zone 1 IIA T3 (RFQ requirement). Note: Honeywell standard is IIB T4 which exceeds the requirement.

**C-HSE-02: NACE MR0175 compliance for all wetted parts.**
Sour service (H2S) requires NACE compliance. The 316SS flow tube is standard but verify all small-bore fittings, plugs, and valves also comply.
- **Action:** Include NACE compliance requirement on every line item in the BOM. Request MTR certificates showing compliance.

**C-HSE-03: Offshore re-assembly hot work permits.**
Re-assembly on Snorre A may require welding or mechanical work near live production systems.
- **Action:** Clarify with Guidant/Equinor what work restrictions apply during the installation window. Plan for zero hot work if possible.

---

## 8. QUALITY MANAGEMENT

### 8.1 Caution Items

**C-QM-01: Factory incoming inspection is mandatory.**
On NOA/Valhall, 14 quality issues were found after the provers arrived in Norway. If these had not been caught, the provers would have been installed offshore with water ingress paths, wrong wiring, and ungrounded shields.
- **Action:** Plan for Sifab engineer on site at TruStop during the last 2 weeks of fabrication (pre-FAT inspection). Budget travel to Arizona.

**C-QM-02: Every BOM line must specify SS 316 explicitly.**
Honeywell's BOM used generic "SS" — the factory used 304 for cable ties, cable tray strips, and edge protection. All had to be replaced.
- **Action:** Include in the PO specification: "All stainless steel components, including cable ties, cable tray hardware, bolts, and edge protection, shall be grade 316 / 316L minimum."

**C-QM-03: Punch list pattern is predictable — prepare in advance.**
Both NOA and Valhall had nearly identical 23–25 item punch lists. The issues are systemic, not random.
- **Action:** Issue a pre-FAT checklist based on the NOA/Valhall punch lists. Have Honeywell complete this checklist BEFORE inviting Sifab for FAT. Items on the checklist:
  - [ ] All cables routed through cable trays
  - [ ] Cable trays sized with margin, covers installed
  - [ ] All cable ties SS 316
  - [ ] Round-head bolts only inside cable trays
  - [ ] Edge protection on all sharp edges
  - [ ] Bonding cables with Yellow/Green sleeves
  - [ ] All tags and markings applied
  - [ ] Motor installed (not temporary)
  - [ ] Cable wiring verified against termination diagram
  - [ ] Ferrules correct size for wire gauge
  - [ ] No heat shrink inside cable glands
  - [ ] Braid armour properly grounded
  - [ ] Polarity verified on all transmitters

**C-QM-04: Expired QTR risk.**
On Valhall, the QTR (Quality Technical Requirement) document expired during the project. Materials had to be confirmed as purchased before expiry.
- **Action:** Check QTR validity dates for BD20X material at project start. Ensure all material orders are placed within QTR validity.

---

## 9. CLIENT & STAKEHOLDER MANAGEMENT

### 9.1 Caution Items

**C-CLI-01: Multi-party supply chain creates communication delays.**
On NOA/Valhall: Honeywell → Sifab → FMC → Aker BP. Clarifications passed through 3–4 parties. The coating deviation alone required a formal letter traversing the entire chain.
- **Action:** For Snorre A (Honeywell → Sifab → Guidant → Equinor), establish a direct technical clarification channel. Propose joint Teams calls with all parties for critical TQs.

**C-CLI-02: Client-caused delays cascade into schedule slippage.**
FMC's delayed approval of painting procedures, wiring diagrams, and 50+ documents directly caused factory holds, milestone payment delays, and a 6-month documentation tail.
- **Action:** Include a "Client obligations schedule" in the contract, listing Guidant's approval deadlines. Include a delay-relief clause for Sifab if Guidant exceeds agreed review times.

**C-CLI-03: Spare seal kits were in the LOI but not in the PO.**
Sifab ordered parts based on the Letter of Intent, but the formal PO from FMC didn't include them. Could not cancel.
- **Action:** Verify that every item in the Guidant LOI/letter of award is reflected in the formal PO before committing to subcontracts.

---

## 10. SNORRE A–SPECIFIC NEW RISKS (No Precedent)

| # | New Risk | Impact | Mitigation |
|---|----------|--------|------------|
| N-01 | Modular split engineering | Unproven for SVP085. May affect calibration. | Get Honeywell concept before pricing. |
| N-02 | Offshore re-assembly | Expensive, weather-dependent, requires HE engineer | Partner with Intertek. Budget 50% contingency on man-hours. |
| N-03 | Re-assembly calibration proof | Must demonstrate ≤0.020% after re-assembly | Contractual SAT with water draw on Snorre A. |
| N-04 | CL 600 RTJ connections (12") | Higher pressure class than any previous Sifab prover project | Verify Honeywell has manufactured SVP085 with CL 600 before. |
| N-05 | Duplex SS barrel request | Not Honeywell standard (316SS is standard) | Confirm if Honeywell can do Duplex, or if 316SS with BD20X is acceptable. |
| N-06 | 60Hz motor in Norway | Unusual — Norway is 50Hz. RFQ says 60Hz. | TQ-001 to Guidant. Must resolve before ordering. |
| N-07 | Warranty starts at site release | 28-month warranty from offshore re-assembly, not from PO | Factor into Honeywell extended warranty quote. |
| N-08 | US tariffs on imports | Political risk affecting Honeywell pricing | Include tariff escalation clause. |

---

## 11. TOP 10 ACTIONS FOR A SMOOTH PROJECT

| Priority | Action | Owner | When |
|----------|--------|-------|------|
| 1 | **Resolve TQ-001 (50Hz vs 60Hz)** with Guidant before ordering | Sondre | Before quote submission |
| 2 | **Get modular split concept from Honeywell** before committing price | Tom / Sidney | With Honeywell quote |
| 3 | **Prepare Factory Instruction Package** with NORSOK electrical standards, photos, visual examples | Oliver | Before Honeywell PO |
| 4 | **Negotiate granular milestone payments** (30/20/20/20/10 or monthly progress billing) | Sondre | During contract negotiation |
| 5 | **Issue pre-FAT checklist** based on NOA/Valhall punch lists — Honeywell must complete before inviting Sifab | Oliver | 8 WAO |
| 6 | **Plan Sifab engineer presence at TruStop** during last 2 weeks of fabrication | Tom / Oliver | 2 weeks before FAT |
| 7 | **Define all free-issue parts with firm need-dates** at kick-off | Oliver | Kick-off meeting |
| 8 | **Include Seraphin can FAT check + water draw kit 1" tubing** in base scope (not VOR) | Sondre | In quote |
| 9 | **Confirm System 6C coating** with Guidant/Equinor in the technical submission | Tom | 2 WAO |
| 10 | **Establish document tracker with Guidant** — max 2-week review, escalation at 3 weeks | Tom | Week 1 |
