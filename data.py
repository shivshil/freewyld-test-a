"""Seed data used to build listings.db (see db.py)."""

LISTINGS = [
    {"id": "aspen-a", "market": "aspen", "bookable_nights": 300, "booked_nights": 250, "adr": 420},
    {"id": "aspen-b", "market": "aspen", "bookable_nights": 280, "booked_nights": 210, "adr": 390},
    {"id": "tahoe-1", "market": "tahoe", "bookable_nights": 0,   "booked_nights": 0,   "adr": 0},    # inactive / off-market
    {"id": "tahoe-2", "market": "tahoe", "bookable_nights": 200, "booked_nights": 120, "adr": 350},
    {"id": "maui-1",  "market": "Maui",  "bookable_nights": 330, "booked_nights": 300, "adr": 610},
]

# Region lookup, one row per market. NOTE: this is real-world-messy source data.
MARKET_META = [
    ("aspen", "Mountain West"),
    ("aspen", "Mountain West"),   # duplicate row
    ("tahoe", "Sierra"),
    ("Maui", "Hawaii"),
]
