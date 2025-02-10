from django.shortcuts import render, redirect
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from django.core.validators import URLValidator
from django.core.exceptions import ValidationError
from django.db import models
import hashlib
import json
from django.views.decorators.csrf import csrf_exempt
from django.views.decorators.http import require_POST
from .models import URLMapping


# Create your views here.
def index(request):
    return render(request, 'urlshortnerapp/index.html')


def generate_short_code(url):
    return hashlib.md5(url.encode()).hexdigest()[:6]


@csrf_exempt
@require_POST
def shorten_url(request):
    print("%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%")
    if request.method == 'POST':
        try:
            data = json.loads(request.body)
            long_url = data.get('long_url')

            validator = URLValidator()
            validator(long_url)

            short_code = generate_short_code(long_url)
            obj, created = URLMapping.objects.get_or_create(long_url=long_url, defaults={'short_code': short_code})
            return JsonResponse({'short_url': f'http://short.ner/{obj.short_code}'})
        except ValidationError:
            return JsonResponse({'error': 'Invalid URL. Must start with http:// or https://'}, status=400)
        except Exception as e:
            return JsonResponse({'error': str(e)}, status=500)

    return JsonResponse({'error': 'Invalid request method'}, status=405)


def redirect_url(request, short_code):
    try:
        mapping = URLMapping.objects.get(short_code=short_code)
        return redirect(mapping.long_url)
    except URLMapping.DoesNotExist:
        return JsonResponse({'error': 'Short URL not found'}, status=404)
