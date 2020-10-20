class Animal:
    def fazer_barulho(self):
        print('Barulho de um animal')
    pass


class Domestico:
    def esta_dormindo(self):
        return True


class Mamifero(Animal):
    pass


class Cachorro(Mamifero, Domestico):
    def enterrar_osso(self):
        print('O osso foi enterrado!')


class Gato(Mamifero):
    def fazer_barulho(self):
        print('Miau')


cachorro = Cachorro()

cachorro.fazer_barulho()
print(cachorro.esta_dormindo())
cachorro.enterrar_osso()

gato = Gato()

gato.fazer_barulho()
