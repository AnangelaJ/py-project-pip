import matplotlib.pyplot as plt

def generate_pie_charts():
    labels = ['A', 'B', 'C']
    values = [10,30,54]
    
    fig, ax = plt.subplots()
    ax.pie(values, labels=labels)
    plt.savefig('pie.png') #Con esta funcion, al generar la gráfica no la mostrará sino que la guardará como un archivo .png
    plt.close()