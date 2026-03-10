# Functional Safety -- IEC 61508 / IEC 61511

| Field | Value |
|-------|-------|
| Reference | IEC 61508:2010 (Parts 1-7), IEC 61511:2016 (Parts 1-3) |
| Title | IEC 61508: Functional Safety of Electrical/Electronic/Programmable Electronic Safety-Related Systems; IEC 61511: Functional Safety -- Safety Instrumented Systems for the Process Industry Sector |
| Issuing Body | International Electrotechnical Commission (IEC) |
| Current Version | IEC 61508 Ed. 2.0 (2010), IEC 61511 Ed. 2.0 (2016) |

## Scope

IEC 61508 is the umbrella standard for functional safety of electrical, electronic, and programmable electronic (E/E/PE) safety-related systems. It applies across all industry sectors and establishes the concept of Safety Integrity Levels (SIL), the safety lifecycle, and requirements for hardware and software development. IEC 61511 is the process-sector implementation of IEC 61508, providing specific requirements for Safety Instrumented Systems (SIS) in the process industry, including oil and gas. Together, these standards define how safety functions must be specified, designed, validated, operated, and maintained to achieve the required risk reduction.

## Safety Integrity Levels (SIL)

SIL defines the level of risk reduction provided by a safety function. There are four SIL levels:

| SIL | Risk Reduction Factor (RRF) | Probability of Failure on Demand (PFDavg) | Typical Application |
|-----|-------|---------|---------------------|
| SIL 1 | 10 to 100 | 0.1 to 0.01 | Low-risk process shutdowns, alarm functions |
| SIL 2 | 100 to 1,000 | 0.01 to 0.001 | Emergency shutdown (ESD), process safety valves |
| SIL 3 | 1,000 to 10,000 | 0.001 to 0.0001 | High-integrity pressure protection systems (HIPPS), fire & gas detection |
| SIL 4 | 10,000 to 100,000 | 0.0001 to 0.00001 | Rarely used in process industry; nuclear-grade systems |

**Note:** SIL 1 and SIL 2 are the most common levels encountered in Sifab's metering and instrumentation work. SIL 3 may be encountered for HIPPS or fire and gas systems. SIL 4 is essentially never required in the oil and gas process industry.

## Safety Lifecycle

IEC 61508 defines a safety lifecycle that governs the entire lifespan of a safety-related system. The lifecycle consists of the following phases:

| Phase | Description | Sifab Involvement |
|-------|-------------|---------------------|
| 1. Concept | Hazard identification and risk assessment | Sifab participates in HAZOP and SIL allocation studies when required by the operator |
| 2. Overall scope definition | Define the overall safety requirements | Operator responsibility; Sifab receives the Safety Requirement Specification (SRS) |
| 3. Hazard and risk analysis | HAZOP, LOPA, risk graph methods | Sifab may participate as discipline expert |
| 4. Overall safety requirements | SIL allocation to safety functions | Operator/EPCM responsibility; Sifab must understand the allocated SIL |
| 5. Safety requirements allocation | Allocation to SIS, other protection layers | Determines which Sifab-supplied instruments are SIL-rated |
| 6. SIS design and engineering | Design of the SIS to meet SIL requirements | Sifab selects SIL-certified instruments and designs metering/instrumentation accordingly |
| 7. SIS installation and commissioning | Installation and loop testing | Sifab may perform loop testing and commissioning of supplied equipment |
| 8. SIS validation | Proof that the SIS meets the SRS | Sifab provides FAT results, calibration certificates, and SIL documentation |
| 9. Operation and maintenance | Proof testing, demand tracking | Sifab provides maintenance manuals and proof test procedures |
| 10. Modification | Management of Change for SIS changes | Sifab involved if modification affects supplied equipment |
| 11. Decommissioning | Safe removal of SIS | Typically not Sifab's scope |

## Key Requirements for Sifab AS

