from rest_framework.decorators import api_view
from rest_framework.response import Response
from .models import MessageModel


# Listar
@api_view(["GET"])
def MessageListApi(request):
    messages = MessageModel.objects.all()

    messages = [{
        "id": m.id,
        "uuid": m.uuid, 
        "username": m.username, 
        "email": m.email
        } for m in messages
    ]

    # send response

    return Response(messages)


# Crear
@api_view(["POST"])
def MessageCreateApi(request):
    data = request.data

    uuid = data["uuid"]
    username = data["username"]
    email = data["email"]
    

    MessageModel(uuid=uuid, username=username, email=email).save()

    return Response({"message": "Message Created"})


# Actualizar
@api_view(["PUT"])
def MessageUpdateApi(request,id):
    data = request.data

    message = MessageModel.objects.get(id=id)

    message.uuid = data["uuid"]
    message.username = data["username"]
    message.email = data["email"]

    message.save()

    return Response({
        'message': 'Message Updated'
    })

# Borrar
@api_view(['DELETE'])
def MessageDeleteApi(request,id):
    
    message = MessageModel.objects.get(id=id)

    message.delete()

    return Response({
        'message': 'Message Deleted'
    })
