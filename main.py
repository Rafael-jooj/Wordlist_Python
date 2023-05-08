import itertools

# Conjunto de palavras utilizadas no arquivo output1.txt
# palavras_chave = ['segurança', 'auditoria', 'sistemas', 'root', 'password', '123']

tamanho_input = int(input("Quantas palavras-chave deseja inserir? "))
palavras_chave = []
wordlist = []

#Interface interativa com o usuário
for i in range(tamanho_input):
    entrada = str(input("Insira a "+ str(i+1) +"° palavra-chave: "))
    palavras_chave.append(entrada)


#Inserção dos próprios parametros de entrada
for i in range(len(palavras_chave)):
    wordlist.append(palavras_chave[i])


#Mesclagem dos parametros de entrada
for i in range(2, len(palavras_chave), 1):
    for comb in itertools.combinations(palavras_chave, i):
        wordlist.append("".join(comb))
        wordlist.append("_".join(comb))
        wordlist.append("".join(reversed(comb)))
        wordlist.append("_".join(reversed(comb)))


#Combinações dos parametros de entrada
for word in palavras_chave:
    for i in range(len(word)):
        for j in range(len(palavras_chave)):
            if j != palavras_chave.index(word):
                wordlist.append(word[:i] + palavras_chave[j] + word[i:])
    

arquivo = open('output.txt', 'w', encoding='utf-8')
for k in range(len(wordlist)):
    arquivo.writelines(wordlist[k]+'\n')

print(wordlist)