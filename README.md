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
| 景點（例：Tokyo 景點） | 呼叫 search_attractions，搜尋熱門景點與旅遊注意事項 | 龎靚伊 |
| （例：建議） | 呼叫 advice_tool，取得隨機建議         |          |
| （例：出發） | 執行 trip_briefing Skill，產出行前簡報 |          |

---

## 組員與分工

| 姓名 | 負責功能     | 檔案      | 使用的 API |
| ---- | ------------ | --------- | ---------- |
|      |            | `tools/`  |           |
|   邱家悅   |      新增隨機冷知識 Tool           | `tools/fact_tool.py`  |     https://uselessfacts.jsph.pl/api/v2/facts/random        |
|   龎靚伊   |      搜尋當地熱門景點 Tool         | `tools/search_tool.py`  |     DuckDuckGo Search (ddgs)        |
|      |              | `tools/`  |            |
|  張紹謙    | Skill 整合   | `skills/` | —          |
|  張紹謙    | Agent 主程式 | `main.py` | —          |

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

### [功能名稱]（負責：邱家悅）

- **Tool 名稱**：fact_tool 
- **使用 API**：https://uselessfacts.jsph.pl/api/v2/facts/random
- **輸入**：
- **輸出範例**：隨機冷知識：Bruce Lee was so fast that they had to slow the film down so you could see his moves.

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

> 因為使用 Antigravity 進行 vibe coding，實作過程相對順暢。最難的部分反而是理解 `TOOL` 宣告的格式，不確定 `parameters` 的結構要怎麼寫，以及 ddgs 套件的安裝名稱和 import 名稱不一致（`pip install ddgs` 但 `from ddgs import DDGS`），需要查文件才確認正確用法。

### Tool 和 Skill 的差別

> 用自己的話說說，做完後你怎麼理解兩者的不同

> Tool 是單一功能的執行單元，只做一件事，例如搜尋景點；Skill 則是把多個 Tool 組合起來，依照順序執行並整合結果，產出更完整的輸出。Tool 像是工具箱裡的單一工具，Skill 像是一套完整的操作流程。

### 如果再加一個功能

> 如果可以多加一個 Tool，你會加什麼？為什麼？

> 我會加一個「匯率換算 Tool」，因為出國旅遊一定會需要換錢，知道當地景點之後馬上能查匯率，讓 Agent 更實用。
