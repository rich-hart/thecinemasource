from django.db import connections
from django.http import HttpResponse, HttpResponseNotFound


#def posts(request,number):
##    import ipdb; ipdb.set_trace()
#    with connections['recovery'].cursor() as cursor:
#        cursor.execute("SELECT post_title, post_content FROM ts_posts WHERE id = %s", [str(number)])
#        data = cursor.fetchone()
#    if data:
#        html = """
#            <html>
#                <head>
#                    <title>{0}</title>
#                </head>
#                <body>
#                    <h1>{0}</h1>
#                    <pre>{1}</pre>
#                </body>
#            </html>
#        """.format(data[0],data[1])
#        return HttpResponse(html)
#    else:
#        HttpResponseNotFound('<h1>Page not found</h1>')

