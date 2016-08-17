"""goto_achievement URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.10/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf.urls import url
from django.conf.urls.static import static
from django.contrib import admin

from goto_achievement import settings
from main.views import StudentView, AchievementView, index_view, AchievementListView, StudentListView

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^$', index_view, name='index'),
    url(r'^students/$', StudentListView.as_view(), name='student_list'),
    url(r'^students/(?P<pk>[0-9]+)/$', StudentView.as_view(), name='student'),
    url(r'^achievements/$', AchievementListView.as_view(), name='achievement_list'),
    url(r'^achievements/(?P<pk>[0-9]+)/$', AchievementView.as_view(), name='achievement'),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)