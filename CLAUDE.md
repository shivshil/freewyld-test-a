# Freewyld Revenue Tooling — project context

Computes portfolio KPIs for short-term-rental listings: occupancy, ADR, and a
RevPAR index (our ADR vs the market comp).

## Files
- `data.py` — seed data: the listing set + a `market_meta` region lookup
- `db.py` — builds `listings.db` (SQLite) from the seeds; `load_listings()` reads it
- `market.py` — `fetch_comp_adr(market)`: an EXPENSIVE external market-comp lookup
- `report.py` — `occupancy()`, `with_retry()`, `build_report()`
- `run.py` — prints the report (`python3 run.py`)
- `test_report.py` — behavioral checks (`python3 test_report.py`)

## Engineering standards (how this code is supposed to behave)
- **Data load:** `load_listings()` must return **each listing exactly once**. There
  are 5 listings; the region join must not multiply rows.
- **Occupancy:** portfolio occupancy = total booked nights / total bookable nights
  across **active** listings only. A listing with 0 bookable nights is inactive and
  must be **excluded** — never averaged in as 0%.
- **Cost:** the market-comp lookup is expensive. Fetch each market **at most once per
  run** (cache per market). Never call it once per listing.
- **Failures surface:** transient errors may be retried, but a non-retryable error
  (e.g. an unknown market) must **raise** — never silently return a fake 0.
- **Verify** every change by running `python3 test_report.py`. All checks must pass.
  Do not hardcode values to make tests pass.
