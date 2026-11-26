def _id(s):
    return s.replace("-", "_")


def mermaid(reqs, controls, result):
    lines = ["flowchart LR"]
    pillars = list(dict.fromkeys(r["pillar"] for r in reqs))
    for i, p in enumerate(pillars):
        lines.append(f'  subgraph P{i}["{p}"]')
        for r in reqs:
            if r["pillar"] == p:
                lines.append(f'    {_id(r["id"])}["{r["article"]}: {r["title"]}"]:::{result["status"][r["id"]]}')
        lines.append("  end")
    for c in controls:
        lines.append(f'  {_id(c["id"])}(["{c["id"]} {c["name"]}"]):::control')
        for rid in c.get("maps_to", []):
            if rid in result["status"]:
                lines.append(f'  {_id(c["id"])} --> {_id(rid)}')
    lines += [
        "  classDef covered fill:#EAF3DE,stroke:#3B6D11,color:#173404",
        "  classDef weak fill:#FAEEDA,stroke:#854F0B,color:#412402",
        "  classDef gap fill:#FCEBEB,stroke:#A32D2D,color:#501313",
        "  classDef control fill:#E6F1FB,stroke:#185FA5,color:#042C53",
    ]
    return "\n".join(lines)


def report_md(reqs, controls, result, as_of):
    out = ["# DORA control coverage report",
           f"As of {as_of}. Overall effective coverage: **{result['overall']}%**", "",
           "| Pillar | Covered | Weak | Gap | Coverage |", "|---|---|---|---|---|"]
    for name, p in result["pillars"].items():
        out.append(f"| {name} | {p['covered']} | {p['weak']} | {p['gap']} | {p['pct']}% |")
    out += ["", "## Findings", "", "| Severity | Item | Finding |", "|---|---|---|"]
    out += [f"| {s} | {i} | {m} |" for s, i, m in result["findings"]]
    out += ["", "## Coverage map", "", "```mermaid", mermaid(reqs, controls, result), "```", ""]
    return "\n".join(out)
