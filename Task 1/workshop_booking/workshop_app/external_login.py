from django.views.decorators.csrf import csrf_exempt
from django.http import JsonResponse
from django.contrib.auth import authenticate

@csrf_exempt
def external_login(request):
    if request.method == 'POST':
        import json
        data = json.loads(request.body.decode('utf-8'))
        username = data.get('username')
        password = data.get('password')
        user = authenticate(username=username, password=password)
        if user is not None:
            return JsonResponse({'success': True, 'message': 'Login successful.'})
        else:
            return JsonResponse({'success': False, 'message': 'Invalid credentials.'}, status=401)
    return JsonResponse({'success': False, 'message': 'Only POST allowed.'}, status=405)
