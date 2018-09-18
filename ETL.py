#!/usr/bin/python

import sys
import pandas as pd
import sqlalchemy


def main(csv_filename):
    """ETLs specified csv file to DB"""
    import_from_csv(csv_filename)


def import_from_csv(csv_filename):
    """Imports data from csv file"""
    data_frame = pd.read_csv(csv_filename)
    conn = sqlalchemy.create_engine('mysql+mysqlconnector://admin:master123@localhost:3306/snap', echo=False)
    data_frame.to_sql(name='jobs',
                      con=conn,
                      if_exists='replace',
                      index=False,
                      dtype=sqlalchemy.types.VARCHAR(length=255))


if __name__ == '__main__':
    if len(sys.argv) == 2:
        main(sys.argv[1])
    else:
        print('No arguments specified')
