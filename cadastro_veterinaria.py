class Animal:
    def __init__(self, nome):
        self.nome = nome

    def detalhes(self):
        pass

class Cachorro(Animal):
    def detalhes(self):
        return f"Cachorro: {self.nome}"

class Gato(Animal):
    def detalhes(self):
        return f"Gato: {self.nome}"

# Exemplo de uso com polimorfismo
animais = [Cachorro("Rex"), Gato("Mia")]
for a in animais:
    print(a.detalhes())
