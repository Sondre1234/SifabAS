# SifabAS Agents

| # | Agent | Role | Key Standards |
|---|-------|------|---------------|
| 1 | **[Project Manager](project-manager/AGENT.md)** | Coordinates multidisciplinary projects, manages scope/schedule/budget, central hub between all agents | B.SI.01.07, Norsok Z-001, Z-008, Z-015 |
| 2 | **[Instrumentation](instrumentation/AGENT.md)** | Designs and specifies instrumentation and control systems | Norsok I-001, I-002, I-104, IEC 61508/61511 |
| 3 | **[Process](process/AGENT.md)** | Process design, simulation, P&IDs, datasheets | Norsok P-001, P-002, L-001, L-002, R-001 |
| 4 | **[Structural](structural/AGENT.md)** | Structural design, load analysis, skid fabrication | Norsok N-001–N-006, M-001, M-101, M-501, R-003 |
| 5 | **[HSE](hse/AGENT.md)** | Health, safety, environment — HAZOP, SIL, risk assessments | Norsok S-001, S-002, S-003, Z-008, Z-013, PSA |
| 6 | **[Metering](metering/AGENT.md)** | Fiscal/allocation metering systems, uncertainty analysis, provers | Norsok I-104, I-105, NPD/OD Measurement Regulations |
| 7 | **[Quality Management](quality-management/AGENT.md)** | Enforces ISO 9001 QMS, audits, document control | ISO 9001:2015, B.SI.01.07 |
| 8 | **[ISO Document Producer](iso-document-producer/AGENT.md)** | Authors all internal QMS documents, procedures, forms, templates | ISO 9001:2015, B.SI.xx.xx series |
| 9 | **[Email](email/AGENT.md)** | Drafts/parses external and internal email, routes to agents | — |
| 10 | **[Customer Follow-up](customer-followup/AGENT.md)** | Tracks customer commitments, deadlines, satisfaction | — |

## How Agents Work Together

```
                    ┌─────────────────────┐
                    │   Project Manager   │
                    │   (hub / coordinator)│
                    └─────────┬───────────┘
                              │
          ┌───────────┬───────┼───────┬───────────┐
          │           │       │       │           │
   ┌──────┴──┐  ┌────┴───┐ ┌─┴──┐ ┌──┴────┐  ┌───┴──────┐
   │Instrument│  │Process │ │HSE │ │Struct.│  │Metering  │
   │  ation   │  │        │ │    │ │       │  │          │
   └──────────┘  └────────┘ └────┘ └───────┘  └──────────┘

   ┌──────────┐  ┌────────────┐  ┌──────────┐  ┌──────────┐
   │  Quality │  │ISO Document│  │  Email   │  │ Customer │
   │Management│  │  Producer  │  │          │  │Follow-up │
   └──────────┘  └────────────┘  └──────────┘  └──────────┘
```

- **Project Manager** is the hub — assigns tasks, coordinates interfaces
- **Quality Management** enforces standards across all deliverables
- **ISO Document Producer** writes QMS documents on demand
- **Discipline agents** (Instrumentation, Process, Structural, Metering, HSE) produce engineering deliverables
- **Email** handles all external communication
- **Customer Follow-up** tracks commitments and deadlines
- Agents communicate through handoff files in `/projects/<project-id>/handoffs/`
