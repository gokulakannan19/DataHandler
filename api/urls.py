from django.urls import path
from .import views

urlpatterns = [
    # path('checkk', views.check),
    path('accounts/', views.account_list),
    path('accounts/<str:pk>/', views.account_detail),
    path('destinations/', views.destination_list),
    path('destinations/<int:pk>/', views.destination_detail),
    path('headers/', views.header_list),
    path('headers/<int:pk>/', views.header_detail),
    path('get-account-destinations/<str:pk>/', views.get_accounts_destination),
    path('server/incoming_data/', views.data_handler)
]
