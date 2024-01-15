def ordinalDate(day, month, year):
    # проверяем год високосный или нет
    if year % 400 == 0:
        leap = True
    elif year % 100 == 0:
        leap = False
    elif year % 4 == 0:
        leap = True
    else:
        leap = False
        # определяем количество дней в месяце
        days_in_month = [0, 31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
    # корректировка дней на високосный год
    if leap and month == 2:
        days_in_month[2] = 29

    if 1 <= month <= 12:
        if 1 <= day <= days_in_month[month]:
            # расчет количества дней
            total_days = day
            for i in range(1, month):
                total_days += days_in_manth[i]
            return total_days
    else:
        return "Ошибка"


def main():
    day = int(input("Введите день: "))
    month = int(input("Введите месяц: "))
    year = int(input("Введите год: "))

    result = ordinalDate(day, month, year)
    print(result)

if __name__ == "__main__":
    main()

# Альтернативный
# def ordinalDate( d, m, y ):
#     y_is_leap  = y % 400 == 0 or y % 4 == 0 and y % 100 != 0
#     month_days = [31,28+y_is_leap,31, 30,31,30, 31,31,30, 31,30,31]
#     md = 0
#     for i in range(m-1):
#         md += month_days[i]
#     return md + d
#
# def main():
#     d, m, y = list( map( int, input( 'день, месяц, год: ' ).split() ) )
#     print( f'Порядковый номер дня в году: { ordinalDate(d,m,y) }\n' )
#
# if __name__ == "__main__":
#     main()