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

cpfs = set()

def cadastrar_cpf(cpf):
    if cpf in cpfs:
        print("CPF já existe!")
    else:
        cpfs.add(cpf)
        print("CPF cadastrado!")
