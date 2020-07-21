from django.shortcuts import render
from culture_content.models import *
from culture_content.views import get_scenario_results
from .models import Course
from django.contrib.auth.decorators import login_required
from .forms import SignUpForm
from django.shortcuts import render
import random
import string
from django.contrib.auth.hashers import make_password
from django.http import HttpResponse


def request_user(request):
    letters = string.ascii_lowercase
    passw = ''.join(random.choice(letters) for i in range(10))
    if (request.method == 'POST') and request.user.is_anonymous==True:
        form = SignUpForm(request.POST)
        if form.is_valid():
            try:
                email = form.cleaned_data['email']
                data = form.save(commit=False)
                data.username = email
                data.password = make_password(passw)
                data.save()
                return render(request, 'course/details.html', {'user': email, 'passw': passw})
            except:
                HttpResponse('The email is currently in use. Please provide another email address.')
    else:
        form = SignUpForm()
    return render(request, 'course/signup.html', {'form': form})


@login_required
def get_user_data(request):
    user_profile = Profile.objects.get(user=request.user)
    if user_profile.type=='I':
        courses = Course.objects.filter(instructor=request.user)
        return render(request, 'course/instructor.html', {'courses': courses, 'user_language':user_profile.language})
    elif user_profile.type=='S':
        user_scenarios = Response.objects.filter(user=request.user).values('answer__task__scenario')
        scenarios =set([scenario['answer__task__scenario'] for scenario in user_scenarios])
        statistics=[]
        for scene in scenarios:
            if scene is not None:
                options_stats, scenario_stats = get_scenario_results(scene)
                scenario = Scenario.objects.get(id=scene)
                statistics.append([scenario, scenario_stats])

        return render(request, 'course/student.html', {'results': statistics, 'user_language':user_profile.language})





