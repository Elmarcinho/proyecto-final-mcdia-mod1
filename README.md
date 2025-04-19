# Sistema de Gestión de Imágenes Médicas COVID-19

## Introducción
Este repositorio contiene un sistema desarrollado para el curso "Fundamentos de la Ingeniería del Software para Científicos de Datos". El proyecto implementa un módulo para el registro, visualización, actualización y eliminación de imágenes médicas de radiografías de COVID-19 junto con su metadata asociada.

## Descripción del Proyecto
El sistema permite gestionar radiografías médicas del dataset COVID-19 Radiography, implementando operaciones CRUD (Crear, Leer, Actualizar, Eliminar) a través de una interfaz de línea de comandos. Los datos se almacenan en formato JSON, siguiendo principios de programación orientada a objetos y modularización.

## Requisitos
- Python 3.12 o superior
- OpenCV
- NumPy

## Instalación

```bash
# Clonar el repositorio
git clone https://github.com/Elmarcinho/proyecto-final-mcdia-mod1.git
cd proyecto-final-mcdia-mod1

# Crear entorno virtual (recomendado)
python -m venv venv

# Activar entorno virtual
# En Windows:
venv\Scripts\activate
# En macOS/Linux:
source venv/bin/activate

# Instalar dependencias
pip install opencv-python numpy
```

## Estructura del Proyecto

```
proyecto-final-mcdia-mod1/
├── main.py                # Archivo principal de ejecución
├── storage.json           # Almacenamiento de metadata en JSON
├── controllers/           # Controladores para la lógica de negocio
│   └── controller_image.py
├── models/                # Modelos para la representación de datos
│   ├── image.py
│   ├── metadata.py
│   └── storage.py
├── services/              # Servicios para la persistencia y acceso a datos
│   └── storage.py
├── utils/                 # Utilidades generales
│   ├── menu.py
│   └── options.py
└── new_images/            # Carpeta para nuevas imágenes
```

## Uso

Para ejecutar el programa:

```bash
python main.py
```

El sistema presenta un menú con las siguientes opciones:
1. Registrar nueva imagen
2. Listar imágenes disponibles
3. Actualizar metadata
4. Eliminar imagen
5. Salir

## Funcionalidades

### Registro de Imágenes
Permite añadir nuevas imágenes al sistema con su metadata asociada.

### Visualización de Imágenes
Muestra todas las imágenes registradas en el sistema junto con su información.

### Actualización de Metadata
Permite modificar la información asociada a las imágenes previamente registradas:
- Selección de imagen a actualizar
- Visualización de metadata actual
- Actualización de campos (nombre de la imagen y su extensión, tamaño y url)
- Almacenamiento de cambios en el archivo JSON

### Eliminación de Imágenes
Permite eliminar imágenes y su metadata del sistema.

## Dataset
El proyecto utiliza el dataset COVID-19 Radiography Database disponible en Kaggle (https://www.kaggle.com/datasets/tawsifurrahman/covid19-radiography-database), que contiene radiografías pulmonares clasificadas en diferentes categorías.

## Arquitectura
El sistema implementa una arquitectura Modelo-Vista-Controlador (MVC):
- **Modelo**: Representa las estructuras de datos (model_image.py)
- **Vista**: Interfaz de usuario en terminal (utils/menu.py)
- **Controlador**: Maneja la lógica de negocio (controller_image.py)

## Equipo de Desarrollo
- **E. Rodas Banegas**: Eliminación de imágenes, Diagramas de módulos, Repositorio
- **M. Centellas Hinojosa**: Definición del problema, Dataset, Diagramas de clases, Lectura
- **N. Arce Arnez**: Actualización de metadata, Documentación
- **E. Miranda**: Registro de imágenes

## Trabajos Futuros
- Implementación de interfaz gráfica de usuario
- Migración a base de datos relacional
- Incorporación de técnicas de aprendizaje automático para clasificación

## Referencias
1. COVID-19 Radiography Database. Kaggle. https://www.kaggle.com/datasets/tawsifurrahman/covid19-radiography-database
2. Python Software Foundation. PEP 8 - Style Guide for Python Code. https://peps.python.org/pep-0008/
3. JSON.org. Introducing JSON. https://www.json.org/json-en.html