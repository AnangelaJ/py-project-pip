import read_csv as csv
import utils
import sys
import charts
import pandas as pd

def run():
    countries = csv.read_csv('data.csv')
    country = input('Ingrese el código del país a graficar => ')
    result = utils.get_population_by_year(countries, country)
    labels = result.keys()
    values = result.values()
    charts.generate_bar_chart(labels, values, country)

    cntnt = input('Ingrese el continente a graficar => ')
    per, cntr = utils.get_percent_popl(countries, cntnt)

    charts.generate_pie_chart(cntr, per, cntnt)
    
    
def run_pandas(): #Utilizamos la libreria PANDAS para leer y manipular los csv
    df = pd.read_csv('data.csv')
    cntnt = input('Ingrese el continente a graficar => ')
    df = df[df['Continent'] == cntnt]
    cntr = df['CCA3'].values
    per = df['World Population Percentage'].values
    charts.generate_pie_chart(cntr, per, cntnt)
    
if __name__ == '__main__':
    # run()
    run_pandas()