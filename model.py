from transformers import pipeline
import pandas as pd
from transformers import BartTokenizer, BartForConditionalGeneration

df = pd.read_excel(fr".\output\data.xlsx")

# Load the pretrained BART model and tokenizer
model_name = "facebook/bart-large-cnn"
tokenizer = BartTokenizer.from_pretrained(model_name)
model = BartForConditionalGeneration.from_pretrained(model_name)

# Function to generate summaries for each row in the DataFrame
def generate_summary(text):
    inputs = tokenizer.encode("summarize: " + text, return_tensors="pt", max_length=1024, truncation=True)
    summary_ids = model.generate(inputs, max_length=150, min_length=50, length_penalty=2.0, num_beams=4, early_stopping=True)
    summary = tokenizer.decode(summary_ids[0], skip_special_tokens=True)
    return summary

df['summary'] = df['scraped_text'].apply(generate_summary)

df.to_excel(fr".\output\summary.xlsx", index=False)
# Print the DataFrame with the summaries
print("BART", df)