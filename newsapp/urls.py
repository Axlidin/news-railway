from django.urls import path
from .views import (ListPageView, DetailPageView, HomePageView, ContactPageView,
                    LocalNewsViews, XorijNewsViews, SportNewsViews, TechnolgyNewsViews,
                    UpdateNewsView, DeleteNewsView, CreateNewsView)

app_name = 'newsapp'

urlpatterns = [
    path('', HomePageView.as_view(), name='home_page'),
    path('create/', CreateNewsView.as_view(), name='create_news'),
    path('contact-us/', ContactPageView.as_view(), name='contact_page'),
    path('all-news/', ListPageView.as_view(), name='list_page'),
    path('local-news/', LocalNewsViews.as_view(), name='localnews'),
    path('xorij-news/', XorijNewsViews.as_view(), name='xorijnews'),
    path('sport-news/', SportNewsViews.as_view(), name='sportnews'),
    path('technology-news/', TechnolgyNewsViews.as_view(), name='technologynews'),
    path('<slug:slug>/update/', UpdateNewsView.as_view(), name='update_news'),
    path('<slug:slug>/delete/', DeleteNewsView.as_view(), name='delete_news'),
    path('<slug:slug>/', DetailPageView, name='detail_page'),
]