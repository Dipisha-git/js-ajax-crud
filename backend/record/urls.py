from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('student-list', views.api_data),
    path('add-student', views.add_student),
    path('delete-student/<id>', views.delete_student),
    path('edit-student/<id>', views.edit_student),
]
