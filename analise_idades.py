idades = []
maior_masculino = 0
nome_masculino = 0
feminino = 0
for a in range(1,5):
    print(f'**** {a}ª PESSOA ****')
    nome = str(input(f'digite o nome da {a}ª pessoa:')).capitalize()
    idade = int(input(f'digite a idade do(a) {nome}:'))
    sexo = str(input(f'sexo {nome}, M ou F:')).lower()
    idades += [idade]
    media = sum(idades) /4
    if sexo == 'm' and idade > maior_masculino:
        maior_masculino = idade
        nome_masculino = nome
    elif sexo == 'f' and idade<20:
        feminino += 1
print(f'A média das idades é {media:.1f}\nO homem mais velho é {nome_masculino} e tem {maior_masculino}anos\nhá {feminino} mulher(es) com idade menor que 20 anos')