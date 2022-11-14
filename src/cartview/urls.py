from django.urls import path, include

from . import views
app_name = "cartview"

# Cart Urls
urlpatterns = [
    path('cart/', views.ListCart.as_view(), name='carts-list'),
    path('cart/<int:pk>/', views.DetailCart.as_view(), name='cart-detail'),
    path('cart/create/', views.CreateCart.as_view(), name='cart-create'),
    path('cart/<int:pk>/update/', views.UpdateCart.as_view(), name='cart-update'),
    path('cart/<int:pk>/delete/', views.DeleteCart.as_view(), name='cart-delete'),
]

# CartItem Urls
urlpatterns += [
    path('cartitem/', views.ListCartItem.as_view(), name='cartitem-list'),
    path('cartitem/<int:pk>/', views.DetailCartItem.as_view(), name='cartitem-detail'),
    path('cartitem/create/', views.CreateCartItem.as_view(), name='cartitem-create'),
    path('cartitem/<int:pk>/update/', views.UpdateCartItem.as_view(), name='cartitem-update'),
    path('cartitem/<int:pk>/delete/', views.DeleteCartItem.as_view(), name='cartitem-delete'),
]