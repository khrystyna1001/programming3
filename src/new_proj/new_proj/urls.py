"""
URL configuration for new_proj project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""

from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from notes.views import user_page, home_page, add_text_block, update_block, notes_page, note_page, delete_block

urlpatterns = [
    path("", home_page, name='home'),
    path("profile/", user_page, name='profile'),

    path("notes/", notes_page, name='notes_page'),
    path("notes/<int:note_id>/", note_page, name='note_detail'),
    path('notes/<int:note_id>/add_text_block/', add_text_block, name='add_text_block'),
    # path('notes/<int:note_id>/get_blocks/', get_note_blocks, name='get_note_blocks'),

    path('block/<int:block_id>/update/', update_block, name='update_block'),
    path('block/<int:block_id>/delete/', delete_block, name='delete_block'),

    path("admin/", admin.site.urls),
    path("", include("django.contrib.auth.urls"))
]

if settings.DEBUG and settings.INSTALLED_APPS:
    from debug_toolbar.toolbar import debug_toolbar_urls

    urlpatterns = [
        *urlpatterns,
    ] + debug_toolbar_urls()
    
