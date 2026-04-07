import os
from dotenv import load_dotenv
from langchain_google_genai import ChatGoogleGenerativeAI
from langchain.agents import create_agent
from tools.activity_suggester import get_activity_suggestion

# 載入環境變數 (請確保您有 .env 檔案包含 GEMINI_API_KEY)
load_dotenv()

def main():
    # 建立語言模型
    # 根據要求，使用免費的 gemini-2.5-flash
    llm = ChatGoogleGenerativeAI(
        model="gemini-2.5-flash",
        temperature=0.7 
    )

    # 建立工具清單
    tools = [get_activity_suggestion]

    # 設定 Agent Prompt (明確指示 Agent 擔任旅遊助理並根據工具結果產出簡報)
    system_prompt = "你是一位精通旅遊行程規劃的 AI 助理。當用戶輸入他們想去的城市後，你必須調用可用的工具獲取當地的活動建議，接著整合資料，最後給出一份簡短、充滿吸引力的出發前行前簡報。"

    # 建立 Agent Executor
    # 設定 debug=True 來顯示呼叫工具的詳細過程
    agent_executor = create_agent(
        model=llm,
        tools=tools,
        system_prompt=system_prompt,
        debug=True
    )

    # 互動式對話迴圈
    print("=== 旅遊 Agent 已啟動！您可以隨時輸入城市名稱詢問行前建議，輸入 'q' 離開 ===")
    
    # 紀錄對話歷史
    chat_history = []
    
    while True:
        user_input = input("\n您想去哪裡旅行呢？ (輸入 q 離開): ")
        if user_input.strip().lower() in ['q', 'quit', 'exit']:
            print("感謝您的使用，祝您旅途愉快！")
            break
            
        if not user_input.strip():
            continue
            
        print(f"\n[Agent 思考與查詢中...]")
        
        # 將用戶的新訊息加入歷史
        chat_history.append(("user", user_input))
        
        # 呼叫 Agent
        result = agent_executor.invoke({"messages": chat_history})
        
        # 更新對話歷史 (StateGraph 會回傳包含本次互動的完整訊息清單)
        chat_history = result['messages']
        
        print("\n=== 行前簡報 ===")
        # 從最後一個 AIMessage 取出回應內容
        final_message = chat_history[-1].content
        
        # 處理 possible dictionary/list response structure for content
        if isinstance(final_message, list):
            for part in final_message:
                if isinstance(part, dict) and 'text' in part:
                    print(part['text'])
                else:
                    print(part)
        else:
            print(final_message)

if __name__ == "__main__":
    main()
