（請記得將該檔名改命名為 `README.md`）

# AI agent 開發分組實作

> 課程：AI agent 開發 — Tool 與 Skill
> 主題： 旅遊前哨站 /  偵探事務所 /  生活顧問

---

## Agent 功能總覽

> 說明這個 Agent 能做什麼，使用者可以輸入哪些指令

| 使用者輸入   | Agent 行為                             | 負責組員 |
| ------------ | -------------------------------------- | -------- |
| （例：天氣） | 呼叫 weather_tool，查詢即時天氣        |          |
| （例：景點） | 呼叫 search_tool，搜尋熱門景點         |          |
| （例：建議） | 呼叫 advice_tool，取得隨機建議         |          |
| （例：出發） | 執行 trip_briefing Skill，產出行前簡報 |          |

---

## 組員與分工

| 姓名   | 負責功能              | 檔案                          | 使用的 API                                       |
| ------ | --------------------- | ----------------------------- | ------------------------------------------------ |
| 何平   | 取得一則今日活動建議  | `tools/activity_suggester.py` | https://bored-api.appbrewery.com/random          |
|        |                       | `tools/`                      |                                                  |
| 邱家悅 | 新增隨機冷知識 Tool   | `tools/fact_tool.py`          | https://uselessfacts.jsph.pl/api/v2/facts/random |
| 龎靚伊 | 搜尋當地熱門景點 Tool | `tools/search_tool.py`        | DuckDuckGo Search (ddgs)                         |
|        |                       | `tools/`                      |                                                  |
|        |                       | `tools/`                      |                                                  |
|        | Skill 整合            | `skills/`                     | —                                                |
|        | Agent 主程式          | `main.py`                     | —                                                |

---

## 專案架構

範例：

```
├── tools/
│   ├── xxx_tool.py   
│   ├── xxx_tool.py   
│   └── xxx_tool.py  
├── skills/
│   └── xxx_skill.py  
├── main.py        
├── requirements.txt
└── README.md
```

---

## 使用方式

範例：

```bash
python3 -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt
python main.py
```

---

## 執行結果

> 貼上程式執行的實際範例輸出

```
（貼上執行結果，例如下的指令與輸出結果）
```

---

## 各功能說明

### [取得一則今日活動建議]（負責：何平）

- **Tool 名稱**：get_activity_suggestion
- **使用 API**：https://bored-api.appbrewery.com/random
- **輸入**：城市名稱
- **輸出範例**：台北市，準備好迎接一場獨特的城市探險了嗎？

除了品嚐夜市小吃、走訪歷史古蹟，我們為您準備了一項特別的活動：「在您最喜歡的公園撿垃圾」。這不僅能讓您以不同的視角探索台北的綠意空間，更能為這座城市貢獻一份心力，讓您的旅程更添意義！

期待您在台北的精彩旅程！

```python
TOOL = {
    "name": "",
    "description": "",
    "parameters": { ... }
}
```

### 搜尋當地熱門景點（負責：龎靚伊）

- **Tool 名稱**：search_attractions
- **使用 API**：DuckDuckGo Search（ddgs 套件）
- **輸入**：搜尋關鍵字，例如 `Tokyo 景點`、`Paris travel tips`
- **輸出範例**：

  ```text
  🔍 搜尋結果：「Tokyo 景點」
  ──────────────────────────────────────────
  1. 🗺️  東京必去景點推薦
     淺草寺、東京鐵塔、新宿御苑...
     🔗 https://example.com/tokyo
  ```

```python
TOOL = {
    "name": "search_attractions",
    "description": "搜尋某個城市或地點的熱門景點、旅遊注意事項或相關旅遊資訊。",
    "parameters": {
        "type": "object",
        "properties": {
            "query": {"type": "string"},
            "max_results": {"type": "integer"}
        },
        "required": ["query"]
    }
}
```

### [功能名稱]（負責：姓名）

- **Tool 名稱**：
- **使用 API**：
- **輸入**：
- **輸出範例**：

### [功能名稱]（負責：姓名）

- **Tool 名稱**：
- **使用 API**：
- **輸入**：
- **輸出範例**：

### Skill：[Skill 名稱]（負責：姓名）

- **組合了哪些 Tool**：
- **執行順序**：

```
Step 1: 呼叫 ___ → 取得 ___
Step 2: 呼叫 ___ → 取得 ___
Step 3: 組合輸出 → 產生 ___
```

---

## 心得

### 遇到最難的問題

> 寫下這次實作遇到最困難的事，以及怎麼解決的

### Tool 和 Skill 的差別

> 用自己的話說說，做完後你怎麼理解兩者的不同

### 如果再加一個功能

> 如果可以多加一個 Tool，你會加什麼？為什麼？