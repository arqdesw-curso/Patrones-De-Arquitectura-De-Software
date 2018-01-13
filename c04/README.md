# Capítulo 4

## Sistema de Normalización de Ventas (SNV)

Para el ejemplo práctico vamos a suponer que Apple, una empresa estadounidense que ofrece productos tecnológicos, que van desde un smartphone hasta una laptop, pasando por servicios de software. En el año 2017 la empresa registró 4000 ventas en solo tres sucursales ubicadas en Japón, México y Alemania, lo que representó un 15\% más respecto a otros años en esas sucursales.

Dado lo anterior, el CEO de la empresa, Tim Cook, le ha pedido al departamento de ventas de la empresa que realicen el análisis de dichas ventas. Al tratar de analizar las ventas, el departamento encontró que los ingresos de cada venta se encontraba en términos monetarios del país en el que se ubica la sucursal, lo cual impidió que el departamento pudiese realizar el análisis. 

Con el propósito de realizar esta tarea rápidamente, el departamento de ventas solicitó al departamento de desarrollo de software de Apple implementar el Sistema de Normalización de Ventas (SNV), para que normalice dichas ventas antes de su análisis.

En la siguiente figura se muestra el diseño de la propuesta de solución del departamento de desarrollo para el SNV.

![Vista de contenedores del SNV](docs/diagrama_contenedores_capitulo_4.png)

## Prerrequisitos

Para poner en marcha el SNV se requiere instalar algunas dependencias. Podrás encontrar estas dependencias en el archivo `requirements.txt`. También puedes instalar éstas dependencias con el comando:

```shell
pip install -r requirements.txt
```

**Nota:** se asume que el gestor de dependencias `pip` se ha instalado previamente.

## Ejecución

Una vez instaladas las dependencias del SNV, podrás ponerlo en marcha con el comando:

```shell
python load_data.py LoadData --local-scheduler
```

## Versión

1.0 - Enero 2018

## Autores

* **Perla Velasco**
* **Yonathan Martínez**
