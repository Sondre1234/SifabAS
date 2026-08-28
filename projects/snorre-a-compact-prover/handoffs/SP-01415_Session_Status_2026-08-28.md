# SP-01415 Snorre A SVP — Session Status & Handoff (2026-08-28)

> **Purpose:** Continuity note so a new Claude Code session (e.g. on the Windows PC) can pick up exactly where we left off. Written by Sondre's session on 2026-08-28.
> Author/PM: Sondre Falch. Everything below is current as of 2026-08-28.

---

## 1. What was done this session

Three emails were drafted and **sent to Sondre's own mailbox** (`sondre.falch@sifab.no`) so Sondre can review and forward them himself. The draft scripts live only in `/tmp/` on the Mac (local, not in git) — but the **email content is already in Sondre's inbox**, so nothing is lost by leaving the Mac.

### 1.1 GA Rev 1 input — to Honeywell (Samir Sakota + Alex Plumb)
- **Status:** In Sondre's inbox, **NOT yet forwarded** to Honeywell (Sondre gives the go).
- Written in natural first-person (as if Sondre wrote it). Attachments: Equinor TR3032 + Sifab Electrical Installation & Termination Instruction.
- Content: flange facing (RTJ on 12" inlet/outlet + drain valves; **RF on the rest** — DB&B, PT take-off — because Honeywell can only do RTJ on the two main flanges + drains); flow tube 316SS (request material cert); drain blind flange list vs drawing correction (1½" ANSI 600 RTJ, confirm qty); transmitter/free-issue notes; electrical (TR3032 + NORSOK E-001/I-001/TR3023, BFOU cables, NPT thread sizes, wiring diagram SIF-1415-011).
- **Deliberately toned down the DS20/pipe-class references** (Honeywell can't produce fully to DS20; do not press the spec at them).

### 1.2 GA Rev 1 / free-issue split — to Guidant (Martin Carlsson)
- **Status:** In Sondre's inbox, **NOT yet forwarded** to Guidant. Intended for the weekly GM-5341 meeting (Guidant PM logs items into the action tracker).
- Natural first-person voice. Frames **RF on instrument connections as a proposal for Guidant to confirm** (DS20 is nominally RTJ throughout, so RF is effectively a deviation they must accept).
- Includes the **full corrected free-issue split** (see §3 below) and leaves the **temperature-transmitter mounting/post open** ("how would you like these mounted?") — per Sondre's instruction, do NOT commit Honeywell to fabricating the stand.

### 1.3 Seraphin calibration can order — to Pemberton (Ron Gibson)
- **Status: SENT by Sondre to Ron** (`rgibson@seraphinusa.com`).
- Asks Ron to confirm and send **current price + delivery time** (original quote is from March 2026) before Sifab issues the PO.
- Config in the email: Series M, 316SS wetted, **283.9 L** (Honeywell SVP085 displaced/base volume = 75 US gal; Pemberton model **EMSS0283.9L-30-3**), all §2.1 features, **5 mL** graduated-scale resolution (matches previous 151.4 L can S/N 24-67715), **NVLAP/NIST calibration** (Justervesenet dropped — see §4). Delivery quoted to Sifab AS, Bedriftsveien 20, 4313 Sandnes.

---

## 2. Flange facing decision (Snorre A specific)

- **RTJ:** 12" inlet + outlet, drain valves / drain blind flanges (1½" ANSI 600 RTJ per GA drawing p.2).
- **RF:** DB&B (double block & bleed), PT take-off — Honeywell cannot deliver RTJ on these.
- **Threaded (NPTF):** thermowells (½" NPTF) — facing does not apply.
- Snorre A is the **first prover at CL600 RTJ**; NOA (CL300) and Valhall (CL150) were RF throughout, so the RTJ/RF mix is new here.
- Interface position agreed with Sondre: **Guidant controls the onward connection** (their counter-flanges), so Sifab just states the facing per connection on the GA and Guidant matches it. Internally: when Sifab free-issues the DB&B valve, match its facing to whatever Honeywell marks on the GA (avoid an RTJ valve on an RF nozzle).

---

## 3. Corrected free-issue split (reconciled 2026-08-28)

> The old execution-plan note (line 94: "Sifab free-issue: 3 transmitters, RTDs…") was **outdated**. The confirmed split (Guidant KOM 2026-06-15) + Sondre's confirmation supersede it.

**Free-issued by Guidant (installed by Honeywell at the factory):**
- temperature elements / RTDs
- temperature transmitters
- **thermowells (3 process + 1 rod, ½" NPTF)** ← Sondre confirmed thermowells are Guidant, not Sifab

**Free-issued & mounted by Guidant, outside the skid:**
- instrument enclosure / JB with the **pressure transmitters** (prover delivered without pressure transmitters)

**Supplied by Sifab:**
- double block & bleed + instrument valves (316SS)
- tubing & fittings (6Mo, metric, per TR2000 ST701 / SF712)
- cable glands + NPT-to-metric adapters (SS316 / Ni-plated brass, per NORSOK E-001 / TR3023)
- BFOU cables (halogen-free)
- insulation + NORSOK M-501 System 6C painting of flow tube / wetted parts (in Norway, after flow test)

**Open to clarify with Guidant:** how they want the **temperature-transmitter stand/post** mounted; installation responsibility + need-date for the free-issue items.

---

## 4. Seraphin can — open point to chase

Pemberton (Ron Gibson) replied to the RFQ: **"2.2 is the only thing we cannot accommodate. The NVLAP Calibration can be [done], however."**
- RFQ **item 2.2 = Justervesenet certification** → Pemberton cannot provide it. That's fine and expected: **NIST + NVLAP is the accepted route** (precedent: Aker BP + Equinor on NOA/Valhall), and Justervesenet is **not Sifab/can scope** (it only comes in as SAT witnessing, which is Guidant/Equinor scope). Get it **minuted with Guidant** (KOM talking point #7 / DEV-017).

**⚠️ Not yet reconciled into the order — chase when Ron replies (before PO):**
- **Volume scale material: 316SS vs aluminium.** The order email said *aluminium graduated scale* (RFQ + Seraphin standard), but action register **#23** says *"ensure can volume scale is 316… else → deviation."* Ask Ron: *"Can the graduated volume scale be supplied in 316SS rather than aluminium? If aluminium is the only option, confirm and we'll note it (deviation)."*
- **Drain detail per Hugin A drawing (#31):** 2" SS bore drain @7°, 2" NPT-F drain, ½" NPTF ball valve — verify against Ron's quote (RFQ only said "2 SS ball drain valves @7°").
- **Scale tolerance 0.01 + gauge-glass SS (#39):** confirm on the quote (gauge-glass SS already in the email).
- Note: model/volume (283.9 L, EMSS0283.9L-30-3) trace to our internal execution plan marked "per quote" — **the actual Pemberton quote PDF was not re-opened this session**; the email deliberately asks Ron to reconfirm volume/price.

---

## 5. NEXT UP — Shipping & Handling meeting with Guidant + Wood

Sondre flagged an upcoming meeting with **Guidant + Wood** on **shipping & handling**. (Wood is not named in the project docs; assumed to be Equinor's installation/logistics contractor for Snorre A — confirm role.)

**Prep not yet produced.** Data already on hand (from `engineering/Modular_Split_Execution_Plan_SVP085.md`):

| Module | Size (mm) | Weight | Orientation | Handling |
|---|---|---|---|---|
| Flow tube | max 2500 × 800 × 800 | ~1700–2200 kg | Upright | Rolling dolly / temp frame |
| Frame drive-end (2A) | ~1750 × 800 × 1448 | ~400–500 kg | Flipped 90° | Rolling dolly |
| Frame center (2B) | ~1750 × 800 × 1448 | ~400–500 kg | Flipped 90° | Rolling dolly |
| Frame non-drive (2C) | ~1750 × 800 × 1448 | ~400–500 kg | Flipped 90° | Rolling dolly |

- Access door **1400 × 2200 mm**; modules flipped 90° (→ ~756 × 1448 mm) and rolled through on dolly/air-skate.
- Delivery term: **FCA Sandnes** (onward transport by others). If Sifab ships, route via Sandnes / Håkull.

**To GIVE at the meeting:** module sizes/weights, orientation, per-module lifting points (NORSOK R-002), window-passage solution (90° tilt), FCA Sandnes boundary.
**To GET:** Equinor/Wood trellis/wheel-skate handling method (#27/#37), packing orientation, offshore crane capacity, who owns transport from Sandnes onward, FAT witnessing/logistics.

**Action for next session:** build a shipping & handling talking-points doc (à la `SP-01415_KOM_Guidant_Talking_Points_2026-08-05.md`), or an agenda email to Guidant + Wood — Sondre to choose.

---

## 6. Immediate to-do list (for whoever picks this up)

1. **Forward the two GA Rev 1 emails** (Honeywell + Guidant) from Sondre's inbox once Sondre confirms.
2. **When Ron (Pemberton) replies:** add the 316-vs-aluminium scale question + verify drain detail/tolerance, then issue the Sifab PO for the can.
3. **Minute with Guidant** that can certification is NIST+NVLAP (not Justervesenet).
4. **Build shipping & handling prep** for the Guidant + Wood meeting.
5. Log the two sent-to-self GA emails as "sent to Honeywell/Guidant" in the action register **only once Sondre actually forwards them** (per the "sent folder only when actually sent" rule).
