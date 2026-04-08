import pandas as pd 
import numpy as np
import nltk
import re
from nltk.corpus import stopwords
from nltk.tokenize import word_tokenize, sent_tokenize
import heapq

# ==========================================
# NLTK SETUP
# ==========================================
try:
    nltk.data.find('tokenizers/punkt')
    nltk.data.find('corpora/stopwords')
except LookupError:
    print("Downloading NLTK requirements...")
    nltk.download('punkt')
    nltk.download('stopwords')

# ==========================================
# THE SUMMARIZER FUNCTION
# ==========================================
def summarize_text(raw_text, number_of_sentences=3):
    # 1. Clean and Tokenize
    processed_text = re.sub(r'\[[0-9]*\]', ' ', raw_text) # Remove citations [1]
    processed_text = re.sub(r'\s+', ' ', processed_text)
    
    sentences = sent_tokenize(processed_text)
    stop_words = set(stopwords.words('english'))

    # 2. Build Word Frequency Table
    word_frequencies = {}
    for word in word_tokenize(processed_text.lower()):
        if word not in stop_words and word.isalnum():
            if word not in word_frequencies.keys():
                word_frequencies[word] = 1
            else:
                word_frequencies[word] += 1

    # Normalize frequencies (0 to 1 scale)
    max_frequency = max(word_frequencies.values())
    for word in word_frequencies.keys():
        word_frequencies[word] = (word_frequencies[word]/max_frequency)

    # 3. Score Sentences
    sentence_scores = {}
    for sent in sentences:
        for word in word_tokenize(sent.lower()):
            if word in word_frequencies.keys():
                if len(sent.split(' ')) < 30: # Ignore overly long/complex sentences
                    if sent not in sentence_scores.keys():
                        sentence_scores[sent] = word_frequencies[word]
                    else:
                        sentence_scores[sent] += word_frequencies[word]

    # 4. Extract Top Sentences
    summary_sentences = heapq.nlargest(number_of_sentences, sentence_scores, key=sentence_scores.get)
    summary = ' '.join(summary_sentences)
    return summary

# ==========================================
# TEST CASE: A LONG NEWS-STYLE PARAGRAPH
# ==========================================
article = """
Artificial intelligence (AI) is intelligence demonstrated by machines, as opposed to the natural intelligence displayed by animals including humans. 
AI research has been defined as the field of study of intelligent agents, which refers to any system that perceives its environment and takes actions that maximize its chance of achieving its goals. 
As machines become increasingly capable, tasks considered to require "intelligence" are often removed from the definition of AI, a phenomenon known as the AI effect. 
For instance, optical character recognition is frequently excluded from things considered to be AI, having become a routine technology. 
Modern machine learning involves a huge variety of different approaches, including deep learning and reinforcement learning.
"""

print("--- Original Article Length ---")
print(len(article), "characters")

print("\n--- AI Generated Summary ---")
summary = summarize_text(article, number_of_sentences=2)
print(summary)
print("\n--- Summary Length ---")
print(len(summary), "characters")
