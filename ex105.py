def boletim(*notas, situacao=False):
    """
    -> Análise de notas e situação do aluno
    :param notas: uma ou várias notas de um aluno
    :param situacao: opcional, mostra se a situação do aluno ésta BOA, RAZOÁVEL ou RUIM
    :return: retorna um dicionário com informações sobre a situação do aluno
    """
    apv = dict()
    apv['total'] = len(notas)
    apv['Maior'] = max(notas)
    apv['Menor'] = min(notas)
    apv['Media'] = sum(notas) / len(notas)
    if situacao:
        if apv['Media'] < 5:
            apv['Situacao'] = 'Ruim'
        elif apv['Media'] < 8:
            apv['Situacao'] = 'Razoável'
        else:
            apv['Situacao'] = 'Boa'
    return apv


resp = boletim(6.5, 9, 9, 9, 10, 10, 6.5, situacao=True)
print(resp)
help(boletim)
