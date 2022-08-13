# This program downloads every message from VK dialog.
# Эта программа скачивает все сообщения из диалога ВК.
# Author: Mautoz Tech (Mikhail Kuznetsov)
# Youtube channel: https://www.youtube.com/c/mautoz_tech
# Youtube programming channel: https://www.youtube.com/channel/UCQAbEIaWFdARXKqcufV6y_g

import vk_api
from vk_api.longpoll import VkLongPoll, VkEventType
session_api = vk_session.get_api();

# Get your VK token from here https://vkhost.github.io/ and put it below:
# Получите ВК токен здесь https://vkhost.github.io/ и вставьте его ниже (Берете из адресной строки):
vk_session = vk_api.VkApi(token="PASTE-YOUR-TOKEN-HERE");
# Put here ID of person you have conversation with:
# Вставьте сюда ID пользователя с которым у вас диалог:
user_id=171414378;
#You can change name of output file. If file exists, you can delete it, or change name, or change "x" to "w".
#Вы можете поменять название файла, по умолчанию сообщения сохранятся в vk_messages.txt. Если файл уже существует, то вы можете удалить его, сменить название или поменять "x" на "w"
f = open('vk_messages.txt', 'x', encoding="utf-8");


lastMessage = session_api.messages.getHistory(count=1, peer_id=user_id);
pages=int(lastMessage['items'][0]['id']/200+1);
print("Pages (page - 200 messages): " + str(pages));

for i in range(1, pages):
    history = session_api.messages.getHistory(count=200, peer_id=user_id, start_message_id=200*i);
    history = history['items'];
    for j in reversed(history):
        f.write(str(j)+"\n");
    print(str(i)+" out of "+str(pages));    
    
f.close();
print("done");
