from django.urls import path
from . import views
urlpatterns = [
    path("<int:num_page>", views.num_page_view, name="num_page_view"),
    path("<topic>/", views.news_view ,name="news_view"),
    path("<int:num1>/<int:num2>/", views.add_view, name="add_view")

]
