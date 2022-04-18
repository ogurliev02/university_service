from django.urls import path

from adm.views.mentor import MarkView
from adm.views.profile import ProfileListView
from adm.views.project import ProjectListView

urlpatterns = [
    path('users/', ProfileListView.as_view()),
    path('projects/', ProjectListView.as_view()),
    path('mentor/set_mark/<int:student_id>/<int:mark>/', MarkView.as_view()),
    path('mentor/set_mark/<int:student_id>/<int:mark>/', MarkView.as_view()),
]
