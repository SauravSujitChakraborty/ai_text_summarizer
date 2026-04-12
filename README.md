# ai_text_summarizer 

NOTE :- This project was made by me during Nov'25, preserved and finally uploaded on Apr 6,'26. 

==> Summarizes a piece of text information into smaller output

==> The project follows a four-step pipeline: Preprocessing, Weighted Frequency Distribution, Sentence Scoring, and Heuristic Extraction.

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

Summary

This project utilizes a Frequency-Weighted Extractive Algorithm. It maps the semantic importance of a document by calculating a normalized term-frequency distribution $\frac{f_i}{\max(f)}$. Sentences are then ranked as a function of their aggregate word-weights, providing a summary that maximizes information density while minimizing redundant linguistic noise.

Technical Walkthrough :- Complexity Analysis

The summarizer is optimized for high-performance text processing with the following complexity profile:

1. Time Complexity: $O(N + S \log K)$
Preprocessing & Frequency Mapping $O(N)$: Performs a linear scan of $N$ tokens. Utilizing a Hash Map (Python dict) ensures $O(1)$ average-case updates for word frequencies.
Sentence Scoring $O(N)$: Aggregates weights by iterating through the corpus a second time. A heuristic filter is applied to skip sentences >30 words, optimizing for information density.
Selection $O(S \log K)$: Leverages a Priority Queue (via heapq.nlargest) to extract the top $K$ sentences. This avoids the $O(S \log S)$ cost of a full sort, which is critical for low-latency processing of large document sets.
2. Space Complexity: $O(V + S)$
Vocabulary Storage $O(V)$: Memory usage scales with the unique vocabulary size $V$. As per Heaps' Law, $V$ grows significantly slower than the total word count $N$, ensuring a stable memory footprint.
Score Mapping $O(S)$: Stores a numeric priority score for each sentence $S$ in the document.

The "Heap" Mechanism 
When we use heapq.nlargest($$K$$, sentence_scores), the algorithm doesn't just look at the list. It follows this high-efficiency process:
Heap Initialization $O(K)$: The algorithm takes the first $K$ sentences and builds a Min-Heap. In a Min-Heap, the smallest element of the top $K$ is always at the root (the "top" of the pile).
Streaming Comparison $O(S \log K)$: For every remaining sentence in the document (the other $S-K$ sentences):
It compares the new sentence's score to the Root (the smallest of the current top $K$).
If the new sentence is larger than the root, it kicks the root out and inserts the new sentence.

Importance of Log: Re-adjusting the heap after an insertion takes $log K$ steps.

Result: We are left with the $K$ largest elements, but you never spent time sorting the thousands of smaller, irrelevant sentences.
​
Packages Required :-

This project leverages state-of-the-art Natural Language Processing (NLP) libraries to handle deep learning tensors and transformer-based architectures.

==> Transformers: Provided by Hugging Face; used to implement pre-trained BART/T5 models for abstractive summarization.

==> PyTorch : Acts as the deep learning backend for tensor computations and GPU acceleration (CUDA).

==> SentencePiece: A sub-word tokenizer required for modern transformer models to handle vocabulary efficiently.

==> NLTK: Used for text pre-processing and sentence boundary detection to ensure clean input data.
