import requests
from langchain_core.tools import tool
from pydantic import BaseModel, Field

class ActivitySuggestionInput(BaseModel):
    city_name: str = Field(description="用戶想要前往旅行的城市名稱 (例如: '東京', 'London')")

@tool("get_activity_suggestion", args_schema=ActivitySuggestionInput)
def get_activity_suggestion(city_name: str) -> str:
    """提供一則當日在旅行地點可行的隨機活動建議。"""
    
    url = "https://bored-api.appbrewery.com/random"
    
    try:
        # API 呼叫，設定超時時間為 10 秒
        response = requests.get(url, timeout=10)
        
        # 檢查 HTTP 狀態碼是否為 200 系列
        response.raise_for_status()
        
        data = response.json()
        
        activity_name = data.get('activity', '未知活動')
        activity_type = data.get('type', '未知類型')
        
        # 組裝成帶有城市上下文的回傳內容，並符合「活動名稱與類型」的要求
        return f"為您在 {city_name} 找到的活動建議如下：\n活動名稱：{activity_name}\n活動類型：{activity_type}"
        
    except requests.exceptions.Timeout:
        return "無法獲取活動建議：API 無回應 (Timeout 超時，連線至 API 伺服器花費過久時間)。"
    except requests.exceptions.HTTPError as e:
        status_code = e.response.status_code
        # 特殊情況處理 (例如 API 存取限制)
        if status_code == 429:
            return "無法獲取活動建議：呼叫次數過多 (HTTP 429 Too Many Requests)，請稍後再試。"
        return f"無法獲取活動建議：API 回傳錯誤 (HTTP {status_code})。"
    except requests.exceptions.RequestException as e:
        return f"無法獲取活動建議：發生網路連線錯誤 ({str(e)})。"
    except ValueError:
        return "無法獲取活動建議：API 回傳的資料格式錯誤 (非有效的 JSON)。"
    except Exception as e:
        return f"無法獲取活動建議：發生未知的錯誤 ({str(e)})。"
