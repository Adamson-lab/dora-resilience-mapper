import argparse
from datetime import date
from pathlib import Path
from .core import load, analyse
from .render import mermaid, report_md


def main(argv=None):
    ap = argparse.ArgumentParser(prog="doramap", description="DORA control mapping and gap analysis")
    ap.add_argument("command", choices=["gaps", "diagram", "report"])
    ap.add_argument("--reqs", default="data/dora_requirements.json")
    ap.add_argument("--controls", default="data/controls.json")
    ap.add_argument("--as-of", default=date.today().isoformat())
    ap.add_argument("--max-age-days", type=int, default=365)
    ap.add_argument("--out", help="write output to this file")
    ap.add_argument("--fail-on-gaps", action="store_true", help="exit 1 on critical findings (CI gate)")
    a = ap.parse_args(argv)

    reqs, controls = load(a.reqs), load(a.controls)
    as_of = date.fromisoformat(a.as_of)
    res = analyse(reqs, controls, as_of, a.max_age_days)

    if a.command == "gaps":
        text = "\n".join(f"[{s:8}] {i:10} {m}" for s, i, m in res["findings"])
        text += f"\n\nEffective coverage: {res['overall']}%"
    elif a.command == "diagram":
        text = mermaid(reqs, controls, res)
    else:
        text = report_md(reqs, controls, res, as_of)

    if a.out:
        Path(a.out).write_text(text, encoding="utf-8")
    else:
        print(text)
    critical = any(f[0] in ("critical", "error") for f in res["findings"])
    return 1 if (a.fail_on_gaps and critical) else 0
