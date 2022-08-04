#!/usr/bin/python3.7
# -*-coding: utf-8-*-
from functions import Calculator

filepath = 'resources/Aktueller_Schnitt.csv'
noten = Calculator(filepath)

uebersicht = noten.read_csv()
print(f"{uebersicht[['Credits', 'Note']]}\n")

avg = noten.calc()
print(f"Durchschnittsnote:           {round(avg, 4)}")

avg_gewichtet = noten.calc_gewichtet()
print(f"Durchschnittsnote gewichtet: {round(avg_gewichtet, 4)}")

credits_bislang = noten.credits_bislang()
print(f"Bisher erreichte Credits: {credits_bislang}")

# noten.graphic()