#!/usr/bin/env python
# -*- coding: utf-8 -*-
#-------------------------------------------------------------------------
# Archivo: load_data.py
# Capitulo: 4 Patron Pipes and Filters
# Autor(es): Perla Velasco & Yonathan Mtz.
# Version: 1.0 Enero 2018
# Descripción:
#
#   Ésta clase define el rol de un Filter, es decir, procesa los datos de las ventas.
#
#   Las características de ésta clase son las siguientes:
#
#                                            load_data.py
#           +-----------------------+-------------------------+------------------------+
#           |  Nombre del elemento  |     Responsabilidad     |      Propiedades       |
#           +-----------------------+-------------------------+------------------------+
#           |        Filter         |  - Procesar los datos   |         source         |
#           |                       |    de las ventas.       |                        |
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
#           |         run()          |          - N/A           |  - Ejecuta el procesa-|
#           |                        |                          |    miento del Filter. |
#           +------------------------+--------------------------+-----------------------+
#
#-------------------------------------------------------------------------
import luigi
import csv

from jpy_to_usd import JPYToUSD
from eur_to_usd import EURToUSD
from mxn_to_usd import MXNToUSD


class LoadData(luigi.Task):
    source = ("../resources/jpy_to_usd.csv", "../resources/eur_to_usd.csv", "../resources/mxn_to_usd.csv") # entrada(s) del Filter

    def output(self):
        return luigi.LocalTarget("../resources/sales-2017-final.csv") # salida del Filter

    def requires(self):
        return [JPYToUSD(), EURToUSD(), MXNToUSD()] # tarea(s) de las que depende el Filter

    def run(self):
        csv_dataset = self.output()
        with csv_dataset.open('w') as csv_opened:
            headers = ['order_id', 'date', 'client_id', 'employee_id', 'store_id', 'money_code', 'item_id',
                       'total']
            csv_writer = csv.DictWriter(csv_opened, fieldnames=headers)
            csv_writer.writeheader()
            for csv_source in self.source:
                with open(csv_source) as csv_file:
                    csv_reader = csv.DictReader(csv_file)
                    for row in csv_reader:
                        csv_writer.writerow({
                            'order_id': row['order_id'],
                            'date': row['date'],
                            'client_id': row['client_id'],
                            'employee_id': row['employee_id'],
                            'store_id': row['store_id'],
                            'money_code': row['money_code'],
                            'item_id': row['item_id'],
                            'total': row['total']})


if __name__ == '__main__':
    luigi.run()
