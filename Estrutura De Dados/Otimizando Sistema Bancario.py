import textwrap

def menu():
    menu_text = """
    ====== MENU ======
    [d] Depositar
    [s] Sacar
    [c] Consultar Saldo
    [e] Extrato
    [m] Mudar Senha
    [nc] Nova Conta
    [dc] Dados da Conta
    [l] Listar Contas
    [n] Novo Usuário
    [x] Sair do Sistema
    """
    print(textwrap.dedent(menu_text))
    return input("Escolha uma opção: ").strip().lower()

def depositar(saldo, valor, extrato):
    if valor > 0:
        saldo += valor
        extrato.append(['D', valor])

        print("\nValor depositado com sucesso!")

        print("Saldo Atual: R$ {:.2f}".format(saldo))

    else:
        print("\nOperação falhou! O valor informado é inválido.")

    return saldo, extrato

def sacar(saldo, valor, extrato, limite, numero_saques, limite_saques):
    if valor <= 0:
        print("\nOperação falhou! O valor informado é inválido.")

    elif valor > saldo:
        print("\nOperação recusada: você não possui esse valor disponível no seu saldo!")

    elif numero_saques >= limite_saques:
        print("\nOperação recusada: você excedeu a quantidade de saques permitido.")

        print("Total de saque diário autorizado é de {} transações.".format(limite_saques))

    elif valor > limite:
        print("\nOperação recusada: o valor do saque excede o limite.")

    else:
        saldo -= valor
        extrato.append(['S', valor])
        numero_saques += 1
        print("\nSaque realizado com sucesso!")

    return saldo, extrato, numero_saques

def consultar_saldo(saldo):

    print("\nSeu saldo atual é de R$ {:.2f}".format(saldo))

def exibir_extrato(extrato):

    if not extrato:
        print("\nExtrato vazio.")
        return
    print("\nExtrato:\n-----------------------------")
    for movimentacao in extrato:
        tipo, valor = movimentacao
        print(f"Tipo: {tipo} | Valor: R$ {valor:.2f}")
    print('-----------------------------')

def criar_usuario(usuarios):

    cpf = input('\nDigite o CPF (apenas números): ')
    usuario = filtrar_usuario(cpf, usuarios)

    if usuario:
        print("\nJá existe um usuário com esse CPF!")
        return

    nome = input("Digite seu nome completo: ")
    senha = input("Digite sua senha: ")
    email = input("Digite um email: ")
    telefone = input("Digite um telefone para contato: ")
    dataNascimento = input("Data de nascimento no formato DD/MM/AAAA: ")
    endereco = input("Digite o endereço completo (Logradouro, Número, Bairro, Cidade/Estado): ")

    usuarios.append({'CPF': cpf, 'Senha': senha, 'Nome': nome, 'Email': email, 'Telefone': telefone, 'DataNascimento': dataNascimento, 'Endereco': endereco})
    print("Usuário criado com sucesso!\n")

def filtrar_usuario(cpf, usuarios):

    usuario_filtrado = [usuario for usuario in usuarios if usuario["CPF"] == cpf]
    return usuario_filtrado[0] if usuario_filtrado else None

def imprimir_dados_da_conta(conta):

    print(f"\nCPF/CNPJ: {conta['CPF']}")
    print(f"Agência: {conta['Agencia']} \nNúmero da Conta: {conta['Numero']}\nTitular: {conta['Nome']}")
    print(f"Saldo Disponível: R$ {conta['Saldo']:.2f}")

def listar_contas(contas):

    for conta in contas:
        linha = f"Agência: {conta['Agencia']}, Número: {conta['Numero']}, Titular: {conta['Nome']}"
        print(linha)

def main():
    limite_saques = 3
    limite = 500
    saldo = 0
    extrato = []
    numero_saques = 0
    usuarios = []
    contas = []
    numero_conta = 1

    while True:
        opcao = menu()
        if opcao == 'd':
            valor = float(input("\nDigite o valor a ser depositado: R$ "))
            saldo, extrato = depositar(saldo, valor, extrato)
        elif opcao == 's':
            valor = float(input("\nDigite o valor a ser sacado: R$ "))
            saldo, extrato, numero_saques = sacar(saldo, valor, extrato, limite, numero_saques, limite_saques)
        elif opcao == 'c':
            consultar_saldo(saldo)
        elif opcao == 'e':
            exibir_extrato(extrato)
        elif opcao == 'm':
            # Implementação de mudança de senha não fornecida
            print("Opção de mudar senha ainda não implementada.")
        elif opcao == 'nc':
            # Implementação de criação de nova conta não fornecida
            print("Opção de nova conta ainda não implementada.")
        elif opcao == 'dc':
            # Supondo uma função que recupere uma conta baseada em algum critério não fornecido
            cpf = input("\nDigite o CPF do titular da conta: ")
            conta = [conta for conta in contas if conta['CPF'] == cpf]
            if conta:
                imprimir_dados_da_conta(conta[0])
            else:
                print("Conta não encontrada.")
        elif opcao == 'l':
            listar_contas(contas)
        elif opcao == 'n':
            criar_usuario(usuarios)
        elif opcao == 'x':
            print("Saindo do sistema...")
            break
        else:
            print("Opção inválida. Por favor, tente novamente.")

if __name__ == "__main__":
    main()


main()