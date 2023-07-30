"""
    Para instalar la librería en el proyecto:
        - Instalamos pip con el comando python -m pip install -U pip
        - Instalamos la librería matplotlib con el comando python -m pip install -U matplotlib
        EJECUTAR ESTA INSTALACIÓN DESDE EL CMD COMO ADMINISTRADOR
"""

import matplotlib.pyplot as plt #se pueden poner alias a las importaciones

def generate_bar_chart(labels, values, name): #De esta manera generamos una gráfica de barras
    fig, ax = plt.subplots()
    ax.bar(labels, values)
    plt.savefig(f'./imgs/{name}.png')
    plt.close()
    
def generate_pie_chart(labels, values, name): #De esta manera generamos una gráfica de torta
    fig, ax = plt.subplots()
    ax.pie(values, labels=labels) #Para gráficas de torta primero se envían los valores y luego los labels indicando que ese parámetro son los labels
    plt.savefig(f'./imgs/{name}.png')
    plt.close()

if __name__ == '__main__':
    labels = ['a', 'b', 'c']
    values = [140, 60, 125]
    # generate_bar_chart(labels, values)
    generate_pie_chart(labels, values)