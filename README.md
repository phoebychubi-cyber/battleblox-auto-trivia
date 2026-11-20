# Auto trivia for battleblox.gg

A lightweight script to automatically answer trivia questions to earn free money

Open Source & Transparency: The entire source code is publicly available for inspection. Feel free to review the files and verify exactly what the script does before running it. No need to take my word for it — you're welcome to audit the code yourself.

## Made by leaftify
contact for business purposes
discord: @leaftify.dev
gmail: phoebychubi@gmail.com

## Installation

```bash
pip install -r requirements.txt
```

## Quick Start

```python
python3 main.py
```

## Features

- Simple Gemini API integration
- Custom model selection
- Request timeout handling
- HTTP error handling
- Lightweight and easy to use

## Requirements

- Python 3.9+

## Configuration

You need discord account token and google gemini api key

```python
auth = "Your discord auth token"
# used for getting message and sending message in discord

google_api_key = "Your google gemini api key"
# used to get answers from gemini AI
```

Security Notice: Never share your authentication token or API key. Avoid committing credentials to public repositories.

## License

This project is licensed under the MIT License.
