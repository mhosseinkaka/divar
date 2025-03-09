from django.urls import path
from .views import e_devices, tablet_mobile, computers, game_cosoles, video_audio, telephones

urlpatterns = [
    path('', e_devices),
    path('tablet-mobile', tablet_mobile),
    path('computers', computers),
    path('game-consols', game_cosoles),
    path('video-audio', video_audio),
    path('telephones', telephones)
]