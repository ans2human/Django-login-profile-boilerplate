from django.urls import path
from .views import home, SignUp, profile, update_profile, insta, charts


app_name = 'core'
urlpatterns = [
    path('', home, name='home'),
    path('charts/', charts, name='charts'),
    path('signup/', SignUp.as_view(), name='signup'),
    path('profile/', profile, name='profile'),
    path('insta/', insta, name='insta'),
    path('profile/update/', update_profile, name='update_profile')

]