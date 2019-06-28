def vota(n):
    from datetime import date
    atual = date.today().year
    idade = atual - n
    if idade < 16:
        return 'Com ' + str(idade) + ' anos: NÃO VOTA'
    elif 18 <= idade <= 65:
        return 'Com ' + str(idade) + ' anos: VOTO OBRIGATÓRIO'
    else:
        return 'Com ' + str(idade) + ' anos: VOTO OPCIONAL'


ano = int(input('Em qual ano você nasceu? '))
print(vota(ano))
