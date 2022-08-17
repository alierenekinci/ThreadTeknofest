import logging
import pandas as pd
from re import search

from telegram.ext import CommandHandler, Filters, MessageHandler, Updater

import pickle
from unicode_tr import unicode_tr
from nltk.corpus import stopwords
from snowballstemmer import TurkishStemmer
from nltk import ngrams

from rulebasedlearning import searchPattern

BOT_TOKEN = "5408055126:AAEmSc1JknJgl2xZc51ZNrMpyZ7cM7FwPNM"

def metin_onisle(metin):
    kucuk_harfli_metin = unicode_tr(metin).lower()
    istenen_karakterler = set(list(' abcdefghijklmnopqrstuvwxyzâçîöüğış0123456789'))
    harfler = list(kucuk_harfli_metin)
    harfler = [k if k in istenen_karakterler else ' ' for k in harfler]
    temiz_dokuman = "".join(kucuk_harfli_metin)
    temiz_dokuman_kelimeleri = temiz_dokuman.split(' ')
    temiz_dokuman_kelimeleri = [kelime for kelime in temiz_dokuman_kelimeleri if len(kelime) > 0]
    turkStem=TurkishStemmer()
    temiz_dokuman_kelimeleri = [turkStem.stemWord(kelime) for kelime in temiz_dokuman_kelimeleri]
    n = 2
    bigrams = ngrams(temiz_dokuman_kelimeleri, n)
    bigramstr = map(''.join, bigrams)
    ngram = " ".join(list(bigramstr))
    temiz_dokuman = " ".join(temiz_dokuman_kelimeleri) + " " +  "".join(ngram)
    return temiz_dokuman


# Enable logging
logging.basicConfig(
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s', 
    level=logging.INFO)
logger = logging.getLogger(__name__)


def start(update, context):
    """Send a message when the command /start is issued."""
    update.message.reply_text('Merhaba bu bot, Ankara Büyükşehir Belediyesi SSS cevap vermek üzere tasarlanmıştır. Thread Takımı tarafından oluşturulmuştur. Şuan veritabanında aşağıdaki hizmetler için yardımcı olabiriz.\n- Ego Ulaşımkartları\n- Ankara Bel. Psikolojik Danışman\n- Mavi Masa\n- Ankara Kart \n- Önemli Telefonlar \n- Aski  \n- Belediyenin sağladığı diğer hizmetler')


def yardim(update, context):
    """Send a message when the command /help is issued."""

    df = pd.read_excel(r"veri\ankarabbSoruCevapVeriSeti-v02.xlsx", engine="openpyxl")
    message = 'Sorabileceğiniz örnek sorular şunlardır.\n\n'
    
    for i in df["soru"].sample(n=3):
        message += "\n\n- "
        message += str(i).capitalize()
        
    update.message.reply_text(message)

def response(update, context):
    """Machine Learning Response"""

    with open(r'ankarabbHibritChatbot\DecisionTreeClassifierModel.pickle', 'rb') as handle:
        DecisionTreeClassifierModel = pickle.load(handle)

    with open(r'ankarabbHibritChatbot\RandomForestClassifierModel.pickle', 'rb') as handle:
        RandomForestClassifierModel = pickle.load(handle)

    # print(update.message.text)
    patternOutcome = searchPattern(str(update.message.text).lower())
    if patternOutcome == None:

        print(str(update.message.text).split())
        if len(str(update.message.text).split()) == 1:

            if len(str(update.message.text)) > 2:

                n = 10

                probs = RandomForestClassifierModel.predict_proba([metin_onisle(update.message.text)])
                message = sorted( zip( RandomForestClassifierModel.classes_, probs[0] ), key=lambda x:x[1] )[-n:]

                messageSend = False

                for index in range(len(message)-1,-1,-1):
                    print(message[index][0][:20], message[index][1])
                    
                    if metin_onisle(str(update.message.text)) in metin_onisle(str(message[index][0])) and message[index][1] >= 0.1 and messageSend == False:
                        
                        messageSend = True
                        update.message.reply_text(str(message[index][0]))
                    
                if messageSend == False:
                    update.message.reply_text("Sorunuzu bir kaç kelime ile yazabilirmisiniz. Veritabanımda uygun soru bulamadım. \n\nÖrnek: Başkent kart şifre değişikliği")
        elif len(str(update.message.text).split()) > 1:          
            update.message.reply_text(RandomForestClassifierModel.predict([metin_onisle(update.message.text)])[0])
        else :
            update.message.reply_text("Boş bir mesajı anlayamam değil mi? Lütfen biraz daha samimi olalım. Örnek: Kamusal AnkaraKart kaybedilmesi durumunda ne yapılmalı")
    else:   
        print(patternOutcome)
        update.message.reply_text(patternOutcome)

def error(update, context):
    """Log Errors caused by Updates."""
    logger.warning('Update "%s" caused error "%s"', update, context.error)


def main():
    """Start the bot."""
    # Create the Updater and pass it your bot's token.
    # Make sure to set use_context=True to use the new context based callbacks
    # Post version 12 this will no longer be necessary
    updater = Updater(BOT_TOKEN, use_context=True)

    # Get the dispatcher to register handlers
    dp = updater.dispatcher

    # on different commands - answer in Telegram
    dp.add_handler(CommandHandler("start", start))
    dp.add_handler(CommandHandler("yardim", yardim))

    # on noncommand i.e message - echo the message on Telegram
    dp.add_handler(MessageHandler(Filters.text, response))

    # log all errors
    dp.add_error_handler(error)

    # Start the Bot
    updater.start_polling()

    # Run the bot until you press Ctrl-C or the process receives SIGINT,
    # SIGTERM or SIGABRT. This should be used most of the time, since
    # start_polling() is non-blocking and will stop the bot gracefully.
    updater.idle()


if __name__ == '__main__':
    main()
