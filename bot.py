from vk_api.bot_longpoll import VkBotLongPoll, VkBotEventType 
from vk_api.keyboard import VkKeyboard
from messages import *
import vk_api, json, time, random, re


qwe=0
ft=0

with open('login.txt') as login:
     token, gr_id=[line.strip() for line in login]
     gr_id=int(gr_id)

def sendmess(msg):
    #отправляет сообщение
    if type(msg)==list:
        msgtxt=random.choice(msg)
    elif type(msg)==str:
        msgtxt=msg
    else:
        msgtxt=str(msg)
    if event.from_user:
        vk.messages.send(peer_id=event.obj.peer_id, message=msgtxt, random_id=random.randint(1, 2147483647), keyboard=menu)
    else:
        vk.messages.send(peer_id=event.obj.peer_id, message=msgtxt, random_id=random.randint(1, 2147483647), keyboard=None)

def chkmsg(msg, txt):
    #проверяет, есть ли $msg в $txt
    msgtxt=msg.replace("[tlachatbot|@tlachatbot] ", "")
    for s in txt:
        if s==msgtxt.lower():
            return True
            break


vk_session = vk_api.VkApi(token=token)

#interface 
menu = VkKeyboard()

menu.add_button(label="qwe", color="positive")
menu.add_button(label="42", color="negative") 

menu.add_line()

menu.add_button(label="Кто такой IAmTagir?")
menu.add_button(label="TLA это") 

menu.add_line()

menu.add_button(label="TeamRun это",)             
menu.add_button(label="Ссылки", color="primary")

menu.add_line()

menu.add_button(label="Про героев TLA")

menu.add_line()

menu.add_button(label="Про TLA1")
menu.add_button(label="Про TLA2")

menu.add_line()

menu.add_button(label="Про TLA3")
menu.add_button(label="Про TLA4")

menu.add_line()

menu.add_button(label="Про TLA5")
menu.add_button(label="Про бота")

menu = menu.get_keyboard()

vk_session = vk_api.VkApi(token=token)
vk = vk_session.get_api()
longpoll = VkBotLongPoll(vk_session, gr_id)

print('logged in')

while True:
    for event in longpoll.listen():
        if event.type == VkBotEventType.MESSAGE_NEW and event.obj.text:
            messagetext=event.obj.text.strip()
            try:      
                if chkmsg(messagetext, ["кто такой тагир?", "кто такой тагир", "кто такой iamtagir?", "кто такой iamtagir"]):
                    sendmess(iamtagir)
                    print('iamtagir')
                elif chkmsg(messagetext, ["команды","помощь"]):
                    sendmess(help)
                    print('help')
                elif chkmsg(messagetext, ["привет","ghbdtn","здравствуйте"]):
                    sendmess("здрасьте")
                    print('hello')
                elif chkmsg(messagetext, ["пока","gjrf","до свидания"]):
                    sendmess('Пока(')
                    print('goodbye')
                elif chkmsg(messagetext, ["что такое тимран","что такое тимран?","что такое teamrun?","что такое teamrun","teamrun это","тимран это"]):
                    sendmess(teamrun)
                    print('tr')
                elif chkmsg(messagetext, ["tla это","тла это","что такое тла?","что такое tla?","что такое тла","что такое tla"]):
                    sendmess(tla)
                    print('tla')
                elif chkmsg(messagetext, ["про тла1","про tla1","про тла 1","про tla 1"]):
                    sendmess(tla1)
                    print('tla1')
                elif chkmsg(messagetext, ['про tla2', 'про тла2', 'про tla 2', 'про тла 2']):
                    sendmess(tla2)
                    print('tla2')
                elif chkmsg(messagetext, ["про тла3","про tla3","про тла 3","про tla 3"]):
                    sendmess(tla3)
                    print('tla3')
                elif chkmsg(messagetext, ["про тла4","про tla4","про тла 4","про tla 4"]):
                    sendmess(tla4)
                    print('tla4')
                elif chkmsg(messagetext, ["про тла5","про tla5","про тла 5","про tla 5"]):
                    sendmess(tla5)
                    print('tla5')
                elif chkmsg(messagetext, ["кто такой афоня","кто такая изольда","кто такой афоня?","кто такая изольда?","про афоню","про изольду","про героев тла","про героев tla"]):
                    sendmess(heroes)
                    print('heroes')
                elif chkmsg(messagetext, ["ссылки"]):
                    sendmess(links)
                    print('links')
                elif chkmsg(messagetext, ["про бота", "про tlabot"]):
                    sendmess(about)
                    print('about')
                elif chkmsg(messagetext, ["qwe"]):
                    qwe+=1
                    ft-=1
                    if event.from_user==True:
                        sendmess(f'за qwe: {qwe}; за 42: {ft} ;')
                        print('qwe')
                        if qwe%100==0 and qwe!=0:
                                sendmess('Вы юбилейный qwe!')
                                print('qwe100')
                                if qwe>=100:
                                    sendmess('qwe выиграли!')
                                    qwe=0
                                    ft=0
                elif chkmsg(messagetext, ["42"]):
                    ft+=1
                    qwe-=1
                    if event.from_user==True:
                        sendmess(f'за qwe: {qwe}; за 42: {ft};')
                        print('ft')
                        if ft%100==0 and ft!=0:
                                sendmess('Вы юбилейный 42!')
                                print('ft100')
                                if ft>=100:
                                    sendmess('эээ виграли!')
                                    qwe=0
                                    ft=0
                else:
                    time.sleep(1)
                    print(spameggs)                                            
            except Exception as E:
                print(E)
                sendmess(f"Привет! У бота ошибка. Перешли это сообщение @dikey_oficial или @thenextpageofyou\nОшибка:\n {E}")
                time.sleep(1)
