# Sifab AS — Engineering Execution Plan
# SVP085 Modular Split for Snorre A Platform Access

| Field | Value |
|-------|-------|
| **Date** | 2026-02-26 |
| **Document** | INTERNAL — Engineering Working Document |
| **Project** | SP-01415 — Snorre A Small Volume Prover |
| **Prepared by** | Sifab Engineering (Structural, Metering, Process) |
| **Status** | DRAFT — For internal review and Honeywell discussion |

---

## 1. Problem Statement

The Honeywell SVP085 Small Volume Prover must be installed on Equinor's Snorre A platform. The prover must pass through a platform access door with the following constraints:

| Constraint | Dimension |
|------------|-----------|
| **Door width** | 1,400 mm |
| **Door height** | 2,200 mm |

The SVP085 as a complete unit **does not fit through this door in any orientation**:

| SVP085 Dimension | Value | vs. Door |
|------------------|-------|----------|
| Overall length | 5,258 mm | N/A |
| Width at frame | 1,448 mm | **48 mm too wide** |
| Width at feet | 1,588 mm | **188 mm too wide** |
| Height (estimated) | ~2,286 mm | **~86 mm too tall** |
| Weight (dry, est.) | 4,000–5,500 kg | Heavy lift required |

**Conclusion:** The SVP085 must be disassembled into modules that individually fit through a 1,400 × 2,200 mm opening, transported to the installation location, and reassembled with full calibration accuracy maintained.

---

## 2. Reference Data

### 2.1 SVP Model Comparison (from Honeywell Enraf Manual Part No. 44200001)

| Dimension | SVP050 (Hugin A ref.) | SVP085 (Snorre A) | SVP120 |
|-----------|----------------------|-------------------|--------|
| Overall Length (A) | 4,572 mm | 5,258 mm | 5,576 mm |
| Width at Frame (B) | 1,448 mm | 1,448 mm | 1,448 mm |
| Width at Feet (C) | 1,588 mm | 1,588 mm | 1,588 mm |
| Height at I/O (D) | 756 mm | 756 mm | 756 mm |
| I/O Separation (E) | 1,930 mm | 1,930 mm | 1,930 mm |
| Displaced Volume | 40 gal (151 L) | 75 gal (284 L) | 120 gal (454 L) |
| Weight (dry) | 3,674 kg | ~4,500 kg (est.) | ~5,500 kg (est.) |

**Key observation:** All three models share the same frame width (1,448 mm) and foot width (1,588 mm). The only difference is overall length (driven by flow tube length).

### 2.2 Previous Projects — No Splitting Required

| Project | Model | Shipped as | Split? |
|---------|-------|-----------|--------|
| SP-00525 Hugin A | SVP050 | Complete unit on wooden skid | **No** |
| SP-00577 Valhall | SVP015 | Complete unit on wooden skid | **No** |
| SP-01415 Snorre A | SVP085 | **Must be split** | **Yes — 3 modules proposed** |

The Hugin A and Valhall provers were installed during platform construction or through larger openings. Snorre A is a retrofit installation with restricted access.

### 2.3 SVP085 Key Components (to be separated)

| Component | Estimated Dimensions (L×W×H) | Estimated Weight | Notes |
|-----------|------------------------------|-----------------|-------|
| Flow tube assembly | ~3,500 × 400 × 400 mm | ~1,500–2,000 kg | Precision calibrated — MUST NOT be disassembled |
| Hydraulic drive unit | ~1,200 × 800 × 800 mm | ~500–800 kg | Motor, pump, reservoir |
| Frame/skid (structural) | 5,258 × 1,448 × ~800 mm | ~1,000–1,500 kg | SS316L, can be sectioned |
| Controller/electrical | ~600 × 600 × 1,200 mm | ~200–300 kg | SS316 enclosure |
| Piping & instrumentation | Various | ~200–400 kg | Tubing, valves, thermowells |
| Piston & rod assembly | Inside flow tube | Part of flow tube weight | Removed for transport |

---

## 3. Transport Orientation — Flip and Roll

### 3.1 Key Insight: Rotate 90° to Pass Through Door

The SVP085 cross-section in normal upright orientation (1,448 mm W × ~2,286 mm H) does not fit through the 1,400 × 2,200 mm door. However, **if the modules are flipped on their side (rotated 90°)**, the geometry changes dramatically:

| Orientation | Width (through door) | Height (through door) | Fits? |
|-------------|---------------------|----------------------|-------|
| **Upright (normal)** | 1,448 mm | ~2,286 mm | **NO** — too wide AND too tall |
| **Flipped on side** | ~756 mm (I/O height) | 1,448 mm (frame width) | **YES** — 756 < 1,400 and 1,448 < 2,200 |

**Transport method:** Each module is placed on a rolling cradle/dolly, flipped on its side, and rolled through the door opening. This eliminates the width problem entirely.

**Remaining constraint:** The 5,258 mm overall length must be split into sections short enough to maneuver through corridors and around corners on the platform.

### 3.2 Frame Splitting — Weight Distribution is Critical

When splitting the frame into sections, the motor and hydraulic equipment are concentrated at the drive end. If the frame is split unevenly, the drive-end section becomes disproportionately heavy and structurally loaded. **Each frame section must be self-supporting and balanced.**

**Design principle:** Split the frame so that heavy components (motor, hydraulic pump, oil reservoir) are distributed or can be removed and transported separately — preventing any single frame section from being overloaded.

---

## 4. Proposed 3-Module Split Concept

### Module 1: Flow Tube Assembly (THE CRITICAL MODULE)

**Description:** The precision-calibrated flow tube with detector switches, removed from the structural frame. Transported on its side in a custom cradle.

| Parameter | Value |
|-----------|-------|
| Estimated dimensions (tube) | ~3,500 × Ø400 mm |
| With transport cradle (flipped) | ~3,600 × 800 × 600 mm |
| Estimated weight | ~1,500–2,000 kg |
| Transport orientation | Flipped on side, on rolling dolly |
| Fits through door? | **YES** (800 mm W × 600 mm H, well within 1,400 × 2,200) |

**Critical requirements:**
- Flow tube is the heart of the prover — gravimetrically calibrated to ≤0.020% repeatability
- Must be handled as a precision instrument — NO impacts, NO bending loads
- Detector switches must be protected (optical/magnetic switches at each end)
- All openings sealed with VCI (Vapor Corrosion Inhibitor) protection
- **Flow tube valved off and mounted to a temporary transport frame** (Sifab to design and fabricate, SS316L)
- Temporary frame provides structural support, rolling capability, and protection during transport through corridors
- Piston and rod assembly removed and transported separately (inside Module 3)
- **After reassembly, a water draw test is MANDATORY to verify calibration**

**Sifab scope:**
- Design and fabricate SS316L **temporary transport frame** for flow tube — with valve isolation, shock mounts, rollers, and lifting lugs
- Temporary frame sized to fit through door when flipped (max cross-section 1,350 × 2,150 mm)
- Valves on flow tube ends to seal and protect the calibrated bore during transport
- Flange protection covers (ANSI CL600 RTJ faces)
- Lifting lugs per Norsok R-002

### Module 2: Structural Frame + Hydraulic Drive (SPLIT INTO 2 SUB-MODULES)

**Description:** The SS316L support frame split into 2 sections at designed splice points. Motor and hydraulic drive **removed from frame and transported as a separate sub-module** to keep frame sections light and balanced.

#### Module 2A — Frame Section: Drive End
| Parameter | Value |
|-----------|-------|
| Estimated dimensions | ~2,600 × 1,448 × ~800 mm (upright) |
| Flipped for transport | ~2,600 × 800 × 1,448 mm |
| Weight (frame only, drive removed) | ~600–800 kg |
| Fits through door (flipped)? | **YES** (800 mm W × 1,448 mm H) |

#### Module 2B — Frame Section: Non-Drive End
| Parameter | Value |
|-----------|-------|
| Estimated dimensions | ~2,700 × 1,448 × ~800 mm (upright) |
| Flipped for transport | ~2,700 × 800 × 1,448 mm |
| Weight (frame only) | ~500–700 kg |
| Fits through door (flipped)? | **YES** (800 mm W × 1,448 mm H) |

#### Module 2C — Hydraulic Drive Unit (separate from frame)
| Parameter | Value |
|-----------|-------|
| Motor + pump + reservoir | ~1,200 × 800 × 800 mm |
| Weight | ~500–800 kg |
| Fits through door? | **YES** — compact unit |

**Why separate the drive from the frame:**
- Motor + pump + oil reservoir together weigh ~500–800 kg
- If left attached to a frame section during transport, that section becomes ~1,100–1,600 kg with unbalanced COG
- A frame section with drive attached and flipped on its side puts bending loads on the frame splice zone
- **Separating the drive keeps each piece lighter, balanced, and easier to handle**
- Drive unit bolts back onto frame after frame is reassembled and aligned

