import tkinter as tk
from tkinter import messagebox
import random
import numpy as np

# Função para obter letras únicas em uma string
def letras_unicas(palavras):  # Define uma funcao chamada "letras_unicas" que recebe um parametro "palavras"
    todas_letras = ''.join(palavras)  
    # Une todas as strings em "palavras" em uma unica string chamada "todas_letras"
    letras_unicas = ''.join(sorted(set(todas_letras), key=todas_letras.index))  
    # Cria um conjunto com as letras unicas, ordenando-as pela ordem de aparicao em "todas_letras"
    return letras_unicas  # Retorna a string "letras_unicas"

# Função para obter os índices de cada letra da palavra na string de letras únicas
def obter_indices(palavra, palavra_unica):  
    # Define uma funcao chamada "obter_indices"que recebe dois parametros: "palavra" e "palavra_unica"
    indices = [palavra_unica.index(letra) for letra in palavra if letra in palavra_unica] 
    # Cria uma lista "indices" contendo os indices de cada letra de "palavra" 
    # conforme a posicao delas em "palavra_unica", apenas se a letra estiver em "palavra_unica"
    return indices  # Retorna a lista "indices"

# Função para converter índices para um número decimal
def indices_para_decimal(indices):  
    # Define uma funcao chamada "indices_para_decimal" que recebe um parametro "indices"
    numero_str = ''.join(map(str, indices)) 
# Converte cada indice na lista "indices" para uma string e os junta em uma unica string chamada "numero_str"
    return int(numero_str) if numero_str else 0 
# Converte "numero_str" para um inteiro e o retorna; se "numero_str" estiver vazio, retorna 0


