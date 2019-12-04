```python
# coding:utf8
"""
时间方面的操作
https://docs.python.org/3/library/datetime.html#strftime-strptime-behavior
"""
from datetime import datetime
import time
import calendar
import pytz


# timestamp ==> datetime
def timestamp2datetime(timestamp):
    return datetime.fromtimestamp(timestamp)


# datetime ==> str
def datetime2str(datetime_obj, str_format="%Y-%m-%d %H:%M:%S"):
    return datetime_obj.strftime(str_format)


# str ==> datetime
def str2datetime(time_str, str_format="%Y-%m-%d %H:%M:%S"):
    return datetime.strptime(time_str, str_format)


# offset-naive ==> offset-aware
def naive2aware(datetime_obj):
    return datetime_obj.replace(tzinfo=pytz.timezone('UTC'))


# offset-aware ==> offset-naive
def aware2naive(datetime_obj):
    return datetime_obj.replace(tzinfo=None)


# 返回当天星期几和这个月有几天
def get_wday_and_month_range():
    """返回当天星期几和这个月有几天"""
    day_now = time.localtime()
    # 得到本月的天数 第一返回为月第一日为星期几（0-6）, 第二返回为此月天数
    w_day, month_range = calendar.monthrange(day_now.tm_year, day_now.tm_mon)
    w_day_now = w_day + day_now.tm_mday - 1
    w_day_now = w_day_now % 7 + 1
    return w_day_now, month_range
```
