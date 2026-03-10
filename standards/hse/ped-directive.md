# PED -- Pressure Equipment Directive 2014/68/EU

| Field | Value |
|-------|-------|
| Reference | Directive 2014/68/EU |
| Title | Harmonisation of the Laws of the Member States Relating to the Making Available on the Market of Pressure Equipment |
| Issuing Body | European Parliament and Council of the European Union |
| Current Version | 2014/68/EU (replaced 97/23/EC, effective 19 July 2016) |

## Scope

The Pressure Equipment Directive (PED) 2014/68/EU establishes the requirements for the design, manufacture, and conformity assessment of pressure equipment and assemblies with a maximum allowable pressure (PS) greater than 0.5 bar. It applies throughout the European Economic Area (EEA), including Norway. The directive covers pressure vessels, piping, safety accessories, and pressure accessories. Sifab AS, as a fabricator of volume provers, metering skids, pressure-containing piping assemblies, and special items (SI) for offshore and onshore installations, must comply with PED for all pressure equipment that falls within its scope.

## Pressure Equipment Categories

PED classifies pressure equipment into four categories (I through IV) based on the hazard level, which is determined by the type of equipment, the fluid group, and the relationship between maximum allowable pressure (PS) and volume (V) or nominal diameter (DN). Higher categories require more stringent conformity assessment.

### Fluid Groups

| Fluid Group | Description | Examples in Sifab's Work |
|-------------|-------------|--------------------------|
| Group 1 | Dangerous fluids: explosive, flammable, toxic, oxidizing (as defined in CLP Regulation) | Crude oil, natural gas, condensate, H2S-containing fluids |
| Group 2 | All other fluids not in Group 1 | Water, glycol, instrument air, nitrogen |

### Category Determination

The category is determined using conformity assessment charts in Annex II of the PED. The key parameters are:

| Equipment Type | Parameters | Chart Reference |
|---------------|------------|-----------------|
| Vessels -- Group 1 gases | PS x V | Chart 1 |
| Vessels -- Group 2 gases | PS x V | Chart 2 |
| Vessels -- Group 1 liquids | PS x V | Chart 3 |
| Vessels -- Group 2 liquids | PS x V | Chart 4 |
| Piping -- Group 1 gases | PS x DN | Chart 6 |
| Piping -- Group 2 gases | PS x DN | Chart 7 |
| Piping -- Group 1 liquids | PS x DN | Chart 8 |
| Piping -- Group 2 liquids | PS x DN | Chart 9 |

**Examples relevant to Sifab:**
- A small volume prover (PS = 100 barg, V = 500 L, Group 1 liquid) would typically fall in **Category III or IV**
- A metering skid piping assembly (PS = 150 barg, DN 100, Group 1 gas) would typically fall in **Category III**
- An instrument manifold (PS = 400 barg, DN 15, Group 1 gas) may fall in **Category I or II**

### Category Requirements Summary

| Category | Hazard Level | Conformity Assessment Modules | Notified Body Required? |
|----------|-------------|------------------------------|------------------------|
| SEP (Sound Engineering Practice) | Below Category I thresholds | No formal assessment | No -- design and manufacture according to sound engineering practice |
| I | Lowest | Module A (internal production control) | No |
| II | Low-medium | Module A2, D1, or E1 | Yes (limited involvement) |
| III | Medium-high | Module B+D, B+F, B+E, B+C2, or H | Yes (full involvement) |
| IV | Highest | Module B+D, B+F, or G | Yes (full involvement, including final assessment of each unit) |

## Conformity Assessment Modules

| Module | Description | Sifab Applicability |
|--------|-------------|---------------------|
| A | Internal production control | Self-assessment. Sifab can use for Category I equipment. |
| A2 | Internal production control + supervised pressure testing | Sifab can use for Category II. NB witnesses or approves pressure test. |
| B | EU Type Examination | NB examines the technical design. Required for Category III-IV. |
| B1 | EU Design Examination | NB examines the design without a type specimen. Alternative to Module B. |
| C2 | Conformity to type with random checks | NB performs random inspections. Used with Module B for Category III. |
| D | Quality assurance of production | NB approves and surveys Sifab's production QA system. Used with Module B. |
| D1 | Quality assurance of production | NB approves production QA. Can be used alone for Category II. |
| E | Product quality assurance | NB approves and surveys final inspection and testing. Used with Module B. |
| E1 | Product quality assurance | NB approves final inspection QA. Can be used alone for Category II. |
| F | Product verification | NB verifies each unit or statistical sample. Used with Module B. |
| G | Unit verification | NB examines design and verifies each individual unit. For Category IV. |
| H | Full quality assurance | NB approves full QA system (design + production + final inspection). Can be used alone for Category III. |
| H1 | Full quality assurance with design examination | Module H + NB examines each design. For Category IV. |

