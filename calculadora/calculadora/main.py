
def calculadora():
    print('Iniciando Calculadora')

    def calculator(n1, n2, op):
        if op == '+':
            return n1 + n2
        elif op == '-':
            return n1 - n2
        elif op == '*':
            return n1 * n2
        elif op == '/':
            return n1 / n2

    while True:
        n1 = int(input('Primeiro Algoritimo: '))
        op = input('Qual operação desejada: ')
        n2 = int(input('Segundo algoritimo: '))

        print(calculator(n1, n2, op))

        run = int(input('Deseja realizar outra operação? [1]Sim [2]Não '))
        if run == 1:
            continue
        elif run == 2:
            return False


if __name__ == '__main__':
    calculadora()