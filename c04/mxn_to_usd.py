#!/usr/bin/env python
# -*- coding: utf-8 -*-
#-------------------------------------------------------------------------
# Archivo: mxn_to_usd.py
# Capitulo: 4 Patron Pipes and Filters
# Autor(es): Perla Velasco & Yonathan Mtz.
# Version: 1.0 Enero 2018
# Descripción:
#
#   Ésta clase define el rol de un Filter, es decir, procesa los datos de las ventas.
#
#   Las características de ésta clase son las siguientes:
#
#                                            mxn_to_usd.py
#           +-----------------------+-------------------------+------------------------+
#           |  Nombre del elemento  |     Responsabilidad     |      Propiedades       |
#           +-----------------------+-------------------------+------------------------+
#           |        Filter         |  - Procesar los datos   |         source         |
#           |                       |    de las ventas.       |         divisa         |
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

from extract_data import ExtractData


class MXNToUSD(luigi.Task):
    source = "mxn.csv" # entrada del Filter
    divisa = 19.21 # valor de la moneda que será utilizado para convertir los dolares

    def output(self):
        return luigi.LocalTarget("mxn_to_usd.csv") # salida del Filter

    def requires(self):
        return ExtractData() # tarea(s) de las que depende el Filter

    def run(self):
        with open(self.source) as csv_file:
            mxn_dataset = self.output()
            csv_reader = csv.DictReader(csv_file)
            with mxn_dataset.open('w') as mxn_opened:
                headers = ['order_id', 'date', 'client_id', 'employee_id', 'store_id', 'money_code', 'item_id',
                           'total']
                mxn_writer = csv.DictWriter(mxn_opened, fieldnames=headers)
                mxn_writer.writeheader()
                for row in csv_reader:
                    mxn_writer.writerow({
                        'order_id': row['order_id'],
                        'date': row['date'],
                        'client_id': row['client_id'],
                        'employee_id': row['employee_id'],
                        'store_id': row['store_id'],
                        'money_code': row['money_code'],
                        'item_id': row['item_id'],
                        'total': float(row['total']) / self.divisa}) # conversión de pesos mexicanos a dólares


if __name__ == '__main__':
    luigi.run()
