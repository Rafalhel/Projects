class Operacoes:
    def __init__(self):
        try:
            self.escolha = int(input(f'Qual operação deseja usar ?\n'
                                f'1- Soma\n2- subtração\n3- Multiplicação\n'
                                f'4- Divisão\n'))
        except:
            print('Valor inválido')
            return
        if self.escolha == 1:
            self.soma()
        elif self.escolha == 2:
            self.sub()
        elif self.escolha == 3:
            self.multplicador()
        elif self.escolha == 4:
            self.divisor()
        else:
            print('Operação inválida')
            return

    def multplicador(self):
            try:
                self.mult=int(input(f"Digite um número para ver seus múltiplos de 1 a 10:\n"))
                for i in range (1,11):
                    print(f'{self.mult} * {i} = {self.mult*i}')
            except ValueError:
                print(f'Valor inválido')

    def divisor(self):
        try:
            self.mult=int(input(f"Digite um número para ver seus divisores de 1 a 10:\n"))
            for i in range (1,11):
                print(f'{self.mult} / {i} = {self.mult/i}')
        except ValueError:
            print(f'Valor inválido')
        except ZeroDivisionError:
            print(f'Não é possível dividir por 0')

    def soma(self):
        try:
            self.mult=int(input(f"Digite um número para ver suas somas de 1 a 10:\n"))
            for i in range (1,11):
                print(f'{self.mult} + {i} = {self.mult+i}')
        except ValueError:
            print(f'Valor inválido')

    def sub(self):
        try:
            self.mult = int(input(f"Digite um número para ver suas subtrações de 1 a 10:\n"))
            for i in range(1, 11):
                print(f'{self.mult} - {i} = {self.mult - i}')
        except ValueError:
            print(f'Valor inválido')


