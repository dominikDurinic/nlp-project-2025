import time
import json
import numpy as np
from bert_classifier.loadLabeledJSONL import load_jsonl
from datasets import Dataset
from sklearn.metrics import confusion_matrix, classification_report
from transformers import (
    AutoTokenizer,
    AutoModelForSequenceClassification,
    TrainingArguments,
    Trainer,
    TrainerCallback
)

dataset = load_jsonl("./data/train/labeled_comments_shuffled.jsonl")


# razdvoji na train i test skupove
dataset = dataset.train_test_split(test_size=0.2)


# TOKENIZACIJA -  BERTic tokenize
model_name = "classla/bcms-bertic"#"EMBEDDIA/crosloengual-bert"
tokenizer = AutoTokenizer.from_pretrained(model_name)

def tokenize(batch):
    return tokenizer(
        batch["clean_text"],
        padding="max_length",
        truncation=True,
        max_length=128
    )

tokenized = dataset.map(tokenize, batched=True)


# MODEL za klasifikaciju s 3 klase: 0=nostalgija, 1=kritika, 2=neutraln
model = AutoModelForSequenceClassification.from_pretrained(
    model_name,
    num_labels=3
)


# CALLBACK ZA MJERENJE VREMENA EPOH
class TimeCallback(TrainerCallback):
    def on_epoch_begin(self, args, state, control, **kwargs):
        self.start = time.time()

    def on_epoch_end(self, args, state, control, **kwargs):
        duration = time.time() - self.start
        print(f"\nEpoch {int(state.epoch)} trajanje: {duration:.2f} seconds\n")


# PARAMS za trening
'''
args = TrainingArguments(
    output_dir="bert_nostalgia_model",
    evaluation_strategy="epoch",
    save_strategy="epoch",
    learning_rate=2e-5,
    per_device_train_batch_size=8,
    per_device_eval_batch_size=8,
    num_train_epochs=3,
    weight_decay=0.01,
    logging_strategy="steps",
    logging_steps=50,
    logging_dir="./logs",
    load_best_model_at_end=True,
    report_to="none"
)
'''
args = TrainingArguments(
    output_dir="bertic_nostalgia_model",
    evaluation_strategy="epoch",
    save_strategy="epoch",
    learning_rate=2e-5,                 # BERTić voli 2e-5 ili 1.5e-5
    per_device_train_batch_size=16,     # stabilnije od 8
    per_device_eval_batch_size=16,
    num_train_epochs=4,                 # BERTić bolje konvergira s 4 epohe
    weight_decay=0.01,
    warmup_ratio=0.1,                   # VAŽNO za BERTić
    logging_strategy="steps",
    logging_steps=50,
    logging_dir="./logs",
    load_best_model_at_end=True,
    report_to="none"
)


# TRENER
trainer = Trainer(
    model=model,
    args=args,
    train_dataset=tokenized["train"],
    eval_dataset=tokenized["test"],
)

trainer.add_callback(TimeCallback())


# pocetak TRENING
start = time.time()
trainer.train()
end = time.time()

print(f"\nUKUPNO VRIJEME TRENIRANJA: {end - start:.2f} seconds\n")


# evaluacija i spremanje metrika
metrics = trainer.evaluate()
print("\nEvaluacija metrika:\n", metrics)

with open("./data/model/bert_nostalgia_classifier/bertic/training_metrics.json", "w") as f:
    json.dump(metrics, f, indent=2)


# confusion matrix i classification report
preds = trainer.predict(tokenized["test"])
y_true = preds.label_ids
y_pred = np.argmax(preds.predictions, axis=1)

print("\nCONFUSION MATRIX:")
print(confusion_matrix(y_true, y_pred))

print("\nCLASSIFICATION REPORT:")
print(classification_report(y_true, y_pred))

with open("./data/model/bert_nostalgia_classifier/bertic/classification_report.txt", "w") as f:
    f.write(classification_report(y_true, y_pred))


# spremanje pogrešno klasificiranih primjera
wrong = []
test_texts = dataset["test"]["clean_text"]

for i, (true, pred) in enumerate(zip(y_true, y_pred)):
    if true != pred:
        wrong.append({
            "text": test_texts[i],
            "true_label": int(true),
            "predicted_label": int(pred)
        })

with open("./data/model/bert_nostalgia_classifier/bertic/wrong_predictions.jsonl", "w", encoding="utf-8") as f:
    for w in wrong:
        f.write(json.dumps(w, ensure_ascii=False) + "\n")

print(f"\nPogresne predikcije spremljene: {len(wrong)}\n")


# spremanje model
trainer.save_model("./data/model/bert_nostalgia_classifier/bertic")
tokenizer.save_pretrained("./data/model/bert_nostalgia_classifier/bertic")

print("\nModel uspjesno spremljen.\n")
