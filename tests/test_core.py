import unittest
from datetime import date
from doramap.core import analyse

REQS = [{"id": "A", "pillar": "P", "article": "Art 1", "title": "a"},
        {"id": "B", "pillar": "P", "article": "Art 2", "title": "b"},
        {"id": "C", "pillar": "P", "article": "Art 3", "title": "c"}]
TODAY = date(2026, 11, 26)


def ctl(**kw):
    base = {"id": "X", "owner": "o", "status": "implemented", "last_tested": "2026-10-01", "maps_to": ["A"]}
    base.update(kw)
    return [base]


class Tests(unittest.TestCase):
    def test_unmapped_is_critical_gap(self):
        r = analyse(REQS, [], TODAY)
        self.assertEqual(r["status"]["A"], "gap")
        self.assertEqual(r["findings"][0][0], "critical")

    def test_effective_control_covers(self):
        self.assertEqual(analyse(REQS, ctl(), TODAY)["status"]["A"], "covered")

    def test_stale_evidence_is_weak(self):
        self.assertEqual(analyse(REQS, ctl(last_tested="2025-01-01"), TODAY)["status"]["A"], "weak")

    def test_unknown_requirement_flagged(self):
        r = analyse(REQS, ctl(maps_to=["ZZ"]), TODAY)
        self.assertTrue(any(f[0] == "error" for f in r["findings"]))

    def test_pillar_percentage(self):
        self.assertEqual(analyse(REQS, ctl(), TODAY)["pillars"]["P"]["pct"], 33)


if __name__ == "__main__":
    unittest.main()
