from bert_classifier.loadLabeledJSONL import load_jsonl
from datasets import Dataset
from transformers import AutoTokenizer, AutoModelForSequenceClassification
from transformers import TrainingArguments, Trainer

dataset = load_jsonl("data/train/labeled_comments.jsonl")

# razdvoji na train i test skupove
dataset = dataset.train_test_split(test_size=0.2)

# BERTic tokenizer
model_name = "EMBEDDIA/crosloengual-bert"
tokenizer = AutoTokenizer.from_pretrained(model_name)

def tokenize(batch):
    return tokenizer(
        batch["text"],
        padding="max_length",
        truncation=True,
        max_length=128
    )

tokenized = dataset.map(tokenize, batched=True)

# model za klasifikaciju s 3 klase
model = AutoModelForSequenceClassification.from_pretrained(
    model_name,
    num_labels=3
)

# params za trening
args = TrainingArguments(
    output_dir="bert_nostalgia_model",
    evaluation_strategy="epoch",
    save_strategy="epoch",
    learning_rate=2e-5,
    per_device_train_batch_size=8,
    per_device_eval_batch_size=8,
    num_train_epochs=3,
    weight_decay=0.01
)

# trener
trainer = Trainer(
    model=model,
    args=args,
    train_dataset=tokenized["train"],
    eval_dataset=tokenized["test"]
)

# pocetak treninga
trainer.train()

# pohrana modela
trainer.save_model("model/bert_nostalgia_classifier")
tokenizer.save_pretrained("model/bert_nostalgia_classifier")