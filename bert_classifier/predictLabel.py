import torch
from transformers import AutoTokenizer, AutoModelForSequenceClassification

# -----------------------------
# 1) UČITAJ MODEL
# -----------------------------
model_path = "model/bert_nostalgia_classifier"

tokenizer = AutoTokenizer.from_pretrained(model_path)
model = AutoModelForSequenceClassification.from_pretrained(model_path)
model.eval()

# -----------------------------
# 2) FUNKCIJA ZA PREDIKCIJU
# -----------------------------
def predict_label(text):
    inputs = tokenizer(text, return_tensors="pt", truncation=True, padding=True)
    with torch.no_grad():
        logits = model(**inputs).logits
        pred = torch.argmax(logits, dim=1).item()
    return pred  # 0=nostalgija, 1=kritika, 2=neutralno

