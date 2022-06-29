from django.urls import path
from .views import ViewAndCreate, Update, DeleteForAdmin, DeleteForUser


# /api/v1/image/
urlpatterns = [
    path('image/', ViewAndCreate.as_view()),
    path('image/<int:pk>/', Update.as_view()),
    path('image/delete_all/', DeleteForAdmin.as_view()),
    path('image/delete/<int:pk>/', DeleteForUser.as_view()),
]

