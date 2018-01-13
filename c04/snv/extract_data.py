#!/usr/bin/env python
# -*- coding: utf-8 -*-
#-------------------------------------------------------------------------
# Archivo: extract_data.py
# Capitulo: 4 Patron Pipes and Filters
# Autor(es): Perla Velasco & Yonathan Mtz.
# Version: 1.0 Enero 2018
# Descripción:
#
#   Ésta clase define el rol de un Filter, es decir, filtra los datos de las ventas.
#
#   Las características de ésta clase son las siguientes:
#
#                                            extract_data.py
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
import os
import sys


class ExtractData(luigi.Task):
    sys.path.insert(0, os.path.abspath('..'))
    source = "../resource/sales-2017.csv" # entrada del Filter

    def output(self):
        return {'jpy': luigi.LocalTarget("../resource/jpy.csv"), 'eur': luigi.LocalTarget("../resource/eur.csv"),
                'mxn': luigi.LocalTarget("../resource/mxn.csv")} # salida del Filter

    def requires(self):
        return [] # tarea(s) de las que depende el Filter

    def run(self):
        with open(self.source) as csv_file:
            csv_reader = csv.DictReader(csv_file)
            jpy_dataset = self.output()['jpy']
            eur_dataset = self.output()['eur']
            mxn_dataset = self.output()['mxn']
            with jpy_dataset.open('w') as jpy_opened, eur_dataset.open('w') as eur_opened, mxn_dataset.open(
                    'w') as mxn_opened:
                headers = ['order_id', 'date', 'client_id', 'employee_id', 'store_id', 'money_code', 'item_id',
                           'total']
                jpy_writer = csv.DictWriter(jpy_opened, fieldnames=headers)
                eur_writer = csv.DictWriter(eur_opened, fieldnames=headers)
                mxn_writer = csv.DictWriter(mxn_opened, fieldnames=headers)
                jpy_writer.writeheader()
                eur_writer.writeheader()
                mxn_writer.writeheader()
                for row in csv_reader:
                    data_to_write = {'order_id': row['order_id'],
                                     'date': row['date'],
                                     'client_id': row['client_id'],
                                     'employee_id': row['employee_id'],
                                     'store_id': row['store_id'],
                                     'money_code': row['money_code'],
                                     'item_id': row['item_id'],
                                     'total': row['total']}
                    if row['money_code'] == 'JPY': # filtrado de ventas en Japón
                        jpy_writer.writerow(data_to_write)
                    elif row['money_code'] == 'EUR': # filtrado de ventas en Alemania
                        eur_writer.writerow(data_to_write)
                    else: # filtrado de ventas en México
                        mxn_writer.writerow(data_to_write)


if __name__ == '__main__':
    luigi.run()
