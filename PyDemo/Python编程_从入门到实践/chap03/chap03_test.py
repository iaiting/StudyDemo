#!/usr/bin/env python3
# -*- coding: utf-8 -*-

def main():
    pass
    cars = ['bmw', 'audi', 'toyota', 'subaru']
    print(sorted(cars, reverse=True))
    print(cars)
    cars.reverse()
    print(cars)
    print(len(cars))
    cars.sort()
    print(cars)
    cars.sort(reverse=True)
    print(cars)

if __name__ == "__main__":
    main()