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
| **Max module length** | 2,500 mm (corridor/maneuvering constraint) |

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

### 3.1 Key Insight: Different Strategy per Module Type

The SVP085 cross-section in normal upright orientation (1,448 mm W × ~2,286 mm H) does not fit through the 1,400 × 2,200 mm door. The solution uses **two different transport strategies** depending on the component shape:

**A) Flow tube (cylindrical, ~Ø400 mm):** Does NOT need to be flipped. The flow tube is round — it fits through the door in any orientation. It is valved off, mounted to a temporary Sifab-fabricated transport frame, and rolled straight through the door on a dolly.

**B) Frame sections (rectangular, 1,448 mm wide):** Must be flipped 90° on their side. In flipped orientation the cross-section becomes ~756 mm × 1,448 mm — fits within the 1,400 × 2,200 mm door.

| Component | Shape | Transport Orientation | Cross-section through door | Fits? |
|-----------|-------|----------------------|---------------------------|-------|
| **Flow tube on temp. frame** | Cylindrical Ø400 | **Upright — no flip needed** | ~800 × ~600 mm | **YES** |
| **Frame sections** | Rectangular 1,448 W | **Flipped 90° on side** | ~756 × 1,448 mm | **YES** |
| **Hydraulic drive** | Compact box | **Upright** | ~800 × 800 mm | **YES** |
| **Controller + accessories** | Various small | **Upright** | All < 1,200 mm | **YES** |

**Remaining constraint:** No module may exceed 2,500 mm in length. The 5,258 mm overall length must be split into sections that each stay within this limit for corridor maneuvering on the platform.

### 3.2 Frame Splitting — Weight Distribution is Critical

When splitting the frame into sections, the motor and hydraulic equipment are concentrated at the drive end. If the frame is split unevenly, the drive-end section becomes disproportionately heavy and structurally loaded. **Each frame section must be self-supporting and balanced.**

**Design principle:** Split the frame so that heavy components (motor, hydraulic pump, oil reservoir) are distributed or can be removed and transported separately — preventing any single frame section from being overloaded.

---

## 4. Proposed 3-Module Split Concept

### Module 1: Flow Tube on Temporary Transport Frame (THE CRITICAL MODULE)

**Description:** The precision-calibrated flow tube with detector switches, removed from the Honeywell frame, valved off, and mounted to a temporary Sifab-fabricated transport frame. The flow tube is cylindrical (~Ø400 mm) — it does NOT need to be flipped. It rolls straight through the door upright on its temporary frame.

| Parameter | Value |
|-----------|-------|
| Flow tube dimensions | **LENGTH TBD — must be confirmed by Honeywell** × Ø400 mm (cylindrical) |
| Max allowed length | **2,500 mm** (hard constraint) |
| Temporary transport frame | Length to match tube + 100 mm, max 800 × 800 mm cross-section |
| Estimated weight (tube + temp. frame) | ~1,700–2,200 kg |
| Transport orientation | **UPRIGHT — no flipping needed** (tube is round) |
| Fits through door? | **YES** (~800 mm W × ~800 mm H, well within 1,400 × 2,200) |

**CRITICAL: Flow tube length must be confirmed by Honeywell.** The SVP085 overall length is 5,258 mm, but the actual flow tube length may be shorter (the overall dimension includes frame overhang, drive housing, etc.). If the flow tube exceeds 2,500 mm, this must be discussed with Honeywell — the calibrated tube cannot be shortened. Honeywell to advise if the tube length is compatible with the 2,500 mm module limit, and if not, what alternatives exist.

**Temporary transport frame concept:**
- Sifab designs and fabricates a SS316L temporary frame specifically for moving the flow tube through the platform door
- Frame includes: saddle supports for the tube, isolation valves on both ends, rollers/wheels on the base, lifting lugs per Norsok R-002, shock-absorbing mounts
- The flow tube is valved off at both flanged ends to seal and protect the precision-calibrated bore
- Flange protection covers on RTJ faces (ANSI CL600)
- After transport through the door, the flow tube is lifted off the temporary frame and mounted back onto the reassembled original Honeywell frame
- **The temporary frame then comes back out through the door — it is only used for transport**

