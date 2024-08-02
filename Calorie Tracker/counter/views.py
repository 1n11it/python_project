from django.shortcuts import render
from django.http import JsonResponse
import requests

# Create your views here.
def home(request):
    return render(request, 'home.html')

def get_nutrition_data(food_item):
    base_url = "https://world.openfoodfacts.org/cgi/search.pl"
    params = {
        "search_terms": food_item,
        "search_simple": 1,
        "action": "process",
        "json": 1
    }
    
    response = requests.get(base_url, params=params)
    
    if response.status_code == 200:
        data = response.json()
        if data['products']:
            product = data['products'][0]
            nutriments = product.get('nutriments', {})
            
            return {
                "Serving Size": "100 grams",
                "Calories": nutriments.get('energy-kcal_100g', 0),
                "Carbohydrates": nutriments.get('carbohydrates_100g', 0),
                "Cholesterol": nutriments.get('cholesterol_100g', 0),
                "Saturated fat": nutriments.get('saturated-fat_100g', 0),
                "Total Fat": nutriments.get('fat_100g', 0),
                "Fiber Content": nutriments.get('fiber_100g', 0),
                "Potassium": nutriments.get('potassium_100g', 0),
                "Protein": nutriments.get('proteins_100g', 0),
                "Sodium": nutriments.get('sodium_100g', 0),
                "Sugar": nutriments.get('sugars_100g', 0)
            }
    return None

def nutrition_view(request):
    if request.method == 'GET':
        food_item = request.GET.get('food', '')
        if food_item:
            nutrition_data = get_nutrition_data(food_item)
            if nutrition_data:
                return JsonResponse(nutrition_data)
            else:
                return JsonResponse({"error": "Nutrition data not found"}, status=404)
        else:
            return JsonResponse({"error": "No food item specified"}, status=400)
    
    return JsonResponse({"error": "Invalid request method"}, status=405)