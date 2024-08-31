from django.urls import path
from django.contrib.auth.views import LogoutView
from django.urls import path
from sporify.views import UserLoginView, RegisterView, SongsView, ArtistsView, PlaylistView, ProfileView, \
    PlaylistDetailView, SubmitApplicationView, ApplicationListView, ApplicationUpdateView, AdminView, \
    UpdateApplicationStatus
from sporify.views import IndexView

urlpatterns = [
    path('index/', IndexView.as_view(), name='index'),
    path('login/', UserLoginView.as_view(), name='login' ),
    path('logout/', LogoutView.as_view(), name='logout' ),
    path('register/', RegisterView.as_view(), name='register' ),
    path('songs/', SongsView.as_view(), name='songs' ),
    path('artists/', ArtistsView.as_view(), name='artists' ),
    path('playlist/', PlaylistView.as_view(), name='playlist' ),
    path('profile/', ProfileView.as_view(), name='profile' ),
    path('playlist/<int:pk>/', PlaylistDetailView.as_view(), name='playlist_detail'),
    path('submit/', SubmitApplicationView.as_view(), name='submit_application'),
    path('applications/', ApplicationListView.as_view(), name='application_list'),
    path('applications/<int:pk>/update/', ApplicationUpdateView.as_view(), name='application_update'),
    path('admin-view/', AdminView.as_view(), name='admin_view'),
    path('update-application-status/<int:pk>/', UpdateApplicationStatus.as_view(), name='update_application_status'),
]