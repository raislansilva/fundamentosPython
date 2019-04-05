meses = ('Janeiro', 'Fevereiro','Março','Abril','Maio','Junho','Julho','Agosto','Setembro','Outubro','Novembro','Dezembro')
data_nascimento = input("Data de Nascimento: ")
indice = int(data_nascimento[2:4])-1
mes = meses[indice]

#lista["raislan","fulano"]

print ("Você nasceu no mês de", mes)