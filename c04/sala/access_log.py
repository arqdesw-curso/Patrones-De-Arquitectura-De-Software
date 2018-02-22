#!/usr/bin/env python
# -*- coding: utf-8 -*-
#-------------------------------------------------------------------------
# Archivo: access_log.py
# Capitulo: 4 Patron Pipes and Filters
# Autor(es): Perla Velasco & Yonathan Mtz.
# Version: 2.0 Febrero 2018
# Descripción:
#
#   Ésta clase define el rol de una Fuente de datos, es decir, almacena el lote de datos.
#
#   Las características de ésta clase son las siguientes:
#
#                                          access_log.py
#           +-----------------------+-------------------------+------------------------+
#           |  Nombre del elemento  |     Responsabilidad     |      Propiedades       |
#           +-----------------------+-------------------------+------------------------+
#           |    Fuente de datos    |  - Almacena el lote de  |           N/A          |
#           |                       |    datos.               |                        |
#           +-----------------------+-------------------------+------------------------+
#
#   A continuación se describen los métodos que se implementaron en ésta clase:
#
#                                             Métodos:
#           +------------------------+--------------------------+-----------------------+
#           |         Nombre         |        Parámetros        |        Función        |
#           +------------------------+--------------------------+-----------------------+
#           |        output()        |          - N/A           |  - Proporciona un     |
#           |                        |                          |    archivo con el lo- |
#           |                        |                          |    te de datos almace-|
#           |                        |                          |    nados.             |
#           +------------------------+--------------------------+-----------------------+
#
#------------------------------------------------------------------------------------------
import luigi
import os
import sys


class AccessLog(luigi.Task):
    sys.path.insert(0, os.path.abspath('..'))

    def output(self):
        return luigi.LocalTarget("../resource/access_log_20180222-001713.log")