**Critical requirements:**
- Frame splice joints must be bolted (not welded) — designed for reassembly
- Splice joints engineered to maintain flow tube mounting alignment ±0.5 mm
- Each frame section must have temporary feet/supports for flipped transport
- Motor: ATEX Ex de/Ex e, 230 VAC 3-phase (confirm 50/60 Hz)
- Hydraulic connections: Quick-disconnect couplings with dust caps

**Sifab scope:**
- Structural engineering for frame splice design (bolted connections, Norsok M-101)
- Temporary transport supports for flipped orientation
- Alignment verification procedure (laser alignment after reassembly)
- Rolling dollies for corridor transport (Norsok R-002 for lifting)

**KEY ENGINEERING REQUIREMENT — Frame Splice Design:**
The splice must be designed so that when the two frame halves are bolted together and the flow tube is reinstalled, all mounting points are within ±0.5 mm of factory position. Options:
1. **Precision dowel pins + bolted flanges** — dowels provide alignment, bolts provide clamping
2. **Machined register faces** — mating surfaces machined at factory, self-aligning when bolted
3. **Honeywell designs splice from the start** — frame built in two halves with factory-machined joint (preferred)

### Module 3: Controller, Electrical, Piping & Accessories

**Description:** SVP Controller, junction boxes, all instrument tubing, valves, cable assemblies, piston/rod assembly, and spare parts.

| Parameter | Value |
|-----------|-------|
| Controller enclosure | ~600 × 600 × 1,200 mm |
| Piping/tubing (bundled) | ~2,000 × 400 × 400 mm |
| Piston/rod assembly | ~2,500 × Ø300 mm |
| Total estimated weight | ~400–700 kg |
| Fits through door? | **YES** |

**Critical requirements:**
- Controller is a standalone unit — straightforward to transport separately
- All tubing connections tagged and photographed before disassembly
- Cable assemblies labeled at both ends (per Norsok E-001)
- Piston seal (Carbon Fiber PTFE) must be protected from damage and contamination
- Rod thermowell and process thermowells transported with protection caps

### Module Summary

| Module | Contents | Dimensions (transport) | Weight | Transport Method |
|--------|----------|----------------------|--------|-----------------|
| 1 | Flow tube + cradle | 3,600 × 800 × 600 mm | ~1,500–2,000 kg | Flipped, rolling dolly |
| 2A | Frame — drive end | 2,600 × 800 × 1,448 mm | ~600–800 kg | Flipped, rolling dolly |
| 2B | Frame — non-drive end | 2,700 × 800 × 1,448 mm | ~500–700 kg | Flipped, rolling dolly |
| 2C | Hydraulic drive unit | 1,200 × 800 × 800 mm | ~500–800 kg | Upright, dolly or carry |
| 3 | Controller + piping + piston | Various (all < 1,200 mm wide) | ~400–700 kg | Multiple small loads |
| | **TOTAL** | | **~3,500–5,000 kg** | **5–6 loads through door** |

---

## 4. Execution Sequence

### Phase 1: Factory Build & Test (Honeywell, Tempe AZ)

| Step | Activity | Notes |
|------|----------|-------|
| 1.1 | Honeywell builds SVP085 as complete unit | Standard factory build |
| 1.2 | Gravimetric calibration at factory | Witnessed by Buyer, Contractor, End Client, Justervesenet |
| 1.3 | Water draw test with Seraphin can | Establishes baseline calibration |
| 1.4 | Repeatability test ≤0.020% | Per API MPMS 4.2 |
| 1.5 | FAT — full documentation package | All test certificates, dimensional records |
| 1.6 | **Mark all connection points** | Laser-etched reference marks for reassembly alignment |
| 1.7 | **3D scan of assembled prover** | Baseline geometry for reassembly verification |

### Phase 2: Disassembly (Onshore Norway — Sifab workshop, Sandnes)

