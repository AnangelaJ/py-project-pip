"""
    Luego de enlazar el proyecto con GIT debemos ir a la página gitignore.io y generar el archivo respectivo:
        - indicando los 3 principales SO: Windows, macOs, Linux; y el lenguaje a utilizar, en este caso python.
    Adicional se debe crear el archivo README.md con las instrucciones necesarias para que los desarrolladores puedan instalar adecuadamente el proyecto
"""

"""
    Para tener acceso a la lista o librería de paquetes de Python, debe ingresar a la siguiente URL:
        - https://pypi.org/
            Desde alli se pueden buscar los paquetes necesarios.
            Desde alli se indican los comandos para instalar dichos paquetes y su documentacion
"""

"""
    Para obtener la información de librerías instaladas en Python, se debe ejecutar el comando en terminal:
        - pip3 freeze
"""

"""
    Para usar ambientes virtuales debemos:
       Verificar donde esta python y pip
            which python3
            which pip3

        Si estas en linus o wsl debes instalar
            sudo apt install -y python3-venv
            
        Poner cada proyecto en su propio ambiente, entrar en cada carpeta.
            python3 -m venv env
            
        Activar el ambiente
            source env/bin/activate
            
        Salir del ambiente virtual
            deactivate
            
        Podemos instalar las librerias necesarias en el ambiente virtual como por ejemplo
            pip3 install matplotlib==3.5.0
            
        Verificar las instalaciones
            pip3 freeze
"""

"""
    Requirements.txt = Archivo que gestiona todas las dependencias y en que versiones se necesitan.

    Generar el archivo con el siguiente comando
        pip3 freeze > requirements.txt
    
    Revisar lo que hay dentro del archivo
        cat requirements.txt
        
    Instalar las dependencias necesarias para contribuir más rápido en proyectos
        pip3 install -r requirements.txt
    Preparar archivo para contribución

    # App Project
    ```sh
    git clone
    cd app
    python3 -m venv env
    source env/bin/activate
    pip3 install -r requirements.txt
    python3 main.py
"""