# Lessons Learned — NOA/Valhall Fenris Prover Projects
# For Application to Snorre A SVP085 Project (GM-8501-1447)

**Source Projects:**
- SP-00525 — Hugin A (NOA), SVP050, Crude Oil Export Metering
- SP-00577 — Valhall Fenris (PWP), SVP015, Condensate Fiscal Metering
- SP-01415 — Snorre A SVP (current bid, SVP085)

**Prepared by:** Sifab AS Engineering Team
**Date:** 2026-02-24

---

## 1. Reference Project Comparison

| Parameter | Hugin A (SVP050) | Valhall (SVP015) | **Snorre A (SVP085)** |
|---|---|---|---|
| Client | Aker BP via TechnipFMC | Aker BP via TechnipFMC | Equinor via Guidant |
| Fluid | Crude oil | Condensate | **Crude oil** |
| Flow range | 71.4–1,034.5 m³/h | 9.1–211.6 m³/h | **67–750 m³/h** |
| Design pressure | 27 barg | 17.7 barg | **49 barg** |
| Pipe class | BD20 (CL 300, Duplex SS) | AD20 (CL 150, Duplex SS) | **BD20X (CL 600, per TR2000)** |
| Connections | 14" CL 300 RF WN | 8" CL 150 WN | **12" CL 600 RTJ** |
| Barrel material | 316SS standard | 316SS standard | **Duplex SS requested** |
| Seal material | Carbon Fiber PTFE (crude) | Ekonol PTFE (condensate) | **Carbon Fiber PTFE (crude)** |
| Controller | Removed (special ATEX) | Removed (special ATEX) | **Included (standard Honeywell)** |
| Motor | 690V 50Hz ATB (non-standard) | 690V 60Hz ATB (non-standard) | **230V 3ph 60Hz (confirm 50Hz)** |
| Coating | M-501 2A (TSA) | M-501 2A (TSA) | **M-501 6C (recommended)** |
| Modular split | Not required | Not required | **Required (max 1.4×2.56×2.2m)** |
| Re-assembly | N/A | N/A | **Offshore on Snorre A** |
| Honeywell PO no. | O-579505 | O-636399 | **O-1010834** |

---

## 2. Pricing Benchmarks

### 2.1 NOA / Hugin A (SVP050) — Total USD 928,915

| Pos | Item | USD |
|---|---|---|
| 1 | Honeywell Enraf SVP O050, 8" connections | 718,333 |
| 2 | Spare parts (2-year kit) | 13,691 |
| 3 | 151.40 Liter Seraphin Can | 34,303 |
| 4 | Water draw kit fabrication | 18,054 |
| 5 | Project management + documentation | 28,034 |
| 6 | Shipment Arizona → Norway (air) | 40,000 |
| 7 | Painting NORSOK M-501 2A (TSA) | 10,500 |
| 8 | Extended warranty (additional 4.5 years) | 66,000 |

### 2.2 Valhall / Fenris (SVP015) — Total USD 608,175

| Pos | Item | USD |
|---|---|---|
| 1 | Honeywell Enraf SVP O015 | 436,521 |
| 2 | Spare parts (2-year kit) | 13,039 |
| 3 | 75.7 Liter Seraphin Can | 30,023 |
| 4 | Water draw kit fabrication | 17,308 |
| 5 | Project management + documentation | 28,034 |
| 6 | Shipment Arizona → Norway (air) | 30,000 |
| 7 | Painting NORSOK M-501 2A (TSA) | 9,250 |
| 8 | Extended warranty (additional 4.5 years) | 44,000 |

### 2.3 Variation Orders — Total USD 31,438 per unit

| VOR | Description | USD/unit |
|---|---|---|
| VOR 001 | Seraphin Can verification at FAT | 4,970 |
| VOR 003 | Design changes (water draw kit, brackets, motors, DBB valves, travel) | 20,438 |
| VOR 004 | Post-FAT changes (solenoid valve, thermowell, 6Mo plugs, expediting) | 6,030 |

### 2.4 Snorre A Pricing Considerations
- **SVP085 base price** will be significantly higher than SVP050 (USD 718k) due to larger displacement, higher pressure class (CL 600 vs CL 300), and Duplex SS barrel
- **Modular split engineering** is a new cost item not present in reference projects — expect substantial engineering add-on
- **Offshore re-assembly** costs (HE certified engineer + Intertek partnership suggested) — new scope
- **System 6C coating** is the recommended approach after NOA/Valhall TSA lessons
- **US tariffs** flagged as potential cost risk — verify current import duties
- **Budget VOR contingency:** ≥ USD 30,000 based on historical pattern