| Step | Activity | Notes |
|------|----------|-------|
| 2.1 | Ship complete prover from AZ to Sandnes | Standard international freight |
| 2.2 | Receive and inspect at Sifab workshop | Document condition, compare to FAT records |
| 2.3 | Photograph and tag all connections | Per disassembly procedure |
| 2.4 | Remove piston/rod assembly from flow tube | Protect seal, store in clean container |
| 2.5 | Disconnect all tubing and electrical | Tag both ends of every connection |
| 2.6 | Remove controller from frame | Standalone transport |
| 2.7 | Remove hydraulic drive from frame | Drain oil, cap all ports |
| 2.8 | **Lift flow tube from frame** | Using Sifab overhead crane, place in transport cradle |
| 2.9 | **Section frame** | Cut/unbolt at designed splice points |
| 2.10 | **Remove/modify feet** | If needed to meet 1,400 mm width |
| 2.11 | Seal all openings with VCI protection | Per Honeywell QCP 006 |
| 2.12 | Package each module | Max dimensions per module ≤ 1,350 × 2,500 × 2,150 mm |

### Phase 3: Transport to Snorre A

| Step | Activity | Notes |
|------|----------|-------|
| 3.1 | Load modules onto supply vessel | Standard offshore logistics |
| 3.2 | Crane lift modules to platform deck | Each module ≤ 2,300 kg |
| 3.3 | Transport through 1,400 × 2,200 mm door | Manual/rolling transport with air skates or dollies |
| 3.4 | Position in prover room | Using chain hoists / trolley beams |

### Phase 4: Reassembly on Snorre A (Honeywell + Sifab)

| Step | Activity | Notes |
|------|----------|-------|
| 4.1 | Assemble frame sections | Bolt splice joints, torque to spec |
| 4.2 | **Laser-align frame** | Verify alignment vs. factory baseline |
| 4.3 | Install feet and level frame | Spirit level / precision level |
| 4.4 | Lift flow tube into frame | Using platform crane / chain hoist |
| 4.5 | **Align flow tube to frame** | Laser alignment — critical tolerance ±0.5 mm |
| 4.6 | Secure flow tube mounting bolts | Controlled torque sequence |
| 4.7 | Install piston/rod assembly | Clean environment, inspect seal |
| 4.8 | Install hydraulic drive | Reconnect hydraulic lines, fill oil |
| 4.9 | Install controller | Mount, connect power and signal cables |
| 4.10 | Reconnect all tubing | Per tagged connections, leak test |
| 4.11 | Reconnect all electrical | Per cable labels, megger test |
| 4.12 | Functional test — dry run | Piston travel, switch detection, no-load |
| 4.13 | **Water draw test (SAT)** | With Seraphin can — verify ≤0.020% repeatability |
| 4.14 | Commission and hand over | Honeywell to release warranty |

---

## 5. Critical Engineering Challenges

### 5.1 SOLVED: Frame Width — Flip and Roll Strategy

**Original problem:** Frame width (1,448 mm) exceeds door width (1,400 mm).

**Solution:** Rotate each module 90° (flip on side) before passing through the door. In flipped orientation, the cross-section becomes ~756 mm × 1,448 mm — well within the 1,400 × 2,200 mm door opening. Each module is placed on a rolling dolly/cradle and rolled through.

**Remaining considerations:**
- Corridor width and turning radii inside the platform must be verified
- Module length (longest piece ~3,600 mm) must be maneuverable around corners
- Rolling dollies must be rated for the heaviest module (~2,000 kg) with brakes
- Floor loading capacity along the transport route must be checked

**Action required:** Request as-built corridor dimensions and turning radii from Equinor/Guidant for the route from the access door to the prover installation location.

### 5.1b CHALLENGE: Frame Structural Integrity When Split

When the frame is split into two sections, each section must:
- Support itself during flipped transport (lateral loads it was not designed for)
- Support the hydraulic drive weight after reassembly (concentrated load at drive end)
- Maintain precise alignment at the splice joint under operating loads (piston cycling, vibration)

**The motor/pump/reservoir (~500–800 kg) must be removed from the frame before transport.** If left attached to one frame half:
- Unbalanced weight creates handling hazard when flipping
- Bending moment at the splice joint is excessive
- Risk of frame distortion during transport

**Mitigation:**
- Drive unit transported as separate Module 2C
- Frame sections transported empty (structure only)
- Temporary bracing across splice joint during transport (removed after bolting together on platform)
- Splice joint designed with safety factor ≥ 2.0 for combined operating loads

### 5.2 CHALLENGE: Maintaining Calibration After Reassembly

The SVP085 is gravimetrically calibrated at the factory. Disassembly and reassembly introduces risk of:
- Flow tube misalignment (affects swept volume)
- Piston seal damage (affects repeatability)
- Detector switch position change (affects measured volume)

