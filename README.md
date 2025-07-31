# Chat Summary Generator using Llama 3.2 (Ollama) in Django

This project provides a Django REST API that accepts user and bot chat messages and returns a one-line summary using **Llama 3.2 model via Ollama**   

No external API key is required because Ollama runs locally and does not use OpenAI’s API.

## 1. Setup Instructions

### Requirements
- Python 3.10+
- Django 5+
- Django REST Framework
- Ollama installed locally (for Llama 3.2)

### Installation

```bash
# Clone repo
git clone https://github.com/amit-223/chat-summary-generator.git
cd chat-summary-generator

# Create virtual environment
python -m venv myenv
source venv/bin/activate  # Windows: venv\Scripts\activate

# Install dependencies
pip install -r requirements.txt

# Run Ollama locally
ollama run llama3.2  # make sure Ollama is installed and model is available

# Run Django server
python manage.py runserver
```

Issues with OpenAI API Key (FYI)
Originally, I tried using OpenAI's GPT API (gpt-3.5-turbo), but:
It required an API key, and I hit token limit/quota errors during testing.
To avoid these issues, I switched to Llama 3.2 via Ollama which runs locally and is free to use.

### API Endpoint:
POST /api/summarize/

```bash
Example 1: Sample Request
{
  "chat": [
    {"role": "user", "message": "I forgot my password."},
    {"role": "bot", "message": "No problem, I can send you a reset link."}
  ]
}
Response:
{
  "summary": "User requested a password reset and the bot offered to send a link."
}
```

Finally, All requests & responses are logged in requests.log file in the project root folder.

Thank you.
