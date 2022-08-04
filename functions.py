#!/usr/bin/python3.7
# -*-coding: utf-8-*-
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns


class Calculator:

    def __init__(self, filepath):
        self.filepath = filepath
        self.csv_file = None

    def read_csv(self) -> pd.DataFrame:
        """Reads out the csv file and sets university subject as index
        Further replacing the ',' in grades to '.' and adds a new column multiplying the credits with the grades"""
        self.csv_file = pd.read_csv(f"{self.filepath}", sep=";", index_col=0)
        self.csv_file["Note"] = self.csv_file["Note"].replace(",", ".", regex=True).astype(float)
        self.csv_file["Credits_x_Note"] = self.csv_file["Credits"] * self.csv_file["Note"]
        return self.csv_file

    def calc(self) -> np.float64:
        """Simply return the mean value of all grades"""
        return self.csv_file["Note"].mean()

    def calc_gewichtet(self) -> np.float64:
        """Devide the sum of all multiplyed credits and grades by the sum of credits"""
        return self.csv_file["Credits_x_Note"].sum() / self.csv_file["Credits"].sum()

    def credits_bislang(self) -> np.int64:
        return self.csv_file["Credits"].sum()

    def graphic(self):
        x_values = [1.0, 1.3, 1.7, 2.0, 2.3, 2.7, 3.0, 3.3, 3.7, 4.0]
        graphic = sns.displot(self.csv_file["Note"], bins=x_values, kde=True)
        graphic.set(xlabel = "Noten", ylabel="Anzahl", title="Notenverteilung", xlim=(1,4))
        plt.show()