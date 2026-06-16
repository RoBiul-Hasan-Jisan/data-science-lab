import requests

def get_user_countries(handles):
    url = f"https://codeforces.com/api/user.info?handles={';'.join(handles)}"
    try:
        res = requests.get(url).json()
        if res["status"] == "OK":
            return {user["handle"]: user.get("country", "") for user in res["result"]}
    except:
        return {}
    return {}

def list_bangladeshi_skipped(contest_id=2126):
    print(f"🔍 Checking skipped accounts from Bangladesh in contest {contest_id}...\n")
    url = f"https://codeforces.com/api/contest.ratingChanges?contestId={contest_id}"
    res = requests.get(url).json()

    if res["status"] != "OK":
        print("❌ API error:", res.get("comment"))
        return

    skipped = [u for u in res["result"] if u["oldRating"] == u["newRating"]]
    handles = [u["handle"] for u in skipped]

    # Batch in chunks of 100 (Codeforces API limit)
    all_countries = {}
    for i in range(0, len(handles), 100):
        chunk = handles[i:i+100]
        countries = get_user_countries(chunk)
        all_countries.update(countries)

    bd_skipped = [
        u for u in skipped
        if all_countries.get(u["handle"]) == "Bangladesh"
    ]

    if not bd_skipped:
        print("✅ No skipped users from Bangladesh found.")
    else:
        print(f"⚠️ Skipped users from Bangladesh in contest {contest_id}:\n")
        for user in bd_skipped:
            print(f"- {user['handle']} | Rank: {user['rank']} | Rating: {user['oldRating']} → {user['newRating']}")

if __name__ == "__main__":
    list_bangladeshi_skipped(2126)
