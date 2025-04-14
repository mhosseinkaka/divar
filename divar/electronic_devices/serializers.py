from rest_framework.serializers import ModelSerializer
from electronic_devices.models import E_device, Tablet, Mobile, Computers, Game_console, Video_audio

class E_deviceSerializer(ModelSerializer):
    class Meta:
        model = E_device
        fields = '__all__'

class TabletSerializer(ModelSerializer):
    class Meta:
        model = Tablet
        fields = '__all__'

class MobileSerializer(ModelSerializer):
    class Meta:
        model = Mobile
        fields = '__all__'

class ComputersSerializer(ModelSerializer):
    class Meta:
        model = Computers
        fields = '__all__'

class Game_consoleSerializer(ModelSerializer):
    class Meta:
        model = Game_console
        fields = '__all__'

class VideoAudioSerializer(ModelSerializer):
    class Meta:
        model = Video_audio
        fields = '__all__'