from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static
from gamedb.pointcalculations import twitch

# views imported from apps
from general import views as general_views
from users import views as user_views
from gamedb import views as game_views
#from games import views as game_views
from django.contrib.auth import views as auth_views
#from games import scraper

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', general_views.home, name="home"),
    path('team/', general_views.team, name="team"),
    path('games/', game_views.games, name="games"),
    path('waves/', general_views.waves, name="waves"),
    path('register/', user_views.register, name='register'),
    path('login/', auth_views.LoginView.as_view(template_name="users/login.html"), name="login"),
    path('logout/', auth_views.LogoutView.as_view(template_name="general/index.html"), name="logout"),
    path('profile/', user_views.profile, name="profile"),
    # path('register/', user_views.register, name='register'),
    # path('login/', auth_views.LoginView.as_view(template_name="users/login.html"), name="login"),
    path('game/<slug>',game_views.game_page.as_view(template_name="games/game_detail.html")),
    path('game_creation/', game_views.game_creation, name="game_creation"),


    #path('paypal', include('paypal.standard.ipn.urls')),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL,
                          document_root=settings.MEDIA_ROOT)
