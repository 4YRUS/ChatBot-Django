

import os
import google.generativeai as genai

genai.configure(api_key="AIzaSyB6kB-C0ommc3IpbIE0OAUsfIKGTGhxO6k")

# Create the model
def chat(text):
	generation_config = {
	  "temperature": 1,
	  "top_p": 0.95,
	  "top_k": 40,
	  "max_output_tokens": 8192,
	  "response_mime_type": "text/plain",
	}

	model = genai.GenerativeModel(
	  model_name="gemini-1.5-flash",
	  generation_config=generation_config,
	)

	chat_session = model.start_chat(
	  history=[
	  ]
	)

	response = chat_session.send_message(text)
	return response.text
	


def send_chat(text):
	try : 
		message = chat(text)
		print(message)
		return message
	except:
		return None
if __name__=="__main__":
	send_chat("HELLO GOOGLE HOW ARE YOU ??")
