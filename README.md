# ai_text_summarizer
Summarizes a piece of text information into smaller output

The project follows a four-step pipeline: Preprocessing, Weighted Frequency Distribution, Sentence Scoring, and Heuristic Extraction.
1. Preprocessing & Noise Reduction
Before the algorithm can "rank" importance, it must clean the data. Your code uses Regular Expressions (Regex) to remove citations and extra whitespace.
Stop-word Removal: Words like "the," "is," and "and" have high frequency but zero semantic value. By filtering these out using the nltk library, the model ensures it only focuses on "content words" (nouns, verbs, adjectives).
2. Weighted Frequency Distribution
The core "Alpha" of this summarizer is based on the Term Frequency (TF) principle.
1. The Logic: In a specific text, the words that appear most often (excluding stop-words) are the best indicators of the topic.
2. Normalization: To prevent absolute counts from skewing results, the code normalizes frequencies:
$\text{Normalized Weight}(w) = \frac{\text{Count of word } w}{\text{Count of the most frequent word in text}}$
