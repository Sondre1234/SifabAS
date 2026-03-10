# API MPMS — Manual of Petroleum Measurement Standards Overview

## Scope

The API Manual of Petroleum Measurement Standards (MPMS) is the internationally recognized set of standards for measuring petroleum hydrocarbons in custody transfer, fiscal, and allocation applications. Published by the American Petroleum Institute (API) in 23 chapters, it is widely adopted on the Norwegian Continental Shelf: both the Norwegian Measurement Regulations (Måleforskriften) and NORSOK I-104/I-105 reference API MPMS for calculation methods, proving procedures, and metering system design. Sifab AS uses API MPMS as the primary technical foundation for prover design, metering skid piping layout, flow computer configuration, and uncertainty analysis.

## Key Requirements for Sifab AS

This is an index of API MPMS chapters with relevance notes for Sifab. Detailed design requirements are in the individual chapter documents; only the most relevant chapters are listed.

| Chapter | Title | Relevance to Sifab | Priority |
|---------|-------|--------------------|----------|
| Ch. 4 | Proving Systems | Core reference for Sifab's pipe prover and SVP design, calibration methods, pulse interpolation, repeatability requirements (±0.02% over 5 runs), detector placement, and prover operating procedures. Ch. 4.3 is the primary reference for Small Volume Provers (e.g., Snorre A SP-01415). | HIGH |
| Ch. 5 | Metering | Core reference for flow meter types (turbine, PD, Coriolis, ultrasonic), installation requirements (upstream/downstream straight lengths), and flow conditioning. Sifab designs skid piping layouts to comply with Ch. 5.5 straight-length requirements. | HIGH |
| Ch. 6 | Metering Assemblies | Design of meter manifolds, prover connections, isolation valves, and meter run layouts. Directly applicable to Sifab's metering skid piping design and prover loop integration. | HIGH |
| Ch. 11 | Physical Properties Data | Volume correction factor tables and equations (CTL, CPL, CTPL) for correcting measured volumes to standard conditions (15 °C, atmospheric pressure). Sifab configures flow computers with the correct API table set (Tables 5A/5B, 6A/6B, 24A/24B, etc.) for the product being measured. | HIGH |
| Ch. 12 | Calculation of Petroleum Quantities | Flow calculation methods: meter factor, gross standard volume (GSV), net standard volume (NSV), mass, and energy. Defines standard formats for measurement tickets and proving reports. Sifab's provers and flow computers generate proving reports and tickets per Ch. 12.2.3. | HIGH |
| Ch. 21 | Flow Measurement Using Electronic Metering Systems | Electronic flow computer requirements: audit trail, data security, tamper detection, accumulator integrity, alarm management, and communication protocols. Required by Måleforskriften §12. Sifab configures Honeywell Experion and equivalent flow computers per Ch. 21. | HIGH |
| Ch. 2 | Tank Gauging | Relevant to Honeywell Enraf automatic tank gauging systems supplied by Sifab. Covers gauge types, installation, calibration, and uncertainty. | MEDIUM |
| Ch. 8 | Sampling | Crude oil and petroleum product sampling requirements. Sifab integrates sampling probes, mix chambers, and sample containers on metering skids per ISO 3171 and API MPMS Ch. 8. | MEDIUM |
| Ch. 9 | Density Determination | Density measurement methods (online densitometer, laboratory). Relevant to densitometer integration and calibration on Sifab's metering skids. | MEDIUM |
| Ch. 13 | Statistical Aspects of Measuring and Sampling | Uncertainty analysis methods. Reference for metering uncertainty budgets used to demonstrate compliance with Måleforskriften §5 and §6 limits. | MEDIUM |
| Ch. 14 | Natural Gas Fluids Measurement | Gas measurement methods: orifice (Ch. 14.3, based on AGA 3), turbine (AGA 7), and ultrasonic (AGA 9). Relevant to Sifab's gas metering systems and flow computer gas calculations. | MEDIUM |
| Ch. 20 | Allocation Measurement | Allocation metering design and uncertainty requirements. Sifab delivers allocation metering packages and must demonstrate compliance with allocation agreement requirements. | MEDIUM |
| Ch. 22 | Testing Protocol | Testing and certification procedures for measurement devices. Reference for Sifab's Factory Acceptance Test (FAT) procedures and metering system commissioning. | LOW-MED |
| Ch. 7 | Temperature Determination | Temperature measurement methods and instrument specifications. Applicable to RTD selection and calibration on Sifab's metering skids. | LOW-MED |
| Ch. 10 | Sediment and Water | BS&W (basic sediment and water) measurement. Relevant to water-in-oil analyzer integration on metering skids. | LOW-MED |

## SifabAS Agent Usage

- **Primary**: Metering Agent — daily reference for prover design (Ch. 4), metering skid layout (Ch. 5, 6), flow computer configuration (Ch. 11, 12, 21), and uncertainty analysis (Ch. 13)
- **Supporting**: Instrumentation Agent — instrument selection, calibration, and installation requirements from Ch. 5, 7, 8, and 9
- **Supporting**: Quality Management Agent — ensuring proving reports, measurement tickets, and FAT documentation comply with API MPMS Chapter 12 and Chapter 21 formats per B.SI.01.07

## Cross-References

- Måleforskriften / NPD Measurement Regulations — Norwegian regulations that reference API MPMS as the technical standard for calculation methods and proving
- NORSOK I-104 — Liquid fiscal measurement; references API MPMS Ch. 4, 5, 6, 11, 12
- NORSOK I-105 — Gas fiscal measurement; references API MPMS Ch. 14 and AGA reports
- ISO 5168 / GUM — Uncertainty evaluation framework (used alongside API MPMS Ch. 13)
- ISO 3171 — Automatic pipeline sampling (used with API MPMS Ch. 8)
- AGA 3 / AGA 7 / AGA 9 / AGA 11 — Gas measurement standards referenced in API MPMS Ch. 14
- [NPD Measurement Regulations summary](npd-measurement-regs.md)
- [PSA Regulations summary](../hse/psa-regulations.md)
