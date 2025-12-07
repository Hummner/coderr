from django.test import TestCase
from rest_framework.test import APITestCase
from django.contrib.auth.models import User
from rest_framework.test import APIClient
from rest_framework.authtoken.models import Token
from django.urls import reverse
from rest_framework import status
from profile_app.models import Profile
from offer_app.models import Offer, OfferDetails
from order_app.models import Order

# Create your tests here.


class BaseOrderTest(APITestCase):
    def setUp(self):
        self.user = User.objects.create(username="AdamTest", email="test@test.de", password="TestTest")
        self.user2 = User.objects.create(username="AdamTest2", email="test@test2.de", password="TestTest2")
        self.profile = Profile.objects.create(user=self.user, type="customer", username= self.user.username)
        self.profile2 = Profile.objects.create(user=self.user2, type="business", username= self.user2.username)
        self.client = APIClient()
        self.token = Token.objects.create(user=self.user)
        self.client.credentials(HTTP_AUTHORIZATION = "Token " + self.token.key)
        self.offer = Offer.objects.create(title='Grafikdesign-Paket LOW', description = 'Ein umfassendes Grafikdesign-Paket für Unternehmen', creator= self.user)
        self.offer_details = OfferDetails.objects.create(offer=self.offer, title= "Basic Design", revisions= 2, delivery_time_in_days= 5,
                                                         price= 100, features= ["Logo Design"], offer_type = "basic")
  


class CreateOrder(BaseOrderTest):

    def test_create_order(self):
        url = reverse('orders-list')
        data = {
            "offer_detail_id": self.offer_details.id
        }
        response = self.client.post(url, data, format='json')
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)

class PatchOrder(BaseOrderTest):
    def setUp(self):
        super().setUp()
        url_post = reverse('orders-list')
        data = {'offer_detail_id':self.offer_details.id}
        response = self.client.post(url_post, data, format='json')
        response_json = response.json()
        print(response_json['id'])
        self.url = reverse('orders-detail', kwargs={'pk': response_json['id']})


    def test_patch_order(self):
        data = {
             "status": "completed"
        }
        print(self.profile.type)
        
        response = self.client.patch(self.url, data, format='json')

        self.assertEqual(response.status_code, status.HTTP_200_OK)
        


        
