from django.test import TestCase
from rest_framework.test import APITestCase
from django.contrib.auth.models import User
from rest_framework.test import APIClient
from rest_framework.authtoken.models import Token
from django.urls import reverse
from rest_framework import status
from profile_app.models import Profile
from offer_app.models import Offer, OfferDetails

class CreateOffer(APITestCase):

    def setUp(self):
        self.user = User.objects.create(username="AdamTest", email="test@test.de", password="TestTest")
        self.profile = Profile.objects.create(user=self.user, type="business", username= self.user.username)
        self.client = APIClient()
        self.token = Token.objects.create(user=self.user)
        self.client.credentials(HTTP_AUTHORIZATION = "Token " + self.token.key)
        print(self.user)


    def test_offer(self):
        url = reverse("offers-list")
        data = {
            "title": "Grafikdesign-Paket LOW",
            "description": "Ein umfassendes Grafikdesign-Paket für Unternehmen.",
            "details": []
            }
        response = self.client.post(url, data, format='json')
        self.offerId = response.data.get('id')
        print(self.offerId)
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)



class DeleteOffer(APITestCase):

    def setUp(self):
        self.user = User.objects.create(username="AdamTest", email="test@test.de", password="TestTest")
        self.profile = Profile.objects.create(user=self.user, type="business", username= self.user.username)
        self.offer = Offer.objects.create(title="Grafikdesign-Paket LOW", description="Ein umfassendes Grafikdesign-Paket für Unternehmen.", creator = self.user)
        self.client = APIClient()
        self.token = Token.objects.create(user=self.user)
        self.client.credentials(HTTP_AUTHORIZATION = "Token " + self.token.key)



    def test_delete_offer(self):
        url = reverse("offers-detail", kwargs={'pk': self.offer.id})
        response = self.client.delete(url)
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)
        self.client.logout()