# Operador ternário
age = 20
status = "adulto" if age >= 18 else "menor"
print(status)  # adulto

# Palavra 'in'
frutas = ['maçã', 'banana', 'laranja']
if 'banana' in frutas:
    print("Temos bananas!")

# Em strings
email = "user@example.com"
if '@' in email and '.' in email:
    print("Email válido")

# Em dicionários
config = {'debug': True, 'port': 8080}
debug_mode = config.get('debug', False)  # Mais seguro
# ou
debug_mode = 'debug' in config and config['debug']