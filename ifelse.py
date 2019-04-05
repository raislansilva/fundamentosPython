nome = input("Nome do Aluno: ")
nota1 = float(input("Nota da prova 1: "))
nota2 = float(input("Nota da prova 2: "))
faltas = int(input("Total de faltas: "))

media = float(nota1+nota2)/2
presenca = 100 - float(faltas*100)/20
resultado = ""

if media >= 6 and presenca >= 70:
    resultado = "Aprovado"
elif media < 6 and presenca < 70:
    resultado = "Reprovado por faltas e por média"
elif media >= 6 and presenca < 70 :
    resultado = "Reprovado por faltas" 
elif media < 6 and presenca >= 70:
    resultado = "Reprovado por média"   

print(nome)
print(media)
print(presenca,'%')    
print(resultado)