def get_population():
    keys = ['COL', 'BOL']
    values = [300, 400]
    return keys, values

def population_by_country(data, country):
    result = list(filter(lambda item : item['Country'] == country, data))
    return result, result[0]['Population']

def get_population_by_year(countries_dic, country):
    try:
        country_list = list(filter(lambda item : item['CCA3'] == country, countries_dic))
        country_dict = country_list[0]
        result = get_year_popl(country_dict)
        return result
    except Exception as error:
        print(error)

def get_year_popl(dict):
    new_keys = list(filter(lambda match : 'Population' in match[0] and 'Percentage' not in match[0], dict.items()))
    dict = { key[0:4] : int(value) for key, value in new_keys }
    return dict

def get_percent_popl(countries_dic, contnt):
    # perc = []
    # country = []
    # for item in countries_dic:
    #     if  item['Continent'] == contnt:
    #         perc.append(float(item['World Population Percentage']))
    #         country.append(item['CCA3'])
    data = list(filter(lambda item : item['Continent'] == contnt, countries_dic))
    perc = list(map(lambda item : item['World Population Percentage'], data))
    country = list(map(lambda item : item['CCA3'], data))
    return perc, country

A = 'HOLA'