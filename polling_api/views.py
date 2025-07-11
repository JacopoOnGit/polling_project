from django.shortcuts import render
from django.http import JsonResponse
from django.core.management import call_command

def homepage(request):
    return render(request, "client.html")

def force_migrate(request):
    try:
        call_command("migrate")
        return JsonResponse({"status": "success", "message": "Migrazioni completate"})
    except Exception as e:
        return JsonResponse({"status": "error", "message": str(e)})

