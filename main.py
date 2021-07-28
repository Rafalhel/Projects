from Multiplicador import Operacoes

def main():
    a = True
    while a:
        Operacoes()
        t = input('Deseja continuar ? (S/N) ')
        t = t.lower()
        if t == 's' or t == 'y':
            a = True
        elif t == 'n':
            print(f'Até a próxima')
            a = False
        else:
            print(f'Valor inválido')
            a = False

if __name__ == '__main__':
    main()