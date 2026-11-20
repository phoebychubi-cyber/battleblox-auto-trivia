import requests, asyncio, time
import cloudscraper as cs
from gemini import Gemini

# auto trivia for battleblox.gg

auth = "Your discord auth token"
# used for getting message and sending message in discord

google_api_key = "Your google gemini api key"
# used to get answers from gemini AI

headers = {
  "Sec-Ch-Ua": "\"Chromium\";v=\"137\", \"Not/A)Brand\";v=\"24\"",
  "Sec-Ch-Ua-Mobile": "?1",
  "Sec-Ch-Ua-Platform": "\"Android\"",
  "Sec-Fetch-Dest": "empty",
  "Sec-Fetch-Mode": "cors",
  "Sec-Fetch-Site": "same-site",
  "User-Agent": "Mozilla/5.0 (Linux; Android 10; K) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/137.0.0.0 Mobile Safari/537.36"
}

gemini = Gemini(google_api_key)

questions = []

async def send_to_discord(answer):
  scrape = cs.create_scraper()
  data = {
    "mobile_network_type": "wifi",
    "content": answer,
    "nonce": str(time.time_ns() // 1_000_000),
    "tts": False,
    "flags": 0
  }
  dcheaders = headers.copy()
  dcheaders["Origin"] = "https://discord.com"
  dcheaders["Referer"] = "https://discord.com/"
  dcheaders["Authorization"] = auth
  r = scrape.post("https://discord.com/api/v9/channels/1541816227700285591/messages",headers=dcheaders,json=data).json()
  print(r)
    
async def do_trivia(message):
  response = gemini.ask(message)
  print(response)
  if len(response) <= 15:
    await send_to_discord(response)
    
async def main():
  global questions
  scrape = cs.create_scraper()
  dcheaders = headers.copy()
  dcheaders["Origin"] = "https://discord.com"
  dcheaders["Referer"] = "https://discord.com/"
  dcheaders["Authorization"] = auth
  while True:
    try:
      messages = scrape.get("https://discord.com/api/v9/channels/1541816227700285591/messages?limit=3",headers=dcheaders).json()
      for message in messages:
        for embed in message.get("embeds", []):
          description = embed.get("description")

          if description:
            if description not in questions:
              print(description)
              await do_trivia(description)
              questions.append(description)
    except Exception as e:
      print(e)
    await asyncio.sleep(2)

asyncio.run(main())