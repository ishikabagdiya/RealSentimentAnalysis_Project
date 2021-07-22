from nltk.metrics import scores
import streamlit as str
import nltk
from nltk.sentiment.vader import SentimentIntensityAnalyzer
str.write("# Real Time Sentiment Analysis")

user_input = str.text_input("Please Rate our services>>:")
nltk.download("vader_lexicon")
s= SentimentIntensityAnalyzer()
score = s.polarity_scores(user_input)

if score == 0:
    str.write("# Neutral")
elif score["neg"] !=0:
    str.write("# Negative ")
elif score["pos"] !=0:
    str.write("# Positive")







