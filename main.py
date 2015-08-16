__author__ = "Di Monaco Carmine aka CDimonaco"
""" TELEGRAM BOT Parthenope-BOT
    QUESTO BOT FORNISCE INFORMAZIONI SUL CDL IN INFORMATICA DELL'UNIVERSITA' DEGLI STUDI DI NAPOLI "PARTHENOPE"
    CREATO A SCOPO DI STUDIO DA CARMINE DI MONACO
    LIBRERIE UTILIZZATE:
    python-telegram-bot https://github.com/leandrotoledo/python-telegram-bot
    Redis http://redis.io/
    Rq http://python-rq.org/docs/
    CREDITS COMPLETI SULLA PAGINA GITHUB DEL PROGETTO
    ----------------------------
    Perchè usare Rq?
    Tramite la libreria rq,creiamo una coda di "lavori" del nostro bot,
    Cosa significa?
    Significa che ogni messaggio che sarà inviato al nostro bot
    (Invito a guardare la documentazione delle api del bot di telegram)
    Sarà inviato alla funzione che processa i comandi inviati.
    La funzione stessa sarà immessa nella "coda" dei lavori da svolgere.
    Ogni volta che un lavoro sarà terminato si passerà al successivo.
    Questo metodo permette di avere un tempo di risposta e di esecuzione dei lavori molto breve,e di gestire
    anche grandi richieste al bot in poco tempo.
    Nulla vieta di usare altri metodi,anche semplicemente di leggere ogni update dall'api senza usare code e di
    processare i comandi.
    Ciò però in presenza di grandi carichi di richieste riduce drasticamente le performance.
    Invito perciò alla pagina github della libreria python-telegram-bot,dove troverete gli esempi sopracitati.
    Redis ha bisogno di abbastanza ram,usate questo metodo tenendo conto di tale aspetto.
    OGNI CONTRIBUTO E MIGLIORIA AL CODICE E' ACCETTO.
    Grazie dell'attenzione.
    CDimonaco """

import telegram
import time
from rq import Queue
from redis import Redis
from handleMessage import handleTgMessage
import parsing


_botToken="<TOKEN>"
_Botpart=telegram.Bot(token=_botToken)
_updates=_Botpart.getUpdates()
_redisserver=Redis()
# Importo la lista con i professori e gli appelli disponibili.
diction=parsing.lista()
esami=parsing.appelli()

try:
    _lastUpdateID=_updates[-1].update_id
except IndexError:
    _lastUpdateID=0

def checkUpdate(timeToSleep):
    global _lastUpdateID
    time.sleep(timeToSleep)

    for update in _Botpart.getUpdates(offset=_lastUpdateID):
        if update.update_id > _lastUpdateID:
            _lastUpdateID=update.update_id
            if update.message.text:
                sendToQueue(_Botpart,update.message.text,update.update_id,update.message.chat.id,diction,esami)
#Invio il processing dei comandi alla coda che si occuperà di rispondere ai messaggi.
def sendToQueue(tg_Bot,tg_Message,tg_Update_ID,tg_Chat_ID,diction,esami):
    _q=Queue(connection=_redisserver)
    _q.enqueue(handleTgMessage,tg_Bot,tg_Message,tg_Chat_ID,tg_Update_ID,diction,esami)


if __name__=="__main__":
    while True:
        checkUpdate(0.5)
        #Imposto delay con il quale controllare nuovi messaggi.
