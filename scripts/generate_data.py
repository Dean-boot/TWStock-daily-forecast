import json
from datetime import date
import os

sample_data = [
    {
        "messages": [
            {"role": "user", "content": "請分析今天台積電的技術走勢"},
            {"role": "assistant", "content": "台積電今日收高並站穩5日線，成交量放大，顯示短多動能轉強。MACD翻紅，KD有黃金交叉跡象，若續量滾量，將挑戰715元壓力。"}
        ]
    },
    {
        "messages": [
            {"role": "user", "content": "日月光的技術分析如何？"},
            {"role": "assistant", "content": "日月光今天震盪收紅，靠近季線，若能突破168元將有反彈機會。RSI維持強勢區間，留意短期均線支撐。"}
        ]
    }
]

today = date.today().isoformat()
filename = f"training_data/{today}-twstock-analysis.jsonl"

os.makedirs("training_data", exist_ok=True)

with open(filename, "w", encoding="utf-8") as f:
    for item in sample_data:
        f.write(json.dumps(item, ensure_ascii=False) + "\n")

print(f"✅ 產生語料檔案：{filename}")
