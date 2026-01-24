"""
URL configuration for core project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from offer_app.api.views import OfferDetailsView
from order_app.api.views import OrderInProgress, OrderCompleted
from base_info_app.api.views import BaseInfo
from profile_app.api.views import CustomerProfileListView, BusinessProfileListView
from django.conf.urls.static import static
from django.conf import settings
from django.contrib.staticfiles.urls import staticfiles_urlpatterns

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/', include('auth_app.api.urls')),
    path('api/profile/', include('profile_app.api.urls')),
    path('api/profiles/business/', BusinessProfileListView.as_view(), name='business_profiles'),
    path('api/profiles/customer/', CustomerProfileListView.as_view(), name='customer_profiles'),
    path('api/offers/', include('offer_app.api.urls')),
    path('api/orders/', include('order_app.api.urls')),
    path('api/reviews/', include('review_app.api.urls')),
    path('api/offerdetails/<int:pk>/', OfferDetailsView.as_view()),
    path('api/order-count/<int:pk>/', OrderInProgress.as_view()),
    path('api/completed-order-count/<int:pk>/', OrderCompleted.as_view()),
    path('api/base-info/', BaseInfo.as_view())
]

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
urlpatterns += staticfiles_urlpatterns()
