clientes = []
funcionarios = []
produtos = []
formasPag = ("Pix", "Credito", "Debito", "Dinheiro")
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
        clienteEncontrado = None
        funcEncontrado = None
        carrinho = {}

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

        while True:
            prodEncontrado = None

            codProd = int(input("Digite o codigo do produto (0 para finalizar):"))

            if codProd == 0:
                if len(carrinho) == 0:
                    print("O carrinho está vazio! Adicione pelo menos um produto.")
                    continue
                break

            for produto in produtos:
                if produto["codigo"] == codProd:
                    prodEncontrado = produto
                    break

            if prodEncontrado == None:
                print("Produto não encontrado, tente novamente ...")
                continue

            qtdNoCarrinho = 0
            if codProd in carrinho:
                qtdNoCarrinho = carrinho[codProd]["quantidade"]

            estoqueDisponivel = prodEncontrado["estoque"] - qtdNoCarrinho

            print(f"Produto: {prodEncontrado['nome']}")
            print(f"Preco: R$ {prodEncontrado['preco']:.2f}")
            print(f"Estoque disponivel: {estoqueDisponivel}")

            qtdProd = int(input("Digite a quantidade de produto:"))

            while qtdProd <= 0:
                print("A quantidade deve ser um numero inteiro positivo!")
                qtdProd = int(input("Digite a quantidade novamente:"))

            if qtdProd > estoqueDisponivel:
                print("Estoque insuficiente! Quantidade não adicionada.")
                continue

            if codProd in carrinho:
                carrinho[codProd]["quantidade"] += qtdProd
            else:
                carrinho[codProd] = {
                    "codigo": prodEncontrado["codigo"],
                    "nome": prodEncontrado["nome"],
                    "preco": prodEncontrado["preco"],
                    "quantidade": qtdProd
                }

            opCarrinho = str(input("Deseja adicionar outro produto?"))
            if opCarrinho.lower() == "nao":
                break

        subtotal = 0

        print("\n-======== Resumo dos produtos ========-")

        for item in carrinho.values():
            item["subtotal"] = item["preco"] * item["quantidade"]
            subtotal += item["subtotal"]

            print(f"Codigo: {item['codigo']}")
            print(f"Produto: {item['nome']}")
            print(f"Quantidade: {item['quantidade']}")
            print(f"Preco unitario: R$ {item['preco']:.2f}")
            print(f"Subtotal: R$ {item['subtotal']:.2f}")

        print(f"Subtotal da compra: R$ {subtotal:.2f}")

        desconto = float(input("Digite o desconto percentual (0 a 100):"))

        while desconto < 0 or desconto > 100:
            print("Desconto invalido!")
            desconto = float(input("Digite o desconto percentual (0 a 100):"))

        valorDesconto = subtotal * desconto / 100
        totalPagar = subtotal - valorDesconto

        print(f"Valor do desconto: R$ {valorDesconto:.2f}")
        print(f"Total a pagar: R$ {totalPagar:.2f}")

        print("\n-======== Formas de pagamento ========-")

        for i, formaPag in enumerate(formasPag, start=1):
            print(f"{i} --- {formaPag}")

        opPag = int(input("Escolha a forma de pagamento:"))

        while opPag < 1 or opPag > len(formasPag):
            print("Forma de pagamento invalida!")
            opPag = int(input("Escolha a forma de pagamento:"))

        formaEscolhida = formasPag[opPag - 1]

        print("\n-======== Confirmacao da venda ========-")
        print(f"Cliente: {clienteEncontrado['nome']}")
        print(f"Funcionario: {funcEncontrado['nome']}")

        for item in carrinho.values():
            print(f"{item['nome']} - Quantidade: {item['quantidade']} - Subtotal: R$ {item['subtotal']:.2f}")

        print(f"Subtotal: R$ {subtotal:.2f}")
        print(f"Desconto: {desconto:.2f}%")
        print(f"Valor do desconto: R$ {valorDesconto:.2f}")
        print(f"Total a pagar: R$ {totalPagar:.2f}")
        print(f"Forma de pagamento: {formaEscolhida}")

        confirmar = str(input("Deseja confirmar a venda?"))

        if confirmar.lower() == "sim":

            for item in carrinho.values():
                for produto in produtos:
                    if produto["codigo"] == item["codigo"]:
                        produto["estoque"] -= item["quantidade"]
                        break

            print("\n========================================")
            print("          COMPROVANTE DE VENDA")
            print("========================================")

            print("\nDADOS DO CLIENTE")
            print(f"Nome: {clienteEncontrado['nome']}")
            print(f"CPF: {clienteEncontrado['cpf']}")

            print("\nDADOS DO FUNCIONARIO")
            print(f"Nome: {funcEncontrado['nome']}")
            print(f"Cargo: {funcEncontrado['cargo']}")

            print("\nPRODUTOS COMPRADOS")

            for item in carrinho.values():
                print("----------------------------------------")
                print(f"Codigo: {item['codigo']}")
                print(f"Produto: {item['nome']}")
                print(f"Quantidade: {item['quantidade']}")
                print(f"Preco unitario: R$ {item['preco']:.2f}")
                print(f"Subtotal: R$ {item['subtotal']:.2f}")

            print("----------------------------------------")
            print(f"Subtotal: R$ {subtotal:.2f}")
            print(f"Desconto: {desconto:.2f}%")
            print(f"Valor do desconto: R$ {valorDesconto:.2f}")
            print(f"TOTAL A PAGAR: R$ {totalPagar:.2f}")
            print(f"Forma de pagamento: {formaEscolhida}")
            print("========================================")
            print("VENDA CONCLUIDA COM SUCESSO!")

        else:
            print("Venda cancelada! O estoque não foi alterado.")             
        
    elif op == 0:
        print("Programa encerrado!")
        break
    else:
        print("Valor invalido, reiniciando menu . . .")
