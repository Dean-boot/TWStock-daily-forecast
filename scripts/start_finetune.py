import openai
import os
from datetime import date
import json

openai.api_key = os.environ["OPENAI_API_KEY"]

today = date.today().isoformat()
file_path = f"training_data/{today}-twstock-analysis.jsonl"

print("🚀 上傳語料中...")
file = openai.File.create(file=open(file_path, "rb"), purpose="fine-tune")
file_id = file.id

print("🎯 開始微調...")
response = openai.FineTuningJob.create(
    training_file=file_id,
    model="gpt-3.5-turbo",
)

job_id = response["id"]
model_name = response.get("fine_tuned_model", "尚未完成")

# 記錄模型資訊
log = {"date": today, "job_id": job_id, "model": model_name}
log_path = "model_log.json"

logs = []
if os.path.exists(log_path):
    with open(log_path, "r", encoding="utf-8") as f:
        logs = json.load(f)

logs.append(log)

with open(log_path, "w", encoding="utf-8") as f:
    json.dump(logs, f, ensure_ascii=False, indent=2)

print(f"✅ 微調任務啟動：{job_id}")
