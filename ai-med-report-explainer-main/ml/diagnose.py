import torch
import torch.nn.functional as F
from torchvision import transforms
from PIL import Image

LABELS = [
    "Normal",
    "Anaemia",
    "Thrombocytopenia",
    "Leukocytosis",
    "Leukopenia",
    "Macrocytosis",
    "Microcytosis",
    "Eosinophilia",
    "Other"
]

# ---------- RULE BASED DIAGNOSIS ----------
def predict_condition(features):

    hb = features.get("haemoglobin")
    tlc = features.get("t.l.c")
    platelets = features.get("platelet count")
    mcv = features.get("mcv")

    if hb is not None:
        hb = float(hb)
    if tlc is not None:
        tlc = float(tlc) * 1000   # FIX: convert x10^3/uL to real value
    if platelets is not None:
        platelets = float(platelets)
    if mcv is not None:
        mcv = float(mcv)

    if hb is not None and hb < 10:
        if mcv and mcv < 80:
            return "Microcytic Anaemia"
        elif mcv and mcv > 100:
            return "Macrocytic Anaemia"
        return "Anaemia"

    if platelets and platelets < 150:
        return "Thrombocytopenia"

    if tlc:
        if tlc > 11000:
            return "Leukocytosis"
        elif tlc < 4000:
            return "Leukopenia"

    return "Normal / No major abnormality"
# ---------- IMAGE MODEL (SAFE LOAD FIX) ----------
def predict_condition(features):

    hb = features.get("haemoglobin")
    tlc = features.get("t.l.c")
    platelets = features.get("platelet count")
    mcv = features.get("mcv")

    if hb is not None:
        hb = float(hb)

    if tlc is not None:
        tlc = float(tlc)   # already normalized in parser

    if platelets is not None:
        platelets = float(platelets)

    if mcv is not None:
        mcv = float(mcv)

    # ANEMIA
    if hb is not None and hb < 10:
        if mcv and mcv < 80:
            return "Microcytic Anaemia"
        elif mcv and mcv > 100:
            return "Macrocytic Anaemia"
        return "Anaemia"

    # PLATELETS
    if platelets and platelets < 150:
        return "Thrombocytopenia"

    # TLC
    if tlc:
        if tlc > 11000:
            return "Leukocytosis"
        elif tlc < 4000:
            return "Leukopenia"

    return "Normal / No major abnormality"

    # Platelet issue
    if platelets and platelets < 150:
        return "Thrombocytopenia"

    # 🔥 FIXED TLC LOGIC (NOW CONSISTENT)
    if tlc:
        if tlc > 11000:
            return "Leukocytosis"
        elif tlc < 4000:
            return "Leukopenia"

    return "Normal / No major abnormality"