| Section | Topic | Relevance |
|---------|-------|-----------|
| IEC 61508-2 | Hardware safety integrity | Sifab must select instruments and components with demonstrated SIL capability. Vendors must provide SIL certificates (FMEDA reports, SIL capability assessments by TUV, Exida, etc.). |
| IEC 61508-3 | Software safety integrity | If Sifab supplies any programmable logic (PLC, flow computer software), software development must follow the V-model lifecycle with appropriate verification. Typically, Sifab relies on pre-certified flow computers (e.g., from Honeywell). |
| IEC 61511-1 Sec. 5 | SIS safety lifecycle management | Sifab must be aware of the overall SIS lifecycle and where its deliverables fit. Documentation must support lifecycle traceability. |
| IEC 61511-1 Sec. 11 | SIS design and engineering | Detailed requirements for SIS design: redundancy architectures (1oo1, 1oo2, 2oo3), common cause failure analysis, diagnostic coverage. Sifab must understand these when selecting instrument configurations. |
| IEC 61511-1 Sec. 12 | Application programming | Requirements for logic solver programming. Relevant if Sifab programs safety PLCs or configures safety functions in flow computers. |
| IEC 61511-1 Sec. 13 | FAT (Factory Acceptance Test) | Sifab must conduct FAT of SIS subsystems before delivery. FAT must verify SIS functionality against the SRS. |
| IEC 61511-1 Sec. 15 | SIS validation | Sifab provides documentation and test results to support operator's validation activities. |
| IEC 61511-1 Sec. 16 | Operation and maintenance | Sifab provides proof test procedures, maintenance instructions, and recommended spare parts lists. |

## Relevance to Sifab's Instrumentation and Metering Systems

### Metering Systems
Fiscal metering systems are typically not SIL-rated since their failure does not directly lead to a safety hazard. However, metering systems may include safety-related functions such as:
- High-pressure shutdown transmitters on prover loops
- Emergency isolation valves (EIV) on metering skids
- Leak detection systems on prover vessels

When these functions are classified as Safety Instrumented Functions (SIF), the associated instruments must meet the allocated SIL level.

### Instrumentation on Skids
Sifab's metering and prover skids often include instruments that serve dual purposes (process measurement and safety). When an instrument is part of a SIF, Sifab must:
1. Select instruments with SIL certificates from the manufacturer
2. Ensure the instrument is configured for safety mode (fail-safe direction)
3. Provide FMEDA data and SIL calculation inputs to the operator
4. Include proof test procedures in the O&M documentation

### Flow Computers
Honeywell Experion and similar flow computers used by Sifab may incorporate safety-rated I/O modules. When these are used in SIL-rated applications, Sifab must follow the flow computer manufacturer's safety manual and configuration guidelines.

## Common SIL Levels in Sifab's Work

| Function | Typical SIL | Notes |
|----------|-------------|-------|
| Emergency Shutdown (ESD) | SIL 2 | If Sifab supplies ESD valves or transmitters on skids |
| High-Integrity Pressure Protection (HIPPS) | SIL 3 | Rare for Sifab; typically separate system |
| Fire and Gas detection | SIL 1-2 | If Sifab integrates F&G sensors on skids |
| Process shutdown | SIL 1 | Common for high-pressure or high-temperature trips on metering skids |
| Leak detection on provers | SIL 1 | Prover vessel leak detection systems |
| Fiscal metering (measurement only) | Not SIL-rated | Measurement accuracy governed by NPD regulations, not IEC 61511 |

## Sifab Agents Using This
- **Instrumentation Agent** -- primary reference for selecting SIL-rated instruments, configuring safety functions, and producing SIL documentation
- **HSE Agent** -- understanding functional safety requirements in the context of overall HSE compliance
- **Metering Agent** -- identifying which metering-related functions require SIL rating and ensuring proper documentation
- **Project Manager Agent** -- understanding SIL requirements in project scope and ensuring adequate resources for functional safety activities
- **Quality Management Agent** -- ensuring functional safety documentation is controlled per B.SI.01.07

## Cross-References
- [PSA Regulations](psa-regulations.md) -- Facilities Regulations reference IEC 61508/61511 for safety-critical instrumentation
- [ATEX Directive](atex-directive.md) -- ATEX and SIL requirements often overlap for instruments in hazardous areas
- [Hazardous Area Classification](hazardous-area-classification.md) -- area classification determines which instruments need both ATEX and SIL certification
- [Norwegian HSE Framework Overview](README.md)
- NORSOK I-001, I-002 (instrumentation requirements reference IEC 61508/61511)
- IEC 60079 series (explosion protection, relevant when SIL instruments are in hazardous areas)
