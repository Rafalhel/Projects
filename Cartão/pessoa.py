import csv
from datetime import datetime


class Pessoa:
    def __init__(self, nome=input("Digite seu nome: ")):
        self.nome = nome
        self.item = []
        self.dia = int(datetime.today().strftime('%d'))
        self.mes = int(datetime.today().strftime('%m'))
        self.ano = int(datetime.today().strftime('%Y'))
        dataCartao = 5
        cp = []
        print(self.dia)
        if self.dia == dataCartao:
            with open(f'{self.nome}.csv', 'r') as f:
                reader = csv.reader(f)
                for i in reader:
                    x = int(i[3].replace('/',''))
                    hoje = str(self.mes)+str(self.ano)
                    if x >= int(hoje):
                        cp.append(i)
            if cp != '':
                with open(f'{self.nome}.csv', 'w') as f:
                    writer = csv.writer(f, lineterminator='\r')
                    for i in cp:
                        writer.writerow(i)

        try:
            with open(f'{self.nome}.csv', 'r') as f:
                reader = csv.reader(f)
                for i in reader:
                    self.item.append(i)
        except FileNotFoundError:
            with open(f'{self.nome}.csv', 'w') as f:
                reader = csv.writer(f)

    def add(self):
        if self.nome == '':
            return 'Valor inválido'
        item = input('Item: ')
        if item == '':
            return 'Valor inválido'
        total = float(input("Valor total: "))
        if total == '':
            return 'Valor inválido'
        vezes = int(input("Parcelas: "))
        if vezes == '':
            return 'Valor inválido'

        meses = self.mes
        for i in range(vezes):
            meses += 1
            if meses == 12:
                meses = 0
                self.ano ==1

        mesfinal = str(meses)+'/'+str(self.ano)
        # final = int(mesfinal.replace('/',''))
        # print(final)
        print(mesfinal)

        parcela = total / vezes

        print(f'{item} - R${parcela}')
        with open(f'{self.nome}.csv', 'a') as f:
            writer = csv.writer(f, lineterminator='\r')
            writer.writerow([item, parcela, self.mes,mesfinal])

    def lista(self):
        with open(f'{self.nome}.csv', 'r') as f:
            reader = csv.reader(f)
            for i in reader:
                print(f'{i[0]} - R${i[1]}')
            return

    def total(self):
        with open(f'{self.nome}.csv', 'r') as f:
            reader = csv.reader(f)
            soma = 0
            for i in reader:
                soma += float(i[1])
            print(f'Total R${soma}')
            return

    def excluir(self):
        with open(f'{self.nome}.csv', 'w') as f:
            reader = csv.writer(f)
