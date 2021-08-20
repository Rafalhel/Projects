import time
from plyer import notification
import requests
from bs4 import BeautifulSoup
import csv
from datetime import datetime

while True:
    search = "dolar"
    url = f"https://www.google.com/search?q={search}"
    r = requests.get(url)
    s = BeautifulSoup(
    r.text, "html.parser")
    update = s.find("div", class_="BNeawe").text
    print(update)
    t = ""

    for i in update:
        if i == ",":
            t += "."
        elif i != " ":
            t += i
        else:
            break
    t = float(t)
    x = 0
    valores = []
    valoresn = []
    rep = 1
    dol = []
    dia = []
    reais = []
    data_e_hora_atuais = datetime.now()
    data_e_hora_em_texto = data_e_hora_atuais.strftime('%d/%m/%Y')
    horas = data_e_hora_atuais.strftime('%H:%M')


    notification.notify(
        title='Quantos reais?',
        message=f'{update}',
        app_name='Dólares'
    )
    with open('dados/bd.csv', 'a') as f:
        writer = csv.writer(f, lineterminator='\r')
        writer.writerow([t] + [data_e_hora_em_texto + " " + horas])

    time.sleep(3600)
# print(dia)
# print(dol)
# matplotlib.pyplot.plot(dia, dol)
# matplotlib.pyplot.xlabel('Data')
# matplotlib.pyplot.ylabel('Valor do Dollar')
# matplotlib.pyplot.savefig('grafico.png')
# matplotlib.pyplot.show()
