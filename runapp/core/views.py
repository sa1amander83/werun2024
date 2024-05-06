from django.shortcuts import render


# Create your views here.
from rest_framework.decorators import api_view
from rest_framework.response import Response

from core.models import Runner
from core.serializers import RunnerSerializer


def index(request):
    return render(request, 'core/base.html')


from rest_framework import generics, viewsets, status


@api_view(['GET', 'POST'])
def runners_list(request):
    if request.method == 'GET':
        data = Runner.objects.all()

        serializer = RunnerSerializer(data, context={'request': request}, many=True)

        return Response(serializer.data)

    elif request.method == 'POST':
        serializer = RunnerSerializer.Serializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(status=status.HTTP_201_CREATED)

        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


@api_view(['PUT', 'DELETE'])
def runners_detail(request, pk):
    try:
        runner = Runner.objects.get(id=pk)
    except Runner.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)

    if request.method == 'PUT':
        serializer = RunnerSerializer(runner, data=request.data,context={'request': request})
        if serializer.is_valid():
            serializer.save()
            return Response(status=status.HTTP_204_NO_CONTENT)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    elif request.method == 'DELETE':
        runner.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)

#
# class RunnersListCreate(generics.ListCreateAPIView):
#     queryset = Runner.objects.all()
#     serializer_class = RunnerSerializer
#
#
# class RunnersListSet(viewsets.ModelViewSet):
#     queryset = Runner.objects.all()
#     serializer_class = RunnerSerializer

