from django.shortcuts import render, redirect
from django.views import View
from app.forms import *
from app.models import Document
from app.models import Resume
from django.http import HttpResponseRedirect
from django.shortcuts import render


# Imaginary function to handle an uploaded file.



def start(request):
    return render(request,'start.html')
def Dashboard(request):
    return render(request,'Dashboard.html')



class HomeView(View):
    def get(self, request):
        form = ResumeForm()
        candidates = Resume.objects.all()
        return render(request, 'hello.html', {'candidates': candidates, 'form': form})

    def post(self, request):
        form = ResumeForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('resume')  # Redirect to the same page after form submission
        else:
            # If form is not valid, render the form again with errors
            candidates = Resume.objects.all()
            return render(request, 'hello.html', {'candidates': candidates, 'form': form})

class CandidateView(View):
    def get(self, request, pk):
        candidate = Resume.objects.get(pk=pk)
        return render(request, 'candidate.html', {'candidate': candidate})
    

from django.shortcuts import render, redirect
from app.forms import DocumentForm

def upload_document(request):
    if request.method == 'POST':
        form = DocumentForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('uploaded_documents')
    else:
        form = DocumentForm()
    return render(request, 'upload_document.html', {'form': form})

def uploaded_documents(request):
    documents = Document.objects.all()
    return render(request, 'uploaded_documents.html', {'documents': documents})

