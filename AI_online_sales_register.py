#!/usr/bin/env python
# -*- coding: utf-8 -*-
class OnlineSalesRegisterCollector:
    def __init__(self):
        self.__name_items = []
        self.__number_items = 0
        self.__item_price = {'чипсы': 50, 'кола': 100, 'печенье': 45, 'молоко': 55, 'кефир': 70}
        self.__tax_rate = {'чипсы': 20, 'кола': 20, 'печенье': 20, 'молоко': 10, 'кефир': 10}

    @property
    def name_items(self):
        return self.__name_items

    @property
    def number_items(self):
        return self.__number_items

    def add_item_to_cheque(self, name):
        if len(name) == 0 or len(name) > 40:
            raise ValueError('Нельзя добавить товар, если в его названии нет символов или их больше 40')
        if name not in self.__item_price:
            raise NameError('Позиция отсутствует в товарном справочнике')
        self.__name_items.append(name)
        self.__number_items += 1


    def delete_item_from_check(self, name):
        if name not in self.__name_items:
            raise NameError('Позиция отсутствует в чеке')
        self.__name_items.remove(name)
        self.__number_items -= 1


    def check_amount(self):
        total = 0
        for item in self.__name_items:
            total += self.__item_price[item]

        if self.__number_items > 10:
            total *= 0.9  # применяем скидку 10%

        return total

    def twenty_percent_tax_calculation(self):
        twenty_percent_tax = []
        total = []

        for item in self.__name_items:
            if self.__tax_rate[item] == 20:
                twenty_percent_tax.append(item)
                total.append(self.__item_price[item])

        if len(twenty_percent_tax) > 10:
            for i in range(len(twenty_percent_tax)):
                total[i] *= 0.9  # применяем скидку 10%

        vat_total = sum([price * 0.2 for price in total])
        return vat_total

    def ten_percent_tax_calculation(self):
        ten_percent_tax = []
        total = []

        for item in self.__name_items:
            if self.__tax_rate[item] == 10:
                ten_percent_tax.append(item)
                total.append(self.__item_price[item])

        if len(ten_percent_tax) > 10:
            for i in range(len(ten_percent_tax)):
                total[i] *= 0.9  # применяем скидку 10%

        vat_total = sum([price * 0.1 for price in total])
        return vat_total

    def total_tax(self):
        total_tax = sum([self.__item_price[item] * self.__tax_rate[item] / 100 for item in self.__name_items])
        return total_tax


    @staticmethod
    def get_telephone_number(telephone_number):
        if not isinstance(telephone_number, int):
            raise ValueError('Необходимо ввести цифры')
        elif len(str(telephone_number)) > 10:
            raise ValueError('Необходимо ввести 10 цифр после "+7"')
        else:
            return '+7' + str(telephone_number)