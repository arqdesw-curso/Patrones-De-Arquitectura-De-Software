#!/usr/bin/env python
# -*- coding: utf-8 -*-
#-------------------------------------------------------------------------
# Archivo: jpy_to_usd.py
# Capitulo: 4 Patron Pipes and Filters
# Autor(es): Perla Velasco & Yonathan Mtz.
# Version: 1.0 Enero 2018
# Descripción:
#
#   Ésta clase define el rol de un Filter, es decir, procesa los datos de las ventas.
#
#   Las características de ésta clase son las siguientes:
#
#                                            jpy_to_usd.py
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


class JPYToUSD(luigi.Task):
    source = "jpy.csv" # entrada del Filter
    divisa = 113.25 # valor de la moneda que será utilizado para convertir los dólares

    def output(self):
        return luigi.LocalTarget("jpy_to_usd.csv") # salida del Filter

    def requires(self):
        return ExtractData() # tarea(s) de las que depende el Filter

    def run(self):
        with open(self.source) as csv_file:
            csv_reader = csv.DictReader(csv_file)
            jpy_dataset = self.output()
            with jpy_dataset.open('w') as jpy_opened:
                headers = ['order_id', 'date', 'client_id', 'employee_id', 'store_id', 'money_code', 'item_id',
                       'total']
                jpy_writer = csv.DictWriter(jpy_opened, fieldnames=headers)
                jpy_writer.writeheader()
                for row in csv_reader:
                    jpy_writer.writerow({
                        'order_id': row['order_id'],
                        'date': row['date'],
                        'client_id': row['client_id'],
                        'employee_id': row['employee_id'],
                        'store_id': row['store_id'],
                        'money_code': row['money_code'],
                        'item_id': row['item_id'],
                        'total': float(row['total']) / self.divisa }) # conversión de yenes a dólares


if __name__ == '__main__':
    luigi.run()
