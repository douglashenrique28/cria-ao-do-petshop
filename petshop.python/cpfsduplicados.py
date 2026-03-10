cpfs = set()

def cadastrar_cpf(cpf):
    if cpf in cpfs:
        print("CPF já existe!")
    else:
        cpfs.add(cpf)
        print("CPF cadastrado!")

