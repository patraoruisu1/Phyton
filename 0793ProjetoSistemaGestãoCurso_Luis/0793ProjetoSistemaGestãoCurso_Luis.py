def main():
    projetos = {}
    nomes_projetos = set()
    
    while True:
        mostrar_menu()
        opcao = input("Selecione uma opção (1-6): ")
        
        if opcao == "1":
            adicionar_projeto(projetos, nomes_projetos)
        # elif é uma abreviação de "else if"
        elif opcao == "2":
            ver_detalhes_projeto(projetos)
        elif opcao == "3":
            listar_projetos(projetos)
        elif opcao == "4":
            remover_projeto(projetos, nomes_projetos)
        elif opcao == "5":
            calcular_receita_total(projetos)
        elif opcao == "6":
            print("Saindo do sistema... Obrigado!")
            break
        else:
            print("Opção inválida. Por favor, escolha uma opção de 1 a 6.")

def mostrar_menu():
    print("\n=== MENU PRINCIPAL ===")
    print("1. Adicionar um novo projeto")
    print("2. Ver os detalhes de um projeto")
    print("3. Listar todos os projetos")
    print("4. Remover um projeto")
    print("5. Calcular a receita total")
    print("6. Sair")

def adicionar_projeto(projetos, nomes_projetos):
    print("\n--- ADICIONAR UM NOVO PROJETO ---")
    nome = input("Nome do projeto: ").strip()
    
    if not nome:
        print("Erro: O nome do projeto não pode estar vazio.")
        return
    if nome in nomes_projetos:
        print("Erro: Já existe um projeto com esse nome.")
        return
    
    try:
        inscricoes = int(input("Número de inscrições: "))
        duracao = int(input("Duração do curso (horas): "))
        valor = float(input("Valor do curso por inscrição (EUROS): "))
        
        if inscricoes <= 0 or duracao <= 0 or valor <= 0:
            print("Erro: Todos os valores devem ser positivos.")
            return
            
        projetos[nome] = {
            'inscrições': inscricoes,
            'duração': duracao,
            'valor': valor
        }
        nomes_projetos.add(nome)
        print(f"\n Projeto '{nome}' adicionado com sucesso!")
        
    except ValueError:
        print("Erro: Insira valores numéricos válidos.")

def ver_detalhes_projeto(projetos):
    print("\n--- DETALHES DO PROJETO ---")
    nome = input("Nome do projeto: ").strip()
    
    projeto = projetos.get(nome)
    if projeto:
        print("\n Detalhes do projeto:")
        print(f"Nome: {nome}")
        print(f"Inscrições: {projeto['inscrições']} participantes")
        print(f"Duração: {projeto['duração']} horas")
        print(f"Valor por inscrição: EURO {projeto['valor']:.2f}")
        
        receita = projeto['inscrições'] * projeto['valor']
        print(f"\n Receita estimada: EURO {receita:.2f}")
    else:
        print("Projeto não encontrado.")

def listar_projetos(projetos):
    print("\n--- LISTA DE PROJETOS ---")
    
    if not projetos:
        print("Nenhum projeto cadastrado.")
    else:
        print("Projetos disponíveis:")
        for i, nome in enumerate(sorted(projetos.keys()), 1):
            print(f"{i}. {nome}")

def remover_projeto(projetos, nomes_projetos):
    print("\n--- REMOVER PROJETO ---")
    nome = input("Nome do projeto a remover: ").strip()
    
    if nome in projetos:
        confirmacao = input(f"Quer remover '{nome}'? (s/n): ").lower()
        if confirmacao == 's':
            del projetos[nome]
            nomes_projetos.remove(nome)
            print(f"Projeto '{nome}' removido com sucesso.")
    else:
        print("Projeto não encontrado.")

def calcular_receita_total(projetos):
    print("\n--- RECEITA TOTAL ---")
    
    if not projetos:
        print("Nenhum projeto cadastrado para cálculo.")
        return
    
    total = 0.0
    print("Receita por projeto:")
    for nome, dados in projetos.items():
        receita = dados['inscrições'] * dados['valor']
        total += receita
        print(f"► {nome}: EURO {receita:.2f}")
    
    print(f"\n RECEITA TOTAL ESTIMADA: EURO {total:.2f}")

if __name__ == "__main__":
    main()
