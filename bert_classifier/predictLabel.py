import torch
from transformers import AutoTokenizer, AutoModelForSequenceClassification


# učitavanje modela i tokenizatora

model_path = "./data/model/bert_nostalgia_classifier/crosloengual"

tokenizer = AutoTokenizer.from_pretrained(model_path, local_files_only=True)
model = AutoModelForSequenceClassification.from_pretrained(model_path, local_files_only=True)
model.eval()

#funkcija za predikciju

def predict_label(text):
    inputs = tokenizer(text, return_tensors="pt", truncation=True, padding=True)
    with torch.no_grad():
        logits = model(**inputs).logits
        pred = torch.argmax(logits, dim=1).item()
    return pred  # 0=nostalgija, 1=kritika, 2=neutralno

