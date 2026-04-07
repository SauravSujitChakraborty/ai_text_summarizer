# ai_text_summarizer

NOTE :- This project was made by me during Nov 2025, preserved and finally uploaded on Apr 6,'26.

Summarizes a piece of text information into smaller output

The project follows a four-step pipeline: Preprocessing, Weighted Frequency Distribution, Sentence Scoring, and Heuristic Extraction.

1. Preprocessing & Noise Reduction
Before the algorithm can "rank" importance, it must clean the data. My code uses Regular Expressions (Regex) to remove citations and extra whitespace.

i)Stop-word Removal: Words like "the," "is," and "and" have high frequency but zero semantic value. By filtering these out using the NLTK library, the model ensures it only focuses on "content words" (nouns, verbs, adjectives).

2. Weighted Frequency Distribution
The clmost important part of this summarizer is based on the Term Frequency (TF) principle.

i) The Logic: In a specific text, the words that appear most often (excluding stop-words) are the best indicators of the topic.

ii) Normalization: To prevent absolute counts from skewing results, the code normalizes frequencies:
$\text{Normalized Weight}(w) = \frac{\text{Count of word } w}{\text{Count of the most frequent word in text}}$
This ensures every word has a weight $W \in [0, 1]$.

3. Sentence Scoring Algorithm*
​The model treats each sentence as a "container" of importance. The score of a sentence S is the sum of the normalized weights of its constituent words:
$\text{Score}(S) = \sum_{w \in S} \text{Normalized Weight}(w)$

*Heuristic Constraint: I have included a length filter (len(sent.split(' ')) < 30). This is a "Heuristic" to prevent the model from biasedly picking extremely long sentences just because they contain more words.

4. Selection via Priority Queue
To extract the top N sentences without sorting the entire list (which is computationally expensive for large documents), the code uses a Heap Queue (heapq). This is an efficient $O(n/logk)$ operation to find the "largest" elements, making the code scalable for longer articles.
