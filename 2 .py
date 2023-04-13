num = int(input("Digite um Número:"))
fibonacci = [0,1]
for i in range(2, num):
        proximo = fibonacci[i-1] + fibonacci[i-2]
        fibonacci.append(proximo)

if num in fibonacci:
        print('O Número é encontrado na Sequência!')
else:
        print("O Número não se encontra na Sequência!")