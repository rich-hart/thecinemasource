#./manage.py sqlsequencereset
import ipdb; ipdb.set_trace()
import os
from os import listdir
from os.path import isfile, join
import psycopg2
import mysql.connector

OLD_WEBSITE_IMAGE_UPLOADS = '/home/rich/Projects/dan_website_rewrite/backup/public_html/wp-content/uploads/'

DATABASES = {
    'default': {
        'NAME': os.environ.get('THECINEMASOURCE_DATABASE_NAME'),
        'USER': os.environ.get('THECINEMASOURCE_DATABASE_USER'),
        'PASSWORD': os.environ.get('THECINEMASOURCE_DATABASE_PASSWORD'),
        'HOST': os.environ.get('THECINEMASOURCE_DATABASE_HOST'),
        'PORT': os.environ.get('THECINEMASOURCE_DATABASE_PORT'),
    },
    'recovery': {
        'NAME': 'thecinemasource',
        'USER': 'rich',
        'PASSWORD': 'password',
        'PORT': 3306,
        'HOST': 'localhost',
    },    
}

media_files = [f for f in listdir(OLD_WEBSITE_IMAGE_UPLOADS) if isfile(join(OLD_WEBSITE_IMAGE_UPLOADS, f))]

mysql_db_conn = mysql.connector.connect(
  host=DATABASES['recovery']['HOST'],
  user=DATABASES['recovery']['USER'],
  passwd=DATABASES['recovery']['PASSWORD'],
  database=DATABASES['recovery']['NAME'],
)
mysql_db_cursor = mysql_db_conn.cursor(dictionary=True)

#mysql_db_cursor.execute('SELECT * FROM ts_posts WHERE post_title LIKE "%Interview for%"')
mysql_db_cursor.execute('SELECT * FROM ts_posts WHERE post_type="interview" AND post_content!=""')

mysql_db_result = mysql_db_cursor.fetchall()

psql_db_conn = psycopg2.connect(
    host=DATABASES['default']['HOST'],
    database=DATABASES['default']['NAME'],
    user=DATABASES['default']['USER'],
    password=DATABASES['default']['PASSWORD'],
)

psql_db_cursor = psql_db_conn.cursor()

for row in mysql_db_result:
    row['post_date'] = row['post_date'].date() 
    psql_db_cursor.execute("INSERT INTO interviews_post (deprecated_id, author, date, content, title, category, excerpt) "
                           "VALUES (%s, %s, %s, %s, %s, %s, %s)",(
                                   row['ID'],
                                   row['post_author'],
                                   row['post_date'],
                                   row['post_content'],
                                   row['post_title'],
                                   "IN",
                                   row['post_excerpt'],
                               )
                           )
    psql_db_conn.commit()
psql_db_conn.close()


