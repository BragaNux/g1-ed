class Pilha:
    def __init__(self):
        self.items = []  # Inicializa a pilha como uma lista vazia

    def vazia(self):
        return self.items == []  # Verifica se a pilha está vazia

    def empilhar(self, item):
        self.items.append(item)  # Adiciona um item no topo da pilha

    def desempilhar(self):
        return self.items.pop()  # Remove e retorna o item do topo da pilha

    def tamanho(self):
        return len(self.items)  # Retorna o número de elementos na pilha

    def mostrar(self):
        return self.items  # Retorna os elementos da pilha

    def soma(self):
        return sum(self.items)  # Retorna a soma de todos os elementos da pilha

    def fim(self, pilha_numeros):
        while not self.vazia() and self.items[-1] != '(':  # Realiza operações até encontrar um '('
            realizar_operacao(pilha_numeros, self)


def calcular(expressao):
    pilha_numeros = Pilha()  # Cria uma pilha para os números
    pilha_operadores = Pilha()  # Cria uma pilha para os operadores
    par_abertos = 0  # Contador de parênteses abertos

    index = 0
    while index < len(expressao):
        char = expressao[index]
        if char.isdigit():
            numero = ''  # Inicializa uma string vazia para armazenar o número
            while index < len(expressao) and expressao[index].isdigit():
                numero += expressao[index]  # Adiciona cada dígito consecutivo à string `numero`
                index += 1  # Move o índice para o próximo caractere
            pilha_numeros.empilhar(int(numero))  # Converte a string `numero` em um número inteiro e o empilha na pilha de números

        elif char in '(':
            vezes = "*"  # Trata a situação de expressões como 2(3+4), adicionando implicitamente um *
            pilha_operadores.empilhar(vezes)
            pilha_operadores.empilhar(char)
            par_abertos += 1
            index += 1
        elif char in ')':
            if par_abertos == 0:
                raise ValueError("Parênteses desbalanceados: há um parêntese fechando sem um correspondente aberto")
            par_abertos -= 1
            pilha_operadores.fim(pilha_numeros)  # Executa operações até encontrar um '('
            pilha_operadores.desempilhar()  # Remove o '(' da pilha de operadores
            index += 1
        elif char in '°^√':
            pilha_operadores.empilhar(char)
            index += 1
        elif char in '+-*/':
            while (not pilha_operadores.vazia() and
                   pilha_operadores.mostrar()[-1] != '(' and
                   precedencia(char) <= precedencia(pilha_operadores.mostrar()[-1])):
                realizar_operacao(pilha_numeros, pilha_operadores)  # Realiza operações enquanto a precedência do operador atual for menor ou igual à precedência do operador no topo da pilha de operadores
            pilha_operadores.empilhar(char)  # Adiciona o operador atual à pilha de operadores
            index += 1
        else:
            index += 1

    if par_abertos != 0:
        raise ValueError("Parênteses desbalanceados: há parênteses abertos sem um correspondente fechamento")

    pilha_operadores.fim(pilha_numeros)  # Executa operações restantes após a análise da expressão

    return pilha_numeros.desempilhar()  # Retorna o resultado final da expressão


def precedencia(operador):
    if operador in '+-':
        return 1
    elif operador in '*/':
        return 2
    elif operador in '^√°':
        return 3
    return 0


def realizar_operacao(pilha_numeros, pilha_operadores):
    operador = pilha_operadores.desempilhar()  # Remove o operador do topo da pilha de operadores

    if operador == "°":
        numero = pilha_numeros.desempilhar()  # Remove o número do topo da pilha de números
        def log2(numero):
            if numero <= 0:
                return float('Error')
            else:
                return (numero.bit_length() - 1)
        resultado = log2(numero)  # Calcula o logaritmo na base 2 do número
        pilha_numeros.empilhar(resultado)  # Adiciona o resultado à pilha de números
    elif operador == '^':
        segundo_numero = pilha_numeros.desempilhar()  # Remove o segundo número da pilha de números
        primeiro_numero = pilha_numeros.desempilhar()  # Remove o primeiro número da pilha de números
        resultado = primeiro_numero ** segundo_numero  # Calcula a potência
        pilha_numeros.empilhar(resultado)  # Adiciona o resultado à pilha de números
    elif operador == '√':
        numero = pilha_numeros.desempilhar()  # Remove o número do topo da pilha de números
        resultado = numero ** 0.5  # Calcula a raiz quadrada
        pilha_numeros.empilhar(resultado)  # Adiciona o resultado à pilha de números
    else:
        segundo_numero = pilha_numeros.desempilhar()  # Remove o segundo número da pilha de números
        primeiro_numero = pilha_numeros.desempilhar()  # Remove o primeiro número da pilha de números
        if operador == '+':
            resultado = primeiro_numero + segundo_numero  # Calcula a soma
        elif operador == '-':
            resultado = primeiro_numero - segundo_numero  # Calcula a subtração
        elif operador == '*':
            resultado = primeiro_numero * segundo_numero  # Calcula a multiplicação
        elif operador == '/':
            if segundo_numero == 0:
                raise ValueError("Divisão por zero")
            resultado = primeiro_numero / segundo_numero  # Calcula a divisão
        pilha_numeros.empilhar(resultado)  # Adiciona o resultado à pilha de números

# # Entrada do usuário
# expressao = input("Digite a expressão matemática: ")

# # Calcula e mostra o resultado
# resultado = calcular(expressao)
# print("Resultado:", resultado)
