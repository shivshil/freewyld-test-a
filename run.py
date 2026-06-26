from report import build_report
import market


def main():
    market.reset_calls()
    rep = build_report()
    print("listing     occ%   revpar_index")
    for r in rep["rows"]:
        print(f"  {r['id']:<9} {round(r['occ'] * 100, 1):>5}   {round(r['index'], 2)}")
    print(f"\nPortfolio occupancy: {rep['portfolio_occ'] * 100:.1f}%")
    print(f"External comp API calls made: {market.FETCH_CALLS}")


if __name__ == "__main__":
    main()
