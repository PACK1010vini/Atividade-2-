try:
    string = input("Digite uma string: ")
    if not string.isupper():
        raise ValueError("Erro: A string contém letras minúsculas.")
    print("A string contém apenas letras maiúsculas.")
except ValueError as e:
    print(e)