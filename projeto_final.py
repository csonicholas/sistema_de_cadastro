# Projeto Final Lógica de Programação II (PY) | ED - Santander Coders 2023 (1) - Engenharia de dados
# Professor: Lucas Hermeto
# Aluno: Eric Nicholas Clementino da Silva Oliveira
# Id: 0997022
# email: csonicholas@gmail.com

import json

arquivo_json = 'projetoModuloII.json'
dados = {}
dicionario = {}

def ler():
    # global dados
    try:
        with open(arquivo_json,'r', encoding='utf-8') as arquivo:
            dados = json.load(arquivo)
        return dados   
                        
    except json.JSONDecodeError as e:       
        # print(f"Erro ao decodificar JSON: {e}")
        pass
    except FileNotFoundError as e:
        print(f"Arquivo não encontrado: {e}")
    except Exception as e:
        print(f"Erro desconhecido: {e}")  

   

def salvar(dados):
    with open(arquivo_json,'w', encoding='utf-8') as arquivo:
        json.dump(dados,arquivo, indent=2,ensure_ascii = False)
 
def add_usuario():
    dados = ler()
    qtd_inserir = input('\nQuantos usuários deseja inserir? ')
    if qtd_inserir.isdigit():
        if not dados:
            id_usuario = 0
        else:
            id_usuario = len(dados)       
        if int(qtd_inserir) >= 1:
            for i in range(int(qtd_inserir)):
                id_usuario += 1
                nome = ''
                while len(nome) == 0 or nome.isdigit():
                    nome = input('\nDigite o nome do usuário: ')
                    if len(nome) == 0 or nome.isdigit():
                        print("\nNome inválido!")

                telefone = ''
                while len(telefone) == 0 or not telefone.isdigit():
                    telefone = input('\nDigite o telefone do usuário (Somente números): ')
                    if not telefone.isdigit() or len(telefone) == 0:
                        print('\nTelefone inválido')

                endereco = ''
                while len(endereco) == 0:
                    endereco = input('\nDigite o endereco do usuário: ')
                    if len(endereco) == 0:
                        print('\nEndereco inválido!') 

                dicionario = {
                    str(id_usuario) : {
                        "Status": True,
                        "Nome": nome,
                        "Telefone": int(telefone),
                        "Endereço": endereco
                    }
                }
                if not dados:
                    dados = {}
                    dados.update(dicionario)
                else:
                    dados.update(dicionario)
                print('\nUsuário adicionado com sucesso! ')
                
                print(f'\nID: {id_usuario}\nNome: {nome}\nTelefone: {int(telefone)}\nEndereço: {endereco}\n ')
                salvar(dados)
                      
    else:
        print('\nA quantida inserida não é um número válido')

def excluir_usuario():
    dados = ler()   
    if not dados:
        print('\nNão existem dados a serem excluidos')
    else:
        id_excluir = input('\nDigite o ID do usuário que deseja excluir: ')
        if id_excluir in dados:
            for chave in dados:
                if id_excluir == chave:
                    print(f'\nID: {chave}\nNome: {dados[chave]["Nome"]}\nTelefone: {dados[chave]["Telefone"]}\nEndereço: {dados[chave]["Endereço"]}\n ')
                    dados[chave]['Status'] = False
                    print('Usuário excluido com sucesso! Status = false')
        else:
            print('Usuário não encontrado')
        
        salvar(dados)
        
   
def atualizar_usuario():
    dados = ler()
    if not dados:
        print('\nNão existem dados a serem atualizados')
    else: 
        id_atualizar = input('Digite o ID do usuário que deseja atualizar: ')
        if id_atualizar not in dados:
            print('Usuário não encontrado')
        else:
            for chave in dados:
                if id_atualizar == chave:
                    print(f' 1 - Nome: {dados[chave]["Nome"]}\n 2 - Telefone: {dados[chave]["Telefone"]}\n 3 - Endereço: {dados[chave]["Endereço"]}\n ')
                    opcao = int(input('Escolha a opção com a informação que deseja atualizar ? \n'))
                    if opcao == 1:
                        dados[chave]["Nome"] = input('Digite o nome atualizado: ')
                    elif opcao == 2:
                        dados[chave]["Telefone"] = input('Digite o telefone atualizado: ')
                    elif opcao == 3:
                        dados[chave]["Endereço"] = input('Digite o endereço atualizado: ')
                    else:
                        print('Opção Inválida, por favor, refaça a solicitação!')
            
            salvar(dados)
            print('Dados atualizados com sucesso!!')
    
def exibir_alguns_ids():
    
    dados = ler()
    if not dados:
        print('\nNão existem dados a serem exibidos')
    else:
        try:
            ids = []
            qtd_ids = ''
            while len(qtd_ids) == 0 or not qtd_ids.isdigit():
                qtd_ids = input('Quantos IDs deseja exibir? \n')
            if int(qtd_ids) > len(dados):
                print('A quantidade de ids que deseja exibir é maior que a quantidade total.')
            else:
                for i in range(qtd_ids):
                    ids.append(input(f'Digite o {i + 1} ID que deseja exibir: \n'))
                    for chave in ids:
                        print(f'\nID: {chave}\nNome: {dados[chave]["Nome"]}\nTelefone: {dados[chave]["Telefone"]}\nEndereço: {dados[chave]["Endereço"]}\n ')
        except Exception:
            print('Usuário não encontrado')
    
def exibir_dados():
    dados = ler()
    if not dados:
        print('\nNão existem dados a serem exibidos')
    else:        
        for chave in dados:
                print(f'ID: {chave}\nNome: {dados[chave]["Nome"]}\nTelefone: {dados[chave]["Telefone"]}\nEndereço: {dados[chave]["Endereço"]}\n ')       
                

        

while True:
    menu = '''
    Boas vindas ao nosso sistema:

    1 - Inserir usuário
    2 - Excluir usuário
    3 - Atualizar usuário
    4 - Informações de um usuário
    5 - Informações de todos os usuários
    6 - Sair
    '''
    print(menu)
    opcao = ''
    try:
        opcao = int(input('Escolha uma opção: '))
    except:
        Exception('A opção escolhida é inválida!! ')

    if opcao == 1:
         add_usuario()
    elif opcao == 2:
         excluir_usuario()
    elif opcao == 3:
         atualizar_usuario()
    elif opcao == 4:
         exibir_alguns_ids()
    elif opcao == 5:
         exibir_dados()
    elif opcao == 6:
        break
    else:
        print('A opção escolhida é inválida!! ')

