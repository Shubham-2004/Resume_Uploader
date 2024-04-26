from django.shortcuts import render, redirect
from django.views import View
from app.forms import ResumeForm
from app.models import Resume

class HomeView(View):
    def get(self, request):
        form = ResumeForm()
        candidates = Resume.objects.all()
        return render(request, 'hello.html', {'candidates': candidates, 'form': form})

    def post(self, request):
        form = ResumeForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('home')  # Redirect to the same page after form submission
        else:
            # If form is not valid, render the form again with errors
            candidates = Resume.objects.all()
            return render(request, 'hello.html', {'candidates': candidates, 'form': form})

class CandidateView(View):
    def get(self, request, pk):
        candidate = Resume.objects.get(pk=pk)
        return render(request, 'candidate.html', {'candidate': candidate})
