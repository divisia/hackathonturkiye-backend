import json
from django.test import TestCase, Client
from django.contrib.auth.models import User
from rest_framework.test import APIClient
from event.views import EventViewSet
from .models import *



class EventTest(TestCase):

    def setUp(self):
        User.objects.create_user(username='testserver', password='testserver')
        EventType.objects.create(name='hackathon')

    def test_post(self):
        logged = self.client.login(username='testserver', password='testserver')
        self.assertEqual(logged, True, 'Cannot login')
        response = self.client.post('/events/', {
            'name':'Lorem ipsum hackathon',
            'starts_at':'2020-01-02T00:00',
            'origin_url':'https://hackathonturkiye.com',
            'description':'Test test test test',
            'location':'online',
            'etype.name': 'hackathon'
        })
        self.assertEqual(response.status_code, 201, "Unwanted status code returned.")
        

    def test_is_publicly_writeable_better_not(self):
        # test whether only logged in users can post
        self.client.logout()
        response = self.client.post('/events/', {
            'name':'Lorem ipsum hackathon2',
            'starts_at':'2020-01-02T00:10',
            'origin_url':'https://hackathonturkiye.com',
            'description':'Test test test test',
            'location':'online',
            'etype':'hackathon'
        })
        self.assertEqual(response.status_code, 403, "POST method publicly available.")


    def test_get(self):
        location = 'online'
        response = self.client.get(f'/events/?location={location}&format=json')
        json = response.json()
        self.assertIsInstance(json.get('results', False), list, "Response was not containing a JSON.")
        results = json.get('results')
        for o in results:
            self.assertEqual(o.get(location, None), location, "Query string didn't do its job.")
        self.assertEqual(response.status_code, 200, 'Response code is not OK')