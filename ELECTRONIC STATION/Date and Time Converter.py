def date_time(time: str) -> str:
    month_dict = {'01': 'January', '02': 'February', '03': 'March', '04': 'April', '05': 'May', '06': 'June',
                  '07': 'July', '08': 'August', '09': 'September', '10': 'October', '11': 'November', '12': 'December'}

    def process_lead_zero(s):
        return s[1] if int(s) < 10 else s

    time, clock = time.split(' ')
    day, month, year = time.split('.')
    hour, minute = clock.split(':')
    day, hour, minute = [process_lead_zero(i) for i in [day, hour, minute]]
    hour_suffix = 'hour' if hour == '1' else 'hours'
    minute_suffix = 'minute' if minute == '1' else 'minutes'
    return ' '.join([day, month_dict[month], year, 'year', hour, hour_suffix, minute, minute_suffix])


print(date_time('11.04.1812 01:01'))

# 比我更好的方法， 利用系统提供的转化工具
from datetime import datetime


def date_time(time: str) -> str:
    s, dt = ('s', ''), datetime.strptime(time, '%d.%m.%Y %H:%M')
    return '{0} {1:%B %Y year} {2} hour{4} {3} minute{5}'.format(dt.day, dt, dt.hour, dt.minute, s[dt.hour == 1],
                                                                 s[dt.minute == 1])


# 第一的答案，利用strftime的函数特性（C源代码的特性解决了补0的问题）
def checkio(time):
    dt = datetime.strptime(time, '%d.%m.%Y %H:%M')
    hour = 'hour' if dt.hour == 1 else 'hours'
    minute = 'minute' if dt.minute == 1 else 'minutes'
    return dt.strftime(f'%-d %B %Y year %-H {hour} %-M {minute}')


"""
strftime   str format/from time
strptime   str parsed time
"""