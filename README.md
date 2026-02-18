# Jarvis – AI Voice Assistant (Python)

An AI-powered voice assistant built using Python that performs real-time speech recognition, web automation, music playback, news reading, and AI-powered conversations using OpenAI.

Inspired by Alexa and Google Assistant, Jarvis listens for a wake word and executes voice commands intelligently.

---

## Features

- Wake-word activation ("Jarvis")
- Speech Recognition (Google Speech API)
- Text-to-Speech (gTTS + Pygame)
- Open websites (Google, YouTube, Facebook, LinkedIn)
- Play music from custom music library
- Fetch latest news headlines (NewsAPI)
- AI-powered responses using OpenAI GPT
- Continuous listening loop

---

## System Architecture

Microphone Input  
→ Speech Recognition  
→ Command Processing  
→  
• Web Automation  
• Music Playback  
• News Fetching  
• AI Processing (OpenAI GPT)  
→ Text-to-Speech Output  

---

## Tech Stack

- Python
- SpeechRecognition
- gTTS
- Pygame
- OpenAI API
- Requests
- Webbrowser Module

---

## Project Structure


---

## Installation

### 1. Clone the Repository

```bash
git clone https://github.com/YOUR_USERNAME/jarvis-voice-assistant.git
cd jarvis-voice-assistant
```
### 2. Create Virtual Environment (Recommended)
python -m venv venv


Mac/Linux:

source venv/bin/activate


Windows:

venv\Scripts\activate

### 3. Install Dependencies
pip install speechrecognition pyttsx3 gtts pygame requests openai


If microphone issues occur:

pip install pyaudio

---

### API Keys Required

---

OpenAI API Key

Inside main.py:

client = OpenAI(api_key="YOUR_OPENAI_KEY")

News API Key
newsapi = "YOUR_NEWSAPI_KEY"


Get API keys from:

OpenAI: https://platform.openai.com

NewsAPI: https://newsapi.org

---

## How It Works

---

Wake Word Detection
Continuously listens for the word "Jarvis".

Command Routing
If predefined command → execute locally.
Else → send to OpenAI GPT model for intelligent response.

Music System
Uses dictionary-based mapping in musicLibrary.py:

music = {
    "calling": "YouTube link",
    "timeless": "YouTube link"
}


AI Processing
Uses OpenAI Chat Completion API for intelligent conversations.

### Learning Outcomes

Real-time speech processing

AI API integration

Event-driven programming

Text-to-speech systems

Voice command parsing

Third-party API integration

### Future Improvements

Add GUI interface

Add task scheduling

Add reminder system

Add weather API

Add email automation

Add system control commands

Package as desktop application

### Security Note

Do not hardcode API keys in public repositories.
Use environment variables instead:

Mac/Linux:

export OPENAI_API_KEY="your_key_here"


Windows:

setx OPENAI_API_KEY "your_key_here"


    - name: Check Python version
      run: python --version
