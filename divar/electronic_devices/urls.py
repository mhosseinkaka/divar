from django.urls import path
from electronic_devices.views import *

urlpatterns = [
    path('', e_devices),
    path('tablet-mobile', tablet_mobile),
    path('computers', computers),
    path('game-consols', game_cosoles),
    path('video-audio', video_audio),
    path('telephones', telephones),
    path('edevic-lc/', EdeviceNew.as_view()),
    path('edevic-rud/<int:pk>', EdeviceNew2.as_view()),
    path('mobil-lc/', MobileNew.as_view()),
    path('mobile-rud/<int:pk>',MobileNew2.as_view()),
    path('tablet-lc/', TabletNew.as_view()),
    path('tablet-rud/<int:pk>',TabletNew2.as_view()),
    path('computer-lc/', ComputerNew.as_view()),
    path('computer-rud/<int:pk>',ComputerNew2.as_view()),
    path('game-consol-lc/', GameConsolNew.as_view()),
    path('game-consol-rud/<int:pk>',GameConsolNew.as_view()),
    path('video-audio-lc/', VideoAudioNew.as_view()),
    path('video-audio-rud/<int:pk>',VideoAudioNew2.as_view()),
]