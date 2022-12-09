#!/usr/bin/env python3
# -*- coding: utf-8 -*-


#################################################################################
def main():
    commutes = ['car', 'bike', 'bus']
    for commute in commutes:
        if commute == 'car':
            print(f'I use {commute} in 下雨天')

        if commute == 'bike':
            print(f'I use {commute} in 晴天')

        if commute == 'bus':
            print(f'I use {commute} in 下雪天')
    
    
#################################################################################
if __name__ == "__main__":
    main()
