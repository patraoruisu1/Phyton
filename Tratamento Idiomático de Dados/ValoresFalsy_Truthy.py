# Valores Falsy
falsy_values = [False, None, 0, 0.0, '', [], {}, set()]
for value in falsy_values:
    if not value:
        print(f"{value} é Falsy")

# Uso prático
def processar_lista(items):
    if not items:  # Mais pythônico que len(items) == 0
        return "Lista vazia"
    return f"Processando {len(items)} items"