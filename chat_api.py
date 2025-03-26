# chat_api.py
import requests

def call_deepseek(prompt):
    url = "http://localhost:1234/v1/completions"  # Địa chỉ LM Studio API
    headers = {"Content-Type": "application/json"}
    payload = {
        "model": "deepseek-r1-distill-qwen-7b",  # hoặc tên model bạn đã load
        "prompt": prompt,
        "max_tokens": 100,
        "temperature": 0.25
    }

    try:
        response = requests.post(url, headers=headers, json=payload)
        return response.json()["choices"][0]["text"].strip()
    except Exception as e:
        return f"Lỗi khi gọi model: {e}"
