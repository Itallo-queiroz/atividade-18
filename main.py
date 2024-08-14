# Crie, em Python, um CRUD de usuários completo (Cadastrar, Pesquisar/Listar, Alterar e Excluir).
# O programa deverá:

# - Cadastrar usuário
# - Listar todos os usuários
# - Pesquisar por um usuário
# - Alterar os dados do usuário
# - Excluir usuário
# - Sair do programa

# O usuário deverá cadastrar:

# - Nome completo
# - Data de Nascimento
# - CPF
# - Profissão
# - E-mail
# - Endereço
# - Telefone
# 

# Inportar biblioteca
import os

# Boas vindas
print('\n\033[4m\033[35m Bem-vindo ao Sistema de Gerenciamento de usúario! \n\033[0m')


# Cadrasto do usúario
usuario = {}

#loop
while True:
    print('\n\033[4m\033[35m Menu \n\033[0m')
    print('1 - Cadastrar Usuário')
    print('2 - Listar Usuários')
    print('3 - Pesquisar Usuário')
    print('4 - Alterar Usuário')
    print('5 - Excluir Usuário')
    print('6 - Sair')

    ('\n')
    
    # Usuário Informa a opção desejada
    opcao = input('Escolha uma opção: ')

    match opcao:
        case '1':
            nome = input('Informe o Nome Completo: ')
            data_nascimento = input('Informe a Data de Nascimento: ')
            cpf = input('Informe o CPF: ')
            profissao = input('Informe a Profissão: ')
            email = input('Informe o E-mail: ')
            endereco = input('Informe o Endereço: ')
            telefone = input('Informe o  Telefone: ')
            usuario.append(nome)

            


