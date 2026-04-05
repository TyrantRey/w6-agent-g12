import urllib.request
import json

TOOL = {
    "name": "random_fact_tool",
    "description": "取得一則隨機的冷知識，可以用來當作旅遊行前簡報的趣味開場或結尾",
    "parameters": {
        "type": "object",
        "properties": {}
    }
}

def run() -> str:
    url = "https://uselessfacts.jsph.pl/api/v2/facts/random"
    
    try:
        req = urllib.request.Request(url, headers={'Accept': 'application/json'})
        with urllib.request.urlopen(req) as response:
            data = json.loads(response.read().decode('utf-8'))
            
            fact = data.get("text", "無法取得冷知識")
            
            return f"隨機冷知識：{fact}"
            
    except Exception as e:
        return f"取得冷知識時發生錯誤: {str(e)}"

if __name__ == "__main__":
    print(run())