__author__ = 'Carmine Di Monaco aka CDimonaco'
infoseg="Sede: Centro Direzionale - Isola C4\nOrari di attenzione telefonica:\nGiorni Pari:13:00 - 14:00\nGiorni Dispari:8:00 - 9:00 / 13:00 - 14:30\nOrario di sportello:\nLunedì, Mercoledì e Venerdì : 09.00 – 12.00\nMartedì e Giovedì : 09.00 - 12.30 e 14.00 – 15.30\nNumeri di telefono:+39-081-547-6652 -  	+39-081-547-6655\nEmail:segreteria.direzionale@uniparthenope.it\n"
helpesami="Esami aggiornati alle 00:00,lettura esami: Nome esame - Intervallo prenotazione - Data e ora esame - Tipo esame - Professori - Numero iscritti  \n"
""" FUNZIONE PER IL CONTROLLO DEI COMANDI E LA RISPOSTA
    Tra i parametri passati ritroviamo anche tgUpdateID,da me non usato ma utile per identificare meglio
    i messaggi arrivati e le i loro attributi(Nickname etc..)
    Con dei costrutti if controllo i messaggi arrivati.
    Se corrispondono ai comandi concessi rispondo adeguatamente.
    Le operazioni sulla variabile nome servono ad identicare il prof da cercare dividendo nome e cognome inseriti nel comando
    Sintassi comando (/cercaprof SPAZIO cognome SPAZIO nome)
    """
def handleTgMessage(tgBot,tgMessage,tgChatID,tgUpdateID,diction,esami):
    print("Messaggio arrivato {0} da chat id : {1}".format(tgMessage,tgChatID))
    comando=tgMessage
    if(comando.startswith("/cercaprof")):
        comando.lower()
        nome=comando.split(" ")
        nome=nome[1:]
        prof=" ".join(nome)
        try:
            result=diction[prof]
            tgBot.sendMessage(chat_id=tgChatID, text=(result[0]+"\n"+result[1]+"\n"+result[2]))
        except:
            tgBot.sendMessage(chat_id=tgChatID, text="Nome prof non presente")
    elif (comando==("/appelli")):
        tgBot.sendMessage(chat_id=tgChatID, text=helpesami+esami)
    elif(comando==("/credits")):
        tgBot.sendMessage(chat_id=tgChatID, text="Inf-Bot , Creato da Di Monaco Carmine, credits completi e source su ...")
    elif (comando==("/segreteria")):
        tgBot.sendMessage(chat_id=tgChatID,text=infoseg)
        tgBot.sendLocation(chat_id=tgChatID,longitude=40.856845,latitude=14.284453)
    else:
        tgBot.sendMessage(chat_id=tgChatID, text="Comando non riconosciuto. Riprova")