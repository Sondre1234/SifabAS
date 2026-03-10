# ATEX Directive 2014/34/EU

| Field | Value |
|-------|-------|
| Reference | Directive 2014/34/EU (ATEX Equipment Directive) |
| Title | Equipment and Protective Systems Intended for Use in Potentially Explosive Atmospheres |
| Issuing Body | European Parliament and Council of the European Union |
| Current Version | 2014/34/EU (replaced 94/9/EC, effective 20 April 2016) |

## Scope

ATEX Directive 2014/34/EU establishes the essential health and safety requirements for equipment and protective systems intended for use in potentially explosive atmospheres. It covers all equipment -- electrical and non-electrical, mechanical and instrumentation -- placed on the market or put into service within the European Economic Area (EEA), including Norway. The directive applies to the design, manufacture, and conformity assessment of equipment, and requires CE marking before the equipment can be placed on the market. Sifab AS, as a supplier of metering instruments, flow computers, transmitters, valves, and complete skid assemblies for offshore installations, must ensure that all equipment destined for hazardous areas meets ATEX requirements.

## Equipment Groups and Categories

ATEX divides equipment into two groups based on the intended environment:

### Group I -- Mining (Not Relevant to Sifab)
Equipment intended for use in underground mines and surface installations of mines endangered by firedamp and/or combustible dust.

### Group II -- All Other Explosive Atmospheres (Relevant to Sifab)
Equipment intended for use in potentially explosive atmospheres other than mines. This group is subdivided into three categories based on the level of protection:

| Category | Protection Level | Applicable Zones (Gas) | Applicable Zones (Dust) | Description |
|----------|-----------------|----------------------|------------------------|-------------|
| **1G / 1D** | Very high | Zone 0 / Zone 20 | Zone 20 | Equipment remains safe with two independent faults. Required where explosive atmosphere is present continuously or for long periods. |
| **2G / 2D** | High | Zone 1 / Zone 21 | Zone 21 | Equipment remains safe with one fault. Required where explosive atmosphere is likely to occur in normal operation. |
| **3G / 3D** | Normal | Zone 2 / Zone 22 | Zone 22 | Equipment provides normal level of protection. Required where explosive atmosphere is not likely to occur, or only for short periods. |

**For Sifab:** Most offshore process areas are classified as Zone 1 or Zone 2 (gas). Sifab typically supplies equipment for:
- **Zone 1** areas (Category 2G) -- metering systems in process areas, prover areas
- **Zone 2** areas (Category 3G) -- utility areas, some pump rooms

## Zone Definitions (per IEC 60079-10-1)

| Zone | Definition | Typical Locations on Offshore Installations |
|------|-----------|----------------------------------------------|
| Zone 0 | Explosive atmosphere present continuously or for long periods (>1000 hrs/year) | Inside process equipment (vessels, pipes) -- Sifab equipment not normally installed inside Zone 0 |
| Zone 1 | Explosive atmosphere likely to occur in normal operation (10-1000 hrs/year) | Around flanges, valves, sampling points, open drains, prover areas |
| Zone 2 | Explosive atmosphere not likely in normal operation; if it occurs, only for short periods (<10 hrs/year) | Enclosed areas adjacent to Zone 1, well-ventilated process areas |

## ATEX Marking Requirements

All ATEX-certified equipment must bear specific marking. The marking format is:

```
CE [Notified Body number]
Ex [symbol]  II [Category] G/D  [Temperature class]  [Protection type]

Example: CE 0539
         Ex II 2G  T4  Ex d IIB+H2
```

### Marking Elements Explained

| Element | Meaning | Example |
|---------|---------|---------|
| CE + NB number | CE mark with Notified Body number (for Cat. 1 and 2) | CE 0539 (DEKRA) |
| Ex (hexagon) | ATEX-specific marking | Stylized Ex in hexagon |
| Group II | Surface industries (not mining) | II |
| Category | Protection level (1, 2, or 3) | 2 |
| G or D | Gas (G) or Dust (D) atmosphere | G |
| Temperature class | Maximum surface temperature | T1 (450C) through T6 (85C) |
| Protection type | IEC 60079 protection concept | Ex d (flameproof), Ex e (increased safety), Ex i (intrinsic safety) |
| Gas group | Categorizes gases by ignition energy | IIA (propane), IIB (ethylene), IIC (hydrogen) |

### Common Protection Types in Sifab's Equipment

| Code | Protection Type | Typical Use in Sifab Equipment |
|------|----------------|-------------------------------|
| Ex d | Flameproof enclosure | Junction boxes, local displays, flow computers in Zone 1 |
| Ex e | Increased safety | Terminal boxes, motors, lighting in Zone 1/2 |
| Ex i | Intrinsic safety (ia/ib) | Transmitters, sensors, 4-20mA loops in Zone 0/1/2 |
| Ex p | Pressurization | Analyzer houses, large control panels in Zone 1/2 |
| Ex n | Non-sparking | Equipment designed for Zone 2 only |
| Ex t | Protection by enclosure (dust) | Rarely applicable to Sifab's offshore work |

## Conformity Assessment Procedures

The conformity assessment route depends on the equipment category:

