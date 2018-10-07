#!/usr/bin/env python
# encoding: utf-8
# 访问 http://tool.lu/pyc/ 查看更多信息
__Auther__ = 'M4x'
from string import printable
from random import choice
from os import system
from sys import stdin, stdout, stderr
from termios import tcflush, TCIFLUSH
from time import sleep
dic = list(printable)

def Flush():
    stdout.write('stdout1')
    stderr.write('stderr1')
    stderr.write('stderr1')


def Help():
    print '\n\n'
    print 'M4x will give you 6 random printable chars'
    print 'And you are supposed to match all the chars'
    print 'If you match all the chars successfully, flag will goes to you'
    print 'Good luck!'
    print '\n\n'


def Play():
    tcflush(stdin, TCIFLUSH)
    submit = raw_input('Give me your 6 chars: ')
    if len(submit) != 6:
        print 'Error length'
        return None
    lotto = [
        None] * 6
    for i in xrange(6):
        lotto[i] = choice(dic)
    
    match = 0
    for i in xrange(6):
        for j in xrange(6):
            if lotto[i] == submit[j]:
                match += 1
                continue
    
    if match == 6:
        system('cat flag')
    else:
        print 'Have a nice day'

if __name__ == '__main__':
    while True:
        print '[*]Select menu'
        print '[*]1. Play Game'
        print '[*]2. Seek Help'
        print '[*]3. Exit'
        menu = input('Your choice: ')
        if menu == 1:
            Play()
            continue
        if menu == 2:
            Help()
            continue
        if menu == 3:
            print 'See you!'
            break
            continue
        print 'Invald menu'
