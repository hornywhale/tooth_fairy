from pyrogram import Client, filters, types
from json import load, dump
from pymorphy2 import MorphAnalyzer
import asyncio
import openai
from time import sleep

config = []


def load_config():
    global config
    with open("config.json", "r") as json_file:
        config = load(json_file)


load_config()

user_id = 1

# if len(config["users"]) > 1:
#     print("Choose user:")
#     for i in range(len(config["users"])):
#         user = config["users"][i]
#         print(f"{i}. {user['name']}")
#     user_id = int(input("Input account's id: \n"))

API_ID = config["users"][user_id]["API_ID"]
API_HASH = config["users"][user_id]["API_HASH"]
SUPER_ID = config["SUPER_ID"]
print(config["users"][user_id])

KEYWORDS = config["keywords"]
OPENAI_KEY = config["OPENAI_KEY"]
app = Client("my_account", API_ID, API_HASH)
analyzer = MorphAnalyzer()
openai_client = openai.OpenAI(api_key=OPENAI_KEY)

input_string = """t.me/oogaboogauzbek"""

links = set()

for link in input_string.split("\n- "):
    links.add(link)

links = list(links)
print(links)


@app.on_message(filters.command("lic", prefixes="."))
async def get_chat_id(client, message: types.Message):
    for link in links:
        try:
            if "t.me" in link:
                link = link[link.find("t.me") + 5 if "+" not in link else link.find("t.me"):]
                load_config()
                flag = False
                for el in config["chats_serbia"]:
                    if el["link"] == link:
                        print(f"Skipped chat {link}")
                        flag = True
                if not flag:
                    print(f"Trying to join chat {link}")
                    chat = await app.join_chat(link)
                    print(f"Successfully joined chat {chat.title} with id {chat.id}")
                    config["chats_serbia"].append({"link": link, "id": chat.id, "name": chat.title})
                    with open("config.json", "w+") as json_file:
                        dump(config, json_file, indent=2)
                    sleep(5)
        except Exception as e:
            print(f"Something just happened... {e}")
            error = f"{e}"
            if "wait" in error:
                wait = int(error[error.find("A wait of ") + 10:error.find("seconds")])
                sleep(wait)
            sleep(5)


@app.on_message(filters.command("id", prefixes="."))
def get_chat_id(client, message: types.Message):
    chat_id = message.chat.id
    link = message.chat.invite_link
    title = message.chat.title
    app.delete_messages(chat_id, message.id)
    app.send_message("me", f"New chat scanned:\ntitle: {title}\nid: `{chat_id}`\nlink: "
                           f"{f'`{link}`' if link is not None else 'link is not available'}")


@app.on_message(filters.command("idw", prefixes="."))
def get_chat_id(client, message: types.Message):
    chat_id = message.chat.id
    link = message.chat.invite_link
    title = message.chat.title
    app.delete_messages(chat_id, message.id)
    app.send_message("me", f"New chat scanned:\ntitle: {title}\nid: `{chat_id}`\nlink: "
                           f"{f'`{link}`' if link is not None else 'link is not available'}")
    try:
        chat_info = {
            "link": link,
            "id": chat_id,
            "title": title
        }
        if chat_info not in config["chats_serbia"]:
            config["chats_serbia"].append(chat_info)
            with open("config.json", "w+") as json_file:
                dump(config, json_file, indent=2)
            app.send_message("me", "Added new chat successfully!")
        else:
            app.send_message("me", "Chat is already added to config!")
    except Exception as error:
        app.send_message("me", f"Unfortunately, an error occurred while adding new chat to configuration, "
                               f"here's an error message: {error}")


# print([_["id"] for _ in config["chats_serbia"]])
# @app.on_message(filters.chat([_["id"] for _ in config["chats_serbia"]]))
@app.on_message()
async def parser(client, message: types.Message):
    # pure conditional matching
    try:
        if message.chat.id in [_["id"] for _ in config["chats_serbia"]] and message.text is not None:
            for word in message.text.split(" "):
                word = "".join(_ for _ in word if _.isalpha())
                if analyzer.parse(word)[0].normal_form in KEYWORDS:
                    chat_id = message.chat.id
                    chat_link = None
                    chat_name = None
                    for el in config["chats_serbia"]:
                        if el["id"] == chat_id:
                            chat_link = el["link"]
                            chat_name = el["name"]
                            break
                    method = "#conditional"

                    content = f"Here is user's message. You need to determine whether or not it relates to " \
                              f"finding dentist services or not. Here's the text: '{message.text}', " \
                              f"reply with python-style bool value (True, False), based on relation " \
                              f"to finding dentist services."
                    print(message.text)
                    completion = openai_client.chat.completions.create(
                        model="gpt-3.5-turbo",
                        messages=[
                            {"role": "system",
                             "content": "You are smm bot assistant."},
                            {"role": "user",
                             "content": content}
                        ]
                    )
                    print(completion.choices[0].message.content)
                    if completion.choices[0].message.content == "True":
                        method = "#ai"
                    text = f"Got new message from {message.from_user.first_name} @{message.from_user.username}, " \
                           f"telegram id: {message.from_user.id}\n" \
                           f"Sender link: {f'tg://user?id={message.from_user.id}'}\n" \
                           f"Message text: {message.text}\n" \
                           f"Chat: {chat_name if chat_name is not None else 'chat name is not availible'}, " \
                           f"link: {chat_link if chat_link is not None else 'chat link is not availible'}\n" \
                           f"Parsed by: {method}"
                    await app.send_message(chat_id=SUPER_ID, text=text)
    except Exception as e:
        await app.send_message(chat_id=SUPER_ID, text=f"Something just happened... {e}")
        print(f"Something just happened... {e}")
        error = f"{e}"
        if "wait" in error:
            wait = int(error[error.find("A wait of ") + 10:error.find("seconds")])
            sleep(wait)
        sleep(5)

app.run()
