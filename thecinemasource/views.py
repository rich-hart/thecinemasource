from django.db import connections
from django.http import HttpResponse, HttpResponseNotFound


def posts(request,number):
#    import ipdb; ipdb.set_trace()
    with connections['recovery'].cursor() as cursor:
        cursor.execute("SELECT post_content FROM ts_posts WHERE id = %s", [str(number)])
        content = cursor.fetchone()
    if content and content[0]:
        html = "<html><body><p>{0}</p></body></html>".format(content[0])
        return HttpResponse(html)
    else:
        HttpResponseNotFound('<h1>Page not found</h1>')

