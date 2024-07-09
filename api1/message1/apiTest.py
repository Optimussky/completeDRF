from rest_framework.decorators import api_view
from rest_framework.response import Response

@api_view(['GET'])
def MessageListApi(request):
    messages = [
        {
            'uuid': 'abc1234',
            'username': 'user1',
            'email': 'user1@mail.com',
        },
        {
            'uuid': 'abcd12345',
            'username': 'user2',
            'email': 'user2@mail.com',
        },
        {
            'uuid': 'ab12c3',
            'username': 'user1',
            'email': 'user1@mail.com',
        }

    ]

    return Response(messages)