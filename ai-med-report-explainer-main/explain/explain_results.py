import requests

OLLAMA_URL = "http://localhost:11434/api/generate"

def explain_medical_report(text, model="llama3.2:1b"):

    text = text[:300]

    prompt = f"""
You are a professional medical assistant AI.

Analyze the medical report and give a structured explanation like a doctor.

Follow EXACT format:

🧾 1. Overall Result:
- Normal or Abnormal summary

📊 2. Key Findings:
- Explain each CBC parameter in simple words

🧠 3. Interpretation:
- What the values mean for health

💡 4. Advice:
- What patient should do (diet, lifestyle, checkups)

⚠️ 5. Warning:
- When to consult doctor

Rules:
- Use simple English
- Be clear and helpful
- Do NOT give panic or extreme diagnosis
- Do NOT use long paragraphs

Medical Report:
{text}
"""

    try:
        res = requests.post(
            OLLAMA_URL,
            json={
                "model": model,
                "prompt": prompt,
                "stream": False,
                "options": {
                    "num_predict": 200,
                    "temperature": 0.3
                }
            },
            timeout=60
        )

        return res.json().get("response", "").strip()

    except Exception as e:
        return "AI error: " + str(e)