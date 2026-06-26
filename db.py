"""Listings load from a SQLite DB (listings.db), rebuilt from data.py seeds."""

import os
import sqlite3

from data import LISTINGS, MARKET_META

DB_PATH = os.path.join(os.path.dirname(__file__), "listings.db")


def build_db():
    if os.path.exists(DB_PATH):
        os.remove(DB_PATH)
    con = sqlite3.connect(DB_PATH)
    cur = con.cursor()
    cur.execute(
        "CREATE TABLE listings (id TEXT, market TEXT, bookable_nights INT, booked_nights INT, adr INT)"
    )
    cur.execute("CREATE TABLE market_meta (market TEXT, region TEXT)")
    for l in LISTINGS:
        cur.execute(
            "INSERT INTO listings VALUES (?,?,?,?,?)",
            (l["id"], l["market"], l["bookable_nights"], l["booked_nights"], l["adr"]),
        )
    cur.executemany("INSERT INTO market_meta VALUES (?,?)", MARKET_META)
    con.commit()
    con.close()


def load_listings():
    build_db()
    con = sqlite3.connect(DB_PATH)
    con.row_factory = sqlite3.Row
    cur = con.cursor()
    cur.execute(
        """
        SELECT l.id, l.market, l.bookable_nights, l.booked_nights, l.adr, m.region
        FROM listings l
        JOIN (SELECT market, region FROM market_meta GROUP BY market) m
          ON l.market = m.market
        """
    )
    rows = [dict(r) for r in cur.fetchall()]
    con.close()
    return rows
