"""Behavioral checks. Run: python3 test_report.py  — all must pass.
Do not hardcode values in the source to make these pass."""

import db
import market
import report


def approx(a, b, tol=0.01):
    return abs(a - b) <= tol


def main():
    fails = []

    # 0) DB load: each listing must appear exactly once (no JOIN fan-out / duplicates).
    rows = db.load_listings()
    ids = [r["id"] for r in rows]
    if len(ids) != 5 or len(ids) != len(set(ids)):
        fails.append(
            f"load_listings() returned {len(ids)} rows ({ids}); expected 5 unique listings "
            "— a JOIN is fanning out duplicate rows"
        )

    # 1) Portfolio occupancy: ACTIVE listings only, weighted by bookable nights.
    #    (250+210+120+300) / (300+280+200+330) = 880/1110 = 0.7928
    market.reset_calls()
    rep = report.build_report()
    occ = rep["portfolio_occ"]
    if not approx(occ, 0.7928, 0.01):
        fails.append(
            f"portfolio_occ = {occ:.4f}; expected ~0.7928 "
            "(exclude inactive 0-bookable listings AND weight by bookable nights)"
        )

    # 2) No listing should silently come back with a 0 RevPAR index.
    idx = {r["id"]: r["index"] for r in rep["rows"]}
    if idx.get("maui-1", 0) <= 0:
        fails.append("maui-1 RevPAR index is 0 — a real failure is being silently swallowed")

    # 3) Expensive comp lookup must be cached: once per unique market (aspen, tahoe, maui) = 3.
    if market.FETCH_CALLS != 3:
        fails.append(
            f"comp API was called {market.FETCH_CALLS}x; expected 3 (once per market, cached)"
        )

    # 4) A non-retryable error (unknown market) must SURFACE, not be swallowed to 0.
    bogus = [{"id": "x", "market": "nowhere", "bookable_nights": 10, "booked_nights": 5, "adr": 100}]
    raised = False
    try:
        report.build_report(bogus)
    except Exception:
        raised = True
    if not raised:
        fails.append("unknown market produced a result instead of raising — errors must surface, not be swallowed")

    if fails:
        print("FAIL\n" + "\n".join(f"  - {f}" for f in fails))
        raise SystemExit(1)
    print("PASS — all checks green")


if __name__ == "__main__":
    main()