# Função para processar as palavras inseridas pelo usuário
def processar_palavras():  # Define uma funcao chamada "processar_palavras" que nao recebe parametros
    palavras = [palavra_entrada1.get(), palavra_entrada2.get(), palavra_entrada3.get()]  
    # Cria uma lista "palavras" contendo as strings obtidas a partir de tres entradas de texto
    # (palavra_entrada1, palavra_entrada2, palavra_entrada3)
    palavra_unica = letras_unicas(palavras) 
    # Chama a funcao "letras_unicas" com a lista "palavras" e armazena o resultado na variavel "palavra_unica"
    if len(palavra_unica) > 10:  # Verifica se o comprimento de "palavra_unica" é maior que 10 caracteres
        messagebox.showerror("Erro", "O resultado da palavra formada excede 10 caracteres.")  
        # Se for, exibe uma mensagem de erro com um alerta
    else:  # Caso contrario, continua o processamento
        indices_palavras = [obter_indices(palavra, palavra_unica) for palavra in palavras] 
        # Cria uma lista "indices_palavras" contendo os indices de cada palavra em "palavras" 
        # com base na "palavra_unica"
        indices_palavra_unica = list(range(len(palavra_unica)))  
        # Gera uma lista de indices para "palavra_unica", que sera uma 
        # lista de numeros de 0 ate o comprimento de "palavra_unica" menos 1

        numeros_decimais = [indices_para_decimal(indices) for indices in indices_palavras]  
        # Converte cada lista de indices em "indices_palavras" em um numero 
        # decimal e armazena em "numeros_decimais"
        numero_decimal_palavra_unica = indices_para_decimal(indices_palavra_unica)  
        # Converte a lista de indices de "palavra_unica" em um numero decimal
        subtracao = numeros_decimais[2] - (numeros_decimais[0] + numeros_decimais[1])  
        # Realiza a subtracao do terceiro numero decimal com a soma dos dois 
        # primeiros numeros decimais e armazena o resultado em "subtracao"

        vetores = []  # Inicializa uma lista vazia chamada "vetores"
        for _ in range(100):  # Inicia um loop que sera repetido 100 vezes
            indices_palavras_aleatorios = [ 
    # Cria uma lista "indices_palavras_aleatorios" que contem permutacoes 
    # aleatorias dos indices das palavras originais
                np.random.permutation(indices_palavras[0]),  
                # Permutacao aleatoria dos indices da primeira palavra
                np.random.permutation(indices_palavras[1]),  
                # Permutacao aleatoria dos indices da segunda palavra
                np.random.permutation(indices_palavras[2])   
                # Permutacao aleatoria dos indices da terceira palavra
            ]
            subtracao_aleatoria = indices_para_decimal(indices_palavras_aleatorios[2]) - ( 
  # Calcula a subtracao do numero decimal correspondente aos indices 
  # permutados da terceira palavra menos a soma dos numeros decimais das duas primeiras palavras permutadas
                indices_para_decimal(indices_palavras_aleatorios[0]) + indices_para_decimal(indices_palavras_aleatorios[1])  
                # Soma dos numeros decimais das duas primeiras palavras permutadas
            )
            vetor_com_palavra_unica = np.concatenate([indices_palavra_unica, indices_palavras_aleatorios[1]]) 
            # Combina os indices de "palavra_unica" com os indices permutados da segunda palavra
            vetor_com_palavra_unica = np.unique(vetor_com_palavra_unica)  
            # Remove os elementos duplicados em "vetor_com_palavra_unica"
            np.random.shuffle(vetor_com_palavra_unica)  
            # Embaralha aleatoriamente os elementos de "vetor_com_palavra_unica"

            vetor_mutado = vetor_com_palavra_unica.copy()  
            # Cria uma copia de "vetor_com_palavra_unica" chamada "vetor_mutado"
            pos1, pos2 = np.random.choice(len(vetor_mutado), 2, replace=False)  
            # Seleciona aleatoriamente duas posicoes diferentes em "vetor_mutado"
            vetor_mutado[pos1], vetor_mutado[pos2] = vetor_mutado[pos2], vetor_mutado[pos1]  
            # Troca os elementos nas posicoes "pos1" e "pos2" em "vetor_mutado"

            vetores.append((vetor_com_palavra_unica, vetor_mutado, subtracao_aleatoria)) 
            # Adiciona uma tupla com "vetor_com_palavra_unica", "vetor_mutado", 
            # e "subtracao_aleatoria" à lista "vetores"

        resultado = f"Palavra Formada: {palavra_unica}\n" 
        # Inicia a string "resultado" com a "palavra_unica" formada
        posicoes_letras = [f"{letra}: {i}" for i, letra in enumerate(palavra_unica)]  
        # Cria uma lista "posicoes_letras" que mapeia cada letra de "palavra_unica" para sua posicao
        resultado += "Posicao das Letras na Palavra Formada:\n" + "\n".join(posicoes_letras) + "\n" 
        # Adiciona as posicoes das letras à string "resultado"

        
    for i, (palavra, indices) in enumerate(zip(palavras, indices_palavras)): 
           # Loop sobre as palavras e seus indices associados, obtendo o indice "i" e o par (palavra, indices)
            resultado += f"\nPalavra {i + 1}: {palavra}\nIndices: {indices}\nNumero Decimal: {indices_para_decimal(indices)}" 
            # Adiciona informacoes sobre cada palavra, seus indices e o numero decimal correspondente 
            # à string "resultado"
            resultado += f"\n\nfitness: = {subtracao}"  
            # Adiciona a informacao sobre o fitness, que e a subtracao calculada, à string "resultado"

            with open("resultado.txt", "w") as file:  
                # Abre ou cria um arquivo chamado "resultado.txt" em modo de escrita
                file.write(resultado)  
                # Escreve o conteudo de "resultado" no arquivo
            resultado_label.config(text=resultado) 
            # Atualiza o texto do label "resultado_label" com o conteudo da string "resultado"

