# to import response from api
from rest_framework.response import Response
# to make (get,post,delete,put) methods
from rest_framework.decorators import api_view
#  to import data base from models and serializer
from .serializer import *
from .models import *  
from rest_framework.status import *


@api_view(['GET'])
def traineeList(req,id=None):
    if (id is not None):
        data = Trainee.objects.get(id=id)
    else:
        data = Trainee.objects.all()

    if (data):
        if (id is not None):
            data_ser = TraineeSerializer(data)
            return Response(status=HTTP_200_OK,data={'data':data_ser.data})
        else:
            data_ser = TraineeSerializer(data,many=True)
        return Response(status=HTTP_207_MULTI_STATUS,data={'data':data_ser.data})
    else:
        return Response(status=HTTP_404_NOT_FOUND)
    
@api_view(['POST'])
def traineeAdd(req):
    item = TraineeSerializer(data=req.data)
    print(req.data)
    ''' item is vaalid used to check if data is send with keys or format not in TraineeSerializer
    he will not be able to convert it ''' 
    if (item.is_valid()):
        item.save()
    return Response(status=HTTP_200_OK)

@api_view(['PUT'])
def traineeUpdate(req,id):
        # check if id is found or not 
        if(len(Trainee.objects.filter(id=id))!= 0):
            # if id is found get data of this id 
            get_data = Trainee.objects.get(id=id)
            ''' then change it by serializer ----> we here used serialzier because of get_data is query set 
            and req.data is object '''
            update_data_ser = TraineeSerializer(instance=get_data,data=req.data)
            # then check updated data is valid
            if (update_data_ser.is_valid()):
                # if data is valid save it 
                update_data_ser.save()
                return Response(status=HTTP_200_OK,data=update_data_ser.data)
        else:
            return Response(status=HTTP_400_BAD_REQUEST,data={'message':'id not found'})



@api_view(['delete'])
def traineeDelete(req,id):
    data = Trainee.objects.get(id=id)
    if (data is not None):
        data.delete()
        return Response(status=HTTP_200_OK)
    else:
        return Response(status=HTTP_404_NOT_FOUND)




