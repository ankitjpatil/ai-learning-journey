# Week 1 Notes — Karpathy LLM Video

## 1. What is a token
A token is a small chunk of text that the LLM uses to process language. 
The model never sees letters or full words — it only ever sees tokens.
Example: "unbelievable" might be split into "un" + "believ" + "able" = 3 tokens.
A rough rule: 1 token ≈ 0.75 words.
All text — your question, the response, documents — gets broken into tokens before the model processes it.
Tokens are NOT parameters — these are two completely different things.

## 2. What is a context window
The context window is everything the model can "see" at once during a conversation.
It works like RAM — finite, fast, and temporary.
It includes: your current question, the full conversation history, and any documents you feed in.
Once something falls outside the context window, the model completely forgets it.
This is why very long conversations can degrade in quality — older messages fall out of the window.
Larger context window = model can "remember" more of the conversation.

## 3. What is a parameter
Parameters are not inputs you give the model — they ARE the model itself.
Think of parameters as billions of tiny knobs inside a neural network.
During training, those knobs get adjusted until the model gets good at predicting the next token.
GPT-4 has roughly 1 trillion parameters.
When you download a model, you are literally downloading a file full of these numbers.
More parameters generally means a more capable but slower and more expensive model.

## 4. What is RLHF
RLHF stands for Reinforcement Learning from Human Feedback.
It is what turns a raw base model into a helpful assistant.
Without RLHF, the model just predicts the next token — it has no concept of being helpful.
With RLHF, human raters score model responses and the model learns to produce responses
humans prefer — helpful, harmless, and honest.
This is stage 2 of training, after the base model is created from raw internet data.

## 5. Something that surprised me
The security vulnerabilities of LLMs were eye opening.
Key threats:
- Prompt injection: attackers embed hidden instructions in text to hijack the model
- Jailbreaks: users trick the model into bypassing its safety guidelines
- Data poisoning: bad data in training corrupts model behaviour
The fact that LLMs are trained on raw unfiltered internet data makes them inherently 
vulnerable — the model has no way to distinguish trustworthy from malicious content.
This is a critical concern for any production AI system deployed for real clients.

## Key takeaway
A token is the unit of text. A parameter is a number inside the model.
The context window is working memory. RLHF is what makes the model behave well.
Security is not an afterthought — it is a core architectural concern from day one.








---

## Progress Tracker

### Phase 1 — Foundation

#### Week 1–2
- [x] GitHub profile live — ankitjpatil
- [x] ai-learning-journey repo created
- [x] Karpathy LLM video watched
- [x] Notes written and corrected
- [x] Virtual environment set up
- [x] First AI packages installed (openai, python-dotenv)
- [x] API key secured in .env
- [x] .gitignore protecting sensitive files
- [x] First LLM API call working — GPT-4o responded
- [x] first_llm_call.py pushed to GitHub
- [ ] HuggingFace NLP course chapters 1–4
- [ ] AWS Bedrock first call
- [ ] AWS Skill Builder started
- [ ] LangChain tutorials completed
- [ ] PDF Q&A exit project live