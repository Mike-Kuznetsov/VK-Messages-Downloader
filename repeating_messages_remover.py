#This code filters vk_messages.txt and skips repeating messages
#Этот код фильтрует файл со скачанными сообщениями vk_messages.txt, пропуская повторяющиеся сообщения

import ast
#You need to set name of the file that you created
inputFile = open('vk_messages.txt','r', encoding="utf-8");
outputFile = open('vk_messages_processed.txt','w', encoding="utf-8");
lastNum=0;
for line in inputFile:
    myDict=ast.literal_eval(line);
    num=myDict['conversation_message_id'];
    if (num>lastNum):
        outputFile.write(line);
        lastNum=num;
print("done");
inputFile.close();
outputFile.close();


