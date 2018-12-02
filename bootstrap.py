#./manage.py sqlsequencereset
#import ipdb; ipdb.set_trace()
import re
import os
from os import listdir
from os.path import isfile, join
import psycopg2
import mysql.connector
TEST=False
OLD_WEBSITE_IMAGE_UPLOADS = '/home/rich/Projects/dan_website_rewrite/thecinemasource/media'

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

count = 0

interview_errors = []

for row in mysql_db_result:
    if TEST:
        count+=1
        if count >10:
            break
    try:
        psql_db_cursor = psql_db_conn.cursor()
    
        title_tokens = row['post_title'].lower().split(' interview for ')
    
        name = title_tokens[0]
        name = name.lower().replace(' ','_')
    
        film = title_tokens[1]
        film = film.lower().replace(' ','_')
#        for image_file in media_files:
#            image_tokens = re.split('-|_|\.', image_file.lower())
#            for token in title_tokens:

#        image_files = [ i for i in media_files if name in i.lower() and film in i.lower()]
        file_prefix = name + '-' + film
        image_files = [ i for i in media_files if file_prefix in i.lower()]
        row['post_date'] = row['post_date'].date() 
        psql_db_cursor.execute("INSERT INTO interviews_post (deprecated_id, author, date, content, title, category, excerpt) "
                               "VALUES (%s, %s, %s, %s, %s, %s, %s) RETURNING id",(
                                       row['ID'],
                                       row['post_author'],
                                       row['post_date'],
                                       row['post_content'],
                                       row['post_title'],
                                       "IN",
                                       row['post_excerpt'],
                                   )
                               )
#        psql_db_conn.commit()
        row_id = psql_db_cursor.fetchone()[0]
        if image_files:
            for image_file in image_files:
                psql_db_cursor.execute("INSERT INTO interviews_photograph (upload, post_id) VALUES (%s, %s)",
                    (image_file,row_id)
                )

        psql_db_conn.commit()
    except psycopg2.DataError as e:
        interview_errors.append(row['post_title'])
        psql_db_conn.commit()
        psql_db_cursor = psql_db_conn.cursor()
#        import ipdb; ipdb.set_trace()
#        pass

psql_db_conn.close()

print("ERRORS ON INTERVIEWS:")
for error in interview_errors:
    print(error)
