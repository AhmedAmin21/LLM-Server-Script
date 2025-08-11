import frappe
import requests

@frappe.whitelist()
def chat_with_groq(prompt):
    api_key = "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"  # Replace this
    model = "gemma2-9b-it"  # Or another GROQ-supported model

    headers = {
        "Authorization": f"Bearer {api_key}",
        "Content-Type": "application/json"
    }

    payload = {
        "model": model,
        "messages": [
            {"role": "user", "content": prompt}
        ]
    }

    response = requests.post("https://api.groq.com/openai/v1/chat/completions", json=payload, headers=headers)

    if response.status_code == 200:
        return response.json()["choices"][0]["message"]["content"]
    else:
        frappe.log_error(response.text, "GROQ API Error")
        return "Sorry, something went wrong."




