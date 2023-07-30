import utils
import project

countries = [
        {
            'Country': 'COL',
            'Population': 50000000
        },
        {
            'Country': 'BOL',
            'Population': 10000000
        },
        {
            'Country': 'VE',
            'Population': 15000000
        }
    ]
    
def run():
    keys, values = utils.get_population() #Llamando funciones del módulo o archivo importado
    print(keys, values)

    print(utils.A) #Llamando variables del módulo o archivo importado

    result = utils.population_by_country(countries, 'VE')
    print(result)
    
#Con esta línea de código indicamos al archivo que si es llamado desde la terminal, ejecute toda la funcionalidad. 
#Si el archivo se importa como un modulo, no se ejecutará toda la funcionalidad si no es llamada especificamente
if( __name__ == '__main__' ):
    #run()
    project.run()