cpfs = []

while True:
    cpf = input("Digite o CPF: ")

    if cpf == "":
        print("O CPF é obrigatório!")
    elif cpf in cpfs:
        print("CPF já cadastrado! Digite outro.")
    else:
        cpfs.append(cpf)
        print("CPF cadastrado com sucesso!")
        break

print("Lista de CPFs:", cpfs)