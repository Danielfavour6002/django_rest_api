from rest_framework import generics
from rest_framework.permissions import IsAuthenticated, AllowAny
from .models import Registration
from .serializers import RegistrationSerializer, UserProfileSerializer

class RegistrationView(generics.CreateAPIView):
    queryset = Registration.objects.all()
    serializer_class = RegistrationSerializer
    permission_classes = [AllowAny]

    
class UserProfileView(generics.RetrieveUpdateAPIView):
    queryset =  Registration.objects.all()
    serializer_class = UserProfileSerializer
    permission_classes = [IsAuthenticated]

    def get_object(self):
        return self.request.user
