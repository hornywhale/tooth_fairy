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

input_string = """- https://t.me/belgradeitmeetups
- https://t.me/designers_serbia
- https://serbiainrussian.info/
- https://t.me/bg_basket
- https://t.me/SerbiaInMyMind
- https://t.me/RPGSerbia
- https://t.me/+sMXyzfPevbkyYzIy
- https://t.me/block61_71
- https://t.me/rus_BW
- https://t.me/rsbusines
- https://t.me/zarko_tusic
- https://t.me/beograd_service
- https://t.me/takemyrabbits
- https://t.me/kuce_beograd
- https://t.me/+sVat07GmZeJmYTAy
- https://t.me/rusloznica
- https://t.me/serbiarusman
- https://t.me/starigrad_belgrade
- https://t.me/rusrbfinance
- https://t.me/ru_zemun
- https://t.me/Serbia_GoTravel
- https://t.me/scammer_serbia
- https://t.me/tennis_serbia
- https://t.me/serbiaspecialists
- https://t.me/psysrb
- https://t.me/social_dancing_serbia
- https://t.me/vracar
- https://t.me/palilula
- https://t.me/pettrip
- https://t.me/serbia_jobs
- https://t.me/rus_nis
- https://t.me/belgrad_serbia
- https://t.me/+2UCmCgfbicQyNTBi
- https://docs.google.com/spreadsheets/d/1LDDsWT_H1KhilCA4F1uUsEy6_rknlQI9DSjlnb-PFEQ/edit#gid=0
- https://t.me/musicaSerbia
- https://t.me/vozdovac_ru
- https://t.me/youritjob
- https://t.me/it_serbia
- https://t.me/rabotavserbii
- https://t.me/photographic_belgrade
- https://t.me/living_zaedno_beo
- https://t.me/lekarstvaserbii
- https://t.me/alcoholic_belgrade
- https://t.me/serbskaj
- https://t.me/+6r67H3IEZ65hYzVi
- https://t.me/belgradewinerun
- https://t.me/serbia_self_it
- https://t.me/kragujevac_live
- https://t.me/dog040622
- https://t.me/belgrad_chat
- https://t.me/relocationguideserbia
- https://t.me/+MkBVbwBJsgUxOGVi
- https://t.me/+TFKZrUB_zjtkMDFk
- https://t.me/autoserbia
- https://t.me/+yWzEAFJxSfZlOTdi
- https://t.me/snowserbia
- https://t.me/zhenskaja_rs
- https://t.me/stroika_srbija
- https://t.me/reuse_beograd
- https://t.me/vrachivserbii
- https://t.me/handmade_serbia
- https://t.me/avito_serbia
- https://t.me/specialistibelgrad
- https://t.me/nis_serbia_ru_ua_by
- https://t.me/veganbelgrade
- https://t.me/+aSvfaV2KXmhiMjU0
- https://t.me/+XdxQEEFLBb00MzEy
- https://t.me/begbezdurakov
- https://t.me/girlsinserbia
- https://t.me/immi_gration
- https://t.me/belgrade_boardgames
- https://t.me/srbija_deca
- https://t.me/rentserbiarus
- https://t.me/vozdovac_chat
- https://t.me/rabota_serbia
- https://t.me/golubmiru
- https://t.me/RU_Sombor
- https://t.me/rodjenje_serbia
- https://t.me/fz_belgrad
- https://t.me/mapamagrus
- https://t.me/novibeogradrusski
- https://t.me/serbska_baraholka
- https://t.me/sta_imas_beograd
- https://t.me/beogradsadecom
- https://t.me/russiansubotica
- https://t.me/beoqviz
- https://t.me/Belgrad_Chat_Go
- https://t.me/poputchiki_serbia
- https://t.me/RDO_Serbia
- https://t.me/serbocoin
- https://t.me/BussinesSerbia
- https://t.me/srpski5min
- https://t.me/Rus_zvezdara
- https://t.me/belgrade_school_chat
- https://docs.google.com/document/d/1HvDtWyaUu6MMkD41wA-l1htoIKyF36_ea_j0LeNZbus/edit?usp=sharing
- https://t.me/serbskiyslivarik_v_kartinkah
- https://t.me/sealkia_tea
- https://t.me/beograd_service
- https://stomatolog-novisad.ru/
- https://t.me/yutniycatik
- https://t.me/mastermaindbelgrade
- http://t.me/novisad_alky
- https://t.me/natali_bakery_ns
- https://t.me/photographic_belgrade
- https://t.me/kontaktnovisad
- https://t.me/designers_serbia
- https://www.google.com/maps/d/u/0/viewer?mid=12l4BVYg_FV0d9CMeEWEtnJDQioL9
- https://t.me/balkanoutdoor
- https://t.me/novisad_basketball
- https://t.me/belgradewinerun
- https://t.me/ChatforBelgradd
- https://t.me/beogradsadecom
- https://t.me/visarunserb
- https://t.me/politics_conspirology
- https://t.me/mikhail_in_serbia
- https://serbiainrussian.info/
- https://t.me/KidsLab_chat
- https://t.me/slovodnia
- https://eliksirkaluga.com/
- https://t.me/ods_ns
- https://pillintrip.com/ru
- https://t.me/postupim_v_Univer_in_Serbia
- https://t.me/nenevreme
- https://t.me/tvojdrugserb
- https://t.me/fz_belgrad
- https://t.me/VisaRunBg
- https://t.me/kniznyjsad
- https://t.me/visa_run_serbia
- https://t.me/+yGkZBKXzpO5jZWRi
- https://t.me/rus_nis
- https://t.me/+Gsjk4T_q61llNDBi
- https://t.me/valjevors
- https://t.me/vrnjackabanja
- https://t.me/standup_beo
- https://t.me/palilula
- https://t.me/serbocoin
- https://t.me/begbezdurakov
- https://mediately.co/rs/
- https://t.me/visarun_NoviSad
- https://docs.google.com/document/d/1buubJt3W8JizcUqiKo7Sfm88K_8i1C8hrAevTTJupMo/edit
- https://t.me/zarko_tusic
- https://t.me/+2UCmCgfbicQyNTBi
- http://t.me/novisadaily
- https://t.me/+XdxQEEFLBb00MzEy
- https://t.me/+N94hIXb8ufVhMTI6
- https://sveuredu.rs/ru
- https://t.me/rodjenje_serbia
- https://t.me/+0H0JEWVm78piMDYy
- https://t.me/social_dancing_serbia
- https://t.me/settler_serbia
- https://t.me/KoshatnikiNoviSad
- https://t.me/sta_imas_beograd
- https://t.me/kralevo
- https://www.google.com/maps/d/u/0/viewer?mid=12l4BVYg_FV0d9CMeEWEtnJDQioL9804&ll=44.81404374354849%2C20.462787317997474&z=14
- https://t.me/serbiaManufacture
- https://t.me/chast_rechi_school
- https://t.me/BussinesSerbia
- https://docs.google.com/document/d/1UlOkmqrgUvvrQoHT5aZXsb73CEsfjF8_Nhsm-6n96yI
- https://www.alims.gov.rs/medicinska-sredstva/pretrazivanje-medicinskih-sredstava/
- https://t.me/VamZdesNeTut
- https://t.me/serbiaspecialists
- https://t.me/shmel_rs
- https://www.srb.guide
- https://t.me/starigrad_belgrade
- https://t.me/sosedi_cacak
- https://t.me/rus_BW
- https://t.me/ourserbia
- https://t.me/srb_drones
- https://t.me/designovisad
- https://t.me/srb_product
- http://t.me/+WJPxpZQPeXVkMTA8
- https://t.me/rabotavbelgrade
- https://t.me/vrachivserbii
- https://t.me/CleaningNoviSad
- https://t.me/+8A-2wEweJBM1MDE0
- https://t.me/teainserbia
- https://t.me/belgrade_in_blue
- https://t.me/snimaem_kvartiru_vmeste
- https://t.me/serbska_baraholka
- https://t.me/sosedskizlatibor
- https://drsljapic.com
- http://www.panakeia.rs/
- https://t.me/belyaevs_in_serbia
- https://t.me/n1inforu
- https://t.me/srbija_deca
- https://t.me/elena_ryba_v_Serbia
- https://t.me/qigong_beo
- https://t.me/kids_goods_bg
- https://t.me/lekarstvaserbii
- https://t.me/Capoeira_rs
- https://t.me/thehappywizardns
- https://t.me/serbia4rent
- https://t.me/CashFlowBelgrade
- https://t.me/+tAl4k_Fm-MZjNGQy
- https://t.me/boltns
- https://t.me/petsmoving
- https://t.me/beograd_stan
- https://t.me/serbian_citizenship
- https://t.me/novisad_stan
- https://t.me/srdmedia
- https://t.me/girlsinserbia
- https://t.me/immi_gration
- https://t.me/+OnUykRmpUtg5MGFi
- https://t.me/serbia_chat
- https://t.me/+qyDpgDflTTc1ZjYy
- https://t.me/odnazhdy_v_serbii
- https://t.me/nis_serbia_ru_ua_by
- https://t.me/novi_sad_parents
- https://t.me/stroika_srbija
- https://t.me/eda_rs
- https://t.me/o_serbii
- https://t.me/swalle_serbia
- https://t.me/veloserbia
- https://t.me/garbage_bag_Novi_sad
- https://t.me/izlet_novi_sad
- https://docs.google.com/document/d/1HvDtWyaUu6MMkD41wA-l1htoIKyF36_ea_j0LeNZbus/edit
- https://t.me/deathdoomserbia
- https://t.me/IT_Belgrade
- https://t.me/relogame_serbia
- https://t.me/zurka_novisad-
- http://t.me/novisad_football
- https://t.me/SerbiaBelarus
- https://t.me/+BUscUPeORGtjNGY6
- Chast-rechi.com
- https://t.me/tennis_serbia
- https://t.me/vyshee_obrazovanie_v_Serbii
- https://t.me/rusrbfinance
- https://t.me/teaclubnsserbia
- https://t.me/+5V0BZUlqinFjNjgy
- https://t.me/vkusnosti_beograd
- https://t.me/v_kamensky
- https://pillintrip.com/ru/
- https://t.me/ru_zemun
- https://t.me/ambiance_nis
- https://t.me/autoserbia
- https://t.me/novisad_apartmens
- https://t.me/+jtO-m08zzMJmZWVi
- https://t.me/dog040622
- https://t.me/P2p4rusi
- https://t.me/serbia_self_it
- https://t.me/+_3qeauboJ-djMzFk
- https://t.me/zhenskiclub_bg
- https://t.me/+llAGYPdR7TYyZDQy
- https://t.me/osetiaserbia
- https://t.me/specialistinovisada
- https://t.me/mafia_novisad
- https://t.me/transfer_ns
- Mefody.org
- https://t.me/WordsOutOfBounds
- https://t.me/vracar
- https://t.me/snowserbia
- https://t.me/rabotavserbii
- https://t.me/cgserbia
- https://t.me/it_serbia
- https://t.me/visarun_tours
- https://t.me/sns_serbia
- https://t.me/belgradeitmeetups
- https://t.me/+MkBVbwBJsgUxOGVi
- https://t.me/parents_little_kids_NoviSad
- http://t.me/generozova_s
- https://t.me/kuce_beograd
- https://t.me/youritjob
- https://t.me/vmeste_events
- https://t.me/ns_boardgame
- https://t.me/rabota_serbia
- https://t.me/oncraftinnovisad
- https://t.me/+jj9JD2n_SFJmNTI8
- https://t.me/talantserbia
- https://t.me/relocateserbia
- https://t.me/+ygWgXAID-eIwM2Vi
- https://t.me/otzovik_serbia
- https://t.me/hustleinSerbia
- https://t.me/logistika021
- https://t.me/ballet_serbia_russo
- https://t.me/history_dance_Beograd
- https://t.me/RDO_Serbia
- https://t.me/lekarstva_v_serbii
- https://t.me/DVA_MEDVEDA
- https://t.me/rsdrivers
- https://t.me/block61_71
- https://t.me/beoqviz
- https://t.me/serbiawork
- https://t.me/serbskaj
- https://t.me/tattooroy_rs
- https://t.me/serbskiyslivarik_v_kartinkah
- https://t.me/catalog_russpeaking_serbia
- https://t.me/boardgames_ns
- https://docs.google.com/document/d/134xD-72zMy458j4Tv-RWOnRIgYB-fwUAjkIrh-TCmxM/edit
- https://t.me/RU_Sombor
- https://t.me/serbiadatingrus
- https://t.me/vstrechi_v_belgrade
- https://t.me/rentalserbia
- https://t.me/rsbusines
- https://t.me/zajednovserbii
- https://t.me/serbiya_arenda
- https://t.me/serbiapc
- https://t.me/vozdovac_ru
- https://t.me/belgradmuseum
- https://t.me/+a_Kb-FKD-tM0Y2Ri
- https://t.me/handmade_serbia
- https://t.me/bg_basket
- https://t.me/profmasazbeograd
- https://t.me/+-fYKE8oZGjsyZWEy
- https://t.me/amelin917
- https://t.me/Hikaon
- https://t.me/izbashkiriivserbiu
- https://t.me/nashi_v_zrenjanine
- https://t.me/kidsCodingBelgrade
- https://t.me/escapeinbelgrade
- https://t.me/+Cm_ikyupPDQ4ZDdi
- https://t.me/+aSvfaV2KXmhiMjU0
- https://t.me/ptica_story
- https://t.me/serbia_exchange_rates
- https://t.me/belgrade_boardgames
- https://t.me/novisad_pref
- https://t.me/teamdesigninteriors
- https://t.me/coworkingNS
- https://t.me/novi_sad_serbia
- https://t.me/dunavspot_chat
- https://t.me/musicaSerbia
- https://t.me/PriceNaNoC
- https://t.me/belgrad_serbia
- https://t.me/business_breakfast_NS
- https://t.me/belgrad_chat
- https://t.me/specialistibelgrad
- http://t.me/nssportchat
- https://docs.google.com/spreadsheets/d/1LDDsWT_H1KhilCA4F1uUsEy6_rknlQI9DSjlnb-PFEQ/edit#gid=0
- https://t.me/risuem_novi_sad
- https://t.me/dogsns
- https://t.me/SerbianFlatCallerBot
- https://t.me/kragujevac_live
- https://t.me/RPGSerbia
- https://t.me/serbia_jobs
- https://t.me/yoga_novisad
- http://mefody.org/
- https://t.me/universal_serbia_novisad
- https://t.me/becreating
- https://t.me/chatsrbhr
- https://t.me/novisad_ru
- https://t.me/novibeogradrusski
- https://t.me/nsautochat
- https://t.me/serbia_iliqchuan
- https://t.me/Tourserbia
- https://t.me/getparcelbot
- https://t.me/suboticaRU
- https://t.me/dunav2
- http://t.me/+VbgOO7pcyhdhNGM0
- https://t.me/interiorserbia
- https://www.rfzo.rs/index.php/osiguranalica/lekovi-info/lekovi-actual
- https://t.me/vozdovac_chat
- https://www.paragraf.rs/propisi/lista-lekova-koji-se-izdaju-bez-lekarskog-recepta-koji-se-
- https://profi.ru/profile/LarichkinaES/
- https://goo.gl/maps/vWEuF3RTHDGaGgRe6
- https://t.me/hloyastore
- https://t.me/qazchange
- https://t.me/concertsrb
- https://t.me/kvartiranovisad
- https://docs.google.com/document/d/1KwNS7gXDPgiUPy36Cv3mvkWlbxkICFMx1_5Ei0yJBtM
- https://t.me/psysrb
- https://t.me/serbianforcajniks
- https://t.me/Vmeste_Serbia
- https://t.me/SrpskiCas
- https://t.me/gorki_list
- https://russian.rs/
- https://docs.google.com/document/d/1UlOkmqrgUvvrQoHT5aZXsb73CEsfjF8_N
- https://t.me/repair_service_Serbia
- https://t.me/vinkolozic
- https://t.me/tea_environment
- https://t.me/SrbijaVizarun
- https://t.me/visarun_serbia
- https://t.me/+sMXyzfPevbkyYzIy
- https://t.me/serbiarusman
- https://t.me/zurka_novisad
- https://t.me/lucas_on_tour
- https://t.me/russiansubotica
- https://t.me/srpski5min
- t.me/novi_sad_parents
- https://t.me/serbianwine
- https://t.me/chgk_u_bg
- https://t.me/SrbMarket
- https://t.me/golubmiru
- https://t.me/+TFKZrUB_zjtkMDFk
- https://t.me/triponSerbia
- https://t.me/SerbiaInMyMind
- https://t.me/serbia_portugal
- https://www.paragraf.rs/propisi/lista-lekova-koji-se-izdaju-bez-lekarskog-recepta-koji-se-mogu-reklamirati.html
- https://t.me/art_beograd
- https://t.me/alexproquiz
- https://masterus.org
- https://t.me/people3e
- https://t.me/kulturno_druzenje
- https://t.me/+kUkFBZAfAeE0YjFi
- https://t.me/doctor_stomatologich
- https://t.me/motoserbia
- https://t.me/+T9GMqqQEwsU0Y2Q6
- https://t.me/serbia_progulki
- https://t.me/belgrade_school_chat
- https://t.me/salesinserbia
- https://t.me/+dzYBVRHKtPdhMjZk
- https://t.me/+8r-UqKxIBsFjYjBi
- https://t.me/novisadarenda
- https://t.me/alcoholic_belgrade
- https://t.me/gripsoundlab
- https://t.me/+OZDR_T_sUiczODgy
- https://t.me/letsmeetbelgrade
- https://t.me/ursaschool
- https://docs.google.com/document/d/1KwNS7gXDPgiUPy36Cv3mvkWlbxkICFMx
- https://t.me/tennis_novisad
- https://t.me/mapamagrus
- https://Masterus.org
- https://t.me/+0toXyPPvcp8zNTg1
- https://t.me/avito_serbia
- https://t.me/DVA_MEDVEDA_DnD
- https://t.me/rusloznica
- https://t.me/desireappBot
- https://t.me/Rus_zvezdara
- https://t.me/+iu8DfYn_qBViOGVi
- https://t.me/kolekcija
- https://goo.gl/maps/nDYdJVe6PEo7A6cM6
- https://t.me/+6V3F9ImACfthNjNi
- https://t.me/novisad_events
- https://t.me/+RTbs1gvNVyczNDdi
- https://t.me/living_zaedno_beo"""

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


@app.on_message(filters.chat([_["id"] for _ in config["chats_serbia"]]))
async def parser(client, message: types.Message):
    # pure conditional matching
    try:
        if message.text is not None:
            for word in message.text.split(" "):
                word = "".join(_ for _ in word if _.isalpha())
                if analyzer.parse(word)[0].normal_form in KEYWORDS:
                    chat_id = message.chat.id
                    chat_link = None
                    chat_name = None
                    for el in config["chats_serbia"]:
                        if el["id"] == chat_id:
                            chat_link = el["link"]
                            chat_name = el["title"]
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
        print(f"Something just happened... {e}")
        error = f"{e}"
        if "wait" in error:
            wait = int(error[error.find("A wait of ") + 10:error.find("seconds")])
            sleep(wait)
        sleep(5)

app.run()