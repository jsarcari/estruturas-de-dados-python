from vetores import vetor
from listas import lista_ligada
from listas import lista_duplamente_ligada
from arvores import arvore, no_arvore_inteiro
from pilhas import pilha
from filas import fila

print(30 * '-', "MENU", 30 * '-')
print('1 - Vetores')
print('2 - Listas ligadas')
print('3 - Árvores')
print('4 - Listas duplamente ligadas')
print('5 - Pilhas')
print('6 - Filas')
opcao = int(input('Opção desejada: '))
if opcao == 1:
    vetor_teste = vetor.Vetor(0)
    while True:
        valor = int(input('Valor: '))
        if valor==999:
            break
        vetor_teste.inserir_elemento_final(valor)
    for i in range(0,vetor_teste.tamanho_vetor):
        print(vetor_teste.listar_elemento(i), end=' ')
    valor = int(input('\nNovo valor: '))
    posicao = int(input(f'Uma posição do vetor para ser inserido o valor {valor}: '))
    vetor_teste.inserir_elemento_posicao(valor, posicao)
    for i in range(0,vetor_teste.tamanho_vetor):
        print(vetor_teste.listar_elemento(i), end=' ')
    num = int(input('\nInforme um valor: '))
    if vetor_teste.contem(num):
        print(f'O valor {num} está no vetor.')
    else:
        print(f'O valor {num} não está no vetor.')
    num1 = int(input('\nInforme outro valor: '))
    if vetor_teste.indice(num1) >= 0:
        print(f'O valor {num1} está na posição {vetor_teste.indice(num1)} vetor.')
    else:
        print(f'O valor {num1} não está no vetor.')
    index = int(input('Insira um índice a ser removido: '))
    vetor_teste.remover_elemento_posicao(index)
    for i in range(0, vetor_teste.tamanho_vetor):
        print(vetor_teste.listar_elemento(i), end=' ')
    elem = int(input('\nInforme um valor a ser removido: '))
    vetor_teste.remover_elemento(elem)
    for i in range(0, vetor_teste.tamanho_vetor):
        print(vetor_teste.listar_elemento(i), end=' ')
elif opcao == 2:
    lista_teste = lista_ligada.ListaLigada()
    lista_teste.inserir(1)
    lista_teste.inserir(2)
    lista_teste.inserir(3)
    print(lista_teste)
    print(lista_teste.recuperar_elemento_no(2))
    lista_teste.inserir_posicao(0, 10)
    lista_teste.inserir_posicao(1, 4)
    print(lista_teste)
    print(lista_teste.contem(5))
    print(lista_teste.indice(3))
elif opcao==3:
    arvore_teste = arvore.Arvore()
    arvore_teste.inserir_elemento(no_arvore_inteiro.NoArvoreInteiro(5))
    arvore_teste.inserir_elemento(no_arvore_inteiro.NoArvoreInteiro(4))
    arvore_teste.inserir_elemento(no_arvore_inteiro.NoArvoreInteiro(6))
    arvore_teste.inserir_elemento(no_arvore_inteiro.NoArvoreInteiro(7))
    arvore_teste.inserir_elemento(no_arvore_inteiro.NoArvoreInteiro(3))
    arvore_teste.inserir_elemento(no_arvore_inteiro.NoArvoreInteiro(1))
    print(arvore_teste)
elif opcao == 4:
    lista_teste = lista_duplamente_ligada.ListaDuplamenteLigada()
    lista_teste.inserir(1)
    lista_teste.inserir(2)
    lista_teste.inserir(3)
    print(lista_teste)
    print(lista_teste.recuperar_elemento_no(2))
    lista_teste.inserir_posicao(0, 10)
    lista_teste.inserir_posicao(1, 4)
    print(lista_teste)
    print(lista_teste.contem(5))
    print(lista_teste.indice(3))
elif opcao==5:
    pilha_teste = pilha.Pilha()
    pilha_teste.empilhar(5)
    print(pilha_teste.desempilhar())
elif opcao==6:
    fila_teste = fila.Fila()
    fila_teste.enfileirar(1)
    fila_teste.enfileirar(2)
    fila_teste.enfileirar(3)
    fila_teste.enfileirar(4)
    print(fila_teste)
    print(fila_teste.desenfileirar())
    print(fila_teste)
    print(fila_teste.desenfileirar())
    fila_teste.enfileirar(1)
    print(fila_teste)
else:
    print('Opção inválida.')