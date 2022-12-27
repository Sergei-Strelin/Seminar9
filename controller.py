from telegram.ext import Updater, CommandHandler, ConversationHandler, MessageHandler, Filters 
from view import view, surname, add_user, del_user, edit_user1, edit_user2, start, help, edit_row
from model import find, add_row, del_row, read_spr_file, view_read_spr, stop


def main():
    TOKEN = input('Введите TOKEN: ')
    updater = Updater(token = TOKEN)
    dispatcher = updater.dispatcher
    

    find_surname = ConversationHandler(entry_points=[CommandHandler('surname', surname)],
                                       states={1: [MessageHandler(Filters.text & ~Filters.command, find)]},
                                       fallbacks=[CommandHandler('stop', stop)])

    add_us = ConversationHandler(entry_points=[CommandHandler('add_user', add_user)],
                                       states={1: [MessageHandler(Filters.text & ~Filters.command, add_row)]},
                                       fallbacks=[CommandHandler('stop', stop)])

    edit_us = ConversationHandler(entry_points=[CommandHandler('edit_user', edit_user1)],
                                       states={1: [MessageHandler(Filters.text & ~Filters.command, edit_user2)],
                                               2: [MessageHandler(Filters.text & ~Filters.command, edit_row)]},
                                       fallbacks=[CommandHandler('stop', stop)])

    del_us = ConversationHandler(entry_points=[CommandHandler('del_user', del_user)],
                                       states={1: [MessageHandler(Filters.text & ~Filters.command, del_row)]},
                                       fallbacks=[CommandHandler('stop', stop)])   
 
    dispatcher.add_handler(CommandHandler('start', start))		
    dispatcher.add_handler(CommandHandler('view', view))		
    dispatcher.add_handler(find_surname)	
    dispatcher.add_handler(add_us)	
    dispatcher.add_handler(edit_us)	
    dispatcher.add_handler(del_us)	    
    dispatcher.add_handler(CommandHandler('help', help))	

    updater.start_polling()
    print('bot start')
    
    updater.idle()