# Função para gerar vetores aleatórios
def gerarVetores(num_vetores, tamanho_vetor, num_range=10):  
    # Define uma funcao chamada "gerarVetores" que recebe tres parametros: 
    # "num_vetores", "tamanho_vetor", e "num_range" com valor padrao 10
    vetores = []  # Inicializa uma lista vazia chamada "vetores"
    for _ in range(num_vetores):  
        # Inicia um loop que sera repetido "num_vetores" vezes
        vetor = random.sample(range(num_range), tamanho_vetor)  
# Cria uma lista "vetor" com "tamanho_vetor" elementos distintos aleatorios no intervalo de 0 a "num_range"-1
        vetores.append(vetor)  # Adiciona o "vetor" gerado à lista "vetores"
    return vetores  # Retorna a lista "vetores" contendo todos os vetores gerados


# Função para converter um vetor em um número inteiro com base nas posições fornecidas
def converterParaInt(vetor, posicoes):  
    # Define uma funcao chamada "converterParaInt" que recebe dois parametros: "vetor" e "posicoes"
    digitos_selecionados = [vetor[pos] for pos in posicoes] 
    # Cria uma lista "digitos_selecionados" contendo os elementos do "vetor"
    # nas posicoes especificadas pela lista "posicoes"
    concatenado_str = ''.join(map(str, digitos_selecionados)) 
    # Converte os elementos de "digitos_selecionados" para strings 
    # e os une em uma unica string chamada "concatenado_str"
    resultadoInt = int(concatenado_str)  
    # Converte a string "concatenado_str" para um inteiro e armazena em "resultadoInt"
    return resultadoInt  # Retorna o valor inteiro "resultadoInt"

# Função para realizar a mutação em um vetor
def mutacao(vetor):  # Define uma funcao chamada "mutacao" que recebe um parametro "vetor"
    vetor_copia = vetor.copy()  # Cria uma copia do "vetor" chamada "vetor_copia"
    i, j = random.sample(range(len(vetor_copia)), 2)  
    # Seleciona aleatoriamente dois indices distintos "i" e "j" 
    # dentro do intervalo do comprimento de "vetor_copia"
    vetor_copia[i], vetor_copia[j] = vetor_copia[j], vetor_copia[i] 
    # Troca os elementos nas posicoes "i" e "j" em "vetor_copia"
    return vetor_copia  # Retorna a lista "vetor_copia" com os elementos trocados

# Função de avaliação de fitness dos vetores
def fitness(vetores, palavra1, palavra2, palavra3, unigram, imprimir): 
    # Define uma funcao chamada "fitness" que recebe cinco parametros: 
    # "vetores", "palavra1", "palavra2", "palavra3", "unigram" e "imprimir"
    vetorpalavra1 = identificar(palavra1, unigram)  
    # Chama a funcao "identificar" com "palavra1" e "unigram" e armazena o resultado em "vetorpalavra1"
    vetorpalavra2 = identificar(palavra2, unigram)  
    # Chama a funcao "identificar" com "palavra2" e "unigram" e armazena o resultado em "vetorpalavra2"
    vetorpalavra3 = identificar(palavra3, unigram)  
    # Chama a funcao "identificar" com "palavra3" e "unigram" e armazena o resultado em "vetorpalavra3"

    resultados = []  # Inicializa uma lista vazia chamada "resultados"

    for idx, vetor in enumerate(vetores):  
        # Loop sobre "vetores", obtendo o indice "idx" e o vetor correspondente "vetor"
        palavra1 = converterParaInt(vetor, vetorpalavra1)  
        # Converte o "vetor" usando "vetorpalavra1" para um inteiro e armazena em "palavra1"
        palavra2 = converterParaInt(vetor, vetorpalavra2)  
        # Converte o "vetor" usando "vetorpalavra2" para um inteiro e armazena em "palavra2"
        palavra3 = converterParaInt(vetor, vetorpalavra3)  
        # Converte o "vetor" usando "vetorpalavra3" para um inteiro e armazena em "palavra3"
        fitnessVetor = palavra3 - (palavra1 + palavra2)  
        # Calcula o fitness do vetor como a subtracao de "palavra1" e "palavra2" de "palavra3"
    
        resultados.append((fitnessVetor, vetor))  
        # Adiciona uma tupla contendo "fitnessVetor" e "vetor" à lista "resultados"
    
    resultadosOrdenados = sorted(resultados, key=lambda x: abs(x[0]))  
    # Ordena a lista "resultados" com base no valor absoluto 
    # do primeiro elemento de cada tupla (o fitness), armazenando o resultado em "resultadosOrdenados"
    if imprimir == 1:  # Verifica se o parametro "imprimir" é igual a 1
        for idx, (fitnessVetor, vetor) in enumerate(resultadosOrdenados, start=1):  
            # Loop sobre "resultadosOrdenados", obtendo o indice "idx" e a tupla (fitnessVetor, vetor),
            # começando a contagem do indice a partir de 1
            print(f"Vetor {idx}: {vetor} Fitness: {fitnessVetor}") 
            # Imprime o vetor e seu valor de fitness formatado com o indice correspondente
    
    return resultadosOrdenados  # Retorna a lista "resultadosOrdenados"


