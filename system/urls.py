"""system URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.1/topics/http/urls/
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
from django.conf.urls import url
from django.contrib import admin
from django.conf.urls.static import static
from django.conf import settings
from django.contrib.staticfiles.urls import staticfiles_urlpatterns


from system.views import HomeView, NirvanaHeart, NirvanaMan, NirvanaSmells, GreenAmerican, GreenDreams, GreenWake, \
    ParkDone, ParkEnd, ParkNumb, AcBlack, AcHell, AcThunder, GraceMachine, GracePain, GraceRace, StudentsView, \
    GroupView, GroupsView, CreateGroupView, StudentView, AuthorsView, SongsView, SongView

urlpatterns = [
    url(r'^$', HomeView.as_view(), name="home"),

    url(r'^1.1.html$', NirvanaSmells.as_view(), name="smells"),
    url(r'^1.2.html$', NirvanaHeart.as_view(), name="heart"),
    url(r'^1.3.html$', NirvanaMan.as_view(), name="man"),

    url(r'^2.1.html$', GreenAmerican.as_view(), name="american"),
    url(r'^2.2.html$', GreenDreams.as_view(), name="dreams"),
    url(r'^2.3.html$', GreenWake.as_view(), name="wake"),

    url(r'^3.1.html$', ParkNumb.as_view(), name="numb"),
    url(r'^3.2.html$', ParkEnd.as_view(), name="end"),
    url(r'^3.3.html$', ParkDone.as_view(), name="done"),

    url(r'^4.1.html$', AcBlack.as_view(), name="black"),
    url(r'^4.2.html$', AcHell.as_view(), name="hell"),
    url(r'^4.3.html$', AcThunder.as_view(), name="thunder"),

    url(r'^5.1.html$', GracePain.as_view(), name="pain"),
    url(r'^5.2.html$', GraceMachine.as_view(), name="machine"),
    url(r'^5.3.html$', GraceRace.as_view(), name="race"),

    url(r'^songs/$', SongsView.as_view(), name="songs"),
    url(r'^song/(?P<id>\d+)/$', SongView.as_view(), name="song"),

    url(r'^students/$', StudentsView.as_view(), name="Student"),
    url(r'^students/(?P<id>\d+)/$', StudentView.as_view(), name="Students"),
    url(r'^group/(?P<group_id>\d+)/$', GroupView.as_view(), name="group"),
    url(r'^groups/$', GroupsView.as_view(), name="groups"),
    url(r'^groups/new/$', CreateGroupView.as_view(), name="new_group"),
    url(r'^authors/$', AuthorsView.as_view(), name="authors"),

    url(r'admin/', admin.site.urls),
] + static(settings.STATIC_URL, document_root=settings.STATICFILES_DIRS)

