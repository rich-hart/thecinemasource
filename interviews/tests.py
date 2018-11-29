from django.test import TestCase
from rest_framework.test import APIClient
# Create your tests here.
class TestIntervies(TestCase):
    def test_post(self):
        import ipdb; ipdb.set_trace()
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

