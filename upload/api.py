from rest_framework import generics, permissions
from rest_framework.response import Response
from rest_framework import status
from .models import Lead
from .serializers import LeadSerializer

class LeadList(generics.ListCreateAPIView, generics.RetrieveUpdateDestroyAPIView):
    model = Lead
    serializer_class = LeadSerializer
    permission_classes = {
        permissions.AllowAny
    }
    def get_queryset(self):
        return self.model.objects.all().order_by('-date_created')
    
#     def post(self, request, format=None):
#         serializer = LeadSerializer(data=request.DATA)
#         if serializer.is_valid():
#             serializer.save()
#             return Response(serializer.data, status=status.HTTP_201_CREATED)
#         return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
#       