**Mitigation:**
1. Flow tube itself is NOT disassembled — transported as a single precision unit
2. Detector switch positions laser-marked at factory and verified after reassembly
3. Water draw test (SAT) with Seraphin can is MANDATORY after reassembly
4. Honeywell must confirm that recalibration certificate can be issued based on SAT results
5. Justervesenet (Norwegian Metrology Service) must witness SAT

### 5.3 CHALLENGE: Offshore Man-Hours and Schedule

| Activity | Estimated Man-Hours | Personnel |
|----------|-------------------|-----------|
| Frame reassembly and alignment | 24–40 hrs | 2 Honeywell + 2 Sifab mechanics |
| Flow tube installation | 8–16 hrs | 2 Honeywell + 1 Sifab |
| Hydraulic system reinstallation | 8–12 hrs | 1 Honeywell |
| Electrical/instrumentation | 16–24 hrs | 1 Honeywell + 1 Sifab E&I |
| Piping reconnection and leak test | 8–16 hrs | 1 Sifab piping |
| Functional testing | 8–16 hrs | 1 Honeywell |
| Water draw test (SAT) | 16–24 hrs | 1 Honeywell + Justervesenet |
| **Total estimated** | **88–148 hrs** | **8–12 people over ~2–3 weeks** |

**Cost estimate for offshore work:** 88–148 man-hours × NOK 2,500–3,500/hr (offshore rate) = **NOK 220,000–518,000** (approx. USD 20,000–48,000) for labor alone, plus mobilization, travel, accommodation, tool rental.

### 5.4 CHALLENGE: Honeywell Warranty

Honeywell standard warranty starts at delivery. If Sifab/others disassemble the prover, Honeywell may void the warranty unless:
- Honeywell approves the disassembly procedure in writing
- Honeywell supervises or performs the disassembly
- Honeywell performs the reassembly and SAT
- Warranty start date is after SAT completion (per RFQ: min 28 months from commissioning)

**Action required:** Honeywell must be contractually committed to the modular split concept from the beginning. This must be in the purchase order scope.

---

## 6. Questions for Honeywell (TQ Addendum)

| TQ# | Question | Priority |
|-----|----------|----------|
| TQ-009 | Please provide detailed GA drawing of SVP085 showing all external dimensions, including frame cross-section and foot attachment details. We need to confirm whether the frame width (1,448 mm) can be reduced by removing feet. | **CRITICAL** |
| TQ-010 | Has Honeywell ever split/disassembled an SVP085 (or any SVP model) for transport through restricted access on an offshore platform? If yes, please share the procedure and lessons learned. | **CRITICAL** |
| TQ-011 | What is the exact dry weight of the SVP085 in CL600 RTJ configuration? What is the weight breakdown by major component (flow tube, frame, drive, controller)? | **HIGH** |
| TQ-012 | Can the flow tube be removed from the frame and reinstalled without affecting the gravimetric calibration? What alignment tolerances are required? | **CRITICAL** |
| TQ-013 | Will Honeywell provide a warranty that covers disassembly, transport, and reassembly on Snorre A? What are the conditions? | **HIGH** |
| TQ-014 | Can Honeywell laser-mark alignment reference points at the factory to facilitate reassembly alignment verification? | **MEDIUM** |
| TQ-015 | What is the recommended procedure for piston seal protection during transport? Should a new seal be installed after reassembly? | **HIGH** |
| TQ-016 | Can the SVP085 frame be designed from the start with bolted splice joints to facilitate modular splitting? (i.e., design-for-split rather than cut-and-splice after factory build) | **CRITICAL** |
| TQ-017 | We plan to transport the modules through the platform door by flipping them 90° on their side (rotating the cross-section). Can the flow tube and frame withstand being transported in a horizontal/flipped orientation? Any restrictions? | **HIGH** |
| TQ-018 | What is the weight of the hydraulic drive unit (motor + pump + oil reservoir) separately from the frame? We plan to remove it for transport to avoid overloading the split frame sections. | **HIGH** |
| TQ-019 | Can the frame be designed with the splice joint positioned so that the drive-end section and non-drive-end section have approximately equal weight? | **MEDIUM** |

---

## 7. Sifab Engineering Scope

### 7.1 Structural Engineering (Norsok M-101, L-004, R-002)
- Frame modification design (splice joints or foot removal procedure)
- Transport cradle design for flow tube (SS316L, shock-mounted)
- Lifting lug design for each module (Norsok R-002, DNV-ST-N001)
- Weight and COG calculations for each module
- Structural analysis of modified frame (FEA if required)

