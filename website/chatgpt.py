from openai import OpenAI
import os

client = OpenAI(api_key='ENTER YOUR CHAT API HERE')

def chat(text):
	completion = client.chat.completions.create(
		model="gpt-3.5-turbo",
		messages=[
		{"role": "user", "content": text}
		]
	)

	return completion.choices[0].message

def send_chat(text):
	try : 
		return chat(text)
	except:
		return None
