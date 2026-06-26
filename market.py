"""Expensive external market-comp lookup (pretend this hits a paid API)."""

MARKET_COMP_ADR = {"aspen": 405, "tahoe": 360, "maui": 590}

FETCH_CALLS = 0


def fetch_comp_adr(market):
    global FETCH_CALLS
    FETCH_CALLS += 1
    if market not in MARKET_COMP_ADR:
        raise ValueError(f"unknown market: {market}")
    return MARKET_COMP_ADR[market]


def reset_calls():
    global FETCH_CALLS
    FETCH_CALLS = 0