### 7.2 Metering Engineering (API MPMS 4.2)
- Alignment verification procedure (factory baseline vs. reassembly)
- Water draw test procedure for SAT
- Calibration uncertainty analysis (effect of disassembly/reassembly)
- Coordination with Justervesenet for SAT witness

### 7.3 Process / Piping (Norsok L-004, M-630)
- Disassembly/reassembly procedure for process piping
- Leak test procedure after reassembly
- Pressure test procedure (hydrostatic 1.5× design)

### 7.4 E&I Engineering (Norsok E-001, I-001, TR3023, TR3032)
- Cable and tubing tagging scheme
- Reconnection verification procedure
- ATEX integrity check after reassembly
- Functional test procedure (switches, controller, motor)

### 7.5 HSE (Norsok S-001, S-002)
- Lifting plan for each module (crane capacity, rigging plan)
- Transport plan through platform corridors
- Risk assessment (HAZID) for offshore reassembly
- Permit to Work requirements

---

## 8. Recommended Strategy for Honeywell Discussion

**Key message to Honeywell:** Sifab needs Honeywell to design the SVP085 from the start as a "split-ready" unit. This means:

1. **Frame designed with bolted splice joints** — not welded, so it can be disassembled without cutting
2. **Flow tube mounted with bolted connections** — easy to remove from frame without special tools
3. **Hydraulic system with quick-disconnect couplings** — rapid disconnect/reconnect
4. **All alignment reference points laser-marked at factory** — for reassembly verification
5. **Factory-documented disassembly/reassembly procedure** — step-by-step with torque values, alignment tolerances
6. **Warranty explicitly covers the split process** — warranty starts after SAT on Snorre A

**This is not a standard request.** Honeywell has built 100+ offshore SVPs, but we cannot find evidence of a modular split design. Sifab must make the case that this is technically feasible and commercially necessary.

**Sifab's value-add:** We have the structural fabrication capability to design and manufacture the transport cradles, modified frame components, and lifting arrangements — all to Norsok standards. We can take ownership of the split engineering while Honeywell focuses on the prover itself.

---

## 9. Next Steps

| # | Action | Owner | Deadline |
|---|--------|-------|----------|
| 1 | Send TQ-009 through TQ-016 to Honeywell (via Sidney Swart) | Sondre / Tom | Before 4 March 2026 bid |
| 2 | Request SVP085 GA drawing from Honeywell | Tom | ASAP |
| 3 | Confirm door opening dimensions with Equinor/Guidant (exact as-built) | Tom | This week |
| 4 | Ask Equinor if door frame can be temporarily removed for extra width | Tom | This week |
| 5 | Structural engineering — preliminary frame sectioning concept | Sifab Structural | 2 weeks |
| 6 | Transport cradle concept design | Sifab Structural | 2 weeks |
| 7 | Metering — alignment verification procedure (draft) | Sifab Metering | 3 weeks |
| 8 | HSE — preliminary lifting plan and HAZID | Sifab HSE | 3 weeks |
| 9 | Commercial — estimate cost for split engineering scope | Sondre / Tom | For bid submission |
| 10 | Meeting with Honeywell to discuss split concept | All | ASAP after TQ response |

---

## 10. Risk Register

| Risk | Likelihood | Impact | Mitigation |
|------|-----------|--------|------------|
| Frame cannot be narrowed to <1,400 mm | Medium | Critical | Option B (custom Sifab frame) or Option D (modify door) |
| Calibration accuracy lost after reassembly | Low | Critical | SAT water draw test mandatory; Honeywell oversight |
| Honeywell refuses warranty for split prover | Medium | High | Contractual agreement before PO; Honeywell performs SAT |
| Piston seal damaged during transport | Low | High | Remove piston, transport in sealed container, inspect before install |
| Offshore reassembly takes longer than planned | Medium | Medium | Detailed procedure, practice run at Sifab workshop |
| Justervesenet unavailable for SAT witness | Low | High | Schedule early, coordinate with Justervesenet |
| Platform crane capacity insufficient for modules | Low | High | Verify crane capacity before splitting into modules; may need smaller splits |
| Alignment tolerance not achievable offshore | Low | Critical | Laser alignment equipment; practice at Sifab first |

---

*This document is a working engineering plan. It will be updated as Honeywell provides GA drawings, weight data, and responds to technical queries.*

**Sifab AS** — Bedriftsveien 24, 4313 Sandnes, Norway