**Critical requirements:**
- Flow tube is the heart of the prover — gravimetrically calibrated to ≤0.020% repeatability
- Must be handled as a precision instrument — NO impacts, NO bending loads
- Detector switches must be protected (optical/magnetic switches at each end)
- All openings sealed with VCI (Vapor Corrosion Inhibitor) protection
- Piston and rod assembly removed and transported separately (inside Module 3)
- **After reassembly on the original Honeywell frame, a water draw test (SAT) is MANDATORY to verify calibration**

**Honeywell scope (included in bid):**
- Design and supply SS316L **temporary transport frame** with:
  - Saddle supports sized to flow tube OD
  - Isolation valves (CL600) on both ends
  - Rollers/wheels rated for ~2,200 kg
  - Shock-absorbing mounts to protect calibrated bore
  - Lifting lugs per Norsok R-002
- Flange protection covers (ANSI CL600 RTJ faces)
- Transport procedure and rigging plan

### Module 2: Structural Frame + Hydraulic Drive (SPLIT INTO SUB-MODULES)

**Description:** The SS316L support frame split into 3 sections at designed splice points, each section max 2,500 mm long. Motor and hydraulic drive **removed from frame and transported as a separate sub-module** to keep frame sections light and balanced.

#### Module 2A — Frame Section: Drive End
| Parameter | Value |
|-----------|-------|
| Estimated dimensions | ~1,750 × 1,448 × ~800 mm (upright) |
| Flipped for transport | ~1,750 × 800 × 1,448 mm |
| Weight (frame only, drive removed) | ~400–500 kg |
| Fits through door (flipped)? | **YES** (800 mm W × 1,448 mm H) |

#### Module 2B — Frame Section: Center
| Parameter | Value |
|-----------|-------|
| Estimated dimensions | ~1,750 × 1,448 × ~800 mm (upright) |
| Flipped for transport | ~1,750 × 800 × 1,448 mm |
| Weight (frame only) | ~400–500 kg |
| Fits through door (flipped)? | **YES** (800 mm W × 1,448 mm H) |

#### Module 2C — Frame Section: Non-Drive End
| Parameter | Value |
|-----------|-------|
| Estimated dimensions | ~1,750 × 1,448 × ~800 mm (upright) |
| Flipped for transport | ~1,750 × 800 × 1,448 mm |
| Weight (frame only) | ~400–500 kg |
| Fits through door (flipped)? | **YES** (800 mm W × 1,448 mm H) |

#### Module 2D — Hydraulic Drive Unit (separate from frame)
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

**Honeywell scope (included in bid):**
- Frame splice design engineering (bolted connections, Norsok M-101)
- Temporary transport supports for flipped orientation
- Alignment verification procedure (laser alignment after reassembly)
- Rolling dollies for corridor transport (Norsok R-002 for lifting)

**KEY ENGINEERING REQUIREMENT 1 — Frame Splice Design:**
The splice must be designed so that when the two frame halves are bolted together and the flow tube is reinstalled, all mounting points are within ±0.5 mm of factory position. Options:
1. **Precision dowel pins + bolted flanges** — dowels provide alignment, bolts provide clamping
2. **Machined register faces** — mating surfaces machined at factory, self-aligning when bolted
3. **Honeywell designs splice from the start** — frame built in two halves with factory-machined joint (preferred)

**KEY ENGINEERING REQUIREMENT 2 — Additional Flow Tube Mounting Points:**
The standard SVP085 has only 2 mounting points where the flow tube attaches to the frame. When the frame is split, the flow tube must also be supported at each splice location. Otherwise the tube will be unsupported at the joint, creating a bending moment under operating loads (piston cycling, vibration, thermal expansion).

**Requirement:** Add a flow tube mounting/support point at each frame splice location. This means:
- Frame is split into 3 sections → 2 additional mounting points at the splices (total: 4)
- Each frame section must have at least 1 flow tube mounting point
- Additional mounting points must NOT alter the calibrated bore geometry — they must be external saddle supports, not clamps that deform the tube
- Honeywell to confirm that additional mounting points do not affect calibration or introduce stress concentrations
- **This must be part of the factory design — not a field modification**

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

