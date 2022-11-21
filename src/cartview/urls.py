from django.urls import path, include

from . import views
app_name = "cartview"

# Cart Urls
urlpatterns = [
    path('cart/', views.cart, name='cart'),
    path('cart-list', views.ListCart.as_view(), name='cart_list'),
    path('cart/create/', views.CreateCart.as_view(), name='cart_create'),
    path('cart/<int:pk>/update/', views.UpdateCart.as_view(), name='cart_update'),
    path('cart/<int:pk>/delete/', views.DeleteCart.as_view(), name='cart_delete'),
]

# CartItem Urls
urlpatterns += [
    path('cartitem/', views.ListCartItem.as_view(), name='cartitem_list'),
    path('cartitem/<int:pk>/', views.DetailCartItem.as_view(), name='cartitem_detail'),
    path('cartitem/create/', views.CreateCartItem.as_view(), name='cartitem_create'),
    path('cartitem/<int:pk>/update/', views.UpdateCartItem.as_view(), name='cartitem_update'),
    path('cartitem/<int:pk>/delete/', views.DeleteCartItem.as_view(), name='cartitem_delete'),
]