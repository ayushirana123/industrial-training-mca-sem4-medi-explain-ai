import re

def parse_lab_report(text):

    text = text.lower()

    def clean_value(val):
        try:
            return float(val)
        except:
            return None

    patterns = {
        "haemoglobin": r"haemoglobin\s*[:\-]?\s*([\d.]+)",
        "mcv": r"\bmcv\b\s*[:\-]?\s*([\d.]+)",
        "platelet count": r"platelet\s*count\s*[:\-]?\s*([\d.]+)",
        "t.l.c": r"(?:tlc|t\.l\.c|total\s*leukocyte\s*count)\s*[:\-]?\s*([\d.]+)",
    }

    results = []

    for name, pattern in patterns.items():
        match = re.search(pattern, text)

        if match:
            value = clean_value(match.group(1))

            # 🔥 FIX: convert TLC properly (x10^3/uL → real scale)
            if name == "t.l.c" and value is not None:
                value = value * 1000

            results.append({
                "name": name,
                "value": value,
                "unit": ""
            })

    return results