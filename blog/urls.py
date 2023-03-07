from django.urls import path
from blog.views import index, student_delete, student_edit


urlpatterns= [
    path('', index, name="home"),
    path('<int:id>/delete', student_delete, name='student_delete'),
    path('<int:id>/edit', student_edit, name='student_edit'),
]