# Função de seleção por torneio
def torneio(vetores, tamanho_torneio=3): 
    # Define uma funcao chamada "torneio" que recebe dois parametros: "vetores" e
    # "tamanho_torneio" com valor padrao 3
    pais_selecionados = []  # Inicializa uma lista vazia chamada "pais_selecionados"
    for _ in range(len(vetores)): 
        # Inicia um loop que sera repetido o numero de vezes igual ao comprimento de "vetores"
        competidores = random.sample(vetores, tamanho_torneio)  
        # Seleciona aleatoriamente "tamanho_torneio" vetores da lista "vetores" para competir
        melhor = min(competidores, key=lambda x: abs(x[0]))  
        # Encontra o vetor com o menor valor absoluto de fitness entre os "competidores"
        pais_selecionados.append(melhor[1]) 
        # Adiciona o segundo elemento (o vetor) da tupla "melhor" à lista "pais_selecionados"
    return pais_selecionados  # Retorna a lista "pais_selecionados" contendo os vetores selecionados

# Função de seleção por roleta
def roleta(vetores):  # Define uma funcao chamada "roleta" que recebe um parametro "vetores"
    if not vetores:  # Verifica se a lista "vetores" esta vazia
        return []  # Retorna uma lista vazia se "vetores" estiver vazia
    
    aptidoes, individuos = zip(*vetores)  # Descompacta "vetores" em duas listas: "aptidoes" e "individuos"
    aptidao_total = sum(aptidoes)  # Calcula a soma total das aptidoes
    probabilidades = [apt / aptidao_total for apt in aptidoes]  
    # Calcula a probabilidade relativa de cada individuo com base na sua aptidao
    
    limites_acumulados = []  # Inicializa uma lista vazia chamada "limites_acumulados"
    acumulado = 0  # Inicializa a variavel "acumulado" com 0
    for prob in probabilidades:  # Loop sobre cada probabilidade
        acumulado += prob  # Adiciona a probabilidade ao acumulado
        limites_acumulados.append(acumulado)  # Adiciona o acumulado à lista "limites_acumulados"
    
    pais_selecionados = []  # Inicializa uma lista vazia chamada "pais_selecionados"
    for _ in range(len(vetores)):  
        # Loop que sera repetido o numero de vezes igual ao comprimento de "vetores"
        r = random.random()  # Gera um numero aleatorio "r" no intervalo [0, 1)
        for i, limite in enumerate(limites_acumulados):  # Loop sobre os limites acumulados
            if r <= limite:  # Verifica se o numero aleatorio "r" e menor ou igual ao limite acumulado
                pais_selecionados.append(individuos[i])  
                # Adiciona o individuo correspondente ao limite acumulado na lista "pais_selecionados"
                break  # Sai do loop se o individuo foi selecionado
    return pais_selecionados  # Retorna a lista "pais_selecionados" contendo os individuos selecionados

