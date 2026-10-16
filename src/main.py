def validar_titulo():
    """Solicita um título até que ele tenha algum conteúdo."""
    while True:
        titulo = input("Título da tarefa: ").strip()
        if titulo:
            return titulo
        print("Erro: o título é obrigatório e não pode conter apenas espaços.")


def validar_prioridade():
    """Solicita uma prioridade permitida e retorna seu formato padronizado."""
    prioridades = {
        "alta": "Alta",
        "média": "Média",
        "media": "Média",
        "baixa": "Baixa",
    }

    while True:
        prioridade = input("Prioridade (Alta, Média ou Baixa): ").strip().casefold()
        if prioridade in prioridades:
            return prioridades[prioridade]
        print("Erro: escolha Alta, Média ou Baixa.")


def cadastrar_tarefa(tarefas):
    """Recolhe os dados, cria uma tarefa e adiciona à lista."""
    print("\n========== NOVA TAREFA ==========")
    titulo = validar_titulo()
    descricao = input("Descrição: ")
    prioridade = validar_prioridade()
    data_limite = input("Data limite: ")

    tarefa = {
        "titulo": titulo,
        "descricao": descricao,
        "prioridade": prioridade,
        "data_limite": data_limite,
        "status": "Pendente",
    }
    tarefas.append(tarefa)
    print("Tarefa cadastrada com sucesso!\n")


def listar_tarefas(tarefas):
    """Mostra todas as tarefas ou informa quando a lista está vazia."""
    if not tarefas:
        print("\nNenhuma tarefa cadastrada no momento.\n")
        return

    print("\n========== MINHAS TAREFAS ==========")
    for numero, tarefa in enumerate(tarefas, start=1):
        print(f"\nTarefa {numero}")
        print(f"Título: {tarefa['titulo']}")
        print(f"Descrição: {tarefa['descricao']}")
        print(f"Prioridade: {tarefa['prioridade']}")
        print(f"Data limite: {tarefa['data_limite']}")
        print(f"Status: {tarefa['status']}")
    print("\n====================================\n")


def menu():
    """Mantém o menu ativo até que a pessoa escolha sair."""
    tarefas = []

    while True:
        print("=================================")
        print("           TASKTRACKER")
        print("=================================")
        print("1 - Cadastrar nova tarefa")
        print("2 - Visualizar tarefas cadastradas")
        print("3 - Sair")

        opcao = input("\nEscolha uma opção: ").strip()

        if opcao == "1":
            cadastrar_tarefa(tarefas)
        elif opcao == "2":
            listar_tarefas(tarefas)
        elif opcao == "3":
            print("Encerrando o TaskTracker. Até mais!")
            break
        else:
            print("Opção inválida. Escolha 1, 2 ou 3.\n")


if __name__ == "__main__":
    menu()
