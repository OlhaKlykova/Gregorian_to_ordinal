def reversOrdinalDate(year, ordinal_day):

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
    if leap:
        days_in_month[2] = 29

    if 1 <= ordinal_day <= 366:
        month = 1
        while ordinal_day > days_in_month[month]:
            ordinal_day -= days_in_month[month]
            month += 1

        return ordinal_day, month

    else:
        return "ошибка"


def main():
    term = int(input("Введите срок (в днях): "))
    ordinal_day1 = int(input("Введите порядковый день день первой даты: "))
    year1 = int(input("Введите год: "))

    # Получаем порядковую дату для введенной первой даты
    result1 = reversOrdinalDate(year1, ordinal_day1)
    print(f"Первая дата: {result1[0]}-{result1[1]}-{year1}")
    # Добавляем к полученной дате срок term
    day_plus_term = ordinal_day1 + term
    if day_plus_term <= 366:
        result2 = reversOrdinalDate(year1, day_plus_term)
        print(f"Дата через {term} дней: {result2[0]}-{result2[1]}-{year1}")
    else:
        # Если вторая дата выходит за пределы текущего года
        year2 = year1 + 1
        day_plus_term -= 366
        result2 = reversOrdinalDate(year2, day_plus_term)
        print(f"Дата через {term} дней: {result2[0]}-{result2[1]}-{year2}")


if __name__ == "__main__":
    main()
