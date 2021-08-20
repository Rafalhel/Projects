from Multiplicador import Operacoes

if __name__ == '__main__':

    a=True
    while a:
        x = Operacoes()
        t = input('Deseja continuar ? (S/N) ')
        
        t = t.lower()
        if t == 's' or t == 'y':
            a = True
        elif t == 'n':
            print(f'Até a próxima')
            a = False
        else:
            print(f'Valor inválido')
            a=False
    
