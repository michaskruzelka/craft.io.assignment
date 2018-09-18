#!/usr/bin/python

import sys
import pandas as pd
import sqlalchemy
import config


def main(csv_filename):
    """ETLs specified csv file to DB"""
    data_frame = pd.read_csv(csv_filename)
    mysql_host = 'mysql+mysqlconnector://' \
                 + config.USER + ':' \
                 + config.PASSWORD + '@' \
                 + config.HOST + ':' \
                 + str(config.PORT) + '/' \
                 + config.DB
    conn = sqlalchemy.create_engine(mysql_host, echo=False)
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
