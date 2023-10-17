from django.urls import path

from . import views

app_name = "vitrineApp"
urlpatterns = [
    path('', views.index, name='index'),
    path('index/', views.index, name='index'),
    path('foire-africaine-de-paris/', views.fap, name='fap'),
    path('marche-de-noel-africain/', views.mna, name='mna'),
    path('african-fashion-cook/', views.afc, name='afc'),
    path('fashion-west-africa/', views.fwa, name='fwa'),
    path('billetterie/', views.billetterie, name='billetterie'),
    path('juste-une-danse/', views.juste, name='juste'),
    path('foire-aux-questions/', views.faq, name='faq'),
    path('fica/', views.fica, name='fica'),
    
    path('events/participation/purchase/<uuid:id>/', views.purchase, name='purchase'),
    
    # path('programme', views.programme, name='programme'),
    # path('participants', views.participants, name='participants'),
    path('stand/', views.stand, name='stand'),
    # path('unes', views.unes, name='unes'),
    path('contacts/', views.contacts, name='contacts'),
]