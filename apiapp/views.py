from .serializers import apiserializer
from rest_framework.decorators import api_view
from rest_framework.response import Response
from .models import apimodel


# Create your views here.
@api_view(['GET'])
def home(request):
    app = apimodel.objects.all()
    serialize = apiserializer(app, many=True)
    return Response(serialize.data)


@api_view(['PUT'])
def new(request, pk):
    app = apimodel.objects.get(pk=pk)
    serialize = apiserializer(instance=app, data=request.data)
    if serialize.is_valid():
        serialize.save()

    return Response(serialize.data)
