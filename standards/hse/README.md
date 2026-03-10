# Norwegian HSE Framework Overview for Offshore Suppliers

| Field | Value |
|-------|-------|
| Reference | Multiple (see below) |
| Title | Norwegian HSE Regulatory Framework for Offshore Equipment Suppliers |
| Issuing Body | Petroleumstilsynet (PSA), Standards Norway, EU |
| Current Version | Ongoing (framework regulations last consolidated 2024) |

## Scope

This document provides an overview of the Norwegian health, safety, and environment (HSE) regulatory framework as it applies to offshore equipment suppliers such as Sifab AS. It describes the hierarchy of regulations, the interplay between Norwegian law, PSA regulations, NORSOK standards, and EU directives, and clarifies the distinction between operator obligations and supplier obligations. The purpose is to give Sifab engineers and agents a single reference point for understanding which regulations govern their work.

## Regulatory Hierarchy

The Norwegian offshore HSE framework follows a tiered structure:

```
Level 1: Norwegian Law (Acts of Parliament)
  - Petroleum Act (Petroleumsloven)
  - Working Environment Act (Arbeidsmiljoloven)
  - Pollution Control Act (Forurensingsloven)
  - Fire and Explosion Prevention Act
  |
Level 2: Framework Regulations (Rammeforskriften)
  - Establishes overall principles, scope, and responsibility allocation
  |
Level 3: PSA Regulations (4 main sets)
  - Facilities Regulations (Innretningsforskriften)
  - Management Regulations (Styringsforskriften)
  - Activities Regulations (Aktivitetsforskriften)
  - Technical and Operational Regulations (Teknisk og operasjonell forskrift)
  |
Level 4: NORSOK Standards & Industry Standards
  - Referenced by PSA regulations as "recognized norms"
  - Compliance with NORSOK creates presumption of regulatory compliance
  |
Level 5: Company-Specific Requirements
  - Operator technical requirements (e.g., Equinor TR2000, Aker BP specs)
  - Contract-specific specifications
```

## How NORSOK, PED, ATEX, and IEC Fit Together

### NORSOK Standards
NORSOK standards are developed by the Norwegian petroleum industry to ensure adequate safety, value creation, and cost-effectiveness. They are not legally binding on their own but are referenced as "recognized norms" by PSA regulations. When PSA regulations reference a NORSOK standard, compliance with that standard creates a presumption of regulatory compliance. Key NORSOK standards for Sifab include:

- **S-001** Safety requirements for design (fire, explosion, escape)
- **S-002** Working environment
- **I-001** / **I-002** Instrumentation requirements
- **I-104** Fiscal metering
- **Z-001** / **Z-008** / **Z-015** Documentation, criticality analysis, temporary equipment
- **R-003** Safe use of lifting equipment

### PED (Pressure Equipment Directive 2014/68/EU)
The PED is an EU directive implemented in Norwegian law through EEA membership. It applies to the design, manufacture, and conformity assessment of pressure equipment and assemblies with a maximum allowable pressure greater than 0.5 bar. Sifab must comply with PED for prover vessels, pressure-containing skid assemblies, and piping above the directive thresholds. PED compliance is separate from, but complementary to, NORSOK requirements.

### ATEX (Directive 2014/34/EU)
ATEX governs equipment intended for use in potentially explosive atmospheres. Since Sifab supplies metering and instrumentation equipment for offshore installations (Zone 1 and Zone 2 areas), all such equipment must carry appropriate ATEX certification and marking. ATEX requirements interact with IEC 60079 series standards for equipment design and with IEC 60079-10 for area classification.

### IEC 61508 / IEC 61511
These international standards govern functional safety of electrical, electronic, and programmable electronic safety-related systems. PSA regulations require that safety instrumented systems on Norwegian offshore installations comply with IEC 61508/61511. When Sifab supplies instrumentation that forms part of a Safety Instrumented System (SIS), the equipment must meet the required Safety Integrity Level (SIL).

## Sifab AS Obligations as Supplier

As an equipment supplier (not an operator), Sifab's obligations differ from those of the operator but are nonetheless significant:

### Direct Obligations
1. **Product compliance**: All equipment delivered must comply with applicable EU directives (PED, ATEX, Machinery Directive) as implemented in Norwegian law.
2. **CE marking**: Equipment requiring CE marking under EU directives must be properly marked and accompanied by declarations of conformity.
3. **Documentation delivery**: Sifab must deliver documentation packages compliant with NORSOK Z-001 and the operator's project-specific requirements.
4. **Quality management**: Sifab's ISO 9001 certified QMS must be maintained and applied to all project work.
5. **Material traceability**: Full material traceability (3.1/3.2 certificates per EN 10204) is required for pressure-retaining and safety-critical components.
6. **Workplace safety**: Sifab must comply with the Working Environment Act for its own employees and subcontractors.

### Operator-Driven Obligations (Contractual)
Operators are legally responsible for ensuring overall installation safety. They flow down regulatory requirements to suppliers through contracts. Common contractual obligations for Sifab include:
- Compliance with specific NORSOK standards
- Compliance with operator-specific technical requirements (e.g., TR2000)
- Participation in HAZOP, SIL assessments, and design reviews
- Delivery of as-built documentation, test records, and certificates
- Compliance with operator Management of Change (MoC) procedures

### Operator Obligations (Not Sifab's Responsibility)
The operator retains ultimate responsibility for:
- Installation-level risk assessments (QRA, HAZID)
- Hazardous area classification of the installation
- Safety case / ALARP demonstration
- Overall documentation management for the installation
- Regulatory reporting to PSA
- Maintenance and inspection programs post-delivery

## Key Regulatory Bodies

| Body | Role | Relevance to Sifab |
|------|------|---------------------|
| **PSA** (Petroleumstilsynet) | Regulates safety, working environment, and emergency preparedness in petroleum activities | Sets the regulatory framework; conducts audits of operators and key suppliers |
| **DSB** (Direktoratet for samfunnssikkerhet og beredskap) | Regulates electrical equipment, pressure equipment, and transport of dangerous goods onshore | Oversees PED and ATEX market surveillance in Norway |
| **Arbeidstilsynet** | Norwegian Labour Inspection Authority | Regulates workplace safety for onshore activities (Sifab workshop) |
| **Miljodirektoratet** | Norwegian Environment Agency | Environmental regulations, emissions, waste handling |
| **Standards Norway** | Develops and publishes NORSOK standards | Publishes standards referenced by PSA |

## Sifab Agents Using This
- **HSE Agent** -- primary reference for all HSE compliance decisions and risk assessments
- **Project Manager Agent** -- understanding regulatory requirements when scoping projects
- **Quality Management Agent** -- ensuring QMS aligns with regulatory expectations
- **Structural Agent** -- PED and material compliance for fabrication
- **Instrumentation Agent** -- ATEX and functional safety requirements
- **Metering Agent** -- fiscal metering regulatory context

## Cross-References
- [PSA Regulations](psa-regulations.md)
- [Functional Safety (IEC 61508/61511)](functional-safety.md)
- [ATEX Directive](atex-directive.md)
- [PED Directive](ped-directive.md)
- [TR2000 Guidelines](tr2000-guidelines.md)
- [NACE Sour Service](nace-sour-service.md)
- [Hazardous Area Classification](hazardous-area-classification.md)
- [NPD Measurement Regulations](../metering/npd-measurement-regs.md)
- NORSOK S-001, S-002, I-001, I-002, Z-001, Z-008, Z-015
