import textwrap
from abc import ABC, abstractmethod
from datetime import datetime

class Cliente:
    def __init__(self, nome, endereco):
        self.nome = nome
        self.endereco = endereco
        self.contas = []
    
    def realizar_transacoes(self, conta, transacao):
        transacao.registrar(conta)

    def adicionar_conta(self, conta):
        self.contas.append(conta)

class PessoaFisica(Cliente):
    def __init__(self, nome, data_nascimento, cpf, endereco):
        super().__init__(nome, endereco)
        self.data_nascimento = data_nascimento
        self.cpf = cpf

class Conta:
    def __init__(self, numero, cliente):
        self._saldo = 0
        self._numero = numero
        self._agencia = "0001"
        self._cliente = cliente
        self._historico = Historico()

    @classmethod
    def nova_conta(cls, cliente, numero):
        return cls(numero, cliente)
        
    @property
    def saldo(self):
        return self._saldo
        
    @property
    def numero(self):
        return self._numero
        
    @property
    def agencia(self):
        return self._agencia

    @property
    def cliente(self):
        return self._cliente 

    @property
    def historico(self):
        return self._historico

    def sacar(self, valor):
        if valor <= self._saldo:
            self._saldo -= valor
            self._historico.adicionar_transacao("Saque", valor)
            return True
        else:
            print("Saldo insuficiente")
            return False

    def depositar(self, valor):
        if valor > 0:
            self._saldo += valor
            self._historico.adicionar_transacao("Depósito", valor)
            return True
        else:
            print("Valor de depósito inválido")
            return False

class Historico:
    def __init__(self):
        self.transacoes = []

    def adicionar_transacao(self, tipo, valor):
        transacao = {"tipo": tipo, "valor": valor, "data": datetime.now()}
        self.transacoes.append(transacao)

class Transacao(ABC):
    @abstractmethod
    def registrar(self, conta):
        pass

class Saque(Transacao):
    def __init__(self, valor):
        self.valor = valor

    def registrar(self, conta):
        conta.sacar(self.valor)

class Deposito(Transacao):
    def __init__(self, valor):
        self.valor = valor

    def registrar(self, conta):
        conta.depositar(self.valor)

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

def depositar(conta, valor):
    if conta.depositar(valor):
        print("\nValor depositado com sucesso!")
        print("Saldo Atual: R$ {:.2f}".format(conta.saldo))
    else:
        print("\nOperação falhou! O valor informado é inválido.")

def sacar(conta, valor):
    if conta.sacar(valor):
        print("\nSaque realizado com sucesso!")
    else:
        print("\nOperação falhou! Saldo insuficiente ou valor inválido.")

def consultar_saldo(conta):
    print("\nSeu saldo atual é de R$ {:.2f}".format(conta.saldo))

def exibir_extrato(conta):
    if not conta.historico.transacoes:
        print("\nExtrato vazio.")
        return
    print("\nExtrato:\n-----------------------------")
    for movimentacao in conta.historico.transacoes:
        tipo = movimentacao["tipo"]
        valor = movimentacao["valor"]
        print(f"Tipo: {tipo} | Valor: R$ {valor:.2f}")
    print('-----------------------------')

def criar_usuario(usuarios):
    cpf = input('\nDigite o CPF (apenas números): ')
    usuario = filtrar_usuario(cpf, usuarios)

    if usuario:
        print("\nJá existe um usuário com esse CPF!")
        return

    nome = input("Digite seu nome completo: ")
    data_nascimento = input("Data de nascimento no formato DD/MM/AAAA: ")
    endereco = input("Digite o endereço completo (Logradouro, Número, Bairro, Cidade/Estado): ")

    usuarios.append(PessoaFisica(nome, data_nascimento, cpf, endereco))
    print("Usuário criado com sucesso!\n")

def filtrar_usuario(cpf, usuarios):
    for usuario in usuarios:
        if isinstance(usuario, PessoaFisica) and usuario.cpf == cpf:
            return usuario
    return None

def criar_conta(usuarios, contas):
    cpf = input("Digite o CPF do titular da conta: ")
    usuario = filtrar_usuario(cpf, usuarios)

    if not usuario:
        print("Usuário não encontrado. Crie um novo usuário primeiro.")
        return

    numero = input("Digite o número da nova conta: ")
    nova_conta = Conta.nova_conta(usuario, numero)
    usuario.adicionar_conta(nova_conta)
    contas.append(nova_conta)
    print("Conta criada com sucesso!\n")

def imprimir_dados_da_conta(conta):
    print(f"\nCPF: {conta.cliente.cpf}")
    print(f"Agência: {conta.agencia} \nNúmero da Conta: {conta.numero}\nTitular: {conta.cliente.nome}")
    print(f"Saldo Disponível: R$ {conta.saldo:.2f}")

def listar_contas(contas):
    for conta in contas:
        linha = f"Agência: {conta.agencia}, Número: {conta.numero}, Titular: {conta.cliente.nome}"
        print(linha)

def main():
    limite_saques = 3
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
            conta_numero = input("Digite o número da conta: ")
            conta = next((conta for conta in contas if conta.numero == conta_numero), None)
            if conta:
                depositar(conta, valor)
            else:
                print("Conta não encontrada.")
        elif opcao == 's':
            valor = float(input("\nDigite o valor a ser sacado: R$ "))
            conta_numero = input("Digite o número da conta: ")
            conta = next((conta for conta in contas if conta.numero == conta_numero), None)
            if conta:
                sacar(conta, valor)
            else:
                print("Conta não encontrada.")
        elif opcao == 'c':
            conta_numero = input("Digite o número da conta: ")
            conta = next((conta for conta in contas if conta.numero == conta_numero), None)
            if conta:
                consultar_saldo(conta)
            else:
                print("Conta não encontrada.")
        elif opcao == 'e':
            conta_numero = input("Digite o número da conta: ")
            conta = next((conta for conta in contas if conta.numero == conta_numero), None)
            if conta:
                exibir_extrato(conta)
            else:
                print("Conta não encontrada.")
        elif opcao == 'm':
            print("Opção de mudar senha ainda não implementada.")
        elif opcao == 'nc':
            criar_conta(usuarios, contas)
        elif opcao == 'dc':
            conta_numero = input("Digite o número da conta: ")
            conta = next((conta for conta in contas if conta.numero == conta_numero), None)
            if conta:
                imprimir_dados_da_conta(conta)
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
