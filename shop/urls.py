from django.urls import path
from . import views
from .views import search, AboutView, ContactsView, GuaranteeView

app_name = 'shop'

urlpatterns = [
    path('search/', search, name='search'),
    path('', views.product_list, name='product_list'),
    path('about/', AboutView.as_view(), name='about'),
    path('guarantee/', GuaranteeView.as_view(), name='guarantee'),
    path('contacts/', ContactsView.as_view(), name='contacts'),    
    path('<slug:category_slug>/', views.product_list, name='product_list_by_category'),
    path('<int:id>/<slug:slug>/', views.product_detail, name='product_detail'),
    path('filter/price/', views.filter_by_price, name='filter_by_price'),
]
