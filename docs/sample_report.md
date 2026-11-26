# DORA control coverage report
As of 2026-11-26. Overall effective coverage: **55%**

| Pillar | Covered | Weak | Gap | Coverage |
|---|---|---|---|---|
| ICT risk management | 6 | 2 | 2 | 60% |
| Incident reporting | 2 | 1 | 0 | 67% |
| Resilience testing | 2 | 0 | 1 | 67% |
| Third-party risk | 1 | 1 | 1 | 33% |
| Information sharing | 0 | 0 | 1 | 0% |

## Findings

| Severity | Item | Finding |
|---|---|---|
| critical | ICT-13 | no control mapped: Learning and evolving |
| critical | ICT-14 | no control mapped: Communication |
| critical | INF-45 | no control mapped: Threat intelligence sharing |
| critical | TPR-EXIT | no control mapped: Exit strategies |
| critical | TST-26 | no control mapped: Threat-led penetration testing |
| high | CTL-006 | no accountable owner |
| high | CTL-008 | no accountable owner |
| high | CTL-008 | never tested |
| medium | CTL-005 | evidence stale (555 days old) |
| medium | CTL-008 | status is in_progress |
| medium | CTL-011 | status is in_progress |

## Coverage map

```mermaid
flowchart LR
  subgraph P0["ICT risk management"]
    ICT_05["Art 5: Governance and organisation"]:::covered
    ICT_06["Art 6: ICT risk management framework"]:::covered
    ICT_07["Art 7: ICT systems, protocols and tools"]:::covered
    ICT_08["Art 8: Identification of assets"]:::covered
    ICT_09["Art 9: Protection and prevention"]:::covered
    ICT_10["Art 10: Detection"]:::covered
    ICT_11["Art 11: Response and recovery"]:::weak
    ICT_12["Art 12: Backup and restoration"]:::weak
    ICT_13["Art 13: Learning and evolving"]:::gap
    ICT_14["Art 14: Communication"]:::gap
  end
  subgraph P1["Incident reporting"]
    INC_17["Art 17: Incident management process"]:::covered
    INC_18["Art 18: Incident classification"]:::covered
    INC_19["Art 19: Major incident reporting"]:::weak
  end
  subgraph P2["Resilience testing"]
    TST_24["Art 24: General testing programme"]:::covered
    TST_25["Art 25: Testing tools and methods"]:::covered
    TST_26["Art 26: Threat-led penetration testing"]:::gap
  end
  subgraph P3["Third-party risk"]
    TPR_28["Art 28: Register of information"]:::covered
    TPR_EXIT["Art 28(8): Exit strategies"]:::gap
    TPR_30["Art 30: Key contractual provisions"]:::weak
  end
  subgraph P4["Information sharing"]
    INF_45["Art 45: Threat intelligence sharing"]:::gap
  end
  CTL_001(["CTL-001 Board-approved ICT risk framework"]):::control
  CTL_001 --> ICT_05
  CTL_001 --> ICT_06
  CTL_002(["CTL-002 Critical asset inventory"]):::control
  CTL_002 --> ICT_08
  CTL_003(["CTL-003 Privileged access and segmentation"]):::control
  CTL_003 --> ICT_07
  CTL_003 --> ICT_09
  CTL_004(["CTL-004 24x7 SOC detection"]):::control
  CTL_004 --> ICT_10
  CTL_005(["CTL-005 DR failover runbooks"]):::control
  CTL_005 --> ICT_11
  CTL_006(["CTL-006 Immutable backup and restore test"]):::control
  CTL_006 --> ICT_12
  CTL_007(["CTL-007 Incident classification playbook"]):::control
  CTL_007 --> INC_17
  CTL_007 --> INC_18
  CTL_008(["CTL-008 Regulator notification workflow"]):::control
  CTL_008 --> INC_19
  CTL_009(["CTL-009 Annual scenario testing"]):::control
  CTL_009 --> TST_24
  CTL_009 --> TST_25
  CTL_010(["CTL-010 Third-party register"]):::control
  CTL_010 --> TPR_28
  CTL_011(["CTL-011 Contract clause baseline"]):::control
  CTL_011 --> TPR_30
  classDef covered fill:#EAF3DE,stroke:#3B6D11,color:#173404
  classDef weak fill:#FAEEDA,stroke:#854F0B,color:#412402
  classDef gap fill:#FCEBEB,stroke:#A32D2D,color:#501313
  classDef control fill:#E6F1FB,stroke:#185FA5,color:#042C53
```