**Sifab's typical approach:**
- Category I: Module A (internal production control)
- Category II: Module A2 or D1 (Sifab's ISO 9001 QMS supports Module D1)
- Category III: Module B+D or Module H (Sifab uses Notified Body for type/design examination and production QA surveillance)
- Category IV: Module G (unit verification by NB) or Module B+F

## Essential Safety Requirements (Annex I)

PED Annex I contains the Essential Safety Requirements (ESRs) that all pressure equipment must meet. Key requirements relevant to Sifab:

| Section | Topic | Relevance |
|---------|-------|-----------|
| 1. General | Design for adequate lifetime, safe use | All Sifab pressure equipment must be designed considering all foreseeable operating conditions, including start-up, shutdown, and upset conditions. |
| 2.2.1 | Design method -- calculation | Pressure equipment must be designed by calculation (e.g., EN 13445, ASME VIII) or experimentally. Sifab typically uses EN 13445 or ASME VIII Div.1 for prover vessels. |
| 2.2.3 | Allowable stresses | Design stresses must account for material properties at design temperature, corrosion allowance, and safety factors. |
| 3.1 | Materials -- general | Materials must be suitable for the intended operating conditions (temperature, pressure, corrosion, fatigue). Must have adequate ductility and toughness. |
| 3.1.2 | Material certificates | Materials must be identified and traceable. Certificates per EN 10204 (3.1 or 3.2 as required). |
| 3.1.4 | Material for Group 1 fluids | Additional requirements for materials in contact with dangerous fluids (brittleness, corrosion resistance). Critical for Sifab's sour service applications. |
| 3.2 | Welding | Welding must be performed by appropriately qualified welders using approved procedures. WPS per EN ISO 15614, welder qualifications per EN ISO 9606. |
| 3.2.2 | Welding procedure test | All production weld types must be covered by qualified WPS. Sifab maintains a library of WPQR/WPS for common joint configurations. |
| 3.2.3 | NDE | Non-destructive examination must be performed by qualified personnel (EN ISO 9712). Extent of NDE depends on the PED category and design code. |
| 3.3 | Pressure testing | Final pressure test (hydrostatic preferred) at 1.43x PS (or as per harmonized standard). Every pressure equipment unit must be pressure-tested. |
| 3.4 | Marking and labeling | Equipment must bear CE marking, identification of manufacturer, year, PS, TS, volume, fluid group, and relevant references. |

## Harmonized Standards

PED references harmonized European standards that provide presumption of conformity with the ESRs:

| Standard | Title | Sifab Usage |
|----------|-------|-------------|
| EN 13445 | Unfired pressure vessels | Design and fabrication of prover vessels, separator vessels |
| EN 13480 | Industrial metallic piping | Design and fabrication of skid piping, prover piping |
| EN 12952 / EN 12953 | Water-tube / Shell boilers | Not typically used by Sifab |
| EN 764 series | Pressure equipment -- general | Terminology, documentation, materials |
| EN 10204 | Metallic products -- inspection documents | Material certificates (3.1 / 3.2) for all pressure-retaining materials |
| EN ISO 15614 | Welding procedure qualification | WPQR for all welding on PED equipment |
| EN ISO 9606 | Welder qualification | Qualification of manual and semi-automatic welders |
| EN ISO 9712 | NDE personnel qualification | Qualification of NDE operators (RT, UT, MT, PT) |

**Note:** Sifab also uses ASME codes (ASME VIII Div.1, ASME B31.3) when specified by the operator or for equipment destined for non-EU markets or when contractually required. When ASME codes are used for PED-scope equipment, a Particular Material Appraisal (PMA) may be required for materials not covered by harmonized European material standards.

## Key Requirements for Sifab AS

| Section | Topic | Relevance |
|---------|-------|-----------|
| Art. 4 | Free movement | PED-compliant equipment may be placed on the market throughout the EEA. Sifab's CE-marked equipment is accepted across Norway and the EU. |
| Art. 6 | Essential safety requirements | All pressure equipment must meet Annex I ESRs. Sifab must design, fabricate, and test per these requirements. |
| Art. 12 | Manufacturer's obligations | Sifab must: prepare technical documentation, apply conformity assessment, affix CE marking, issue EU Declaration of Conformity. |
| Art. 14 | Authorized representative | Sifab can appoint an authorized representative for administrative PED tasks (not for manufacturing obligations). |
| Art. 19 | Notified Body obligations | Notified Bodies must be competent, impartial, and independent. Sifab's NB must hold appropriate scope. |
| Annex I, 3.3 | Pressure testing | Hydrostatic test pressure = max of (1.43 x PS at 20C or 1.25 x PS at max operating temp). Sifab must test every unit. |
| Annex I, 3.4 | Marking | CE marking + NB number (for Cat. II-IV) + manufacturer ID + year + PS + TS + V + fluid group. Sifab must engrave or permanently affix markings. |
| Annex III | Conformity assessment procedures | Sifab must follow the appropriate module(s) based on equipment category. |

## Sifab Agents Using This
- **Structural Agent** -- primary reference for design, fabrication, and testing of pressure-containing equipment; selection of design codes (EN 13445, EN 13480, ASME VIII)
- **Quality Management Agent** -- ensuring PED documentation (technical file, DoC, NB certificates) is properly controlled per B.SI.01.07; managing welder and NDE qualifications
- **HSE Agent** -- understanding PED as part of the overall regulatory compliance framework
- **Project Manager Agent** -- scoping PED category and conformity assessment requirements during project setup; scheduling NB inspections
- **Metering Agent** -- prover vessel and metering skid pressure equipment compliance

## Cross-References
- [Norwegian HSE Framework Overview](README.md) -- PED in the context of Norwegian regulations
- [PSA Regulations](psa-regulations.md) -- Facilities Regulations reference PED compliance
- [TR2000 Guidelines](tr2000-guidelines.md) -- Equinor material requirements that supplement PED for sour service
- [NACE Sour Service](nace-sour-service.md) -- NACE MR0175/ISO 15156 for materials in H2S environments
- EN 13445 (unfired pressure vessels)
- EN 13480 (metallic piping)
- EN 10204 (material inspection documents)
- ASME VIII Division 1 (alternative design code when contractually specified)
- ASME B31.3 (process piping, alternative when contractually specified)
