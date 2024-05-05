# csr

# import requests
#
# url = "https://conversational-speech-repository.p.rapidapi.com/api/conversational-speech-repository"
#
# payload = { "data": "Here is user's message. You need to determine whether or not it relates to finding dentist services or not. Here's the text: 'есть у кого знакомые работающие в стоматологии? кого можете посоветовать?', reply with python-style bool value (True, False), based on relation to finding dentist services." }
# headers = {
# 	"content-type": "application/x-www-form-urlencoded",
# 	"X-RapidAPI-Key": "c03b5a6c59msh0b3975b9f00603cp1fabb4jsnab2ec4808c05",
# 	"X-RapidAPI-Host": "conversational-speech-repository.p.rapidapi.com"
# }
#
# response = requests.post(url, data=payload, headers=headers)
#
# print(response.json())

# vertex gemini

# import vertexai
# from vertexai.generative_models import GenerativeModel, ChatSession
#
# # TODO(developer): Update and un-comment below lines
# project_id = "toothfairy-420511"
# location = "us-central1"
#
# vertexai.init(project=project_id, location=location)
# model = GenerativeModel("gemini-1.0-pro")
# chat = model.start_chat()
#
# def get_chat_response(chat: ChatSession, prompt: str) -> str:
#     text_response = []
#     responses = chat.send_message(prompt, stream=True)
#     for chunk in responses:
#         text_response.append(chunk.text)
#     return "".join(text_response)
#
# prompt = "Hello."
# print(get_chat_response(chat, prompt))
#
# prompt = "What are all the colors in a rainbow?"
# print(get_chat_response(chat, prompt))
#
# prompt = "Why does it appear when it rains?"
# print(get_chat_response(chat, prompt))


# pure gemini

API_KEY = "AIzaSyBIPclFco7P1lt85KM_mGIyp2Axvjut1dA"

import google.generativeai as genai
import os

genai.configure(api_key=API_KEY)

model = genai.GenerativeModel('gemini-pro')
response = model.generate_content('Hi!')

print(response.text)
