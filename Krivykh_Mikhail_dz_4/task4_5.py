"""Импортируем пакет utils, в который входит модуль currency"""
import utils

"""Импортируем пакет sys для ввода аргуменетов в терминале"""
import sys

"""делаем запросы курса  валют с аргументом из терминала"""

utils.currency.currency_rates(sys.argv[1])
