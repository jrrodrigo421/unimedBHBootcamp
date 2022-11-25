class Bicicleta:
    def __init__(self, cor, modelo, ano, valor):
        self.cor = cor
        self.modelo = modelo
        self.ano = ano
        self.valor = valor

    def buzinar(self):
        print('plim plim')
    def parar(self):
        print("PARE")
    def corre(self):
        print('VRRUUUUNNNMMM')
    #def __str__(self):
        #return f"Bicicleta: {self.cor}, {self.modelo}, {self.ano}, {self.valor}"


    def __str__(self):
        return  f"{self.__class__.__name__}:{', '.join([f'{chave}={valor}' for chave, valor in self.__dict__.items()])}"


caloi = Bicicleta('Amarelo', 'MTB', 2022, 'R$10000,00')

caloi.buzinar()
caloi.parar()
caloi.corre()

Bicicleta.buzinar(caloi)
print(caloi.cor, caloi.modelo, caloi.ano, caloi.valor)

print(caloi.cor)


print(caloi)

