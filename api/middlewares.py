from rest_framework.authtoken.models import Token

class TokenAuthenticateMiddleware:
    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request):
        # ここに処理を記述すると、view関数が実行される前に実行される
        header_text = request.META.get("HTTP_AUTHORIZATION", None)
        if header_text != None:
            token = header_text.split(" ")[1]
            request.user = Token.objects.get(key=token).user
        response = self.get_response(request)
	    # ここに処理を記述すると、view関数が実行された後に実行される
        return response
