from django.urls import path, include

from . import views
app_name = "cartview"

# Cart Urls

urlpatterns = [
    path('cart/', views.cart, name='cart'),
    path('cartitem_del/<int:pk>/', views.DeleteCartItem.as_view(), name='cartitem_del'),
    path('submit_order/', views.Order.as_view(), name='submit_order'),
    path('submit_success/', views.OrderSuccess.as_view(), name='submit_success'),
    #path('cart_item', views.cart_item, name='cart_item'),
    #path('cart_item', views.ViewCartItem.as_view(), name='cart_item'),
    
]

"""
urlpatterns = [
    path('cart/', views.cart, name='cart'),
    path('cart-list', views.ListCart.as_view(), name='cart_list'),
    path('cart/create/', views.CreateCart.as_view(), name='cart_create'),
    path('cart/<int:pk>/update/', views.UpdateCart.as_view(), name='cart_update'),
    path('cart/<int:pk>/delete/', views.DeleteCart.as_view(), name='cart_delete'),
]

# CartItem Urls
urlpatterns += [
    path('cartitem/', views.cart_item, name='cartitem_view'),
    #path('cartitem/', views.ViewCartItem.as_view(), name='cartitem_view'),
    #path('cartitem/<int:pk>/', views.DetailCartItem.as_view(), name='cartitem_detail'),
    path('cartitem/create/', views.CreateCartItem.as_view(), name='cartitem_create'),
    path('cartitem/<int:pk>/update/', views.UpdateCartItem.as_view(), name='cartitem_update'),
    path('cartitem/<int:pk>/delete/', views.DeleteCartItem.as_view(), name='cartitem_delete'),
]

"""