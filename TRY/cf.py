import requests

def check_skipped_contests(handle):
    url = f"https://codeforces.com/api/user.rating?handle={handle}"
    res = requests.get(url).json()
    if res["status"] != "OK":
        print(f"❌ Handle '{handle}' not found or API error.")
        return
    history = res["result"]
    if not history:
        print(f"⚠️ '{handle}' has no contest history.")
        return

    skipped = [
        (c["contestId"], c["contestName"], c.get("rank", "N/A"), f"{c['oldRating']}→{c['newRating']}")
        for c in history
        if c["oldRating"] == c["newRating"]
    ]

    print(f"\n🔎 Checking: {handle}")
    if skipped:
        print(f"⚠️ Skipped contests:")
        for cid, name, rank, rating in skipped:
            print(f"- {name} (ID: {cid}) | Rank: {rank} | Rating: {rating}")
    else:
        print("✅ Rated in all contests.")

if __name__ == "__main__":
    handles = [
        "Toufik"
        
    ]
    for h in handles:
        check_skipped_contests(h)