### 2.5 Payment Milestones (Reference)
- 40% at clarified PO
- 50% at accepted FAT
- 10% at final documentation

### 2.6 Delivery Time (Reference)
- 49 weeks from clarified PO to delivery

---

## 3. Critical Technical Lessons

### 3.1 Coating — Use System 6C, NOT TSA (System 2A/2C)

**Background:** NOA/Valhall provers were specified with NORSOK M-501 system 2A (TSA — Thermal Spray Aluminum). During execution, Honeywell advised strongly against TSA due to:
- High spray temperatures cause **deformation to the flow tube**
- TSA process affects the **hard chrome internal surface**
- Flow tube dimensional integrity is critical for prover calibration accuracy

**Decision for Snorre A:** Use **system 6C** per NORSOK M-501 for process-wetted surfaces. This is aligned with TR0042 requirements and is the proven approach. Desert Coating in Arizona is qualified for NORSOK M-501.

### 3.2 Seal Degradation During Storage

**Issue:** If a prover sits unused for 4+ years, the piston resting on seals causes "flat spots" leading to calibration failure.

**Action for Snorre A:** If there is a gap between FAT and commissioning, plan for **seal replacement** before putting into service. Include seal replacement kit in spare parts scope. Consider periodic exercising of the piston if storage exceeds 2 years.

### 3.3 Flow Tube Shipped Without End Flanges

**Key insight from SP-01415 bid notes:** For the modular split, the flow tube can be **shipped without end flanges** to fit within the 2.5m maximum module length. This is part of the modular split concept.

### 3.4 Prover Barrel Material

**Reference:** Both NOA and Valhall used standard 316SS barrels. For Snorre A, **Duplex SS** is requested due to higher design pressure (49 barg) and BD20X material specification. Fabrication is done in India with hard chrome finishing in the USA.

### 3.5 Motor and Electrical Configuration

| Parameter | NOA/Valhall | Snorre A |
|---|---|---|
| Motor voltage | 690V (non-standard) | 230V 3ph |
| Motor frequency | 50Hz (NOA) / 60Hz (Valhall) | 60Hz (TQ-001: confirm) |
| Motor source | ATB via Lanne Elektriske (frame agreement) | Honeywell standard |
| Controller | Removed (special ATEX approach) | Included (standard Honeywell SVP controller) |
| ATEX | Individual component ATEX certs | Standard Honeywell Ex D |

**Lessons:**
- NOA/Valhall required custom motors via frame agreement, causing delays and VORs
- Snorre A uses standard Honeywell controller and motor — simpler ATEX certification
- **Verify 60Hz frequency requirement** (TQ-001) — Norway standard is 50Hz

---

## 4. Punch List Patterns — Recurring Issues

Both provers (SVP050 and SVP015) had nearly identical punch lists with 23–25 items. These represent systematic gaps at the Honeywell/TruStop factory:

### 4.1 Cable Routing (Items 1, 2, 3, 6, 8)
- Cables NOT routed through cable trays — most common issue
- Cable trays too small for number of cables
- Bonding cables not properly sleeved (Yellow/Green)
- **Fix:** Specify cable tray sizing with margin. Provide routing diagrams to factory before fabrication.

### 4.2 Tagging and Marking (Items 7, 9, 10, 14, 15, 17, 19)
- Tag marking missing on JBs, cables, switches, name plates
- This was a SIFAB/Factory shared responsibility — items appeared on every punch list
- **Fix:** Issue tag marking schedule with material/label procurement before factory work starts.

### 4.3 Material Substitution (Items 3, 5, 11, 13)
- Cable ties in SS 304 instead of SS 316
- Honeywell BOM specified only "SS" without grade
- Hexagon bolts inside cable trays instead of round-head bolts
- "Volvo list" (edge protection strips) not in SS 316
- **Fix:** Every BOM line item must specify SS 316 explicitly. Provide visual examples of edge protection requirements.

### 4.4 SIFAB-Scope Items (Items 11, 12, 13, 16, 18, 19, 21)
- 6Mo Parker plugs for vent valves
- Jumper wiring in JBs per termination diagrams
- Plug and chain for test thermowell
- **Fix:** Pre-manufacture all SIFAB-scope items and ship as a kit to factory.

