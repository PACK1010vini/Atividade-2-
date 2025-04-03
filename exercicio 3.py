try:
    numero = int(input("Digite um número inteiro: "))
    if numero == 0:
        raise ZeroDivisionError("Erro: Divisão por zero não é permitida.")
    resultado = 10 / numero
    print(f"O resultado da divisão é: {resultado}")
except ZeroDivisionError as e:
    print(e)
except ValueError:
    print("Erro: Entrada inválida. Digite um número inteiro.")
