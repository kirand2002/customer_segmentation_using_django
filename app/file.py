from django.core.files.storage import default_storage
import pandas as pd
from io import StringIO

def file_upload(request):
    if request.method == 'POST':
        uploaded_file = request.FILES['file']
        file_path = default_storage.save(uploaded_file.name, uploaded_file)
        df = pd.read_csv(uploaded_file)
        jsonDf = df.to_json()
        return render(request, 'file.html', {'jsonDf': jsonDf})
    return render(request, 'file_upload.html')