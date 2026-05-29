import os
import time

def calculadora(num1: float, num2: float, operador: str) -> float:
    """
    Usar nan como valor inicial é uma boa prática. 
    Se o operador fornecido não corresponder a nenhuma das opções válidas (+, -, etc.), a função retornará nan, 
    sinalizando que o cálculo não pôde ser realizado.
    """
    result = float("nan")
    if operador == '+':
        result = num1 + num2
    elif operador == '-':
        result = num1 - num2
    elif operador == '*':
        result = num1 * num2
    elif operador == '/':
        if num2 != 0:
            result = num1 / num2
        else:
            print('Impossível dividir por zero!')
    elif operador == '**':
        result = num1 ** num2
    elif operador == '%':
        if num2 != 0:
            result = num1 % num2
        else:
            print('Impossível dividir por zero!')
            
    return result

def calculadora_alternativa(num1: float, num2: float, operador: str) -> float:
    
    match operador:
        case '+':
            return num1 + num2
        case '-':
            return num1 - num2
        case '*':
            return num1 * num2
        case '/':
            if num2 != 0:
                return num1 / num2
            else:
                print('Impossível dividir por zero!')
                return float("nan")
        case '**':
            return num1 ** num2
        case '%':
            if num2 != 0:
                return num1 % num2
            else:
                print('Impossível dividir por zero!')
            
                return float("nan")
        


if __name__ == "__main__":

    while True:
        os.system('cls' if os.name == 'nt' else 'clear')

            print('Calculadora')
            print('----------------------------------\n')
            
    try:
        num1 = float(input('Digite o primeiro número: '))
        num2 = float(input('Digite o segundo número: '))
        
        print("\nOperações disponíveis: +, -, *, /, ** (potência), % (resto)")
        operador = input('Escolha o tipo de operação: ').strip()
        
        resultado = calculadora(num1, num2, operador)
        
        import math
        if math.isnan(resultado):
            print('Operação inválida! -> Tente novamente!')
        else:
            print(f'\nResultado: {resultado}')


        except ValueError:
            print('Dados inválidos! -> Tente novamente!')
            time.sleep(2)

        except ZeroDivisionError:
            print('Impossível dividir por zero! -> Tente novamente!')
            time.sleep(2)

    print('\nVolte sempre!\n')  
