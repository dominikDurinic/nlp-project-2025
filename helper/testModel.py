from transformers import AutoModelForSequenceClassification, AutoTokenizer
import torch

# Putanja do tvog spremljenog modela (promijeni ako je drugačija)
model_path = "./data/model/bert_nostalgia_classifier/crosloengual"

# Učitavanje modela i tokenizera
model = AutoModelForSequenceClassification.from_pretrained(model_path)
tokenizer = AutoTokenizer.from_pretrained(model_path)

# Mapiranje labela za lakše čitanje
label_map = {0: "Nostalgija 🕊️", 1: "Kritika ❌", 2: "Neutralno 📝"}

def predict_sentiment(text):
    # Tokenizacija
    inputs = tokenizer(text, return_tensors="pt", truncation=True, padding=True, max_length=280)
    
    # Predikcija
    with torch.no_grad():
        outputs = model(**inputs)
    
    # Pretvaranje u vjerojatnosti
    probs = torch.nn.functional.softmax(outputs.logits, dim=-1)
    prediction = torch.argmax(probs).item()
    
    return label_map[prediction], probs[0][prediction].item()

# --- TESTIRANJE ---
test_komentari = [
    "U to vrijeme svatko je imao posao i nitko nije bio gladan.",
    "Jugoslavija je bila neodrživa tvorevina koja je gušila slobode.",
    "Sjednica predsjedništva održana je u srijedu u Beogradu.",
    "Sjećam se par-nepar vožnje, to je bilo ponižavajuće za narod.",
    "Bilo je odvratno i jadno čekati u redu za kavu kao prosjak.",
    "Hvala Partiji što nam je dala kavu na bonove.",
    "Čekali smo u redovima s bonovima da bismo dobili pola kile kave.",
    "Izgrađeno je mnogo tvornica, ali su danas sve propale."
]

print("--- REZULTATI TESTA U DIVLJINI ---")
for komentar in test_komentari:
    sent, prob = predict_sentiment(komentar)
    print(f"\nKomentar: {komentar}")
    print(f"Predikcija: {sent} (Sigurnost: {prob:.2%})")