def summa(a, b):
    return a + b

def skidka(cena, procent):
    if procent < 0 or procent > 90:
        raise ValueError("неверный процент скидки")
    return round(cena * (1 - procent / 100), 2)
def srednee(chisla):
    if not chisla:
        raise ValueError("список пуст")
    return sum(chisla) / len(chisla)