def vote(yearBirth):
    from datetime import date
    age = date.today().year - yearBirth

    if age < 16:
        return f'Com {age} anos: VOTO NEGADO.'
    elif 16 <= age < 18 or age > 65:
        return f'Com {age} anos: VOTO OPCIONAL.'
    else:
        return f'Com {age} anos: VOTO OBRIGATÓRIO.'


# Main Program
birthYear = int(input('Em que ano você nasceu? '))

print(vote(birthYear))
