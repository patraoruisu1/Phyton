class Voador:
    def voar(self):
        return "Voando alto!"

class Nadador:
    def nadar(self):
        return "Nadando rápido!"

class Pato(Animal, Voador, Nadador):
    def __init__(self, nome):
        super().__init__(nome, "Pato")
    
    def quack(self):
        return f"{self.nome} faz: Quack!"

# Uso
pato = Pato("Donald")
print(pato.quack())    # Donald faz: Quack!
print(pato.voar())     # Voando alto!
print(pato.nadar())    # Nadando rápido!

# Verificar MRO (Method Resolution Order)
print(Pato.__mro__)

# Verificação de instância e herança
print(isinstance(pato, Animal))   # True
print(isinstance(pato, Voador))   # True
print(issubclass(Pato, Animal))   # True