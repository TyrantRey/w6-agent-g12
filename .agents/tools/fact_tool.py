import urllib.request
import json

TOOL = {
    "name": "random_fact_tool",
    "description": "取得一則隨機的冷知識，可以用來當作旅遊行前簡報的趣味開場或結尾",
    "parameters": {} # 這個 API 不需要輸入參數，所以保持空白
}

def run() -> str:
    """呼叫 Useless Facts API 取得隨機冷知識"""
    url = "https://uselessfacts.jsph.pl/api/v2/facts/random"
    
    try:
        # 設定 headers 確保 API 回傳 JSON 格式
        req = urllib.request.Request(url, headers={'Accept': 'application/json'})
        with urllib.request.urlopen(req) as response:
            data = json.loads(response.read().decode('utf-8'))
            
            # API 回傳的 JSON 中，'text' 欄位就是冷知識的內容
            fact = data.get("text", "無法取得冷知識")
            
            return f"隨機冷知識：{fact}"
            
    except Exception as e:
        return f"取得冷知識時發生錯誤: {str(e)}"

if __name__ == "__main__":
    print(run())