from django.http import JsonResponse

# Create your views here.
def home(request):
    data = {
        'message': 'Welcome to Soft84ya'
    }
    return JsonResponse(data)
