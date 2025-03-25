from rest_framework import serializers
from .models import Consumer, Barber, Service, HaircutOrder, Feedback, Leave

class ConsumerSerializer(serializers.ModelSerializer):
    class Meta:
        model = Consumer
        fields = '__all__'

class BarberSerializer(serializers.ModelSerializer):
    class Meta:
        model = Barber
        fields = '__all__'

class ServiceSerializer(serializers.ModelSerializer):
    class Meta:
        model = Service
        fields = '__all__'

class HaircutOrderSerializer(serializers.ModelSerializer):
    class Meta:
        model = HaircutOrder
        fields = '__all__'

class FeedbackSerializer(serializers.ModelSerializer):
    class Meta:
        model = Feedback
        fields = '__all__'

class LeaveSerializer(serializers.ModelSerializer):
    class Meta:
        model = Leave
        fields = '__all__'