import json
from datetime import date
from pathlib import Path

SEVERITY = {"critical": 0, "error": 0, "high": 1, "medium": 2}


def load(path):
    return json.loads(Path(path).read_text(encoding="utf-8"))


def is_effective(control, as_of, max_age):
    """A control counts as evidence only if implemented, owned and recently tested."""
    if control.get("status") != "implemented" or not control.get("owner"):
        return False
    last = control.get("last_tested")
    return bool(last) and (as_of - date.fromisoformat(last)).days <= max_age


def analyse(reqs, controls, as_of, max_age=365):
    ids = {r["id"] for r in reqs}
    by_req = {rid: [] for rid in ids}
    findings = []

    for c in controls:
        for rid in c.get("maps_to", []):
            if rid in ids:
                by_req[rid].append(c)
            else:
                findings.append(("error", c["id"], f"maps to unknown requirement {rid}"))
        if not c.get("owner"):
            findings.append(("high", c["id"], "no accountable owner"))
        last = c.get("last_tested")
        if not last:
            findings.append(("high", c["id"], "never tested"))
        else:
            age = (as_of - date.fromisoformat(last)).days
            if age > max_age:
                findings.append(("medium", c["id"], f"evidence stale ({age} days old)"))
        if c.get("status") != "implemented":
            findings.append(("medium", c["id"], f"status is {c.get('status')}"))

    status = {}
    for r in reqs:
        mapped = by_req[r["id"]]
        if not mapped:
            status[r["id"]] = "gap"
            findings.append(("critical", r["id"], f"no control mapped: {r['title']}"))
        elif any(is_effective(c, as_of, max_age) for c in mapped):
            status[r["id"]] = "covered"
        else:
            status[r["id"]] = "weak"

    pillars = {}
    for r in reqs:
        p = pillars.setdefault(r["pillar"], {"covered": 0, "weak": 0, "gap": 0, "total": 0})
        p[status[r["id"]]] += 1
        p["total"] += 1
    for p in pillars.values():
        p["pct"] = round(100 * p["covered"] / p["total"])

    findings.sort(key=lambda f: (SEVERITY[f[0]], f[1]))
    overall = round(100 * sum(1 for s in status.values() if s == "covered") / len(status))
    return {"status": status, "by_req": by_req, "pillars": pillars,
            "findings": findings, "overall": overall}
