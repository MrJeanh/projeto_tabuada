import funcoes as f
def menu():
    opcao = int(input('Escolha uma opção:\n1: Adição \n2: Multiplicação \n3: Divisão\nOpção: '))
    numero = int(input('Digite a tabuada desejada: ')) # Será armazenado no parametro da função da tabuada selecionada
    if opcao == 1:
        f.tabuada_adicao(numero) 
    elif opcao == 2:
        f.tabuada_multiplicacao(numero)
    elif opcao == 3:
        f.tabuada_adicao(numero)
    else:
        print("Opção inválida!")
menu()