---

## 5. Quality Concerns at Factory — 14 Issues Documented

### 5.1 Electrical Workmanship (10 of 14 issues)
| Issue | Root Cause | Frequency |
|---|---|---|
| Cable braid armour destroyed during routing | Factory never did this before | First-time issue |
| Wire insulation damage pushing through glands | Insufficient care | Repeat risk |
| Optical switch cable damage from bolts in tray | Cable trays too small + sharp bolts | Design + workmanship |
| Cable lugs over-crimped | Wrong tool/operator error | Operator training |
| Wrong ferrule sizes (red 1.5mm² on 0.75mm² wire) | Unclear specification | BOM/specification gap |
| Wiring polarity reversed in transmitters | Human error | Operator training |
| Cables switched in JB terminals | Human error | Check procedure needed |
| Cable tray strips in SS 304 vs SS 316 | BOM said "SS" only | Specification gap |
| Braid armour not grounded in transmitters | Unclear instruction | Wiring diagram gap |
| No ferrules on temperature sensor cables | Human error | Operator training |

### 5.2 Mechanical Issues (4 of 14)
| Issue | Root Cause |
|---|---|
| Hexagon bolts inside cable tray | Not specified to use round heads |
| Cable support distance too long (>10D) | Design limitation, approved |
| Cables resting on sharp edges | Not enough edge protection |
| "Volvo list" material (SS 304 vs 316) | Factory didn't understand the term |

### 5.3 Key Takeaway for Snorre A
**The Honeywell/TruStop factory is not familiar with NORSOK offshore electrical installation standards.** Every specification must be explicit, with visual examples and step-by-step instructions. Do not assume factory knowledge of:
- Cable braid armour handling
- SS 316 vs SS 304 material grades
- Edge protection ("volvo list") requirements
- Scandinavian electrical terminology

**Recommended approach for Snorre A:**
1. Issue a "Factory Instruction Package" before fabrication with photos/diagrams for all non-standard items
2. Require factory sign-off checklists per cable
3. Send SIFAB engineer to factory for electrical installation review at 50% completion (before FAT)
4. Pre-manufacture all SIFAB-scope electrical items (JBs, cable glands, ferrules, tags) as a complete kit

---

## 6. Variation Order Root Causes and Prevention

### 6.1 VOR Summary by Root Cause

| Root Cause | VOR Items | Total Cost/Unit |
|---|---|---|
| Design specification changes | Water draw kit (1/2" → 1"), solenoid valve, thermowell | ~USD 14,000 |
| Supplier/frame agreement changes | Motors (Siemens → Lanne), DBB valves (Emerson → MRC Global) | ~USD 2,400 |
| Insulation/mounting requirements | Temperature transmitter brackets | ~USD 3,300 |
| Client-requested additions at FAT | Seraphin can check, 6Mo plugs, expediting | ~USD 11,500 |
| Travel/coordination | Extra trip to Arizona | ~USD 1,500 |

### 6.2 Prevention Measures for Snorre A

1. **Lock down water draw kit design early** — the 1/2" to 1" change was the single largest VOR item. Specify sizes in quote request.
2. **Confirm motor supplier and approvals** before PO — avoid frame agreement complications
3. **Include Seraphin can FAT verification** in base scope — this was VOR 001 on both projects
4. **Freeze design before FAT** — VOR 004 items were all post-FAT changes
5. **Include all 6Mo material requirements** in initial specification — the hex plug upgrade was a preventable VOR
6. **Build delivery schedule buffer** — expediting cost USD 4,500 per unit

---

## 7. Documentation Deliverables — Honeywell Standard Package

Based on the delivered documentation structure for SVP050 and SVP015:

| Package | Contents |
|---|---|
| 1. Drawings & Documents | GA drawing, service clearance, frame mounting, base structure, name plate, paint procedure/cert |
| 2. SVP Test Procedures & Certificate | Gravimetric calibration, FAT certificates, instrument calibration certs, CMC traceability |
| 3. Flow Tube - Welding | Certification package index, vendor checklists, casting MTRs, weld documentation for all components |
| 4. Major Wetted Parts and Components | Material certificates for all wetted parts per EN 10204 3.1 |
| 5. SVP System Certifications | ATEX certs, PED, design code compliance, conformity declarations |
| 6. SVP Controller and Transmitter | Controller documentation, transmitter specs and calibration |
| 7. Motor Documents | Motor specifications, ATEX certification, test reports |
| 8. Project-Specific Equipment | Configuration sheets, customer-specific items, special materials |
| 9. SVP Operation & Service Manual | Full IOM manual for operation and maintenance |

