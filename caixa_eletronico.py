print('##' * 20)
print('BEM VINDO AO BANCO XERECARD')
print('##' * 20)
valor = int(input('Quanto gostaria de sacar? '))
print('=-=-' * 20)
print('AGUARDE A CONTAGEM DAS CÉDULAS')
print('=-=-' * 20)
total = valor
ced = 100
totced = 0
while True:
    if total >= ced:
        total -= ced
        totced += 1
    else:
        if totced > 0:
            print('Total de {} cédulas de {} R$'.format(totced, ced))
        if ced == 100:
            ced = 50
        elif ced == 50:
            ced = 20
        elif ced == 20:
            ced = 10
        elif ced == 10:
            ced = 5
        elif ced == 5:
            ced = 2
        elif ced == 2:
            ced = 1
        totced = 0
        if total == 0:
            break
print('=-=-' * 20)
print('OBRIGADO POR USAR O XERECARD')
print('=-=-' * 20)
