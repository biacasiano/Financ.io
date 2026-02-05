import json
import os

ARQUIVO_DADOS = "financas.json"

def carregar():
    if not os.path.exists(ARQUIVO_DADOS):
        return []
    try:
        with open(ARQUIVO_DADOS, 'r', encoding='utf-8') as arquivo:
            return json.load(arquivo)
    except:
        return []

def salvar(lista):
    try:
        with open(ARQUIVO_DADOS, 'w', encoding='utf-8') as arquivo:
            json.dump(lista, arquivo, indent=4, ensure_ascii=False)
        print("Dados salvos com sucesso!")
    except:
        print("Erro ao salvar os dados.")

def listar(lista):
    if not lista:
        print("\nNenhum gasto registrado.")
        return

    print(f"\n{'ID':<5} | {'Mês':<12} | {'Descrição':<20} | {'Valor (R$)':<10}")
    print("-" * 55)
    for item in lista:
        print(f"{item['id']:<5} | {item['mes']:<12} | {item['descricao']:<20} | R$ {item['valor']:.2f}")
    print("-" * 55)

def criar(lista):
    print("\n--- Novo Gasto ---")
    mes = input("Digite o Mês (ex: Janeiro): ").strip()
    descricao = input("Descrição do gasto: ").strip()
    
    if not mes or not descricao:
        print("Erro: Mês e Descrição são obrigatórios.")
        return

    try:
        valor = float(input("Valor do gasto: "))
    except ValueError:
        print("Erro: O valor deve ser um número válido.")
        return

    novo_id = len(lista) + 1
    
    novo_gasto = {
        "id": novo_id,
        "mes": mes,
        "descricao": descricao,
        "valor": valor
    }
    
    lista.append(novo_gasto)
    salvar(lista)
    print(f"Gasto '{descricao}' adicionado com ID {novo_id}.")

def ler(lista, id_busca):
    encontrado = False
    for item in lista:
        if item['id'] == id_busca:
            print("\n--- Detalhes do Gasto ---")
            print(f"ID: {item['id']}")
            print(f"Mês: {item['mes']}")
            print(f"Descrição: {item['descricao']}")
            print(f"Valor: R$ {item['valor']:.2f}")
            encontrado = True
            return item
    
    if not encontrado:
        print("ID não encontrado.")
    return None

def atualizar(lista, id_busca):
    item = ler(lista, id_busca)
    
    if item:
        print("\n--- Atualizando Dados (Deixe vazio para manter o atual) ---")
        novo_mes = input(f"Novo Mês ({item['mes']}): ").strip()
        nova_desc = input(f"Nova Descrição ({item['descricao']}): ").strip()
        novo_valor_str = input(f"Novo Valor ({item['valor']}): ").strip()

        if novo_mes:
            item['mes'] = novo_mes
        if nova_desc:
            item['descricao'] = nova_desc
        if novo_valor_str:
            try:
                item['valor'] = float(novo_valor_str)
            except ValueError:
                print("Valor inválido. O valor anterior foi mantido.")

        salvar(lista)
        print("Registro atualizado com sucesso.")

def deletar(lista, id_busca):
    for i, item in enumerate(lista):
        if item['id'] == id_busca:
            lista.pop(i)
            salvar(lista)
            print("Registro deletado com sucesso.")
            return
    print("ID não encontrado para deleção.")

def menu():
    lista_financas = carregar()

    while True:
        print("\n=== GERENCIADOR DE FINANÇAS ===")
        print("1 - Listar tudo")
        print("2 - Criar novo gasto")
        print("3 - Ler por ID")
        print("4 - Atualizar")
        print("5 - Deletar")
        print("0 - Sair")
        
        opcao = input("Escolha uma opção: ")

        if opcao == "1":
            listar(lista_financas)
        elif opcao == "2":
            criar(lista_financas)
        elif opcao == "3":
            try:
                id_busca = int(input("Digite o ID para buscar: "))
                ler(lista_financas, id_busca)
            except ValueError:
                print("O ID deve ser um número inteiro.")
        elif opcao == "4":
            try:
                id_busca = int(input("Digite o ID para atualizar: "))
                atualizar(lista_financas, id_busca)
            except ValueError:
                print("O ID deve ser um número inteiro.")
        elif opcao == "5":
            try:
                id_busca = int(input("Digite o ID para deletar: "))
                deletar(lista_financas, id_busca)
            except ValueError:
                print("O ID deve ser um número inteiro.")
        elif opcao == "0":
            print("Saindo do sistema...")
            break
        else:
            print("Opção inválida. Tente novamente.")

if __name__ == "__main__":
    menu()