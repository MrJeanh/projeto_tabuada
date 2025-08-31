def tabuada_adicao(numero): # Tabuada de Adição
    print(f'Tabuada de adição do {numero}: ')
    for x in range(1, 11): # Conta do 1 ao 10
      print(f'{numero} + {x} = {numero + x}') 
def tabuada_multiplicacao(numero): # Tabuada de Multiplicação
    print(f'Tabuada de Multiplicação do {numero}: ')
    for x in range(1, 11): # Conta do 1 ao 10
        print(f'{numero} x {x} = {numero * x}')
def tabuada_divisao(numero): # Tabuada de Divisão
    print(f"Tabuada de divisão do {numero}:")
    for i in range(1, 11): # Conta do 1 ao 10
        print(f"{numero} ÷ {i} = {numero / i:.2f}")
