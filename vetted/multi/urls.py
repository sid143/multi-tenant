from django.urls import path
from . import views
urlpatterns = [
    path('',views.IndexView.as_view(),name='index'),
    path('mainemployee/',views.MainEmployeeView.as_view(),name='mainemployee'),
    path('newhtml/',views.NewhtmlView.as_view(),name='newhtml'),
    path('profess/',views.ProfessView.as_view(),name='profess'),
]