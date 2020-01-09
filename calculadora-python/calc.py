def sel_operation():

    print('Selecione o número da operação desejada:\n1 - Soma\n2 - Subtração\n3 - Multiplicação\n4 - Divisão\n')

    ok_selections = [1,2,3,4]

    selection = int(input('Digite sua opção (1/2/3/4):'))
    if selection not in ok_selections:
        print('Você selecionou um valor não permitido')
        sel_operation()
    else:
        return selection

def get_params():
    number1 = int(input('Digite o primeiro número:'))
    number2 = int(input('Digite o segundo número:'))

    return number1, number2

def calculate():

    operation = sel_operation()
    x,y = get_params()

    if operation == 1:
        return x+y
    elif operation == 2:
        return x-y
    elif operation == 3:
        return x*y
    elif operation == 4:
        return x/y

if __name__ == "__main__":
    print('*'*15 + ' Python Calculator ' + '*'*15)
    result = calculate()
    print(f'O resultado da sua operação é: {result}')
