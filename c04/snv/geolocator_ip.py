#!/usr/bin/env python
# -*- coding: utf-8 -*-
#-------------------------------------------------------------------------
# Archivo: geolocator_ip.py
# Capitulo: 4 Patron Pipes and Filters
# Autor(es): Perla Velasco & Yonathan Mtz.
# Version: 2.0 Febrero 2018
# Descripción:
#
#   Ésta clase define el rol de un Procesador, es decir, procesa o transforma datos
#
#   Las características de ésta clase son las siguientes:
#
#                                         geolocator_ip.py
#           +-----------------------+-------------------------+------------------------+
#           |  Nombre del elemento  |     Responsabilidad     |      Propiedades       |
#           +-----------------------+-------------------------+------------------------+
#           |       Procesador      |  - Procesar o transfor- |           N/A          |
#           |                       |    mar datos.           |                        |
#           +-----------------------+-------------------------+------------------------+
#
#   A continuación se describen los métodos que se implementaron en ésta clase:
#
#                                             Métodos:
#           +------------------------+--------------------------+-----------------------+
#           |         Nombre         |        Parámetros        |        Función        |
#           +------------------------+--------------------------+-----------------------+
#           |        output()        |          - N/A           |  - Genera un archivo  |
#           |                        |                          |    con los datos pro- |
#           |                        |                          |    cesados.           |
#           +------------------------+--------------------------+-----------------------+
#           |       requires()       |          - N/A           |  - Ejecuta las tareas |
#           |                        |                          |    de las que depende |
#           |                        |                          |    el Filter.         |
#           +------------------------+--------------------------+-----------------------+
#           |         run()          |          - N/A           |  - Procesa o transfor-|
#           |                        |                          |    ma los datos.      |
#           +------------------------+--------------------------+-----------------------+
#
#-------------------------------------------------------------------------
import luigi
import csv
import os
import sys
import urllib
import json

from reducer_ip import ReducerIP


class GeolocatorIP(luigi.Task):
    sys.path.insert(0, os.path.abspath('..'))

    def output(self):
        return luigi.LocalTarget("../resource/access_ip.csv") # salida del Filter

    def requires(self):
        return ReducerIP() # tarea(s) de la que depende éste Filter

    def run(self):
        with self.input().open() as reader:
            with self.output().open('w') as writer:
                headers = ['query','status','country','regionName','city','zip','lat','lon']
                csv_writer = csv.DictWriter(writer, fieldnames=headers)
                csv_writer.writeheader()
                for line in reader:
                    ip = line
                    url_ip_locator = urllib.urlopen('http://ip-api.com/json/' + ip)
                    locator_response = url_ip_locator.read()
                    result = json.loads(locator_response)
                    if result['status'] == "success":
                        csv_writer.writerow({
                            'query': result['query'],
                            'status': result['status'],
                            'country': result['country'],
                            'regionName': result['regionName'],
                            'city': result['city'],
                            'zip': result['zip'],
                            'lat': result['lat'],
                            'lon': result['lon']
                            })
                    else:
                        csv_writer.writerow({
                            'query': result['query'],
                            'status': result['status']
                            })


if __name__ == '__main__':
    luigi.run(["--local-scheduler"], main_task_cls=GeolocatorIP)
