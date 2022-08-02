somaidade = 0
mediaidade = 0
nomevelho = ''
maioridadehomen = 0
mulher20 = 0
for p in range (1, 5):
    print(f'-------{p}ª PESSOA-------')
    nome = str(input('Nome:')).strip()
    idade = int(input('Idade:'))
    sexo = str(input('Sexo [F/M]:')).strip()
    somaidade += idade
    if p == 1 and sexo in 'Mm':
        maioridadehomen = idade
        nomevelho = nome
    if sexo in 'Mm' and idade > maioridadehomen:
        maioridadehomen = idade
        nomevelho = nome
    if sexo in 'Ff' and idade < 20:
        mulher20 += 1

mediaidade = somaidade / 4
print(f'A média da idade do grupo é {mediaidade}')
print(f'A idade do homem mais velho é {maioridadehomen} anos e ele se chama {nomevelho}')
print(f'Ao todo são {mulher20} mulheres com menos de 20 anos')
