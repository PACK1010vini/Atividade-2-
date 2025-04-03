try:
    numero = int(input("Digite um número inteiro: "))
    if numero % 2 != 0:
        raise Exception(f"Erro: O número {numero} é ímpar. Apenas números pares são permitidos.")
    print(f"O número {numero} é par.")
except Exception as e:
    print(e)
except ValueError:
    print("Erro: Entrada inválida. Por favor, digite um número inteiro.")
