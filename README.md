# Test Automation Project: December Labs

Este proyecto es un conjunto de pruebas automatizadas utilizando Selenium, Pytest y Python para probar la funcionalidad del sitio web de December Labs.

Este proyecto incluye pruebas automatizadas para el sitio web de December Labs utilizando Selenium y Pytest, permitiendo validar diferentes funcionalidades de las páginas principales del sitio y la página de Houston.



##Requisitos

Python 3.x

Selenium WebDriver

Pytest

##Instalación

1. Instalar Python en tu sistema, puedes descargar la última versión de [Python aquí](https://www.python.org/downloads/).
   
2. Instalar Selenium WebDriver:
    pip install selenium

3. Instalar pytest:
   pip install pytest

##Clona el repositorio del proyecto:

git clone https://github.com/lucascalvimonte/DecLabsProject.git

##Ejecucion de las pruebas

Para ejecutar las pruebas, en la línea de comandos, navega hasta la carpeta del proyecto y ejecuta el comando pytest:

python -m pytest -v


##Estructura del proyecto

El proyecto "December Labs" está compuesto por los siguientes componentes y clases:

- `HoustonPage`: Esta clase representa la página de Houston y contiene los elementos y métodos relacionados con dicha página. Algunos de los elementos incluyen el botón para programar una consulta gratuita y el formulario emergente. La página también define la URL base para la página de Houston.

- `DecemberLabsPage`: Esta clase representa la página principal de December Labs y contiene los elementos y métodos relacionados con dicha página. Algunos de los elementos incluyen los botones de navegación (Acerca de nosotros, Servicios, Nuestro trabajo, Blog, Preguntas frecuentes, Carreras y Contacto), así como la URL base para la página principal. 

- `BasePage`: Esta clase es una clase base que proporciona métodos comunes para interactuar con los elementos de las páginas. Contiene métodos para buscar elementos, verificar la visibilidad de los elementos y hacer scroll en la página. También contiene métodos auxiliares para la espera de elementos y verificación de visibilidad.

- `TestDecemberLabs`: Esta clase de prueba contiene los casos de prueba relacionados con la validación de la página web y la navegación a través de las páginas. Utiliza las clases anteriores para interactuar con los elementos y realizar las aserciones necesarias.


Las pruebas en el proyecto se implementan utilizando el framework de pruebas pytest. Pytest es una herramienta poderosa y flexible que simplifica la escritura y ejecución de casos de prueba. Permite una sintaxis sencilla y clara para escribir aserciones y proporciona una amplia gama de funcionalidades adicionales, como la parametrización de casos de prueba y la generación de informes detallados. Utilizar pytest en el proyecto ofrece ventajas en términos de legibilidad del código y facilidad de mantenimiento de las pruebas.

La estructura del proyecto se organiza de manera lógica, con clases específicas para cada página y una clase de prueba que utiliza esas clases para validar el funcionamiento de la aplicación. El uso de una clase base (`BasePage`) ayuda a encapsular la lógica común de interacción con los elementos de la página.

## Pruebas Implementadas

Las pruebas implementadas en este proyecto son:

- Navegación a la página principal de December Labs (`test_navigate_to_dec_labs`).
- Validación del título de la página principal de December Labs (`test_validate_title_dec_labs`).
- Validación de la visibilidad de los elementos del menú en la página principal de December Labs (`test_validate_menu_dec_labs`).
- Navegación a la página de la ubicación de Houston (`test_navigate_to_houston`).
- Validación del título de la página de la ubicación de Houston (`test_houston_page_title`).
- Validación de la URL de la página de la ubicación de Houston (`test_validate_url_houston`).
- Apertura del formulario emergente en la página de la ubicación de Houston (`test_open_form_popup`).
- Cierre del formulario emergente en la página de la ubicación de Houston (`test_close_form_popup`).



##Mejoras realizadas

Refactorización del código para utilizar un enfoque basado en clases y métodos reutilizables.
Extracción de elementos de la página a clases separadas para una mejor organización y mantenibilidad.
Implementación de un método find_elements en la clase BasePage para buscar múltiples elementos de manera eficiente.
Uso de diccionarios para almacenar los elementos de la página en la clase DecemberLabsPage.
Agregado del método scroll_down en la clase BasePage para hacer scroll hacia abajo en la página.
Agregado del método element_is_not_visible_by_xpath en la clase BasePage para verificar que un elemento no sea visible en la página.

Migración a un enfoque de pruebas basado en el framework pytest, lo que permite una estructura más clara y concisa de los casos de prueba, así como la integración de fixtures para la configuración y limpieza del entorno de prueba.

Implementación de un sistema de manejo de configuración flexible, por ejemplo, utilizando archivos de configuración externos o variables de entorno, para facilitar la personalización de los parámetros de ejecución de las pruebas.

Uso de anotaciones y decoradores de pytest para aprovechar características adicionales, como la parametrización de casos de prueba y la generación de informes detallados de ejecución.

Incorporación de buenas prácticas de desarrollo de pruebas, como la separación de las pruebas unitarias de las pruebas de integración, el uso de mocks para simular dependencias externas y la implementación de aserciones claras y significativas.

#Notas adicionales

Asegúrate de tener el controlador del navegador (en este caso, ChromeDriver) configurado correctamente y en tu variable de entorno PATH.
