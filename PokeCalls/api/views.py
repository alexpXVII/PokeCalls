import json
from django.http import JsonResponse, HttpResponseBadRequest
from django.views.decorators.csrf import csrf_exempt
from logic.game import GAME_INSTANCE

@csrf_exempt # Use csrf_exempt for simplicity, but use proper CSRF for production
def guess_pokemon(request):
    if request.method != 'POST':
        return HttpResponseBadRequest("Only POST method is allowed.")

    try:
        data = json.loads(request.body)
        pokemon_guess = data.get('guess')
        if not pokemon_guess:
            return HttpResponseBadRequest("Missing 'guess' in request body.")

        results = GAME_INSTANCE.guess_pokemon(pokemon_guess)
        if results is None:
            return JsonResponse({'error': f"Could not find Pokémon '{pokemon_guess}'"}, status=404)
        
        return JsonResponse({'results': results})

    except json.JSONDecodeError:
        return HttpResponseBadRequest("Invalid JSON.")
    except Exception as e:
        return JsonResponse({'error': str(e)}, status=500)

@csrf_exempt
def guess_move(request):
    if request.method != 'POST':
        return HttpResponseBadRequest("Only POST method is allowed.")

    try:
        data = json.loads(request.body)
        move_guess = data.get('guess')
        if not move_guess:
            return HttpResponseBadRequest("Missing 'guess' in request body.")

        results = GAME_INSTANCE.guess_move(move_guess, GAME_INSTANCE.secret_move)
        if results is None:
            return JsonResponse({'error': f"Could not find move '{move_guess}'"}, status=404)

        return JsonResponse({'results': results})

    except json.JSONDecodeError:
        return HttpResponseBadRequest("Invalid JSON.")
    except Exception as e:
        return JsonResponse({'error': str(e)}, status=500)