# Função para aplicar mutação nos vetores com uma certa taxa de mutação
def mutacaoFitness(vetores, taxaMutacao):  # Define uma funcao chamada "mutacaoFitness" 
    #que recebe dois parametros: "vetores" e "taxaMutacao"
    indicesMutacao = []  # Inicializa uma lista vazia chamada "indicesMutacao"
    taxaMutacao = round((taxaMutacao * len(vetores)) / 100) 
    # Calcula o numero de vetores a serem mutados com base na "taxaMutacao" e no comprimento de "vetores"
    indicesMutacao = random.sample(range(len(vetores)), taxaMutacao)  
    # Seleciona aleatoriamente "taxaMutacao" indices distintos dentro do 
    # intervalo do comprimento de "vetores"
    for index in indicesMutacao:  # Loop sobre cada indice em "indicesMutacao"
        vetores[index] = mutacao(vetores[index])  # Aplica a funcao de mutacao ao vetor no indice
        #correspondente e atualiza "vetores"
    return vetores  # Retorna a lista "vetores" com as mutacoes aplicadas

# Função de crossover cíclico
def crossoverCiclico(pais, taxaCrossover):  # Define uma funcao chamada "crossoverCiclico"
    #que recebe dois parametros: "pais" e "taxaCrossover"
    filhos = []  # Inicializa uma lista vazia chamada "filhos"
    for i in range(0, len(pais) - 1, 2):  # Loop sobre os indices dos pais, de dois em dois, 
        #começando do zero
        if random.random() < taxaCrossover:  # Verifica se um numero aleatorio gerado e
            #menor que a "taxaCrossover"
            pai1 = pais[i]  # Seleciona o pai na posicao "i"
            pai2 = pais[i + 1]  # Seleciona o pai na posicao "i + 1"
            filho1 = pai1.copy()  # Cria uma copia do pai1 chamada "filho1"
            filho2 = pai2.copy()  # Cria uma copia do pai2 chamada "filho2"
            
            ciclico = [0]  # Inicializa uma lista "ciclico" com o primeiro indice 0
            while True:  # Inicia um loop infinito
                idx = ciclico[-1]  # Define o indice atual como o ultimo valor da lista "ciclico"
                if pai2[idx] in pai1:  # Verifica se o valor em "pai2" no indice "idx" esta em "pai1"
                    idx = pai1.index(pai2[idx])  # Atualiza o indice "idx" para a posicao do valor
                    #correspondente em "pai1"
                    if idx in ciclico:  # Verifica se o novo indice "idx" ja esta na lista "ciclico"
                        break  # Se estiver, sai do loop
                    ciclico.append(idx)  # Adiciona o novo indice à lista "ciclico"
                else:  # Caso o valor nao esteja em "pai1"
                    break  # Sai do loop
            
            for idx in ciclico:  # Loop sobre cada indice em "ciclico"
                filho1[idx], filho2[idx] = filho2[idx], filho1[idx]  
                # Troca os valores nos indices correspondentes entre "filho1" e "filho2"
            
            filhos.append(filho1)  # Adiciona "filho1" à lista "filhos"
            filhos.append(filho2)  # Adiciona "filho2" à lista "filhos"
        else:  # Se a taxa de crossover nao for satisfeita
            filhos.append(pais[i].copy())  # Adiciona uma copia do pai na posicao "i" à lista "filhos"
            filhos.append(pais[i + 1].copy())  # Adiciona uma copia do pai na posicao "i + 1" 
            #à lista "filhos"
    
    return filhos  # Retorna a lista "filhos" contendo os filhos gerados


