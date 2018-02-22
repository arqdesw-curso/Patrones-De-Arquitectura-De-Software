#!/usr/bin/env python
# -*- coding: utf-8 -*-
#-------------------------------------------------------------------------
# Archivo: extract-ip.py
# Capitulo: 4 Patron Pipes and Filters
# Autor(es): Perla Velasco & Yonathan Mtz.
# Version: 2.0 Febrero 2018
# Descripción:
#
#   Ésta clase define el rol de un Procesador de datos, es decir, procesa o transforma datos
#
#   Las características de ésta clase son las siguientes:
#
#                                          extract_ip.py
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
#           |                        |                          |    el procesador.     |
#           +------------------------+--------------------------+-----------------------+
#           |         run()          |          - N/A           |  - Procesa o transfor-|
#           |                        |                          |    ma los datos.      |
#           +------------------------+--------------------------+-----------------------+
#
#-------------------------------------------------------------------------
import luigi
import os
import sys

from access_log import AccessLog


class ExtractIP(luigi.Task):
    sys.path.insert(0, os.path.abspath('..'))

    def output(self):
        return luigi.LocalTarget("../resource/ip_access.log")

    def requires(self):
        return AccessLog()

    def run(self):
        with self.input().open() as f:
            with self.output().open('w') as out:
                for line in f:
                    ip = line.split()[0]
                    out.write(str(ip) + "\n")
