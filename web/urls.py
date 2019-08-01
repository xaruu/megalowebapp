from django.urls import path
from .views import HomeView, EpisodioDetailView, link_discover

urlpatterns= [
	path('', HomeView.as_view(), name="home"),
	path('<slug>/', EpisodioDetailView.as_view()),
	path('link/<int:index>', link_discover)
]