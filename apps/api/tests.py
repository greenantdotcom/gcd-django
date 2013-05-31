from django.test import TestCase
from django.core.urlresolvers import reverse
from django.contrib.auth.models import User
from django.utils import simplejson
from django.conf import settings

from piston import oauth
from piston.models import Consumer, Token
from piston.forms import OAuthAuthenticationForm

import base64
import unittest
from django.test import TestCase

### http://thomas.pelletier.im/2009/12/test-your-django-piston-api-with-auth/

class TestPublisher(TestCase):
    def test_publisher_list(self):
        response = self.client.get('/api/publisher', {})
        self.assertEqual(response.status_code, 200)
    
    def test_real_publisher_info(self):
        response = self.client.get('/api/publisher/88', {})
        self.assertEqual(response.status_code, 200)
    
    def test_missing_publisher_info(self):
        response = self.client.get('/api/publisher/999999')
        self.assertEqual(response.status_code, 404)
    
    def test_brands_found(self):
        response = self.client.get('/api/publisher/88/brands')
        self.assertEqual(response.status_code, 200)
        ## assert size
    
    def test_series_found(self):
        response = self.client.get('/api/publisher/88/series')
        self.assertEqual(response.status_code, 200)
        ## assert size

class TestBrand(TestCase):
    def test_list(self):
        response = self.client.get('/api/brand', {})
        self.assertEqual(response.status_code, 200)
    
    def test_valid_item(self):
        response = self.client.get('/api/brand', {})
        self.assertEqual(response.status_code, 200)
        
    
    # ### TODO: Helpful if there was a deleted entity in the database...
    # def test_deleted_publisher_info(self):
    #     response = self.client.get('/api/publisher/88', {}, **self.extra)
    #     self.assertEqual(response.status_code, 404)

