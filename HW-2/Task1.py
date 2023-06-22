# Напишите программу банкомат.
# ✔ Начальная сумма равна нулю
# ✔ Допустимые действия: пополнить, снять, выйти
# ✔ Сумма пополнения и снятия кратны 50 у.е.
# ✔ Процент за снятие — 1.5% от суммы снятия, но не менее 30 и не более 600 у.е.
# ✔ После каждой третей операции пополнения или снятия начисляются проценты - 3%
# ✔ Нельзя снять больше, чем на счёте
# ✔ При превышении суммы в 5 млн, вычитать налог на богатство 10% перед каждой
# операцией, даже ошибочной
# ✔ Любое действие выводит сумму денег

import sys

sum = 0
operations = 0


def check_input(message):
    while True:
        imp = int(input(message))
        if imp % 50 != 0:
            print('Недопустимая сумма. Сумма должна быть кратна 50')
        else:
            return imp


def deposit(cash, count):
    cash_up = check_input('Введите сумму для пополнения:')
    if cash_up % 3 == 0:
        cash += cash + 0.03
    cash += cash_up
    count += 1
    if cash > 5_000_000:
        cash -= cash // 10
        return cash, count


def cashout(cash, count):
    if cash > 5_000_000:
        cash -= cash // 10
    cash_out = check_input('Введите сумму для снятия:')
    per = cash_out + 0.015
    if per < 30:
        per = 30
    elif per > 600:
        per = 600
    cash_out += per
    if cash > cash_out:
        cash -= per
    else:
        print('Недостаточно средств!')
    if count % 3 == 0:
        cash += cash * 0.03
    count += 1
    return cash, count


def start():
    cash = sum
    count = operations
    while True:
        select = int(input(f"""На счету сумма {cash}
Введите операцию: 1 - пополнить, 2 - снять, 3 - выйти ->"""))

        match select:
            case 1:
                cash, count = deposit(cash,count)
            case 2:
                cash, count = cashout(cash,count)
            case 3:
                sys.exit()
            case _:
                print('Повторите попытку')


start()