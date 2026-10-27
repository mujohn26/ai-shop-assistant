import os
import json

from dotenv import load_dotenv
from openai import OpenAI
from pathlib import Path

BASE_DIR = Path(__file__).parent

system_prompts = (BASE_DIR / "prompts" / "system.txt" ).read_text(encoding="utf-8")

with open(BASE_DIR / "data" / "products.json", encoding="utf-8") as f:
	products = json.load(f)



load_dotenv(override=True)
groq_base_url = "https://api.groq.com/openai/v1"
GPT_MODEL = "openai/gpt-oss-120b"
api_key = os.getenv("GROQ_API_KEY")

groq = OpenAI(api_key=api_key, base_url= groq_base_url )


def find_relevant_products(message,products, limit=30):
	words = [w for w in message.lower().split() if len(w)>2]
	scored = []
	for p in products:
		text = f"{p['name']} {p['brand']} {p['category']} {p['gender']} {' '.join(p['colors'])} {p['material']}".lower()
		score = sum(w in text for w in words)
		if score:
				scored.append((score, p))
	scored.sort(key=lambda x: x[0], reverse=True)
	return [p for _, p in scored[:limit]]




def chat(message, history):
	history = [{"role": h['role'], "content": h['content']} for h in history]
	relevant_message = (
		f"{system_prompts}\n\n"
		f" Here is the store products in json {json.dumps(find_relevant_products(message,products), indent=2)}\n\n"
		)
	if "belt" in message.lower():
		relevant_message += "The store does not sell belts; if you are asked for belts be sure to point out other items on sale"

	messages = [{"role": "system", "content": relevant_message }] +  history + [{"role": "user", "content": message}] 
	streams = groq.chat.completions.create(model=GPT_MODEL, messages=messages, stream=True)
	result = ""

	for chunk in streams:
		result+= chunk.choices[0].delta.content or ""
		yield result