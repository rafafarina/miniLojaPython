clientes = []
funcionarios = []
produtos = []
formasPag = ("Pix", "Credito", "Debito", "Dinheiro")

while True:
    i = 1
    print("-======== Cadastro de cliente ========-")
    print(f"Digite as infomações do cliente {i}:")
    nome = str(input("Nome do cliente:"))
    codigo = int(input("Codigo do cliente:"))
    cpf = int(input("CPF do cliente:"))   
    clientes.append(
        {
            "nome" : nome,
            "codigo" : codigo,
            "cpf" : cpf
            
        }
    )
    if i >= 3:
        op = str(input("Deseja incluir mais clientes?"))
        if op.lower == "nao":
            break
    i += 1

while True:
    i = 1
    print("-======== Cadastro de Funcionarios ========-")
    print(f"Digite as infomações do funcionario {i}:")
    nome = str(input("Nome do funcionario:"))
    codigo = int(input("Codigo do funcionario:"))
    cargo = str(input("Cargo do funcionario:"))    
    clientes.append(
        {
            "nome" : nome,
            "codigo" : codigo,
            "cargo" : cargo
        }
    )
    if i >= 3:
        op = str(input("Deseja incluir mais funcionarios?"))
        if op.lower == "nao":
            break
    i += 1

while True:
    i = 1
    print("-======== Cadastro de produtos ========-")
    print(f"Digite as infomações do produto {i}:")
    nome = str(input("Nome do produto:"))
    codigo = int(input("Codigo do funcionario:"))
    preco = float(input("Preco do produto:"))
    estoque = int(input("Quantidade em estoque:"))
    clientes.append(
        {
            "nome" : nome,
            "codigo" : codigo,
            "preco" : preco,
            "estoque" : estoque
        }
    )
    if i >= 3:
        op = str(input("Deseja incluir mais produtos?"))
        if op.lower == "nao":
            break
    i += 1

