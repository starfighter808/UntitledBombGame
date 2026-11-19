import datetime
import urllib.request
import json

def fetch_wordle_answer():
    #make a string of todays date in YYYY-MM-DD format
    today_str = datetime.date.today().strftime("%Y-%m-%d")
    url = f"https://www.nytimes.com/svc/wordle/v2/{today_str}.json"

    print(f"Requesting puzzle for {today_str}...")
    print(f"Endpoint: {url}")

    try:
        # 2. Make the HTTP request with a standard User-Agent header
        req = urllib.request.Request(
            url, 
            headers={'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64)'}
        )
        
        with urllib.request.urlopen(req, timeout=5) as response:
            if response.status == 200:
                # 3. Parse the JSON response body
                data = json.loads(response.read().decode())
                
                # 4. Extract target fields
                puzzle_id = data.get("id")
                solution = data.get("solution", "").upper()
                print("\n[SUCCESS] Connected to NYT successfully!")
                print(f"Puzzle ID: #{puzzle_id}")
                print(f"Today's Official Word: {solution}")
                return solution
            else:
                print(f"[ERROR] Received HTTP status: {response.status}")
                
    except Exception as e:
        print(f"[WARNING] Request failed: {e}")
        print("Falling back to offline default word: CRANE")
        return "CRANE"

if __name__ == "__main__":
    fetch_wordle_answer()