---

## 8. Shipping and Logistics

### 8.1 Reference Dimensions and Weights
| Prover | Crate Size | Weight |
|---|---|---|
| SVP050 (Hugin A) | 5.0m × 1.5m × 1.5m | ~4,000 kg |
| SVP015 (Valhall) | 4.3m × 1.3m × 1.3m | ~2,500 kg |
| SVP085 (Snorre A) | TBD — larger than SVP050 | TBD |

### 8.2 Shipping Notes
- **Air freight** USD 30,000–40,000 per unit (Arizona → Norway)
- **Sea freight** significantly cheaper, 6–8 weeks transit
- Consolidating multiple units saves cost
- **Honeywell/TruStop address:** Kent Carpenter, 1725 W. 10th Pl., Tempe, AZ 85281 (Attn: Jonathan Koller)

### 8.3 Snorre A Modular Split Shipping Considerations
- SVP085 will be larger than SVP050 — must fit within 1.4×2.56×2.2m per module
- Flow tube shipped **without end flanges** to fit max 2.5m
- Skid frame split into sections — each must have lifting points per Norsok R-002
- Need lifting and handling description for each module
- **Weight of heaviest module** must be documented for platform crane capacity

---

## 9. Key Contacts and Roles (Reference)

### 9.1 NOA/Valhall Project Team
| Role | Person | Organization |
|---|---|---|
| General Manager | Tom Sverre Falch | Sifab AS |
| Sales Manager | Sondre Falch | Sifab AS |
| Project Manager / Engineer | Oliver Vetland | Sifab AS |
| Prover Specialist | Sam (Samir) Sakota | Honeywell |
| Factory (TruStop) | Jon Koller, John Tyree, Dustin Rankin | Honeywell/TruStop |
| Sales / Commercial | Marcel Jurriens, Jean Chfar | Honeywell |
| Engineering | Sanjay Krishnan | Honeywell |

### 9.2 Snorre A Team (Current)
| Role | Person | Organization |
|---|---|---|
| Sales Manager | Sondre Falch | Sifab AS |
| Technical / PM | Tom Sverre Falch | Sifab AS |
| Honeywell Lead | Sidney Swart | Honeywell |
| Prover Specialist | Samir Sakota | Honeywell |
| Commercial | Mark Price, Eric van der Made | Honeywell |
| Client Tender Engineer | Torleif Espegard | Guidant |

---

## 10. Action Items for Snorre A Based on Lessons Learned

| # | Action | Responsible | Priority |
|---|---|---|---|
| 1 | Include Seraphin can FAT verification in base scope (not as VOR) | Sifab (quote) | HIGH |
| 2 | Specify water draw kit tubing size (1/2" or 1") in initial quote | Sifab (engineering) | HIGH |
| 3 | Prepare Factory Instruction Package with NORSOK electrical standards, photos, and visual examples | Sifab (Oliver) | HIGH |
| 4 | Confirm motor frequency (50Hz vs 60Hz) with Guidant — TQ-001 | Sifab (Sondre) | HIGH |
| 5 | Request Honeywell confirm system 6C coating feasibility for SVP085 | Sifab → Honeywell | HIGH |
| 6 | Include modular split concept drawing in Honeywell deliverables list | Sifab (quote) | HIGH |
| 7 | Consider Intertek partnership for offshore re-assembly | Sifab (Tom) | MEDIUM |
| 8 | Specify all SS 316 material grades explicitly in every BOM item | Sifab (engineering) | MEDIUM |
| 9 | Plan SIFAB engineer presence at 50% factory completion | Sifab (Oliver) | MEDIUM |
| 10 | Include seal replacement kit in spare parts if storage > 2 years | Sifab (quote) | MEDIUM |
| 11 | Verify US tariff implications on Honeywell pricing | Sifab (Sondre) | MEDIUM |
| 12 | Pre-fabricate all SIFAB-scope items (thermowells, JBs, cable glands) as a kit | Sifab (engineering) | MEDIUM |
| 13 | Build 4-week delivery schedule buffer to avoid expediting costs | Sifab (PM) | LOW |
| 14 | Request tag marking schedule from Guidant early in project | Sifab (PM) | LOW |
