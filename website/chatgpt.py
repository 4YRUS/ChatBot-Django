from openai import OpenAI
import os

client = OpenAI(api_key='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')

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