from transformers import pipeline

# Load BERT model for fake news classification
model = pipeline('text-classification', model='mrm8488/bert-tiny-finetuned-fake-news')

def predict(text):
    return model(text)
