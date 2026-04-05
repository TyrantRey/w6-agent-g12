"""
Food Search Tool - 搜尋目的地的當地美食
使用 DuckDuckGo Search API 搜尋指定目的地的在地特色美食與餐廳推薦。
"""

from ddgs import DDGS


# ── Gemini Function Declaration ─────────────────────────────────────────────
TOOL = {
    "name": "search_local_food",
    "description": (
        "搜尋指定目的地的當地美食與特色小吃。"
        "回傳該地區的推薦美食、餐廳資訊與相關介紹。"
    ),
    "parameters": {
        "type": "object",
        "properties": {
            "destination": {
                "type": "string",
                "description": "目的地名稱，例如：台南、東京、Bangkok",
            },
            "food_type": {
                "type": "string",
                "description": (
                    "（選填）想搜尋的美食類型，例如：小吃、拉麵、甜點。"
                    "若未指定則搜尋該地所有當地美食。"
                ),
            },
            "max_results": {
                "type": "integer",
                "description": "回傳的搜尋結果數量，預設為 5",
            },
        },
        "required": ["destination"],
    },
}


# ── Tool Implementation ─────────────────────────────────────────────────────
def search_local_food(
    destination: str,
    food_type: str = "",
    max_results: int = 5,
) -> dict:
    """
    使用 DuckDuckGo 搜尋目的地的當地美食。

    Args:
        destination: 目的地名稱
        food_type:   想搜尋的美食類型（選填）
        max_results: 回傳結果數量，預設 5

    Returns:
        dict: 包含搜尋結果的字典
    """
    # 組合搜尋關鍵字
    if food_type:
        query = f"{destination} {food_type} 當地美食 推薦"
    else:
        query = f"{destination} 當地美食 必吃 推薦"

    print(f"🔍 正在搜尋：{query}")

    try:
        with DDGS() as ddgs:
            raw_results = ddgs.text(
                query,
                region="wt-wt",          # 全球搜尋
                safesearch="moderate",
                max_results=max_results,
            )

        if not raw_results:
            return {
                "destination": destination,
                "food_type": food_type or "所有美食",
                "results": [],
                "message": f"找不到 {destination} 的美食資訊，請嘗試其他關鍵字。",
            }

        # 整理搜尋結果
        results = []
        for item in raw_results:
            results.append(
                {
                    "title": item.get("title", ""),
                    "snippet": item.get("body", ""),
                    "url": item.get("href", ""),
                }
            )

        print(f"✅ 找到 {len(results)} 筆 {destination} 美食資訊")

        return {
            "destination": destination,
            "food_type": food_type or "所有美食",
            "results": results,
            "message": f"成功找到 {len(results)} 筆關於 {destination} 的美食資訊。",
        }

    except Exception as e:
        print(f"❌ 搜尋失敗：{e}")
        return {
            "destination": destination,
            "food_type": food_type or "所有美食",
            "results": [],
            "message": f"搜尋過程發生錯誤：{str(e)}",
        }


# ── 獨立測試 ────────────────────────────────────────────────────────────────
if __name__ == "__main__":
    print("=" * 60)
    print("  🍜 當地美食搜尋工具 — 測試模式")
    print("=" * 60)

    # 測試 1：搜尋台南美食
    print("\n📌 測試 1：搜尋台南當地美食")
    result = search_local_food("台南")
    for r in result["results"]:
        print(f"  • {r['title']}")
        print(f"    {r['snippet'][:80]}...")
        print(f"    🔗 {r['url']}\n")

    # 測試 2：搜尋東京拉麵
    print("\n📌 測試 2：搜尋東京拉麵")
    result = search_local_food("東京", food_type="拉麵", max_results=3)
    for r in result["results"]:
        print(f"  • {r['title']}")
        print(f"    {r['snippet'][:80]}...")
        print(f"    🔗 {r['url']}\n")
