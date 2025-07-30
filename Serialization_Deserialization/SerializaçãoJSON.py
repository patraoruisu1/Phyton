import json
from datetime import datetime

# Dados complexos
dados = {
    'nome': 'João Silva',
    'idade': 30,
    'ativo': True,
    'salario': 5000.50,
    'departamentos': ['TI', 'Vendas'],
    'endereco': {
        'rua': 'Rua A, 123',
        'cidade': 'São Paulo'
    }
}

# Serializar para string
json_string = json.dumps(dados, indent=2, ensure_ascii=False)
print(json_string)

# Salvar em arquivo
with open('dados.json', 'w', encoding='utf-8') as f:
    json.dump(dados, f, indent=2, ensure_ascii=False)

# Carregar de arquivo
with open('dados.json', 'r', encoding='utf-8') as f:
    dados_carregados = json.load(f)

print(dados_carregados['nome'])  # João Silva

# Serialização customizada para datetime
class DateTimeEncoder(json.JSONEncoder):
    def default(self, obj):
        if isinstance(obj, datetime):
            return obj.isoformat()
        return super().default(obj)

dados_com_data = {'timestamp': datetime.now()}
json_com_data = json.dumps(dados_com_data, cls=DateTimeEncoder)