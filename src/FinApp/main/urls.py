from django.urls import path
from . import views


urlpatterns = [
    path('', views.index, name='home'),
    path('add_spend', views.calc, name='add_spend'),
    path('add_category', views.add_cat, name='add_cat'),
    path('about', views.about, name='about'),
    path('categoty/<int:cat_id>/', views.show_category, name='category'),
    path('spends_by_date', views.spend_by_date, name='spends_by_date'),
    path('spends_by_date/day', views.spend_by_day, name='spends_by_day'),
    path('spends_by_date/month', views.spend_by_month, name='spends_by_month'),
    path('spends_by_date/year', views.spend_by_year, name='spends_by_year'),
]
