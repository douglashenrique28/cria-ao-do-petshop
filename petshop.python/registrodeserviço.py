# Serviços fixos do sistema
servicos_disponiveis = {
    1: {'nome': 'Banho', 'preco': 80},
    2: {'nome': 'Tosa', 'preco': 100},
    3: {'nome': 'Consulta', 'preco': 120},
    4: {'nome': 'Hospedagem', 'preco': 150}
}

# Mostrar os serviços
print("Serviços disponíveis:")
for codigo, servico in servicos_disponiveis.items():
    print(f"{codigo} - {servico['nome']} | R$ {servico['preco']}")

# Usuário escolhe o serviço
opcao = int(input("Escolha o número do serviço: "))

# Verifica se existe
if opcao in servicos_disponiveis:
    servico = servicos_disponiveis[opcao]
    print(f"Serviço escolhido: {servico['nome']}")
    print(f"Preço: R$ {servico['preco']}")
else:
    print("Serviço inválido.")