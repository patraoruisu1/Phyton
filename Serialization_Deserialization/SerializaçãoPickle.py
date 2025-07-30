import pickle

# Classe customizada
class Pessoa:
    def __init__(self, nome, idade):
        self.nome = nome
        self.idade = idade
    
    def __repr__(self):
        return f"Pessoa('{self.nome}', {self.idade})"

# Objetos complexos
pessoas = [
    Pessoa("Ana", 25),
    Pessoa("Carlos", 30),
    {'meta': 'dados extras'}
]

# Serializar
with open('pessoas.pkl', 'wb') as f:
    pickle.dump(pessoas, f)

# Deserializar
with open('pessoas.pkl', 'rb') as f:
    pessoas_carregadas = pickle.load(f)

print(pessoas_carregadas[0])  # Pessoa('Ana', 25)

# Pickle em string (bytes)
dados_bytes = pickle.dumps(pessoas)
dados_restaurados = pickle.loads(dados_bytes)

# CUIDADO: Pickle pode executar código arbitrário!
# Nunca use pickle.load() com dados de origem não confiável