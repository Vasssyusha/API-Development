from django.urls import path
from rest_framework.urlpatterns import format_suffix_patterns
from . import views

urlpatterns = [
    path('snippets/', views.SnippetList.as_view()), # <--- Обратите внимание на .as_view()
    path('snippets/<int:pk>/', views.SnippetDetail.as_view()), # <--- И здесь тоже
]

urlpatterns = format_suffix_patterns(urlpatterns)