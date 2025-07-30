class Animal:
    def __init__(self, nome, especie):
        self.nome = nome
        self.especie = especie
    
    def dormir(self):
        return f"{self.nome} está dormindo"
    
    @staticmethod
    def respirar():
        return "Inspirar... Expirar..."
    
    @classmethod
    def criar_cao(cls, nome):
        return cls(nome, "Cão")

class Cachorro(Animal):
    def __init__(self, nome, raca):
        super().__init__(nome, "Cão")  # Chama construtor da classe pai
        self.raca = raca
    
    def latir(self):
        return f"{self.nome} faz: Au au!"
    
    def dormir(self):  # Override
        return f"{self.nome} está dormindo na casinha"

# Uso
dog = Cachorro("Rex", "Labrador")
print(dog.latir())     # Rex faz: Au au!
print(dog.dormir())    # Rex está dormindo na casinha
print(Animal.respirar())  # Inspirar... Expirar...

# Factory method
cao2 = Animal.criar_cao("Buddy")
print(cao2.especie)    # Cão