import csv
import os

from report import build_report
import market

CSV_PATH = os.path.join(os.path.dirname(__file__), "report.csv")


def write_report_csv(rep, fetch_calls, path=CSV_PATH):
    """Write the report as CSV for import elsewhere.

    Values match the printed report: occ as a percent (1 dp), index rounded (2 dp).
    Per-listing rows first, then a summary footer (portfolio occupancy, comp API calls).
    """
    with open(path, "w", newline="") as f:
        w = csv.writer(f)
        w.writerow(["id", "occ_pct", "revpar_index"])
        for r in rep["rows"]:
            w.writerow([r["id"], round(r["occ"] * 100, 1), round(r["index"], 2)])
        w.writerow(["portfolio", round(rep["portfolio_occ"] * 100, 1), ""])
        w.writerow(["comp_api_calls", fetch_calls, ""])


def main():
    market.reset_calls()
    rep = build_report()
    print("listing     occ%   revpar_index")
    for r in rep["rows"]:
        print(f"  {r['id']:<9} {round(r['occ'] * 100, 1):>5}   {round(r['index'], 2)}")
    print(f"\nPortfolio occupancy: {rep['portfolio_occ'] * 100:.1f}%")
    print(f"External comp API calls made: {market.FETCH_CALLS}")
    write_report_csv(rep, market.FETCH_CALLS)
    print(f"Wrote {CSV_PATH}")


if __name__ == "__main__":
    main()
