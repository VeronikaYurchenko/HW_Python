# Возьмите задачу о банкомате из семинара 2.
# Разбейте её на отдельные операции — функции.
# Дополнительно сохраняйте все операции поступления и снятия средств в список.

import sys
import logging

def print_message(message):
    print(message)

def is_valid_amount(total_amount, amount, choice):
    limit_min = 50
    if amount % limit_min != 0 or choice == '1' and amount > total_amount:
        return False
    return True

def calc_cashback(cash_back, total_amount, ops_count):

    if ops_count != 0 and ops_count % cashback_rate == 0:
        cash_back += total_amount / 100 * cashback_rate
    return cash_back

def calc_withdraw_fee(wd_fee, amount, choice):

    if choice == '1':
        wd_fee = amount / 100 * wd_rate
        if wd_fee < min_fee:
            wd_fee = min_fee
        elif wd_fee > max_fee:
            wd_fee = max_fee
    return wd_fee

def calc_wealth_tax(w_tax, total_amount):  # налог на богатство рассчитывается из суммы, превышающей 5_000_000

    if total_amount > limit_balance:
        w_tax = (total_amount - limit_balance) / 100 * 10
    return w_tax

def go_menu(total_amount, ops_count):
    print(f'На счету сумма {total_amount}\n'
          "1 - Снять, 2 - Пополнить, 3 - Выйти --> \n")

    choice = input('Выберите операцию: ')
    amount, cash_back, wd_fee, w_tax = 0.0, 0.0, 0.0, 0.0

    match choice:
        case '1' | '2':
            amount = float(input('Введите сумму: '))
            if is_valid_amount(total_amount, amount, choice):
                if choice == '1':
                    total_amount -= amount
                    msg = 'Снято'
                else:
                    total_amount += amount
                    msg = 'Внесено'

                w_tax = calc_wealth_tax(w_tax, total_amount)
                cash_back = calc_cashback(cash_back, total_amount, ops_count)
                wd_fee = calc_withdraw_fee(wd_fee, amount, choice)

                if total_amount + cash_back - wd_fee - w_tax < 0:
                    total_amount += amount - w_tax
                    cash_back, wd_fee = 0.0, 0.0
                    print('Некорректный ввод! Сумма не может превышать баланс!')
                    logging.info(f'Неверная операция. Сумма превышает баланс')
                else:
                    print_message(f'\n Успешно {msg} {amount}')
                    ops_count += 1
                    logging.info(f'{msg} : {amount}.')
            else:
                print_message('\nНекоррекный ввод! Сумма должна быть кратна 50!')
                logging.info(f'Сумма не кратна 50')
        case '3':
            print_message('Хорошего дня!')
            logging.info(f'Завершение работы')
            sys.exit()
        case _:
            print_message('Неправильный ввод! Попробуйте еще раз!')
            logging.info(f'Попробуйте еще раз')

    w_tax = calc_wealth_tax(w_tax, total_amount)
    total_amount += cash_back - wd_fee - w_tax
    go_menu(total_amount, ops_count)

logging.basicConfig(level=logging.INFO, filename="log.log", format="%(asctime)s %(levelname)s %(message)s")
cashback_rate = 3
wd_rate = 1.5
min_fee, max_fee = 30, 600
limit_balance = 5_000_000
amount_total = 0.0
operations_count = 1  # счетчик количества операций для своевременного начисления кэшбэка
go_menu(amount_total, operations_count)


