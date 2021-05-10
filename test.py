from averageCalc import AverageCalc
from csvMapper import CsvMapper

file_path = 'resources/Aktueller_Schnitt.csv'
a = AverageCalc()
mapper = CsvMapper(file_path)
# noten = [(10, 3.7),
#          (5, 2),
#          (5, 1.7),
#          (7, 1.3),
#          (7, 1.3),
#          (5, 1.7),
#          (5, 2),
#          (6, 2),
#          (5, 2),
#          (8, 1.7),
#          (5, 1),
#          (5, 2),
#          (5, 1.3)]

mapped_list = mapper.map_to_list()
schnitt = a.calc(mapped_list)
print(mapped_list)
print(f"Schnitt: {schnitt:1.2f}")