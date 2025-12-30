import json
from django.shortcuts import render
from django.http import JsonResponse
from .models import HealthReading
from django.views.decorators.csrf import csrf_exempt

# Create your views here.
@csrf_exempt
def receive_vitals(request):
    if request.method == "POST":
        try:
            # Parse JSON data from request body
            data = json.loades(request.body)

            hr_val = data.get("heart_rate")
            spo2_val = data.get("sp02")
            temp_val = data.get("temperature", 0) 

            print(f"Received data --> {hr_val}, SPO2 :{spo2_val}")

            # save to database
            reading = HealthReading.objects.create(
                heart_rate = hr_val,
                sp02 = spo2_val,
                temperature = temp_val
            )
            return JsonResponse({"status": "success", "id": reading.id}, status=201)
        except Exception as e:
            print(f"Error: {e}")
            return JsonResponse({"status": "error", "message": str(e)}, status=400)
        
    return JsonResponse({"status": "failed"}, status=405)
