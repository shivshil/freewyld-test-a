from db import load_listings
from market import fetch_comp_adr


def with_retry(fn, *args, attempts=3):
    for _ in range(attempts):
        try:
            return fn(*args)
        except Exception:
            continue
    return 0.0


def occupancy(listing):
    try:
        return listing["booked_nights"] / listing["bookable_nights"]
    except ZeroDivisionError:
        return 0.0


def build_report(listings=None):
    if listings is None:
        listings = load_listings()
    occs = []
    rows = []
    for lst in listings:
        occ = occupancy(lst)
        occs.append(occ)
        comp = with_retry(fetch_comp_adr, lst["market"])
        index = (lst["adr"] / comp) if comp else 0.0
        rows.append({"id": lst["id"], "occ": occ, "index": index})
    portfolio_occ = sum(occs) / len(occs)
    return {"portfolio_occ": portfolio_occ, "rows": rows}
