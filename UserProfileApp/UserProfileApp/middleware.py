import jwt
from django.http import JsonResponse
from UserProfileApp.settings import SECRET_KEY
from rest_framework import status


class CheckIPMiddleware(object):
    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request):
        x_forwarded_for = request.META.get('HTTP_X_FORWARDED_FOR')
        if x_forwarded_for:
            ip = x_forwarded_for.split(',')[0]
        else:
            ip = request.META.get('REMOTE_ADDR')
        request.ip_address = ip
        response = self.get_response(request)
        return response


class JWTAuthMiddleware(object):
    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request):
        print(request.META.get('PATH_INFO'))
        if request.META.get('PATH_INFO') == '/user/login' or '/admin/' in request.META.get('PATH_INFO'):
            response = self.get_response(request)
        else:
            token = request.META.get('HTTP_AUTHORIZATION')
            if token and token.split()[1]:
                try:
                    payload = jwt.decode(token.split()[1], key=SECRET_KEY, algorithms=['HS256'])
                    print(payload)
                    response = self.get_response(request)
                except:
                    return JsonResponse({'message': 'Invalid token!'}, status=status.HTTP_401_UNAUTHORIZED)
            else:
                return JsonResponse({'message': 'Please provide token!'}, status=status.HTTP_401_UNAUTHORIZED)

        return response
