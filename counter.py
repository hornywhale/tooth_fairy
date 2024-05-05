from json import load

with open("config.json", "r") as json_file:
    config = load(json_file)

print(len(config["chats_serbia"]))