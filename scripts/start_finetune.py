import openai
import os

# 初始化 OpenAI client（建議使用環境變數）
client = openai.OpenAI(api_key=os.getenv("OPENAI_API_KEY"))

# 1️⃣ 上傳訓練資料（假設檔名為 fine_tune_data_prepared.jsonl）
print("🚀 上傳語料中...")
file = client.files.create(
    file=open("fine_tune_data_prepared.jsonl", "rb"),
    purpose="fine-tune"
)
print("✅ 上傳完成，File ID:", file.id)

# 2️⃣ 開始 fine-tune 任務（以 gpt-3.5-turbo 為例）
print("🎯 開始微調...")
job = client.fine_tuning.jobs.create(
    training_file=file.id,
    model="gpt-3.5-turbo"
)
print("✅ 微調任務已啟動，Job ID:", job.id)
