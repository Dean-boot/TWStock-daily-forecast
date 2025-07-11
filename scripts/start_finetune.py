import os
import json
from datetime import date
from openai import OpenAI

# 初始化新版 OpenAI 客戶端
client = OpenAI(api_key=os.environ["OPENAI_API_KEY"])

today = date.today().isoformat()
file_path = f"training_data/{today}-twstock-analysis.jsonl"

print("🚀 上傳語料中...")

# 上傳語料
with open(file_path, "rb") as f:
    uploaded_file = client.files.create(
        file=f,
        purpose="fine-tune"
    )

print("🎯 開始微調...")

# 啟動微調任務
job = client.fine_tuning.jobs.create(
    training_file=uploaded_file.id,
    model="gpt-3.5-turbo"
)

# 記錄結果
log = {
    "date": today,
    "job_id": job.id,
    "model": job.fine_tuned_model or "(尚未完成)"
}
log_path = "model_log.json"

# 將結果寫入 log
logs = []
if os.path.exists(log_path):
    with open(log_path, "r", encoding="utf-8") as f:
        logs = json.load(f)

logs.append(log)
with open(log_path, "w", encoding="utf-8") as f:
    json.dump(logs, f, ensure_ascii=False, indent=2)

print(f"✅ 微調任務啟動成功：{job.id}")
