# TaskTracker

## Descrição

TaskTracker é uma aplicação simples de linha de comando para cadastrar tarefas e consultar seus dados no terminal. Cada tarefa contém título, descrição, prioridade, data limite e status. Os registros são mantidos em memória durante a execução do programa.

## Objetivo acadêmico

O projeto integra o Bootcamp II e conecta o planejamento lógico elaborado para a Fase 1 à implementação em Python da Fase 2. A atividade pratica decomposição de problemas, algoritmos, validação de entradas, programação em Python e controle de versão com Git e GitHub.

## Funcionalidades

- Menu contínuo com opções para cadastrar tarefa, visualizar tarefas e sair.
- Validação do título para rejeitar texto vazio ou formado apenas por espaços.
- Validação da prioridade, aceitando Alta, Média, Media e Baixa, sem diferenciar maiúsculas e minúsculas.
- Padronização de “Media” para “Média” no registro.
- Status inicial automático como “Pendente”.
- Listagem organizada de todos os dados das tarefas.
- Mensagem clara quando ainda não há tarefas cadastradas.

Os dados são apagados quando o programa é encerrado. Persistência, edição, exclusão, banco de dados, login e funcionalidades da Fase 3 não fazem parte deste escopo.

## Tecnologias utilizadas

- Python 3
- Git para controle de versão
- GitHub como destino planejado para hospedagem do repositório

A aplicação não utiliza frameworks, bibliotecas externas ou serviços de banco de dados.

## Estrutura de diretórios

```text
tasktracker-projeto/
├── README.md
├── .gitignore
├── docs/
│   └── planejamento_logico.pdf
└── src/
    └── main.py
```

## Requisitos para execução

- Python 3 instalado e disponível no terminal como `python`.
- CMD ou outro terminal compatível com a execução de programas Python.

Confira a instalação com:

```cmd
python --version
```

## Exemplo de utilização

```text
=================================
           TASKTRACKER
=================================
1 - Cadastrar nova tarefa
2 - Visualizar tarefas cadastradas
3 - Sair

Escolha uma opção: 1

========== NOVA TAREFA ==========
Título da tarefa: Estudar Python
Descrição: Revisar funções
Prioridade (Alta, Média ou Baixa): Alta
Data limite: 20/10/2026
Tarefa cadastrada com sucesso!
```

Na listagem, o programa apresenta título, descrição, prioridade, data limite e status. A prioridade aceita “Media” sem acento, mas é exibida padronizada como “Média”.

## Regras de validação

- Título: obrigatório; entradas vazias ou só com espaços são rejeitadas e solicitadas novamente.
- Prioridade: somente Alta, Média, Media ou Baixa são aceitas; a validação ignora diferenças entre maiúsculas e minúsculas e repete a pergunta em caso de erro.
- Descrição: texto livre.
- Data limite: texto livre, sem validação de formato.
- Status: definido automaticamente como “Pendente”.
- Menu: opções diferentes de 1, 2 e 3 exibem uma mensagem de erro e retornam ao menu.

## Principais funções

- `validar_titulo()` solicita e valida o título usando um laço `while` e `strip()`.
- `validar_prioridade()` verifica as opções permitidas e retorna uma forma padronizada.
- `cadastrar_tarefa(tarefas)` recolhe os dados, cria um dicionário e o adiciona à lista.
- `listar_tarefas(tarefas)` informa quando a lista está vazia ou exibe todas as tarefas.
- `menu()` cria a lista em memória e mantém a navegação ativa até a opção de saída.

## Contexto das Fases 1 e 2

A Fase 1 propõe o entendimento do problema, a decomposição dos dados e regras, a receita lógica em português, o planejamento da estrutura Git/GitHub e uma apresentação em vídeo. O documento de planejamento está em `docs/planejamento_logico.pdf` e foi elaborado agora para apoiar este trabalho; não representa uma entrega anterior nem uma aprovação da Fase 1.

A Fase 2 transforma esse planejamento em uma aplicação CLI funcional, registra a evolução com commits e prepara a publicação do repositório. A publicação pública depende de autorização do estudante. O vídeo acadêmico continua pendente e deve ser gravado pelo estudante conforme os requisitos do enunciado.
