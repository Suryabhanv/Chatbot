from django.shortcuts import render

# Create your views here.

from django.shortcuts import render, redirect
from .forms import PDFUploadForm
from .models import PDFFile
from django.http import JsonResponse
import openai

# Configure OpenAI
openai.api_key = 'your_openai_api_key'

def upload_pdf(request):
    if request.method == 'POST':
        form = PDFUploadForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('chat')
    else:
        form = PDFUploadForm()
    return render(request, 'upload.html', {'form': form})

def chat_with_pdf(request):
    if request.method == 'POST':
        query = request.POST.get('query')
        # For demonstration, assume the PDF content is loaded and indexed
        response = openai.Completion.create(
            model="text-davinci-003",
            prompt=f"Answer the following question based on the uploaded PDF: {query}",
            max_tokens=150
        )
        answer = response.choices[0].text.strip()
        return JsonResponse({'answer': answer})
    return render(request, 'chat.html')
