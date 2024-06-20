from django.shortcuts import render
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from django.core.files.storage import default_storage
from django.core.files.base import ContentFile
from pathlib import Path
from django.conf import settings
from .tools_test import FindandReplace, ImageTool, zip_directory  # Import your functions

@csrf_exempt
def tools(request):
    if request.method == 'POST':
        if 'filename' in request.FILES:
            uploaded_file = request.FILES['filename']
            file_path = default_storage.save(uploaded_file.name, ContentFile(uploaded_file.read()))
            file_path = Path(default_storage.path(file_path))

            if 'findAndReplaceForm' in request.POST:
                cleaned_path = FindandReplace(uploaded_file)
                return JsonResponse({
                    'message': 'File processed with FindAndReplace',
                    'file_url': request.build_absolute_uri(f'{settings.MEDIA_URL}/FindAndReplace/{cleaned_path.name}')
                })

            elif 'imageCheckForm' in request.POST:
                images_dir, notifications_path = ImageTool(file_path)
                zip_path = zip_directory(images_dir)
                return JsonResponse({
                    'message': 'File processed with ImageTool',
                    'zip_url': request.build_absolute_uri(f'{settings.MEDIA_URL}{zip_path.name}')
                })

        return JsonResponse({'error': 'No file uploaded'}, status=400)
    
    # Render the HTML page for GET requests
    return render(request, 'tools_test.html')