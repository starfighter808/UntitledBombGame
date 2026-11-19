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
        #Make the HTTP request with a standard User-Agent header
        req = urllib.request.Request(
            url, 
            headers={'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64)'}
        )
        
        with urllib.request.urlopen(req, timeout=5) as response:
            if response.status == 200:
                #save the response
                data = json.loads(response.read().decode())
                
                #get the word out of the json
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

def buttondle_logic(answer_word):
    day = datetime.datetime.weekday()
    match day:
        case 0 | 1:
            correct_letter = answer_word[0]
        case 2:
            correct_letter = answer_word[1]
        case 3:
            correct_letter = answer_word[2]
        case 4:
            correct_letter = answer_word[3]
        case 5 | 6:
            correct_letter = answer_word[4]
    