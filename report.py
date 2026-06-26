from db import load_listings
from market import fetch_comp_adr


def with_retry(fn, *args, attempts=3):
    last = None
    for _ in range(attempts):
        try:
            return fn(*args)
        except ValueError:       # non-retryable (e.g. unknown market) — surface immediately
            raise
        except Exception as e:   # transient — retry, then surface
            last = e
    raise last


def occupancy(listing):
    try:
        return listing["booked_nights"] / listing["bookable_nights"]
    except ZeroDivisionError:
        return 0.0


def build_report(listings=None):
    if listings is None:
        listings = load_listings()
    # Inactive (0 bookable nights) listings are off-market: excluded from the report.
    active = [lst for lst in listings if lst["bookable_nights"] > 0]
    comp_cache = {}
    rows = []
    total_booked = 0
    total_bookable = 0
    for lst in active:
        occ = occupancy(lst)
        # Canonicalize the messy listing market to the comp API's key format,
        # and fetch each market at most once per run.
        key = lst["market"].lower()
        if key not in comp_cache:
            comp_cache[key] = with_retry(fetch_comp_adr, key)
        comp = comp_cache[key]
        index = lst["adr"] / comp
        rows.append({"id": lst["id"], "occ": occ, "index": index})
        total_booked += lst["booked_nights"]
        total_bookable += lst["bookable_nights"]
    portfolio_occ = total_booked / total_bookable if total_bookable else 0.0
    return {"portfolio_occ": portfolio_occ, "rows": rows}
