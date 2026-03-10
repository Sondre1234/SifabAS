# IEC 60079-10-1 / IEC 60079-10-2 — Hazardous Area Classification

## Scope

IEC 60079-10-1 (explosive gas atmospheres, Ed. 3.0, 2020) and IEC 60079-10-2 (combustible dust atmospheres, Ed. 2.0, 2015) define the methodology for classifying locations where flammable gases, vapors, or combustible dusts may be present in quantities sufficient to create an explosion risk. The standards establish zone definitions, classification methodology, ventilation criteria, and documentation requirements. For Sifab AS, the zone classification of an installation determines the Equipment Protection Level (EPL) and ATEX category required for all instruments, junction boxes, and electrical components on metering skids and special items.

## Key Requirements for Sifab AS

- **Zone definitions — gas (IEC 60079-10-1)**:
  - Zone 0: Explosive atmosphere present continuously or for long periods (> 1000 h/year). Typically the interior of process vessels; Sifab's instruments are mounted externally so Zone 0 installation is rare.
  - Zone 1: Explosive atmosphere likely in normal operation (10–1000 h/year). The most common zone for Sifab metering skid equipment — areas around flanged connections, valve packing, sample points, and drain connections.
  - Zone 2: Explosive atmosphere not expected in normal operation; if present, only briefly (< 10 h/year). Applies to the periphery of Zone 1 areas and enclosed skid rooms with adequate ventilation.
- **Zone definitions — dust (IEC 60079-10-2)**:
  - Zone 20 / 21 / 22: Continuous, likely, or occasional combustible dust cloud. Not typically applicable to Sifab's offshore oil and gas metering work.
- **Classification methodology**: Identify release sources and their grade (continuous, primary, or secondary), assess ventilation degree (high/medium/low) and availability (good/fair/poor), then determine zone type and physical extent per IEC 60079-10-1 Annex B.
- **Ventilation effect**: Adequate ventilation reduces zone extent and can downgrade zone type. For enclosed skid enclosures, the ventilation classification directly determines whether Zone 1 or Zone 2 applies inside the enclosure.
- **Equipment Protection Level (EPL)**: Zone 0 requires EPL Ga; Zone 1 requires EPL Gb (minimum); Zone 2 requires EPL Gc (minimum). All instruments, junction boxes, and electrical components Sifab mounts on skids must be certified to at least the EPL for the installation zone.
- **ATEX mapping**: EPL Gb = ATEX Category 2G; EPL Gc = ATEX Category 3G. Equipment must carry the ATEX mark (Directive 2014/34/EU) and be certified for the correct gas group (typically IIB for hydrocarbon offshore service) and temperature class (typically T3 or T4 — confirm against the fluid auto-ignition temperature).
- **NORSOK S-001 §6**: Requires hazardous area classification to be documented as part of the technical safety deliverables, including minimum separation distances for ignition sources from potential release points.
- **NORSOK I-001 §9**: Requires Ex-certified instruments for hazardous area installations; Ex marking, gas group, and temperature class must be documented in the instrument index for every instrument in a classified zone.
- **Documentation**: A hazardous area classification drawing must be produced for each installation showing zone types, extents, release source locations, and equipment EPL requirements. Sifab must obtain this drawing from the operator or EPCM contractor and verify that all supplied equipment meets the classified zone requirements.

## SifabAS Agent Usage

- **Primary**: HSE Agent — interpretation of hazardous area classification drawings, compliance verification against NORSOK S-001, and input to project technical safety assessments
- **Primary**: Instrumentation Agent — selection of Ex-certified instruments, junction boxes, and cable glands to match the installation zone; ATEX certificate verification; Ex data annotation in the instrument index per NORSOK I-001 §9
- **Supporting**: Structural Agent — skid layout positioning of flanges, valves, and vent outlets to manage zone extents; enclosure ventilation design for Zone 1 vs. Zone 2 determination
- **Supporting**: Project Manager Agent — ensuring the hazardous area classification drawing is on the deliverable list and client-approved before instrument procurement commences

## Cross-References

- ATEX Directive 2014/34/EU — EU/EEA market access requirement for Ex equipment; technical requirements met via IEC 60079 series
- IEC 60079-0 — General requirements for explosion-protected equipment
- IEC 60079-14 — Design, selection, and erection of electrical installations in explosive atmospheres
- IEC 60079-17 — Inspection and maintenance of electrical installations in explosive atmospheres
- NORSOK S-001 §6 — Technical safety; hazardous area classification as part of the safety layout deliverables
- NORSOK I-001 §9 — Field instrumentation for hazardous areas; Ex documentation requirements in the instrument index
- NORSOK I-002 — Safety and automation systems; SIL verification interfaces with area classification
- PSA Facilities Regulations §14 — Requires classification of hazardous areas on Norwegian installations
- [PSA Regulations summary](psa-regulations.md)
- [ATEX Directive summary](atex-directive.md)
- [Functional Safety summary](functional-safety.md)