# Função de crossover PMX (Partially Mapped Crossover)
def pmxCrossover(pai1, pai2):  # Define uma funcao chamada "pmxCrossover" 
    #que recebe dois parametros: "pai1" e "pai2"
    tamanho = len(pai1)  # Armazena o comprimento de "pai1" em "tamanho"
    pontos_crossover = sorted(random.sample(range(tamanho), 2))  
    # Seleciona aleatoriamente dois pontos de crossover e os ordena
    inicio_crossover, fim_crossover = pontos_crossover[0], pontos_crossover[1]  
    # Define os pontos de inicio e fim do crossover

    filho1, filho2 = pai1[:], pai2[:]  # Cria copias de "pai1" e "pai2" chamadas "filho1" e "filho2"

    mapeamento1 = {}  # Inicializa um dicionario vazio chamado "mapeamento1"
    mapeamento2 = {}  # Inicializa um dicionario vazio chamado "mapeamento2"

    for i in range(inicio_crossover, fim_crossover):  
        # Loop sobre o intervalo definido pelos pontos de crossover
        filho1[i] = pai2[i]  # Copia o valor de "pai2" para "filho1" no indice "i"
        filho2[i] = pai1[i]  # Copia o valor de "pai1" para "filho2" no indice "i"
        mapeamento1[pai2[i]] = pai1[i]  # Adiciona um mapeamento de "pai2[i]" para "pai1[i]" em "mapeamento1"
        mapeamento2[pai1[i]] = pai2[i]  # Adiciona um mapeamento de "pai1[i]" para "pai2[i]" em "mapeamento2"

    def reparar(child, mapeamento):  # Define uma funcao chamada "reparar" 
        #que corrige o filho com base no mapeamento fornecido
        for i in range(tamanho):  # Loop sobre todos os indices do "child"
            if i < inicio_crossover or i >= fim_crossover:  
                # Verifica se o indice esta fora do intervalo de crossover
                while child[i] in mapeamento:  # Enquanto o valor no indice "i" estiver no mapeamento
                    child[i] = mapeamento[child[i]]  # Substitui o valor no indice "i" com o valor mapeado

    reparar(filho1, mapeamento1)  # Aplica a funcao "reparar" ao "filho1" com o "mapeamento1"
    reparar(filho2, mapeamento2)  # Aplica a funcao "reparar" ao "filho2" com o "mapeamento2"

    return filho1, filho2  # Retorna os dois filhos gerados


# Função para aplicar crossover na população
def crossoverPopulacao(pais_selecionados, taxaCrossover):  
    # Define uma funcao chamada "crossoverPopulacao" que recebe dois parametros: "pais_selecionados" 
    # e "taxaCrossover"
    proxima_geracao = []  # Inicializa uma lista vazia chamada "proxima_geracao"
    for i in range(0, len(pais_selecionados), 2): 
        # Loop sobre os indices de "pais_selecionados", de dois em dois
        if i + 1 < len(pais_selecionados):  # Verifica se existe um pai "i + 1" para formar um par
            if random.random() < taxaCrossover: 
                # Verifica se um numero aleatorio gerado e menor que a "taxaCrossover"
                filho1, filho2 = pmxCrossover(pais_selecionados[i], pais_selecionados[i+1])  
                # Aplica o crossover PMX aos pais selecionados
                proxima_geracao.append(filho1)  # Adiciona o "filho1" à lista "proxima_geracao"
                proxima_geracao.append(filho2)  # Adiciona o "filho2" à lista "proxima_geracao"
            else:  # Se a taxa de crossover nao for satisfeita
                proxima_geracao.append(pais_selecionados[i])  
                # Adiciona o pai na posicao "i" à lista "proxima_geracao"
                proxima_geracao.append(pais_selecionados[i+1])  
                # Adiciona o pai na posicao "i + 1" à lista "proxima_geracao"
        else:  # Se nao houver um pai "i + 1" (caso o numero de pais seja impar)
            proxima_geracao.append(pais_selecionados[i]) 
            # Adiciona o pai na posicao "i" à lista "proxima_geracao"
    return proxima_geracao  # Retorna a lista "proxima_geracao" contendo a nova geracao de pais

