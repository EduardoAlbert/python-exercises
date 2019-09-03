def notes(*note, sit=False):
    """
    -> Função para analisar notas e situações de vários alunos.
    :param note: Uma ou mais notas dos alunos (aceita várias)
    :param sit: Valor opcional, indicando se deve ou não adicionar a situação
    :return: Dicionário com várias informações sobre a situação da turma
    """

    info = {'total': len(note), 'maior': max(note), 'menor': min(note), 'média': sum(note) / len(note)}

    if sit:
        if info['média'] >= 7:
            info['situação'] = 'BOA'
        elif info['média'] >= 5:
            info['situação'] = 'ROZOÁVEL'
        else:
            info['situação'] = 'RUIM'
    return info


# Main Program
resp = notes(10, 10, 10, 10, sit=True)
print(resp)
help(notes)
