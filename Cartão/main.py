from pessoa import Pessoa

pessoa = Pessoa()
i = 0
while i == 0:
    try:
        x = int(input("\n1- Adicionar Item\n2- Ver lista de itens desse mês\n3- Ver total\n4- Excluir tudo\n\n"))
        if x == 1:
            pessoa.add()
        elif x == 2:
            pessoa.lista()
        elif x == 3:
            pessoa.total()
        elif x == 4:
            pessoa.excluir()
        x = input("Deseja continuar? (S/N)\n")
        if x == 'S' or x == 's':
            pass
        elif x == 'N' or x == 'n':
            i += 1
        else:
            print('Valor inválido\n')
    except ValueError:
        print('Valor inválido')
