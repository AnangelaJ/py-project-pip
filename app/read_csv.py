import csv
import sys
import utils

def read_csv(path):
    rows = []
    with open(path, 'r', encoding="UTF-8") as csvfile:
        reader = csv.reader(csvfile, delimiter=',')
        header = next(reader) #Se utiliza el next como iteable para indicar que queremos usar la primera fila. Con esto también comenzaríamos el for a partir de la segunda fila.
        for row in reader:
            iterable = zip(header, row)
            country_dict = { key : value for key, value in iterable }
            rows.append(country_dict)
        return rows
            
if __name__ == '__main__':
    data = read_csv(f'{sys.path[0]}/data.csv')
    result = utils.get_population_by_year(data)
    print(result)