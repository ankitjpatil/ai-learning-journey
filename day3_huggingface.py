from transformers import pipeline

# ─── Exercise 1 — Sentiment Analysis (positive) ───
print("--- Exercise 1: Sentiment Analysis ---")
classifier = pipeline("sentiment-analysis")
result1 = classifier("I love learning AI in Canada!")
print(result1)
print()

# ─── Exercise 2 — Sentiment Analysis (negative) ───
print("--- Exercise 2: Negative Sentiment ---")
result2 = classifier("I hate debugging Git issues!")
print(result2)
print()

# ─── Exercise 3 — Text Generation ───
print("--- Exercise 3: Text Generation ---")
generator = pipeline("text-generation", model="gpt2")
result3 = generator("In Canada, the best AI jobs are", max_length=30)
print(result3)
print()

# ─── Exercise 4 — Zero Shot Classification ───
print("--- Exercise 4: Zero Shot Classification ---")
classifier2 = pipeline("zero-shot-classification")
result4 = classifier2(
    "I need to build a RAG chatbot for manufacturing",
    candidate_labels=["technology", "finance", "healthcare", "manufacturing"]
)
print(result4)
print()

# ─── Exercise 5 — Question Answering ───
print("--- Exercise 5: Question Answering ---")
qa = pipeline("question-answering")
result5 = qa(
    question="What does RAG stand for?",
    context="Retrieval Augmented Generation is a technique that combines information retrieval with text generation to produce more accurate responses."
)
print(result5)
print()

# ─── Exercise 6 — Fill Mask ───
print("--- Exercise 6: Fill Mask ---")
unmasker = pipeline("fill-mask")
result6 = unmasker("HuggingFace is a great [MASK] for AI models.")
print(result6)