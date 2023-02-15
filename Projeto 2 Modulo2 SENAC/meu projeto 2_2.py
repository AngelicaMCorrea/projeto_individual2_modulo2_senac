print( "PROJETO INDIVIDUAL 02 MÓDULO 02" )
print( "ANGÉLICA MONTEIRO" )
print ( "#" * 30 )

def varrendoCurriculos(): # função para checar se temos as palavras-chave necessárias e marcar como um candidato válido para a vaga
    print("#"*30)
    print("PROCURA DE CANDIDATOS POR VAGA")
    for key in todosCurriculos:
        varreduraCur = []
        pergunta = input("Qual o cargo procurado?: ")
        pergunta = pergunta.lower()
       
        if pergunta  == "python" or "programação" or "desenvolvimento" or "análise de dados" or "dados" or "sql" in key:
            varreduraCur.append(todosCurriculos.get(cargo,nome))
        print("Candidatos habilitados para a vaga: ", varreduraCur)
        break

def quantCurrPalavra(): # função que procura na minibios alguma das palavras chaves
        cont = 0
        
        for i in range(len(texto)):
            for j in range(len(palavrasChaves)):
                if palavrasChaves[j] in texto[i]:    
                    cont = cont+1 
                else:
                    cont = cont
                    
        print("QUANTIDADE DE CANDIDATOS COM A PALAVRA CHAVE NA BIOS: ", cont)
            

candidato = ()
todosCurriculos = {}
texto = []
quantCurriculos =[]
palavrasChaves = ("python", "programação", "desenvolvimento", "análise de dados", "dados", "sql")

while candidato != "0": #cadastro do candidato em looping até que se digite 0
    cargo = input ( "Insira o cargo pretendido: " )
    nome = input ( "Insira o nome do candidato: " )
    miniBios = input("Faça aqui um resumo de sua vida profissional: ")  # O texto do resumo/minibio vai ser informado pelo usuário
    
    miniBios.lower()
    miniBios.replace(","," ")
    miniBios.replace("."," ")
    prov = miniBios.split()
    texto.append(prov)

    todosCurriculos[cargo, nome] = [miniBios]

    candidato = (input("Para continuar digite qualquer tecla ou 0 (zero) para fim do cadastro de candidatos :"))

    
    with open("bios.txt", "w", encoding= "utf-8") as curriculo: # texto de arquivos txt que armazena a minibio
        curriculo.write(miniBios)
    with open("bios.txt", "r", encoding= "utf-8") as curriculo:
        miniBios = curriculo.readlines()
    print(miniBios)


    print ( "#" * 30 )
    print("TODOS OS CURRICULOS",todosCurriculos)
    print ( "#" * 30 )
    print("QUANT CURRICULOS", quantCurriculos)
    print ( "#" * 30 )
            
    
cadCurriculos = []

for cargo, nome in todosCurriculos: #quantas pessoas estão inscritas em cada vaga
    cadCurriculos.append(cargo)
procCurriculos = {}
for cargo, nome in todosCurriculos:
    procCurriculos[cargo] = cadCurriculos.count(cargo)
print (cadCurriculos)
print("Quantidade de candidatos por vaga: ",procCurriculos)


varrendoCurriculos()

quantCurrPalavra()