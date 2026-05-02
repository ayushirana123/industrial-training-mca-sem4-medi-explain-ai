from transformers import pipeline
import torch

ner = pipeline(
    "ner",
    model="d4data/biomedical-ner-all",
    tokenizer="d4data/biomedical-ner-all",
    aggregation_strategy="simple",
    device=0 if torch.cuda.is_available() else -1
)

def extract_lab_results_from_ner(text):
    try:
        results = ner(text)
        output = []

        for entity in results:
            word = entity["word"]

            # try extract number from entity
            import re
            match = re.search(r"[\d.]+", word)

            if match:
                output.append({
                    "name": entity["entity_group"].lower(),
                    "value": match.group(),
                    "unit": ""
                })

        return output

    except Exception as e:
        print("NER failed:", e)
        return []