# Função principal do algoritmo genético
def run_genetic_algorithm():  # Define uma funcao chamada "run_genetic_algorithm"
    palavra1 = palavra_entrada1.get().upper()  
    # Obtém o valor da entrada "palavra_entrada1", converte para maiúsculas e armazena em "palavra1"
    palavra2 = palavra_entrada2.get().upper()  
    # Obtém o valor da entrada "palavra_entrada2", converte para maiúsculas e armazena em "palavra2"
    palavra3 = palavra_entrada3.get().upper() 
    # Obtém o valor da entrada "palavra_entrada3", converte para maiúsculas e armazena em "palavra3"
    
    if not palavra1.isalpha() or not palavra2.isalpha() or not palavra3.isalpha():  
        # Verifica se todas as palavras contêm apenas letras
        messagebox.showerror("Erro", "Por favor, insira palavras válidas.")  
        # Exibe uma mensagem de erro se qualquer palavra for inválida
        return  # Encerra a função

    unigram = sorted(set(palavra1 + palavra2 + palavra3))  
    # Cria uma lista de letras únicas presentes nas palavras e a ordena
    numVec = 100  # Define o número de vetores como 100
    tamanhoGeracao = 50  # Define o tamanho da geração como 50
    taxaCrossover = 0.8  # Define a taxa de crossover como 0.7
    taxaMutacao = 5  # Define a taxa de mutacao como 5%

    with open("resultado_algoritmo_genetico.txt", "w") as file:  
        # Abre o arquivo "resultado_algoritmo_genetico.txt" para escrita
        for geracao in range(tamanhoGeracao):  # Loop sobre o número de gerações
            vetores = gerarVetores(numVec, len(unigram)) 
           # Gera vetores aleatórios para a geração atual
            resultadosFitness = fitness(vetores, palavra1, palavra2, palavra3, unigram, 0)  
            # Calcula o fitness dos vetores

            file.write(f"Geração {geracao + 1}:\n")  # Escreve o número da geração no arquivo
            for idx, (fitnessVetor, vetor) in enumerate(resultadosFitness, start=1):  
                # Loop sobre os resultados de fitness
                file.write(f"Vetor {idx}: {vetor} Fitness: {fitnessVetor}\n")  
                # Escreve cada vetor e seu fitness no arquivo

            metodo_selecao = selecao_var.get()  # Obtém o método de seleção escolhido
            if metodo_selecao == "Torneio":  # Se o método de seleção for Torneio
                pais_selecionados = torneio(resultadosFitness)  # Seleciona pais usando o método de torneio
            else:  # Caso contrário, usa o método de Roleta
                pais_selecionados = roleta(resultadosFitness)  # Seleciona pais usando o método de roleta

            metodo_crossover = crossover_var.get()  # Obtém o método de crossover escolhido
            if metodo_crossover == "PMX":  # Se o método de crossover for PMX
                filhos = crossoverPopulacao(pais_selecionados, taxaCrossover)  
                # Gera filhos usando o crossover PMX
            else:  # Caso contrário, usa o crossover Cíclico
                filhos = crossoverCiclico(pais_selecionados, taxaCrossover)  
                # Gera filhos usando o crossover Cíclico

            proxima_geracao = mutacaoFitness(filhos, taxaMutacao)  
            # Aplica mutação aos filhos para criar a próxima geração
            resultadosFitness = fitness(proxima_geracao, palavra1, palavra2, palavra3, unigram, 0)  
            # Calcula o fitness da nova geração
            file.write("\n")  # Adiciona uma linha em branco no arquivo

        melhor_solucao = resultadosFitness[0]  # Obtém a melhor solução final da última geração
        resultado_texto = f"Melhor Solução Final:\nVetor: {melhor_solucao[1]}\nFitness: {melhor_solucao[0]}"  
        # Formata o texto com a melhor solução e seu fitness
        file.write(resultado_texto)  # Escreve a melhor solução no arquivo
        
    resultado_label.config(text="Algoritmo Executado com Sucesso! Resultado salvo em resultado_algoritmo_genetico.txt") 
    # Atualiza o texto do rótulo com uma mensagem de sucesso

