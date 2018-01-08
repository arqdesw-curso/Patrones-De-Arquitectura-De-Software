#!/usr/bin/env python
# -*- coding: utf-8 -*-
#-------------------------------------------------------------------------
# Archivo: eur_to_usd.py
# Capitulo: 4 Patron Pipes and Filters
# Autor(es): Perla Velasco & Yonathan Mtz.
# Version: 1.0 Enero 2018
# Descripción:
#
#   Ésta clase define el rol de un Filter, es decir, procesa los datos de las ventas.
#
#   Las características de ésta clase son las siguientes:
#
#                                            eur_to_usd.py
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


class EURToUSD(luigi.Task):
    source = "eur.csv" # entrada del Filter
    divisa = 0.83 # valor de la moneda que será utilizado para convertir los dólares

    def output(self):
        return luigi.LocalTarget("eur_to_usd.csv") # salida del Filter

    def requires(self):
        return ExtractData() # tarea(s) de la que depende éste Filter

    def run(self):
        with open(self.source) as csv_file:
            csv_reader = csv.DictReader(csv_file)
            eur_dataset = self.output()
            with eur_dataset.open('w') as eur_opened:
                headers = ['order_id', 'date', 'client_id', 'employee_id', 'store_id', 'money_code', 'item_id',
                           'total']
                eur_writer = csv.DictWriter(eur_opened, fieldnames=headers)
                eur_writer.writeheader()
                for row in csv_reader:
                    eur_writer.writerow({
                        'order_id': row['order_id'],
                        'date': row['date'],
                        'client_id': row['client_id'],
                        'employee_id': row['employee_id'],
                        'store_id': row['store_id'],
                        'money_code': row['money_code'],
                        'item_id': row['item_id'],
                        'total': float(row['total']) / self.divisa}) # conversión de euros a dólares


if __name__ == '__main__':
    luigi.run()
