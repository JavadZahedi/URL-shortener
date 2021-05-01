from django.utils import timezone
from . import jalali


def numbers_to_persian(string):
    en_to_fa = {
        '0': '۰',
        '1': '۱',
        '2': '۲',
        '3': '۳',
        '4': '۴',
        '5': '۵',
        '6': '۶',
        '7': '۷',
        '8': '۸',
        '9': '۹',
    }
    for en, fa in en_to_fa.items():
        string = string.replace(en, fa)
    return string


def datetime_to_jalali_str(time):
    jalali_month = (
        'فروردین',
        'اردیبهشت',
        'خرداد',
        'تیر', 
        'مرداد',
        'شهریور',
        'مهر',
        'آبان',
        'آذر',
        'دی',
        'بهمن',
        'اسفند'
    )
    time = timezone.localtime(time)
    year, month, day = jalali.Gregorian(time.year, time.month, time.day).persian_tuple()
    jalali_to_str = '{} {} {} ، ساعت {:02d}:{:02d}'.format(
        day,
        jalali_month[month-1],
        year,
        time.hour,
        time.minute
    )
    return numbers_to_persian(jalali_to_str)


def date_to_jalali_str(date):
    jalali_month = (
        'فروردین',
        'اردیبهشت',
        'خرداد',
        'تیر', 
        'مرداد',
        'شهریور',
        'مهر',
        'آبان',
        'آذر',
        'دی',
        'بهمن',
        'اسفند'
    )
    year, month, day = jalali.Gregorian(date.year, date.month, date.day).persian_tuple()
    jalali_to_str = '{} {} {}'.format(day, jalali_month[month-1], year)
    return numbers_to_persian(jalali_to_str)