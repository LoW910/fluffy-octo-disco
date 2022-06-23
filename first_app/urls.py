from django.urls import path
from . import views
urlpatterns = [
    path("<topic>/", views.news_view ,name="news_view"),
    path("<int:num1>/<int:num2>/", views.add_view, name="add_view")

]
