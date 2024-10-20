!pip install sumy
!pip install nltk  # Install NLTK if not already installed

import pandas as pd
from textblob import TextBlob
from sklearn.model_selection import train_test_split
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.ensemble import RandomForestClassifier
from sumy.parsers.plaintext import PlaintextParser
from sumy.nlp.tokenizers import Tokenizer
from sumy.summarizers.lsa import LsaSummarizer
import nltk

# Download the punkt tokenizer
nltk.download('punkt')

# Load dataset
df = pd.read_csv('/content/review_data.csv')

# Print columns to check if 'reviews' exists
print("Columns in DataFrame:", df.columns.tolist())

# Print first few rows to inspect data
print("First few rows of the DataFrame:")
print(df.head())

# Check for leading/trailing spaces in column names
df.columns = df.columns.str.strip()

# Check if 'reviews' column exists after stripping spaces
column_name = 'reviews'  # This is the expected column name
if column_name not in df.columns:
    raise KeyError(f"The '{column_name}' column is missing from the DataFrame. Please check your CSV file.")

# Preprocess the text
def preprocess_text(text):
    return text.lower()  # Convert to lowercase

df['cleaned_reviews'] = df[column_name].apply(preprocess_text)

# Sentiment Classification using TextBlob
def get_sentiment(text):
    analysis = TextBlob(text)
    if analysis.sentiment.polarity > 0:
        return 'positive'
    elif analysis.sentiment.polarity == 0:
        return 'neutral'
    else:
        return 'negative'

df['sentiment'] = df['cleaned_reviews'].apply(get_sentiment)

# Check the distribution of sentiment labels
sentiment_counts = df['sentiment'].value_counts()
print("Sentiment distribution:\n", sentiment_counts)

# Summarization for each sentiment category
def summarize_text(texts):
    combined_text = " ".join(texts)
    parser = PlaintextParser.from_string(combined_text, Tokenizer("english"))
    summarizer = LsaSummarizer()
    summary = summarizer(parser.document, sentences_count=3)
    return " ".join([str(sentence) for sentence in summary])

# Summarize reviews by sentiment
positive_reviews = df[df['sentiment'] == 'positive']['cleaned_reviews']
neutral_reviews = df[df['sentiment'] == 'neutral']['cleaned_reviews']
negative_reviews = df[df['sentiment'] == 'negative']['cleaned_reviews']

# Generate summaries
positive_summary = summarize_text(positive_reviews)
neutral_summary = summarize_text(neutral_reviews)
negative_summary = summarize_text(negative_reviews)

# Output the summaries
print("Positive Reviews Summary:", positive_summary)
print("Neutral Reviews Summary:", neutral_summary)
print("Negative Reviews Summary:", negative_summary)