| Module | Contents | Dimensions (transport) | Weight | Orientation | Transport Method |
|--------|----------|----------------------|--------|-------------|-----------------|
| 1 | Flow tube on temp. frame | TBD (max 2,500) × 800 × 800 mm | ~1,700–2,200 kg | **Upright** (tube is round) | Rolling dolly/temp. frame |
| 2A | Frame — drive end | ~1,750 × 800 × 1,448 mm | ~400–500 kg | **Flipped 90°** on side | Rolling dolly |
| 2B | Frame — center | ~1,750 × 800 × 1,448 mm | ~400–500 kg | **Flipped 90°** on side | Rolling dolly |
| 2C | Frame — non-drive end | ~1,750 × 800 × 1,448 mm | ~400–500 kg | **Flipped 90°** on side | Rolling dolly |
| 2D | Hydraulic drive unit | 1,200 × 800 × 800 mm | ~500–800 kg | **Upright** | Dolly or carry |
| 3 | Controller + piping + piston | Various (all < 1,200 mm wide) | ~400–700 kg | **Upright** | Multiple small loads |
| | **TOTAL** | **All modules ≤ 2,500 mm long** | **~3,800–5,200 kg** | | **6–7 loads through door** |

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
| TQ-017 | The frame sections will be flipped 90° on their side to pass through the platform door (cross-section becomes 756 × 1,448 mm). The flow tube is cylindrical and will be transported upright on a temporary Sifab-fabricated frame — no flipping needed. Can the frame withstand being transported in a flipped orientation? Any restrictions on the flow tube being temporarily mounted on a transport frame? | **HIGH** |
| TQ-018 | What is the weight of the hydraulic drive unit (motor + pump + oil reservoir) separately from the frame? We plan to remove it for transport to avoid overloading the split frame sections. | **HIGH** |
| TQ-019 | Can the frame be designed with the splice joint positioned so that the drive-end section and non-drive-end section have approximately equal weight? | **MEDIUM** |
| TQ-020 | The standard SVP085 has 2 flow tube mounting points. We are splitting the frame into 3 sections, creating 2 splice locations. We need an additional saddle-type support at each splice so every frame section carries the tube (total: 4 mounting points). Can Honeywell add these without affecting calibration or introducing stress on the flow tube? | **CRITICAL** |
| TQ-021 | What is the exact length of the SVP085 flow tube (calibrated bore only, excluding frame overhang)? All modules must be ≤2,500 mm long for platform corridor maneuvering. If the flow tube exceeds 2,500 mm, what alternatives does Honeywell propose? | **CRITICAL** |

---

## 7. Honeywell Engineering Deliverables (Required in Bid)

All engineering for the modular split is Honeywell's scope. The following must be included in Honeywell's quotation:

### 7.1 Structural (Norsok M-101, L-004, R-002)
- Split-ready frame design with bolted splice joints
- Additional flow tube mounting points at splice locations
- Temporary transport frame for flow tube (SS316L, with rollers and valve isolation)
- Lifting lug design for each module (Norsok R-002, DNV-ST-N001)
- Weight and COG calculations for each module
- Structural analysis of split frame (FEA as required)

### 7.2 Metering (API MPMS 4.2)
- Alignment verification procedure (factory baseline vs. reassembly)
- Water draw test procedure for SAT
- Calibration uncertainty analysis (effect of disassembly/reassembly)
- Confirmation that calibration accuracy is maintained after reassembly

### 7.3 Process / Piping (Norsok L-004, M-630)
- Complete disassembly/reassembly procedure for all process piping
- Leak test procedure after reassembly
- Pressure test procedure (hydrostatic 1.5× design)

### 7.4 E&I (Norsok E-001, I-001, TR3023, TR3032)
- Cable and tubing tagging scheme
- Reconnection verification procedure
- ATEX integrity check after reassembly
- Functional test procedure (switches, controller, motor)

### 7.5 HSE (Norsok S-001, S-002)
- Lifting plan for each module (crane capacity, rigging plan)
- Transport plan through platform corridors
- Risk assessment for offshore reassembly
- Method statements for disassembly and reassembly

### 7.6 Services (included in Honeywell bid)
- Honeywell personnel for disassembly at onshore facility in Norway
- Honeywell certified prover technician on site for reassembly and commissioning on Snorre A
- SAT (water draw test) after reassembly — witnessed by all parties
- All transport frames and temporary supports designed and supplied by Honeywell
- Lifting gear and mounting equipment arranged by end user (Equinor) on the platform

---

## 8. Honeywell Scope — Full Delivery Including Modular Split

