#!/usr/bin/python3.7
# -*-coding: utf-8-*-
import pandas as pd
import numpy as np


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
