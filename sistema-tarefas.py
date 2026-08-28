# 1. Entrada de Dados (Built-ins iniciais)
qtd_tarefas = int(input("Quantas tarefas deseja cadastrar? "))
lista_tarefas = []

for i in range(qtd_tarefas):
    # Opcional: exibe o número da tarefa na pergunta para melhor experiência
    nome = input(f"Digite a tarefa {i + 1}: ")
    lista_tarefas.append(nome)

# 2. Processamento com enumerate() e range()
banco_dados_tarefas = []

for indice, nome_tarefa in enumerate(lista_tarefas, start=1):
    # Lógica de prazo escalonado: tarefa 1 = 2 dias, tarefa 2 = 4 dias, etc.
    prazo_dias = indice * 2
    status = "Pendente"
    
    # Criando a tupla estruturada e adicionando ao banco de dados
    tarefa_tupla = (indice, nome_tarefa, prazo_dias, status)
    banco_dados_tarefas.append(tarefa_tupla)

# 3. Saída de Dados e Desempacotamento
print("\n--- RESUMO DO SISTEMA ---")

for tarefa in banco_dados_tarefas:
    # Desempacotamento de tuplas para garantir legibilidade (sem índices manuais)
    id_tarefa, nome_tarefa, prazo_dias, status = tarefa
    
    # Exibição formatada no console
    print(f"ID: {id_tarefa} | Tarefa: {nome_tarefa} | Prazo: {prazo_dias} dias | Status: {status}")

# Exibição do total utilizando len()
print(f"Total de tarefas gerenciadas: {len(banco_dados_tarefas)}")
