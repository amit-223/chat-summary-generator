# summarizer/ollama_utils.py
import ollama

def generate_summary(chat_messages):
    prompt = "Summarize the following chat conversation in one sentence:\n\n"
    for msg in chat_messages:
        prompt += f"{msg['role'].capitalize()}: {msg['message']}\n"

    # Basic, non-streaming call to local Ollama using llama 3.2
    response = ollama.generate(
        model="llama3.2",
        prompt=prompt + "\nSummary:"
    )

    return response["response"].strip()
