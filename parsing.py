__author__ = 'Carmine Di Monaco aka CDimonaco'
""" LETTURA INFORMAZIONI
    I file che contengono la lista dei prof e degli esami sono dei file di testo.
    Gli esami vengono aggiornati alle 00:00 di ogni giorno,tramite uno scraping della pagina degli appelli.
"""

def lista():
    f=open("text.txt","r",encoding="utf-8")
    parsing=[]
    for line in f:
        result=line
        result=result.strip("\xa0\n")
        parsing.append(result)
    diction={parsing[i] : parsing[i : i + 3] for i in range(0, len(parsing), 3)}
    print("Lista professori importata correttamente. \n")
    f.close()
    return diction

def appelli():
    f=open("appelli.txt","r",encoding="utf-8")
    parsing=[]
    for line in f:
        result=line
        result=result.strip("\n")
        parsing.append(result)
    print("Lista appelli importata correttamente")
    f.close()
    esami="\n".join(parsing)
    return esami

