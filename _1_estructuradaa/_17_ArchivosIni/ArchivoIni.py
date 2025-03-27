import configparser
import sys

if __name__ == '__main__':
    config = configparser.ConfigParser()
    config.read('Config.ini')#abre el archivo antes creado

    #verifica que las secciones y claves existen
    if ('Maximus' in config and 'basedatos' in config['Maximus'] and 'usuario' in config['Maximus'] and 'contrasenia' in config['Maximus']):

        bd = config['Maximus']['basedatos']
        user = config['Maximus']['usuario']
        password = config['Maximus']['contrasenia']
        sys.stdout.write(f"Los usuarios y contraseñas: {bd}-{user}-{password}")