# Função para identificar a posição das letras no unigram
def identificar(palavra, unigram):
    return [unigram.index(char) for char in palavra]

# Configuração da interface gráfica (Tkinter)
janela = tk.Tk()  # Cria uma nova janela principal
janela.title("Decodificador de Criptogramas")  # Define o título da janela

# Adiciona um rótulo "Palavra 1:" e o posiciona na linha 0, coluna 0
tk.Label(janela, text="Palavra 1:").grid(row=0, column=0)
# Cria uma entrada de texto para a primeira palavra e a posiciona na linha 0, coluna 1
palavra_entrada1 = tk.Entry(janela)
palavra_entrada1.grid(row=0, column=1)

# Adiciona um rótulo "Palavra 2:" e o posiciona na linha 1, coluna 0
tk.Label(janela, text="Palavra 2:").grid(row=1, column=0)
# Cria uma entrada de texto para a segunda palavra e a posiciona na linha 1, coluna 1
palavra_entrada2 = tk.Entry(janela)
palavra_entrada2.grid(row=1, column=1)

# Adiciona um rótulo "Palavra 3:" e o posiciona na linha 2, coluna 0
tk.Label(janela, text="Palavra 3:").grid(row=2, column=0)
# Cria uma entrada de texto para a terceira palavra e a posiciona na linha 2, coluna 1
palavra_entrada3 = tk.Entry(janela)
palavra_entrada3.grid(row=2, column=1)

# Define variáveis para os métodos de crossover e seleção com valores padrão
crossover_var = tk.StringVar(value="PMX")
selecao_var = tk.StringVar(value="Torneio")

# Adiciona um rótulo "Método de Crossover:" e o posiciona na linha 3, coluna 0
tk.Label(janela, text="Método de Crossover:").grid(row=3, column=0)
# Adiciona um botão de rádio para o método de crossover "PMX" e o posiciona na linha 3, coluna 1
tk.Radiobutton(janela, text="PMX", variable=crossover_var, value="PMX").grid(row=3, column=1)
# Adiciona um botão de rádio para o método de crossover "Cíclico" e o posiciona na linha 3, coluna 2
tk.Radiobutton(janela, text="Cíclico", variable=crossover_var, value="Cíclico").grid(row=3, column=2)

# Adiciona um rótulo "Método de Seleção:" e o posiciona na linha 4, coluna 0
tk.Label(janela, text="Método de Seleção:").grid(row=4, column=0)
# Adiciona um botão de rádio para o método de seleção "Torneio" e o posiciona na linha 4, coluna 1
tk.Radiobutton(janela, text="Torneio", variable=selecao_var, value="Torneio").grid(row=4, column=1)
# Adiciona um botão de rádio para o método de seleção "Roleta" e o posiciona na linha 4, coluna 2
tk.Radiobutton(janela, text="Roleta", variable=selecao_var, value="Roleta").grid(row=4, column=2)

# Adiciona um botão "Processar Palavras" que chama a função "processar_palavras" e o posiciona na linha 5,
# coluna 0, com expansão em 3 colunas
tk.Button(janela, text="Processar Palavras", command=processar_palavras).grid(row=5, column=0, columnspan=3)
# Adiciona um botão "Executar Algoritmo Genético" que chama a função "run_genetic_algorithm" 
# e o posiciona na linha 6, coluna 0, com expansão em 3 colunas
tk.Button(janela, text="Executar Algoritmo Genético", command=run_genetic_algorithm).grid(row=6, column=0, columnspan=3)

# Adiciona um rótulo para mostrar o resultado e o posiciona na linha 7, coluna 0, com expansão em 3 colunas
resultado_label = tk.Label(janela, text="")
resultado_label.grid(row=7, column=0, columnspan=3)

# Inicia o loop principal da interface gráfica
janela.mainloop()

