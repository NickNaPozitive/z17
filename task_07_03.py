

def inch_to_cen(number):
    result = number * 0.39
    return result

def cen_to_inch(number):
    result = number * 0.39
    return result


def mili_to_kilo(number):
    result = number * 1.61
    return result


def kilo_to_mili(number):
    result = number * 0.62
    return result


def f_to_kilo(number):
    result = number * 0.45
    return result


def kilo_to_f(number):
    result = number * 2.2
    return result


def unc_to_gramm(number):
    result = number * 28.35
    return result


def gramm_to_unc(number):
    result = number * 0.035
    return result


def gal_to_litr(number):
    result = number * 4.55
    return result


def litr_to_gal(number):
    result = number * 0.22
    return result


def pint_to_litr(number):
    result = number * 0.57
    return result


def litr_to_pint(number):
    result = number * 1.76
    return result

dictOfCommands = {
    1: [inch_to_cen, 'дюймов в сантиметры'],
    2: [cen_to_inch, 'сантиметров в дюймы'],
    3: [mili_to_kilo, 'милей в километры'],
    4: [kilo_to_mili, 'километров в мили'],
    5: [f_to_kilo, 'фунтов в килограммы'],
    6: [kilo_to_f, 'килограммов в фунты'],
    7: [unc_to_gramm, 'унций в граммы'],
    8: [gramm_to_unc, 'граммов в унции'],
    9: [gal_to_litr, 'галлонов в литры'],
    10: [litr_to_gal, 'литров в галлоны'],
    11: [pint_to_litr, 'пинт в литры'],
    12: [litr_to_pint, 'литров в пинты']
}

while True:
    type_of = int(input("Введите тип перевода: "))
    number = float(input("Введите количество: "))
    if type_of == 0:
        break
    else:
        a = dictOfCommands.get(type_of)
        print(f"Перевод {a[1]} завершен. Ответ: {a[0](number)}")



