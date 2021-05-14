#!/usr/bin/python3.7
# -*-coding: utf-8-*-
import pandas as pd


class Calculator:

    def __init__(self, filepath):
        self.filepath = filepath
        self.csv_file = None

    def read_csv(self) -> pd.DataFrame:
        self.csv_file = pd.read_csv(f"{self.filepath}", sep=";", index_col=0)
        self.csv_file["Note"] = self.csv_file["Note"].replace(",", ".", regex=True).astype(float)
        self.csv_file["Credits_x_Note"] = self.csv_file["Credits"] * self.csv_file["Note"]
        print(self.csv_file)
        return self.csv_file

    def calc(self):
        return self.csv_file["Note"].mean()

    def calc_gewichtet(self):
        return self.csv_file["Credits_x_Note"].sum() / self.csv_file["Credits"].sum()
