def multplicador():
    try:
        mult=int(input(f"Digite um número para ver seus múltiplos de 1 a 10:\n"))
        for i in range (1,11):
            print(f'{mult} * {i} = {mult*i}')
    except ValueError:
        return f'Valor inválido'

multplicador()