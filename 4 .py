#Dado o valor de faturamento mensal de uma distribuidora, detalhado por estado:

#SP – R$67.836,43
#RJ – R$36.678,66
#MG – R$29.229,88
#ES – R$27.165,48
#Outros – R$19.849,53

#Escreva um programa na linguagem que desejar onde calcule o percentual de representação 
#que cada estado teve dentro do valor total mensal da distribuidora.


faturamento = [['SP',67836.43],['RJ',36678.66],['MG',29229.88],['ES',27165.48],['Outros',19849.53]]
total = 0
cont = (len(faturamento))

for i in range(cont):
    total += faturamento[i][1]
    percentual = (faturamento[i][1]/total)*100
    print('O Estado ',faturamento[i][0],'Teve o Percentual de {:.2f}%, do Faturamento Mensal'.format(percentual))
    print('O Faturamento Total foi de',total,'Reais')