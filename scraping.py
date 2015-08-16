__author__ = 'Carmine Di Monaco'
""" LISTA APPELLI
    Librerie usate:
    lxml lxml.de
    Requests http://www.python-requests.org/en/latest/
    --------------------------
    Invio una richiesta POST alla pagina su esse3
    Mi viene restituito la pagina contente gli appelli per il cdl in Informatica (0124)
    Tramite xpath,prelevo le informazioni sugli esami e le scrivo in un file chiamato appelli.txt """

from lxml import html
import requests
url="https://uniparthenope.esse3.cineca.it/Guide/PaginaListaAppelli.do"
payload={
    "form_id_form1":	"form1",
    "FAC_ID":	"10009",
    "DOCENTE_ID":	"X",
    "DATA_ESA":     "",
    "CDS_ID":	"10120",
    "AD_ID":	"X",
    "actionBar1":	"Cerca"
}
r=requests.post(url,data=payload)
pagina = html.fromstring(r.text)
appelli = pagina.xpath(".//*[@id='tableAppelli']/tbody/tr/td/text()  |.//*[@id='tableAppelli']/tbody/tr/td/child::node()/text()")
f=open("appelli.txt","w")
k=[]
for item in appelli:
    if item != "\n":
        k.append(item)
esami="\n".join(k)
for i in range(0,len(k)):
    f.write(k[i]+"\n")