### 8.1 Core Principle: Honeywell Owns the Entire Process

The modular split, transport, reassembly, and recommissioning is **Honeywell's scope of delivery**. Sifab is the buyer — Honeywell must agree to and deliver the complete solution, including:

- Design of the split-ready frame (bolted splice joints)
- Additional flow tube mounting points at splice locations
- Temporary transport frame/cradle for the flow tube
- Factory build, calibration, and FAT as a complete unit
- Disassembly procedure and execution
- All transport frames, dollies, and lifting equipment
- Reassembly on Snorre A platform
- SAT (water draw test) after reassembly
- Full warranty starting after successful SAT on Snorre A

**Sifab will work together with Honeywell throughout the process**, providing local support, workshop facilities in Sandnes, offshore logistics coordination, and Norsok compliance oversight. But the engineering responsibility and delivery commitment must be Honeywell's.

### 8.2 What Honeywell Must Include in Their Bid

1. **Frame designed with bolted splice joints from the start** — not welded, so it can be unbolted into 2 sections and reassembled. Factory-machined alignment features (dowel pins or register faces).
2. **Additional flow tube mounting point at the splice location** — saddle-type support so each frame section carries the tube. Must not affect calibration.
3. **Temporary transport frame for the flow tube** — with valve isolation, rollers, shock mounts, and lifting lugs. Honeywell to design and supply.
4. **Hydraulic system with quick-disconnect couplings** — rapid disconnect/reconnect for the drive unit.
5. **Alignment reference points laser-marked at factory** — for reassembly verification.
6. **Complete disassembly/reassembly procedure** — documented, with torque values, alignment tolerances, and step-by-step instructions.
7. **Disassembly at onshore facility in Norway** — Honeywell personnel to supervise or execute.
8. **Reassembly and commissioning on Snorre A** — Honeywell personnel on site.
9. **SAT (water draw test) after reassembly** — witnessed by Buyer, Contractor, End Client, and Justervesenet.
10. **Warranty starts after successful SAT on Snorre A** — minimum 28 months from commissioning, not from factory shipment.

### 8.3 Why This is Feasible

The transport concept is straightforward:
- The **flow tube** (the precision part) is cylindrical (~Ø400 mm) — it rolls straight through the 1,400 mm door with plenty of clearance, mounted on a temporary transport frame. No flipping, no complex maneuvering.
- The **frame sections** (structural steel, non-precision) are flipped 90° on their side — simple mechanical handling.
- The **drive unit and controller** are compact boxes that fit through the door easily.
- **Once inside, everything goes back onto the original Honeywell frame exactly as it was at FAT.** The temporary transport frame comes back out.
- A **water draw SAT** confirms calibration is maintained. This is standard practice for any offshore prover installation.
- Honeywell has over 100 offshore SVPs installed worldwide. The modular split is a logistics challenge, not a technical barrier.

### 8.4 Commercial Reality

This is an Equinor fiscal metering project on Snorre A — a significant contract. The modular split engineering is additional scope that Honeywell should price into their bid. We expect Honeywell to include all costs for the split design, temporary transport equipment, disassembly, reassembly, and SAT as line items in their quotation.

---

## 9. Next Steps

| # | Action | Owner | Deadline |
|---|--------|-------|----------|
| 1 | Send this modular split plan + TQ-009 through TQ-020 to Honeywell (via Sidney Swart) | Tom | Before 4 March 2026 bid |
| 2 | Request SVP085 GA drawing from Honeywell | Tom | ASAP |
| 3 | Confirm door opening dimensions with Equinor/Guidant (exact as-built measurements) | Tom | This week |
| 4 | Ask Equinor for corridor dimensions and transport route from door to prover room | Tom | This week |
| 5 | Meeting with Honeywell to discuss split concept and confirm feasibility | Tom / Sondre | ASAP |
| 6 | Honeywell to provide preliminary split concept drawing | Honeywell | With bid |
| 7 | Honeywell to provide weight breakdown by component | Honeywell | With bid |
| 8 | Honeywell to confirm warranty terms for split/reassembly scope | Honeywell | With bid |
| 9 | Honeywell to price modular split as line items in quotation | Honeywell | With bid |
| 10 | Sifab to review Honeywell bid and confirm commercial terms | Sondre / Tom | After bid received |

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
