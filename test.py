#!/usr/bin/env python
# -*- coding:utf-8 -*-

def judge(year):
    return True if not year % 400 or not year % 4 and year % 100 else False


res = judge(2000)
print(res)

print(456)
print(123)
print(456)