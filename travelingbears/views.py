from django.http import JsonResponse
from django.shortcuts import render, redirect
from travelingbears.models import User
from .forms import SignupForm
from .forms import LoginForm
from django.contrib.auth import authenticate, login


def login_view(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect('homePage.html')  # Replace 'home' with the appropriate URL pattern name for the home page
        else:
            error_message = "Invalid username or password. Please try again."
            return render(request, 'login.html', {'error_message': error_message})
    else:
        return render(request, 'login.html')

def signup_view(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        email = request.POST.get('email')
        password = request.POST.get('password')
        User.objects.create_user(username=username, email=email, password=password)
        return redirect('login.html')
    else:
        return render(request, 'signup.html')
    
def redirect_to_login(request):
    return redirect('login.html')   


def process_message(request):
    if request.method == 'POST':
        message = request.POST.get('message')

        if message:
            # Process the message
            print('Message:', message)

            # Return a JSON response indicating success
            return JsonResponse({'success': True})
        else:
            # Return a JSON response indicating a validation error
            return JsonResponse({'error': 'Invalid message'})
    else:
        # Handle non-POST requests
        return JsonResponse({'error': 'Invalid request method'})


def submit_feedback(request):
    if request.method == 'POST':
        name = request.POST.get('name')
        email = request.POST.get('email')
        message = request.POST.get('message')


        return JsonResponse({'success': True})  # Return a JSON response indicating success
    else:
        return JsonResponse({'success': False})  # Return a JSON response indicating failure



def api_matched_pairs(request):
    # fetch the matched pairs from the database
    matched_pairs = [
        {'user1Name': 'User 1', 'user2Name': 'User 2', 'userId': 1},
        {'user1Name': 'User 3', 'user2Name': 'User 4', 'userId': 2},
        
    ]

    return JsonResponse(matched_pairs, safe=False)