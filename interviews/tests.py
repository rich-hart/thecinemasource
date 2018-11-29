from io import BytesIO
from django.conf import settings

from django.test import TestCase
from rest_framework.test import APIClient
# Create your tests here.
class TestIntervies(TestCase):
    def test_post_with_photograph(self):
#        import ipdb; ipdb.set_trace()
        client = APIClient()
        response = client.get('/posts/')
        self.assertEqual(response.status_code,200)
        self.assertEqual(response.data.get('count'),0)

        data = { 
            "deprecated_id": 0,
            "author": "Daniel Deevy",
            "date": "2018-11-26",
            "content": "Post content",
            "title": "Interview Name",
            "category": "IN",
            "excerpt": "Interview with person",
            "name": "Interview Post Name"
        }
        response = client.post('/posts/',data=data,format='json')
        self.assertEqual(response.status_code, 201)

        response = client.get('/posts/')
        self.assertEqual(response.status_code,200)
        self.assertEqual(response.data.get('count'),1)

        expected_id = 1
        returned_id = response.data.get('results').pop().get('id')

        self.assertEqual(expected_id,returned_id)
        with open(settings.BASE_DIR+'/interviews/linux_logo.jpeg',  mode='rb') as fp:
#            image = BytesIO(fp.read())
            response = client.post('/photographs/', data={'post': returned_id, 'upload': fp})

        self.assertEqual(response.status_code, 201)

        self.assertIn('linux_logo.jpeg',response.data.get('upload'))
        self.assertIn(settings.MEDIA_URL,response.data.get('upload'))