| Category | Assessment Route | Notified Body Required? | Documentation |
|----------|-----------------|------------------------|---------------|
| Category 1 (Zone 0/20) | EU Type Examination (Module B) + Quality Assurance (Module D) or Product Verification (Module F) | Yes (design + production) | Full technical file, type examination certificate, ongoing production surveillance |
| Category 2 (Zone 1/21) | EU Type Examination (Module B) + Conformity to Type (Module C1 for non-electrical; Module D or E for electrical) | Yes (design; production for electrical) | Technical file, type examination certificate, internal production control (non-electrical) or NB surveillance (electrical) |
| Category 3 (Zone 2/22) | Internal Production Control (Module A) | No | Technical file, internal checks, self-declaration |

**For Sifab:** When Sifab supplies individual ATEX-certified instruments (from Honeywell, Emerson, etc.), the manufacturer holds the ATEX certificate. When Sifab integrates multiple ATEX-certified components into an assembly (e.g., a metering skid), Sifab may be considered the manufacturer of the assembly and must ensure:
1. Each component is suitable for the intended zone and gas group
2. The assembly as a whole does not compromise individual component certifications
3. An ATEX declaration of conformity is issued for the assembly if required
4. The assembly documentation includes the ATEX installation drawing showing zone boundaries and cable entries

## Key Requirements for Sifab AS

| Section | Topic | Relevance |
|---------|-------|-----------|
| Annex II, 1.0 | General requirements | Equipment must be designed to prevent explosion sources (sparks, hot surfaces, static electricity). Applies to all Sifab-supplied equipment for hazardous areas. |
| Annex II, 1.1 | Potential ignition sources | Equipment must be designed so potential ignition sources cannot become effective. Sifab must verify that all components in hazardous areas are properly certified. |
| Annex II, 1.2 | External influences | Equipment must withstand environmental conditions (temperature, humidity, vibration, corrosion). Relevant to Sifab's offshore equipment specifications. |
| Annex II, 1.5 | Safety devices | Autonomous safety devices must function independently of measuring/control systems. Relevant to safety valves and shutdown devices on metering skids. |
| Annex II, 2.1 | Category 2 requirements | Equipment must ensure protection in the event of one fault. Zone 1 equipment on Sifab's metering skids must meet this. |
| Annex II, 2.2 | Category 3 requirements | Equipment must ensure protection in normal operation. Zone 2 equipment on Sifab's installations must meet this. |
| Art. 5 | Placing on the market | Equipment must carry CE marking and be accompanied by EU Declaration of Conformity. Sifab must verify all procured equipment has valid ATEX documentation. |
| Art. 13 | Manufacturer's obligations | Manufacturer must prepare technical documentation, carry out conformity assessment, affix CE marking. Applies to Sifab when acting as manufacturer of assemblies. |

## Temperature Classes

The temperature class indicates the maximum surface temperature of the equipment. It must be lower than the auto-ignition temperature of the gases present.

| Class | Max Surface Temp | Common Gases Below This Threshold |
|-------|-----------------|-----------------------------------|
| T1 | 450 C | Methane (595C), Ethane (515C), Propane (450C) |
| T2 | 300 C | Butane (365C), Pentane (309C) |
| T3 | 200 C | Gasoline (280C), Diesel (225C), Hydrogen sulfide (260C) |
| T4 | 135 C | Ethyl ether (160C) |
| T5 | 100 C | Carbon disulfide (102C) |
| T6 | 85 C | Rarely required in oil and gas |

**For Sifab:** Most offshore hydrocarbon environments require T3 or T4. Always verify the specific temperature class requirement from the operator's hazardous area classification drawings.

## Sifab Agents Using This
- **Instrumentation Agent** -- primary reference for selecting ATEX-certified instruments, verifying certificates, and specifying explosion protection concepts for metering and instrumentation systems
- **HSE Agent** -- understanding ATEX requirements as part of overall HSE compliance, reviewing ATEX documentation packages
- **Metering Agent** -- ensuring metering system components meet ATEX requirements for the intended installation zones
- **Project Manager Agent** -- understanding ATEX scope in project specifications and procurement
- **Quality Management Agent** -- verifying ATEX certificates and declarations are included in documentation packages per B.SI.01.07

## Cross-References
- [Hazardous Area Classification (IEC 60079-10)](hazardous-area-classification.md) -- how zones are defined, which determines ATEX category requirements
- [Functional Safety (IEC 61508/61511)](functional-safety.md) -- SIL-rated instruments in hazardous areas must meet both ATEX and SIL requirements
- [PSA Regulations](psa-regulations.md) -- Facilities Regulations reference ATEX compliance
- [Norwegian HSE Framework Overview](README.md)
- IEC 60079-0 (general requirements for explosive atmospheres)
- IEC 60079-1 (flameproof enclosures, Ex d)
- IEC 60079-7 (increased safety, Ex e)
- IEC 60079-11 (intrinsic safety, Ex i)
- IEC 60079-14 (installation requirements)
- IEC 60079-17 (inspection and maintenance)
- NORSOK I-001, I-002 (instrumentation requirements for hazardous areas)
