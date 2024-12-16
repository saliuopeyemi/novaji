import google.generativeai as genai
import pathlib
import json

with open("apikey.json","r") as file:
	key = json.load(file)


def response(q):
	genai.configure(api_key=key)

	# for item in genai.list_models():
	# 	print(item.name)

	model = genai.GenerativeModel("gemini-1.5-pro-001")

	response = model.generate_content(q)

	text = str(response.parts[0])

	return text

print(response("Who is Donald Trump?"))

def retrieve_feeds(url)