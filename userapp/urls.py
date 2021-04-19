from django.urls import path
from userapp import views
from .views import BehanceImageView
urlpatterns = [
    path('base/',views.UserInfoView.as_view(),name='base'),
    path('index/',views.UserSearchView.as_view(),name='index'),
    path('userlist/',views.UserListView.as_view(),name='userlist'),
    path('behance/',BehanceImageView,name='behance'),
    path('dashboard/',views.Dashboard.as_view()),
]
