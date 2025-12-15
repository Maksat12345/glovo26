from django.urls import path, include
from rest_framework import routers
from .views import (UserProfileListAPIView, UserProfileDetailAPIView, CategoryListAPIView, CategoryDetailAPIView,
                    StoreListAPIView, StoreDetailAPIView, OrderViewSet, CourierProductViewSet
                    , ReviewCreateAPIView, ReviewEditAPIView, OrderStatusListView, OrderStatusDetailView, StoreViewSet)

router = routers.SimpleRouter()
router.register('status_create', StoreViewSet)
router.register('orders', OrderViewSet)
router.register('courierproducts', CourierProductViewSet)


urlpatterns = [
    path('', include(router.urls)),
    path('users/', UserProfileListAPIView.as_view(), name='user-profile-list'),
    path('users/<int:pk>/', UserProfileDetailAPIView.as_view(), name='user-profile-detail'),
    path('categories/', CategoryListAPIView.as_view(), name='category-list'),
    path('categories/<int:pk>/', CategoryDetailAPIView.as_view(), name='category-detail'),
    path('stores/', StoreListAPIView.as_view(), name='store-list'),
    path('stores/<int:pk>/', StoreDetailAPIView.as_view(), name='store-detail'),
    path('reviews/', ReviewCreateAPIView.as_view(), name='review-create'),
    path('reviews/<int:pk>/', ReviewEditAPIView.as_view(), name='review-edit'),
    path('orderstatus/', OrderStatusListView.as_view(), name='order-list'),
    path('orderstatus/<int:pk>/', OrderStatusDetailView.as_view(), name='order-detail'),
]