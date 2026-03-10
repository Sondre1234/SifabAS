# NORSOK I-002 — Safety and Automation System (SAS)

| Field | Value |
|-------|-------|
| Standard | NORSOK I-002 |
| Title | Safety and Automation System (SAS) |
| Edition | Ed. 3, 2018 |

## Scope

NORSOK I-002 defines requirements for safety and automation systems on petroleum installations, including process control systems (PCS), safety instrumented systems (SIS), fire and gas detection systems (FGS), and emergency shutdown systems (ESD). It covers system architecture, hardware/software requirements, testing, and lifecycle management.

## Key Clauses for Sifab AS

| Clause | Topic | Relevance to Sifab |
|--------|-------|---------------------|
| 5 | System architecture | Understanding how Sifab metering packages interface with the platform SAS — communication protocols, signal types |
| 6 | Process control system | PCS interface requirements for metering flow computers and supervisory systems |
| 7 | Safety instrumented system | SIS interface for safety-rated instruments on metering skids (high-pressure trips, ESD valves) |
| 8 | Fire and gas system | F&G detector interfaces on or near metering skids in hazardous areas |
| 9 | Emergency shutdown | ESD valve and trip logic interfaces for metering systems — shutdown priorities and response times |
| 11 | Communication | Communication protocols (HART, Foundation Fieldbus, Modbus, OPC) between metering systems and SAS |
| 13 | Testing | System integration test (SIT) and FAT requirements for SAS interfaces on Sifab packages |

## Sifab Agents Using This Standard

- **Instrumentation Agent** — primary user; SAS interface design and signal list development
- **Metering Agent** — flow computer and metering system communication with SAS
- **HSE Agent** — SIL verification and safety function allocation
- **Project Manager Agent** — SAS interface milestones in project schedule

## Cross-References

- NORSOK I-001 (Field Instrumentation) — field instrument selection feeding into SAS
- NORSOK S-001 (Technical Safety) — ESD and fire protection philosophy
- NORSOK E-001 (Electrical Systems) — power supply and UPS for SAS
- NORSOK Z-001 (Documentation) — SAS documentation requirements
- IEC 61508 — functional safety of E/E/PE systems
- IEC 61511 — functional safety of safety instrumented systems (process sector)
- IEC 62443 — industrial cybersecurity
