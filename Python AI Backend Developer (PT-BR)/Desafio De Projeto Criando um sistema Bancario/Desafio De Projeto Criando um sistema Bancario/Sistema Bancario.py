# Inicialização de variáveis
saldo = 0
limite = 1000
extrato = []
numero_saque = 0
LIMITE_SAQUES = 3

# Menu de opções
menu = """
[d] Depositar
[s] Sacar
[c] Consultar saldo
[t] Transferir
[e] Extrato
[q] Sair

Escolha uma opção: """

while True:
    opcao = input(menu)

    if opcao == 'd':  # Depositar dinheiro na conta
        valor = float(input("Quantos reais deseja depositar? "))
        saldo += valor
        extrato.append(['Depósito', valor])

    elif opcao == 's':  # Sacar dinheiro da conta
        if numero_saque >= LIMITE_SAQUES:
            print(f'Você já realizou {LIMITE_SAQUES} saques consecutivos!')
        else:
            valor = float(input("Quanto dinheiro você quer sacar? "))
            if valor > saldo:
                print('\033[0;31mVocê não tem essa quantia disponível!\033[m')
            else:
                saldo -= valor
                numero_saque += 1
                extrato.append(['Saque', valor])

    elif opcao == 'c':  # Consultar o saldo da conta
        print(f"\nSaldo atual: R$ {saldo:.2f}")
        print(f"Limite de crédito: R$ {limite:.2f}\n")

    elif opcao == 't':  # Transferência Bancária
        conta_destinatario = input("Digite o número da conta do destinatário: ")
        valor = float(input("Qual é o valor que você quer transferir? "))
        if valor <= saldo:
            saldo -= valor
            extrato.append(['Transferência', valor, conta_destinatario])
        else:
            print('\033[0;31mVocê não tem esse valor disponível.\033[m')

    elif opcao == 'e':  # Histórico de transações
        print('\n\033[7;40;44mHistórico das Transações:\033[m')
        for transacao in extrato:
            print(f"Tipo: {transacao[0]}, Valor: {transacao[1]:.2f}, Detalhes: {transacao[2] if len(transacao) > 2 else ''}")

    elif opcao == 'q':  # Fechar e sair do programa
        print('\nObrigado por usar nossos serviços! Até logo!')
        break




    

        