#!/usr/bin/env python
# -*- coding: utf-8 -*-
#-------------------------------------------------------------------------
# Archivo: reducer_ip.py
# Capitulo: 4 Patron Pipes and Filters
# Autor(es): Perla Velasco & Yonathan Mtz.
# Version: 2.0 Febrero 2018
# Descripción:
#
#   Ésta clase define el rol de un Procesador, es decir, procesa o transforma los datos
#
#   Las características de ésta clase son las siguientes:
#
#                                          reducer_ip.py
#           +-----------------------+-------------------------+------------------------+
#           |  Nombre del elemento  |     Responsabilidad     |      Propiedades       |
#           +-----------------------+-------------------------+------------------------+
#           |        Procesador     |  - Procesar o transfor- |           N/A          |
#           |                       |    mar los datos.       |                        |
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
import os
import sys

from extract_ip import ExtractIP


class ReducerIP(luigi.Task):
    sys.path.insert(0, os.path.abspath('..'))

    def output(self):
        return luigi.LocalTarget("../resource/clean_access_ip.log")

    def requires(self):
        return ExtractIP()

    def run(self):
        ips = []
        with self.input().open() as f:
            with self.output().open('w') as out:
                for line in f:
                    ip = line
                    if ip not in ips:
                        ips.append(ip)
                        out.write(str(ip))