class Cachorro:
    def __int__(self, nome, cor, acordado=True):
        self.nome = nome
        self.cor = cor
        self.acordado = acordado

    def latir(self):
        print('Auau')

    def dormir(self):
        self.acordado=False
        print('Zzzzzzzz..')


cao_1 = Cachorro("Mel", "Amarelo", False)
cao_2 = Cachorro("Belinha", "Branco")

cao_1.latir()

print(cao_2.acordado)
cao_2.latir()
print(cao_2.acordado)