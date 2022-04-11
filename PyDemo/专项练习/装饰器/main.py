#!/usr/bin/env python3
# -*- coding: utf-8 -*-

################################################################################
#
# 从函数中返回函数
#
################################################################################
def hi(name='yasoob'):
    def greet():
        return 'now you are in the greet() function'

    def welcome():
        return 'now you are in the welcome() function'

    if name == 'yasoob':
        return greet
    else:
        return welcome

################################################################################
a = hi()
print(a)
print(a())



################################################################################
#
# 将函数作为参数传给另一个函数
#
################################################################################
def hi2():
    return 'hi yasoob!'

def doSomethingBeforeHi(func):
    print('I am doing some boring work before executing hi()')
    print(func())

print('*******************t101:')
doSomethingBeforeHi(hi2)