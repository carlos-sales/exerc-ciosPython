aluno = dict()
aluno['nome'] = str(input('Nome: ').strip())
aluno['media'] = float(input(f'Média de {aluno["nome"]}: '))
aluno['situacao'] = 'Aprovado' if aluno['media'] >= 6 else 'Reprovado'
print(f'Nome do(a) aluno(a): {aluno["nome"]}')
print(f'Sua média é {aluno["media"]}')
print(f'Situação: {aluno["situacao"]}')
