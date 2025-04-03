try:
    string1 = input("Digite a primeira string: ")
    string2 = input("Digite a segunda string: ")

    if len(string1) != len(string2):
        raise Exception("Erro: As strings têm comprimentos diferentes.")

    print("As strings têm o mesmo comprimento.")
except Exception as e:
    print(e)