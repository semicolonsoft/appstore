
from rest_framework.views import exception_handler
from rest_framework.exceptions import APIException
from django.core.exceptions import ObjectDoesNotExist, FieldError
from django.core.paginator import InvalidPage
from rest_framework.response import Response




def exception_handlers(exc, context):

    if isinstance(exc, APIException):
        response = exception_handler(exc, context)
        if response.status_code == 401:
            return Response({'status':'failed', 'message':'not authorized', 'data':{}}, status=401)
        return Response({'status':'failed', 'message':response.data, 'data':{}}, status=response.status_code)

    elif isinstance(exc, ObjectDoesNotExist):
        return Response({'status':'failed', 'message':str(exc), 'data':{}}, status=472)

    elif isinstance(exc, InvalidPage):
        return Response({'status':'success', 'message':'', 'data':[]})

    elif isinstance(exc, FieldError):
        return Response({'status':'failed', 'message':f'field_error', 'data':{}}, status=422)

    elif isinstance(exc, KeyError):
        return Response({'status':'failed', 'message':f'key_error {exc.args[0]}', 'data':{}}, status=422)

    elif isinstance(exc, ValueError):
        return Response({'status':'failed', 'message':f'value error', 'data':{}}, status=422)
        
    elif isinstance(exc, AttributeError):
        return Response({'status':'failed', 'message':f'attribute error', 'data':{}}, status=422)
        
    elif isinstance(exc, IndexError):
        return Response({'status':'failed', 'message':f'index error', 'data':{}}, status=422)
