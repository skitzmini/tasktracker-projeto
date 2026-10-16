def menu():
    """Exibe o menu principal do TaskTracker."""
    while True:
        print("=================================")
        print("           TASKTRACKER")
        print("=================================")
        print("1 - Cadastrar nova tarefa")
        print("2 - Visualizar tarefas cadastradas")
        print("3 - Sair")

        opcao = input("\nEscolha uma opção: ").strip()

        if opcao == "1":
            print("O cadastro será implementado na próxima etapa.\n")
        elif opcao == "2":
            print("A listagem será implementada na próxima etapa.\n")
        elif opcao == "3":
            print("Encerrando o TaskTracker. Até mais!")
            break
        else:
            print("Opção inválida. Escolha 1, 2 ou 3.\n")


if __name__ == "__main__":
    menu()
