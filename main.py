clientes = []
funcionarios = []
produtos = []
formasPag = ("Pix", "Credito", "Debito", "Dinheiro")
clienteEncontrado = None
funcEncontrado = None
i = 1

while True:
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
        if op.lower() == "nao":
            break
    i += 1

i = 1
while True:
    print("-======== Cadastro de Funcionarios ========-")
    print(f"Digite as infomações do funcionario {i}:")
    nome = str(input("Nome do funcionario:"))
    codigo = int(input("Codigo do funcionario:"))
    cargo = str(input("Cargo do funcionario:"))    
    funcionarios.append(
        {
            "nome" : nome,
            "codigo" : codigo,
            "cargo" : cargo
        }
    )
    if i >= 3:
        op = str(input("Deseja incluir mais funcionarios?"))
        if op.lower() == "nao":
            break
    i += 1
i = 1
while True:
    print("-======== Cadastro de produtos ========-")
    print(f"Digite as infomações do produto {i}:")
    nome = str(input("Nome do produto:"))
    codigo = int(input("Codigo do produto:"))
    preco = float(input("Preco do produto:"))
    estoque = int(input("Quantidade em estoque:"))
    produtos.append(
        {
            "nome" : nome,
            "codigo" : codigo,
            "preco" : preco,
            "estoque" : estoque
        }
    )
    if i >= 5:
        op = str(input("Deseja incluir mais produtos?"))
        if op.lower() == "nao":
            break
    i += 1


while True:
    print("-======== Menu Principal ========-")
    print("1 --- Consultar clientes")
    print("2 --- Consultar funcionarios")
    print("3 --- Consultar produtos")
    print("4 --- Consultar formas de pagamento")
    print("5 --- Realizar uma venda")
    print("0 --- Encerrar sistema")
    op = int(input("Digite sua escolha:"))
    if op == 1:
        i = 1
        for cliente in clientes:
            print(f"Cliente {i}:\nNome = {cliente['nome']}\nCodigo = {cliente['codigo']}\nCPF = {cliente['cpf']}")
            i += 1
    elif op == 2:
        i = 1
        for funcionario in funcionarios:
            print(f"Funcionario {i}:\nNome = {funcionario['nome']}\nCodigo = {funcionario['codigo']}\nCargo = {funcionario['cargo']}")
            i += 1
    elif op == 3:
        i = 1
        for produto in produtos:
            print(f"Produto {i}:\nNome = {produto['nome']}\nCodigo = {produto['codigo']}\nPreco = {produto['preco']}\nEstoque = {produto['estoque']}")
            i += 1
    elif op == 4:
         print("Formas de pagamento:")
         for formaPag in formasPag:
             print(formaPag)
    elif op == 5:
        while clienteEncontrado == None:
            codCliente = int(input("Digite o codigo do cliente:"))
            for cliente in clientes:
                if cliente["codigo"] == codCliente:
                    clienteEncontrado = cliente
                    break
            if clienteEncontrado == None:
                print("Cliente não encontrado, tente novamente ...")
        while funcEncontrado == None:
            codFuncio = int(input("Digite o codigo do funcionario:"))
            for funcionario in funcionarios:
                if funcionario["codigo"] == codFuncio:
                    funcEncontrado = funcionario
                    break
            if funcEncontrado == None:
                print("Funcionario não encontrado, tente novamente ...")

        
    elif op == 0:
        print("Programa encerrado!")
        break
    else:
        print("Valor invalido, reiniciando menu . . .")
