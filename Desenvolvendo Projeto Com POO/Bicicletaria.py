class Bicicleta:
    def __init__(self, marca, ano, modelo, valor):
        self.marca = marca
        self.ano = ano
        self.modelo = modelo
        self.valor = valor

    def mostrar_dados(self):
        print("Marca da Bicicleta:", self.marca)
        print("Modelo da Bicicleta:", self.modelo)
        print("Ano de Fabricação:", self.ano)
        print("Valor da Bicicleta: R$", format(self.valor, ".2f"))

class Bicicletario:
    def __init__(self):
        self.inventario = []

    def adicionar_bicicleta(self, bicicleta):
        self.inventario.append(bicicleta)
        print("Bicicleta adicionada ao inventário!")

    def remover_bicicleta(self, bicicleta):
        if bicicleta in self.inventario:
            self.inventario.remove(bicicleta)
            print("Bicicleta removida do inventário!")
        else:
            print("Bicicleta não encontrada no inventário.")

    def mostrar_inventario(self):
        print("Inventário de Bicicletas:")
        for bicicleta in self.inventario:
            bicicleta.mostrar_dados()
            print("\n")

# Criação de bicicletas
bicicleta1 = Bicicleta("Caloi", 2022, "MTB", 1500.00)
bicicleta2 = Bicicleta("Monark", 2023, "BMX", 693.00)

# Criação do bicicletário e manipulação do inventário
bicicletario = Bicicletario()
bicicletario.adicionar_bicicleta(bicicleta1)
bicicletario.adicionar_bicicleta(bicicleta2)
bicicletario.mostrar_inventario()

# Remover uma bicicleta e mostrar o inventário novamente
bicicletario.remover_bicicleta(bicicleta1)
bicicletario.mostrar_inventario()
