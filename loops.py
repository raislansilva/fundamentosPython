#break = sair do loop
#continue =  não executa a instrução que há depois dele e continua o loop
#not in array = para o loop quando o array tiver determinado elemento
#range

controle = "s"
fatura = []
precoTotal = 0
valid_preco = False

while controle == "s":
    produto= input("Nome do Produto: ")

    while valid_preco == False:
        preco = input("Preco do Produto: ")

        try:
            preco = float(preco)
            if preco <= 0:
                print("O preço tem que ser maio que 0")
            else:
                valid_preco =True
        except:
            print("Formato Inválido! Digite somente números")

    precoTotal+=preco
    fatura.append([produto,preco]) ## a lista fatura esta recebendo outra lista
    valid_preco = False
    controle = input("Você deseja comprar mais algum produto? s n ").lower()

print("========================== Fatura de Produtos =======================================")
#for i in fatura:
    #for item in i:
        #if aux>0:
             #print("Preco do produto:",item)
        #else:
             #print("Nome do produto:",item,end="          ")
        #aux+=1
    #aux = 0    
    #print("-------------------------------------------------------------------------------------")
for i in fatura:
    print(i[0],'-',i[1])

print ("Preco Total:",precoTotal)
   