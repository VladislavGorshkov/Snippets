from django.urls import path
from django.conf.urls.static import static
from django.conf import settings
from MainApp import views

urlpatterns = [
    path('', views.index_page, name='home'),
    path('snippets/add', views.add_snippet_page, name='add_snippet'),
    path('snippets/list', views.snippets_page, name='snippets_page'),
    path('snippets/<int:snippet_id>', views.snippet_detail, name='snippet_detail'),
   # path('snippets/create', views.create_snippet, name='create_snippet'),
   path('snippets/<int:snippet_id>/delete', views.del_snippet_page, name='snippet_delete'),
   path('snippets/<int:snippet_id>/edit', views.edit_snippet_page, name='snippet_edit'),
   path('login', views.login, name='login'),
   path('logout', views.logout, name='logout'),
] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
