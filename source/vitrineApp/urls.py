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
    path('billetterie_visiteurs/', views.billetterie, name='billetterie'),
    path('juste-une-danse/', views.juste, name='juste'),
    path('fica/', views.fica, name='fica'),
    
    path('events/participation/purchase/<uuid:id>/', views.purchase, name='purchase'),
    
    path('billetterie_exposants/', views.stand, name='stand'),
    path('blogs', views.blogs, name='blogs'),
    path('blog/<uuid:id>', views.blog, name='blog'),
    path('contacts/', views.contacts, name='contacts'),
]