from django.urls import path, include
from . import views
from django.contrib.auth.views import LoginView, LogoutView

urlpatterns = [
    path('homepage/', views.homepage, name = 'homepage'),
    path('opensales/', views.open_sales, name = 'open_sales'),
    path('newsale/', views.new_sale, name = 'new_sale'),
    path('newoffer/<int:s_id>', views.new_offer, name = 'new_offer'),
    path('myopensales', views.my_open_sales, name = 'my_open_sales'),
    path('myopensales/delete/<int:s_id>', views.delete_sale, name = 'delete_sale'),
    path('viewoffers/<int:s_id>', views.view_offers, name = 'view_offers'),
    path('mydeck/', views.my_deck, name = 'my_deck'),
    path('offeraccepted/<int:o_id>', views.offer_accepted, name = 'offer_accepted'),
    path('offerrejected/<int:o_id>', views.offer_rejected, name = 'offer_rejected'),
    path('myoffers', views.my_offers, name = 'my_offers'),
]