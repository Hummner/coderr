from django.test import TestCase
from rest_framework.test import APITestCase
from django.contrib.auth.models import User
from rest_framework.test import APIClient
from rest_framework.authtoken.models import Token
from django.urls import reverse
from rest_framework import status
from profile_app.models import Profile
from offer_app.models import Offer, OfferDetails



class BaseOfferTest(APITestCase):
    def setUp(self):
        self.user = User.objects.create(username="AdamTest", email="test@test.de", password="TestTest")
        self.profile = Profile.objects.create(user=self.user, type="business", username= self.user.username)
        self.client = APIClient()
        self.token = Token.objects.create(user=self.user)
        self.client.credentials(HTTP_AUTHORIZATION = "Token " + self.token.key)


class CreateOffer(BaseOfferTest):
    def test_offer(self):
        url = reverse("offers-list")
        data = {
            "title": "Grafikdesign-Paket LOW",
            "description": "Ein umfassendes Grafikdesign-Paket für Unternehmen.",
            "details": []
            }
        response = self.client.post(url, data, format='json')
        self.offerId = response.data.get('id')

        self.assertEqual(response.status_code, status.HTTP_201_CREATED)

    def test_offer_customer_user_no_perm(self):
        self.profile.type = "customer"
        self.profile.save()

        url = reverse("offers-list")
        data = {
            "title": "Grafikdesign-Paket LOW",
            "description": "Ein umfassendes Grafikdesign-Paket für Unternehmen.",
            "details": []
            }

        response = self.client.post(url, data, format='json')
        self.assertEqual(response.status_code, status.HTTP_403_FORBIDDEN)



class DeleteOffer(BaseOfferTest):
    def setUp(self):
        super().setUp()
        self.user2 = User.objects.create(username="AdamTest2", email="test@test2.de", password="TestTest")
        self.profile2 = Profile.objects.create(user=self.user2, type="business", username= self.user.username)
        self.offer = Offer.objects.create(title="Grafikdesign-Paket LOW", description="Ein umfassendes Grafikdesign-Paket für Unternehmen.", creator = self.user)
        self.offer2 = Offer.objects.create(title="Grafikdesign-Paket LOW", description="Ein umfassendes Grafikdesign-Paket für Unternehmen.", creator = self.user2)

    def test_delete_offer_no_permission(self):
        url = reverse("offers-detail", kwargs={'pk': self.offer2.id})
        response = self.client.delete(url)
        self.assertEqual(response.status_code, status.HTTP_403_FORBIDDEN)

    def test_delete_offer(self):
        url = reverse("offers-detail", kwargs={'pk': self.offer.id})
        response = self.client.delete(url)
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)


class PatchOffer(BaseOfferTest):
    def setUp(self):
        super().setUp()
        self.offer = Offer.objects.create(title="Grafikdesign-Paket LOW", description="Ein umfassendes Grafikdesign-Paket für Unternehmen.", creator = self.user)

    def test_patch_offer(self):
        url = reverse("offers-detail", kwargs={'pk': self.offer.id})
        data = {
            "title": "Grafikdesign-Paket LOW PATCHED"
        }
        response = self.client.patch(url, data, format='json')
        self.assertEqual(response.status_code, status.HTTP_200_OK)


class PatchOfferDetails(BaseOfferTest):
    
    def setUp(self):
        super().setUp()
        self.offer = Offer.objects.create(title="Grafikdesign-Paket LOW", description="Ein umfassendes Grafikdesign-Paket für Unternehmen.", creator = self.user)
        self.offerDetail = OfferDetails.objects.create(
            offer = self.offer,
            price = 100,
            title = "Details Title",
            offer_type = "basic",
            features = ['Beest', 'Better'],
            delivery_time_in_days = 3,
            revisions = 0

        )


    def test_patch_details(self):
        url = reverse("offers-detail", kwargs={'pk': self.offer.id})

        data = {
            'title': 'Patched Offer Title',
            'details' : [
                {'offer_type':'basic', 'title': 'Patched'}
            ]
        }

        response = self.client.patch(url, data, format='json')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        print(response.json())