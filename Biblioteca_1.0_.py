livro = []
cliente = []
entrada = []

while True:

    print('\n(1) CADASTRAR   (2) FRENTE DE CAIXA   \n(3) CONSULTAR   (4) SAIR')
    menu = int(input('\n>> '))

    if menu == 4:  # SAIR
        break

    elif menu == 1:  # CADASTRO
        menu = 0
        while menu != 3:
            print('\n(1) CADASTRAR LIVRO   (2) CADASTRAR CLIENTE   (3) VOLTAR ')
            menu = int(input('>> '))

            if menu == 1:  # CADASTRO LIVRO
                print()
                print('-'*30, 'CADASTRO DE LIVROS', '-'*60)
                entrada.append(str(input('NOME: ')))
                entrada.append(str(input('AUTOR: ')))
                entrada.append(int(input('ANO: ')))
                entrada.append(str(input('EDITORA: ')))
                entrada.append(float(input('PREÇO R$: ')))
                entrada.append(int(input('ESTOQUE: ')))
                entrada.append('DISPONÍVEL')

                livro.append(entrada[:])
                print('\nLIVRO CADASTRADO COM SUCESSO!')
                print('-'*90)
                print()
                entrada.clear()

            elif menu == 2:     #CADASTRO CLIENTE
                print()
                print('-'*30, 'CADASTRO DE CLIENTES', '-'*60)
                entrada.append(str(input('NOME: ')))
                entrada.append(str(input('CPF: ')))
                entrada.append(str(input('DATA NASC (ddmmaaaa): ')))
                entrada.append(str(input('END.RUA: ')))
                entrada.append(str(input('END.NUMERO: ')))
                entrada.append(str(input('END.BAIRRO: ')))
                entrada.append(str(input('END.CEP: ')))
                entrada.append(str(input('TEL.DDD: ')))
                entrada.append(str(input('TEL.CEL: ')))

                cliente.append(entrada[:])
                print('\nCLIENTE CADASTRADO COM SUCESSO!')
                print('-'*90)
                print()
                entrada.clear()

    elif menu == 2:
        pass

    elif menu == 3:  # CONSULTA
        menu = 0
        while menu != 3:

            print('\n(1) CONSULTAR LIVRO   (2) CONSULTAR CLIENTE   (3) VOLTAR ')
            menu = int(input('>> '))

            if menu == 1:
                if len(livro) == 0:
                    print('NÃO HÁ LIVROS CADASTRADOS NO SISTEMA')
                    print()

                else:
                    print(f'\n ----------------------------------------- CONSULTA DE LIVROS CADASTRADOS  --------------------------------------------')
                    print('          LIVRO',' '*27, 'AUTOR', ' '*15, 'ANO', ' '*3, 'EDITORA', ' '*13, 'PREÇO (R$)', ' '*3, 'ESTOQUE', ' '*4, 'STATUS')
                    print()

                    enumerado = 1

                    for livro_cad in livro:
                        print(enumerado, f'{livro_cad[0].upper(): <42}{livro_cad[1].upper(): <22}{livro_cad[2]: <8}'
                              f'{livro_cad[3].upper(): <22}{livro_cad[4]: <15.2f}'
                              f'{livro_cad[5]: <13}{livro_cad[6].upper()}')

                        enumerado += 1
                    print('------------------------------------------------------------------------------------------------------------------------')
                    print()

            elif menu == 2:
                if len(cliente) == 0:
                    print('\nNÃO HÁ CLIENTES CADASTRADOS NO SISTEMA')
                    print()

                else:
                    print(f'\n ----------------------------------------- CONSULTA DE CLIENTES CADASTRADOS  --------------------------------------------')
                    print(f'      CLIENTE                     CPF             IDADE       RUA                    NUMERO  BAIRRO              CEP         DDD  CELULAR ')
                    print()

                    enumerado = 1

                    for cliente_cad in cliente:
                        nome        = cliente_cad[0]
                        cpf         = cliente_cad[1]

                        data_nasc   = int(cliente_cad[2][-4:])
                        idade = 2021 - data_nasc

                        rua         = cliente_cad[3]
                        numero      = cliente_cad[4]
                        bairro      = cliente_cad[5]
                        cep         = cliente_cad[6]
                        ddd         = cliente_cad[7]
                        celular     = cliente_cad[8]

                        print(enumerado, f'{nome: <31} {cpf: <15} {idade: <11} '
                              f'{rua: <22} {numero: <7} '
                              f'{bairro: <19} {cep:<11} {ddd:<4} {celular}')

                        enumerado += 1
                    print('------------------------------------------------------------------------------------------------------------------------')
                    print()
                    
