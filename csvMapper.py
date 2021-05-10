import csv
import re
from typing import List, Tuple


class CsvMapper:
    csv_file = None

    def __init__(self, csv_file):
        self.csv_file = csv_file

    def map_to_list(self) -> list:
        return [(int(credit), float(grade)) for credit, grade in self.read_csv()]

    def read_csv(self) -> List[Tuple[str, str]]:
        ret_val = list()
        with open(self.csv_file, 'r'
                , encoding="utf-8-sig") as dat:  # ignore BOM
            # [ret_val.append((row[1], row[2].replace(',', '.'))) for row in
            [ret_val.append((row[1], row[2].replace(',', '.'))) for row in
             csv.reader(dat
                        , delimiter=';'
                        , lineterminator='\r\n'
                        # , quoting=csv.QUOTE_NONNUMERIC
                        ) if not re.search(r'[a-zA-Z]', row[2])] #ignore header row
        return ret_val
