from telegram import ReplyKeyboardMarkup
from telegram.ext import Updater, CommandHandler, ConversationHandler, MessageHandler, Filters 
import csv


def find(update, context):
    surname = update.message.text
    sprav = read_spr_file()
    for row in sprav:
        if row[0] == surname:
            context.bot.send_message(chat_id = update.effective_chat.id,
                             text = ', '.join(row))        
    return ConversationHandler.END


def add_row(update, context):
    with open('spr.csv',mode = 'a', encoding='utf-8', newline = '') as file:
        writer = csv.writer(file, lineterminator="\r")
        writer.writerow(update.message.text.split(sep=','))    
    update.message.reply_text('Данные о новом абоненте добавлены в справочник.')
    
    return ConversationHandler.END


def del_row(update, context):
    with open('spr.csv', 'r', encoding='utf-8',newline = '') as file:
        reader = list(csv.reader(file, delimiter = ','))
    if len(reader) >= int(update.message.text)+1 :
        del reader[int(update.message.text)]
        with open('spr.csv',mode = 'w', encoding='utf-8', newline = '') as file:
            writer = csv.writer(file, delimiter = ",")
            for i in reader:
                writer.writerow(i)
        update.message.reply_text('Данные о абоненте удалены из справочника.')
    else:
        update.message.reply_text(f'Абонента с номером {update.message.text} нет в справочнике!')
 
    return ConversationHandler.END


def read_spr_file():
    with open('spr.csv', 'r', encoding = 'utf-8') as file:
        reader = csv.reader(file, delimiter = ',')
        return list(reader)
 
 
def view_read_spr(sprav):
    text = 'Список аюонентов в справочнике: \n'
    for i,sotrudnik in enumerate(sprav, 0):
        if i != 0:
            text += str(i)+'. ' + ', '.join(sotrudnik) + '\n'
        else:
            text += ', '.join(sotrudnik)+'\n'
    return text


def stop(update, context):
    update.message.reply_text("До свидания")
    return ConversationHandler.END
