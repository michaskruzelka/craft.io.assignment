from flask import Flask
import pymysql
import config

app = Flask(__name__)


@app.route('/jobs/<location>')
def jobs(location):
    conn = pymysql.connect(
        host=config.HOST,
        port=config.PORT,
        user=config.USER,
        password=config.PASSWORD,
        db=config.DB,
        cursorclass=pymysql.cursors.DictCursor)
    with conn.cursor() as cursor:
        sql = "SELECT * FROM `jobs` WHERE `Location` LIKE %s"
        cursor.execute(sql, ('%' + location + '%',))
        rows = cursor.fetchall()
        result = []
        for row in rows:
            row_string = row.get('Job Title') + ', ' + row.get('Category')\
                         + ', ' + row.get('Status') + ', ' + row.get('Location')
            result.append(row_string)
        if len(result) == 0:
            return 'No jobs found in ' + location
        return '<br/>'.join(result)


@app.route('/')
def hello():
    return 'This is API'


app.run(port=80)
