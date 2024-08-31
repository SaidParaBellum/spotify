from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.views import LoginView
from django.core.exceptions import PermissionDenied
from django.shortcuts import render, redirect
from django.urls import reverse_lazy
from django.views.generic import CreateView, TemplateView, DetailView, FormView, ListView, UpdateView, View

from sporify.forms import RegistrationForm, ApplicationForm
from sporify.models import User, Song, Musician, Playlist, Application


# Create your views here.



class UserLoginView(LoginView):
    template_name = 'auth/login.html'

    def get_success_url(self):
        if self.request.user.role is not None:
            if self.request.user.role == 'Admin':
                return reverse_lazy('admin_view')
            else:
                return reverse_lazy('index')
        else:
            return reverse_lazy('index')

class RegisterView(CreateView):
    template_name = 'auth/register.html'
    form_class = RegistrationForm

    def get_success_url(self):
        return reverse_lazy('index')



class IndexView(TemplateView):
    template_name = 'spotify/index.html'



class ProfileView(LoginRequiredMixin, TemplateView):
    template_name = 'spotify/profile.html'
    model = User
    context_object_name = 'user'
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['user'] = self.request.user
        return context


class SongsView(TemplateView):
    template_name = 'spotify/songs.html'
    model = Song
    context_object_name ='songs'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['songs'] = Song.objects.all()
        return context


class ArtistsView(TemplateView):
    template_name = 'spotify/artists.html'
    model = Musician
    context_object_name = 'artists'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        artists = Musician.objects.all()
        context['artists'] = artists
        artist_songs = [
            {'artist': artist, 'songs': Song.objects.filter(musician=artist)}
            for artist in artists
        ]
        context['artist_songs'] = artist_songs
        return context


class PlaylistView(TemplateView):
    template_name = 'spotify/playlist.html'
    model = Playlist
    context_object_name = 'playlists'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['playlists'] = Playlist.objects.all()
        return context

class PlaylistDetailView(DetailView):
    model = Playlist
    template_name = 'spotify/playlist_detail.html'
    context_object_name = 'playlist'


# Apllication Views

class SubmitApplicationView(FormView):
    template_name = 'spotify/submit_application.html'
    form_class = ApplicationForm
    success_url = reverse_lazy('index')

    def form_valid(self, form):
        application = form.save(commit=False)
        application.user = self.request.user
        application.save()
        return super().form_valid(form)

class ApplicationListView(ListView):
    model = Application
    template_name = 'application_list.html'

    def get_queryset(self):
        if self.request.user.role == 'admin':
            return Application.objects.all()
        return Application.objects.filter(user=self.request.user)


class ApplicationUpdateView(UpdateView):
    model = Application
    fields = ['status']
    template_name = 'application_update.html'
    success_url = reverse_lazy('application_list')

    def get_object(self, queryset=None):
        application = super().get_object(queryset)
        if self.request.user.role != 'admin':
            return 'You are not authorized to access this page.'
        return application

class AdminView(ListView):
    model = Application
    template_name = 'spotify/admin_view.html'
    context_object_name = 'applications'
    paginate_by = 10

    def test_func(self):
        return self.request.user.is_superuser

class UpdateApplicationStatus(View):
    def post(self, request, pk):
        application = Application.objects.get(pk=pk)
        action = request.POST.get('action')
        if action == 'approve':
            application.approved = True
            application.rejected = False
        elif action == 'reject':
            application.approved = False
            application.rejected = True
        application.save()
        return redirect('admin_view')