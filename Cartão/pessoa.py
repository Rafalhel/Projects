import csv
from datetime import datetime


class Pessoa:
    def __init__(self, nome=input("Digite seu nome: ")):
        self.nome = nome
        self.item = []

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
        mes = int(datetime.today().strftime('%m'))
        ano = int(datetime.today().strftime('%Y'))
        meses = mes
        for i in range(vezes):
            meses += 1
            if meses == 12:
                meses = 0
                ano ==1

        mesfinal = str(meses)+'/'+str(ano)
        # final = int(mesfinal.replace('/',''))
        # print(final)
        print(mesfinal)

        parcela = total / vezes

        print(f'{item} - R${parcela}')
        with open(f'{self.nome}.csv', 'a') as f:
            writer = csv.writer(f, lineterminator='\r')
            writer.writerow([item, parcela, mes,mesfinal])

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
