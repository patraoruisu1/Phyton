class Pessoa:
    def __init__(self, nome, idade):
        self.nome = nome          # Público
        self._idade = idade       # Privado (convenção)
        self.__cpf = None        # Muito privado (name mangling)
    
    def apresentar(self):
        return f"Olá, sou {self.nome}"
    
    @property
    def idade(self):
        return self._idade
    
    @idade.setter
    def idade(self, nova_idade):
        if nova_idade >= 0:
            self._idade = nova_idade
        else:
            raise ValueError("Idade deve ser positiva")
    
    def _metodo_interno(self):  # Método "privado"
        return "Método interno"

# Uso
p = Pessoa("Ana", 25)
print(p.nome)        # Ana
print(p.idade)       # 25 (via property)
p.idade = 26         # Usando setter
print(p._idade)      # 26 (acessível, mas não recomendado)