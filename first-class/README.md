# AI-Infused First Class

A collection of AI-powered web applications built with Gradio and LLM APIs. This project demonstrates practical use cases of large language models integrated with web scraping and interactive UIs.

## 📋 Project Overview

This repository contains three main applications:

### 1. **Website Summarizer** (`app.py`)
An AI-powered tool that scrapes website content and generates intelligent summaries using Groq's API.
- **Input**: Website URL
- **Output**: Markdown-formatted summary of website content
- **Features**: 
  - Automatic URL scheme detection
  - Intelligent HTML parsing and cleaning
  - LLM-powered content summarization
  - Web-based Gradio interface with shareable link

### 2. **LLM Arena** (`arena_app.py`)
An interactive comparison tool that pits two LLM models against each other.
- **Models**: OpenAI's GPT-4o-mini vs Groq's Llama 3.3-70b-versatile
- **Features**:
  - Side-by-side model response comparison
  - Voting system for user preference tracking
  - Real-time model battles
  - Web-based arena interface

### 3. **Groq API Demo** (`groq_call.py`)
A simple example demonstrating how to interact with Groq's API for question-answering tasks.

## 🛠️ Technologies Used

- **Python 3.x**
- **Gradio** - Web UI framework for ML applications
- **BeautifulSoup4** - HTML parsing and web scraping
- **Requests** - HTTP library for fetching web content
- **OpenAI Python SDK** - API client for both OpenAI and Groq (Groq uses OpenAI-compatible endpoints)
- **python-dotenv** - Environment variable management

## 📦 Installation

### Prerequisites
- Python 3.8 or higher
- API keys for:
  - OpenAI (for GPT-4o-mini in Arena)
  - Groq (for Llama models and summarization)

### Setup

1. **Clone the repository**
   ```bash
   git clone <repository-url>
   cd first-class
   ```

2. **Create a virtual environment**
   ```bash
   python -m venv .venv
   source .venv/bin/activate  # On Windows: .venv\Scripts\activate
   ```

3. **Install dependencies**
   ```bash
   pip install -r requirements.txt
   ```

4. **Configure environment variables**
   Create a `.env` file in the project root:
   ```
   OPENAI_API_KEY=your_openai_api_key_here
   GROQ_API_KEY=your_groq_api_key_here
   ```

## 🚀 Usage

### Website Summarizer
```bash
python app.py
```
- Opens a Gradio interface (typically at `http://localhost:7860`)
- Enter any website URL and get an AI-generated summary
- Click the link to share publicly

### LLM Arena
```bash
python arena_app.py
```
- Opens the LLM battle arena interface
- Enter a prompt and watch both models respond
- Vote for your preferred response using the 👍/👎 buttons

### Groq API Demo
```bash
python groq_call.py
```
- Demonstrates basic Groq API usage
- Answers travel-related questions using Llama 3.3-70b model

## 📁 Project Structure

```
.
├── app.py              # Website Summarizer Gradio app
├── arena_app.py        # LLM Arena battle interface
├── groq_call.py        # Groq API demonstration
├── scraper.py          # Web scraping utilities
├── summarizer.py       # Summarization logic
├── requirements.txt    # Python dependencies
└── README.md          # This file
```

## 🔧 Module Details

### `scraper.py`
- `fetch_website_contents(url)` - Fetches and cleans website content
  - Adds scheme if missing
  - Removes navigation, scripts, styles, and other noise
  - Returns clean text content with page title

### `summarizer.py`
- `summarize(url)` - Summarizes website content using Groq's Llama model
  - Uses the Qwen/Qwen3.8-27b model on Groq
  - Returns markdown-formatted summaries
  - Integrates scraper and LLM capabilities

## 🤖 Models Used

- **Summarization**: Groq - Qwen 3.8 27B
- **Arena Model A**: OpenAI - GPT-4o-mini
- **Arena Model B**: Groq - Llama 3.3-70b-versatile

## ⚙️ Configuration

### Custom System Prompts
Modify the `system_prompt` in `summarizer.py` to change summarization behavior.

### UI Customization
Adjust Gradio component parameters in the app files to customize appearance and behavior.

## 📝 API Rate Limits & Considerations

- Be mindful of API rate limits for both OpenAI and Groq
- Website scraping respects robots.txt and uses appropriate headers
- Gradio's `share=True` creates temporary public links (expires after 72 hours)

## 🐛 Troubleshooting

**Issue**: "Could not fetch the website" error
- Solution: Check URL format, ensure website is accessible, verify network connection

**Issue**: API key errors
- Solution: Verify API keys in `.env` file are correct and have appropriate permissions

**Issue**: Gradio port already in use
- Solution: Change the port in the app or close the application using that port

## 🔐 Security Notes

- Never commit `.env` files with API keys to version control
- API keys should be treated as secrets
- Keep dependencies updated regularly

## 📚 Resources

- [Gradio Documentation](https://www.gradio.app)
- [OpenAI API Documentation](https://platform.openai.com/docs)
- [Groq API Documentation](https://console.groq.com)
- [BeautifulSoup Documentation](https://www.crummy.com/software/BeautifulSoup)

## 📄 License

This project is provided as-is for educational and demonstration purposes.

## 🤝 Contributing

Feel free to fork, modify, and enhance these applications for your own use cases.