"""
search_tool.py

使用 ddgs 套件搜尋當地熱門景點或注意事項。
搜尋關鍵字範例：「Tokyo 景點」、「Paris travel tips」

安裝：pip install ddgs
"""

from ddgs import DDGS


# ── Gemini Function Calling 宣告 ────────────────────────────────────────────
TOOL = {
    "name": "search_attractions",
    "description": (
        "搜尋某個城市或地點的熱門景點、旅遊注意事項或相關旅遊資訊。"
        "例如輸入 'Tokyo 景點' 或 'Paris travel tips'，"
        "回傳標題、摘要與連結。"
    ),
    "parameters": {
        "type": "object",
        "properties": {
            "query": {
                "type": "string",
                "description": "搜尋關鍵字，例如 'Tokyo 景點'、'Kyoto travel tips'",
            },
            "max_results": {
                "type": "integer",
                "description": "最多回傳幾筆結果（預設 5，最多 10）",
            },
        },
        "required": ["query"],
    },
}


# ── 核心搜尋函式 ─────────────────────────────────────────────────────────────
def search_attractions(query: str, max_results: int = 5) -> str:
    """
    使用 DuckDuckGo 搜尋景點或旅遊注意事項。

    Args:
        query:       搜尋關鍵字，例如 "Tokyo 景點"
        max_results: 最多顯示幾筆結果（預設 5，最多 10）

    Returns:
        格式化後的搜尋結果字串（標題 + 摘要 + 連結）
    """
    max_results = min(max_results, 10)

    try:
        with DDGS() as ddgs:
            results = list(ddgs.text(query, max_results=max_results))
    except Exception as exc:
        return f"❌ 搜尋失敗：{exc}"

    if not results:
        return f"🔍 找不到「{query}」的相關結果。"

    lines = [f"🔍 搜尋結果：「{query}」", "─" * 42]
    for i, r in enumerate(results, 1):
        title = r.get("title", "（無標題）")
        body  = r.get("body", "")
        href  = r.get("href", "")
        lines.append(f"\n{i}. 🗺️  {title}")
        if body:
            lines.append(f"   {body}")
        if href:
            lines.append(f"   🔗 {href}")

    return "\n".join(lines)


# ── 獨立測試入口 ─────────────────────────────────────────────────────────────
if __name__ == "__main__":
    test_queries = [
        "Tokyo 景點",
        "Paris travel tips",
        "Kyoto 注意事項",
    ]
    for q in test_queries:
        print(search_attractions(q, max_results=3))
        print("\n" + "=" * 50 + "\n")
