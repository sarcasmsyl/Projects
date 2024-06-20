from pathlib import Path
import openpyxl
import requests
import shutil
import pandas as pd
from django.conf import settings

def FindandReplace(exceldoc):
  FILE_DIR = Path(settings.MEDIA_ROOT) / "FindAndReplace"
  FILE_DIR.mkdir(parents=True, exist_ok=True)

  # Save the input exceldoc to the BASE_DIR
  input_path = FILE_DIR / exceldoc.name
  with open(input_path, 'wb') as f:
      shutil.copyfileobj(exceldoc, f)

  #Add what you want to find and replace in this dictionary, left is what you are looking for, right is what you are replacing it with.
  find_and_replace = {'”' : '"', 
                      '“' : '"',
                      "─" : "─",
                      "–" : "─",
                      "—" : "─",
                      "’" : "'",
                      "‘" : "'",
                      "°" : " Degrees",
                      "™" : "",
                      "®" : "",
                      "©" : "",
                      "…" : "...",
                      "½" : "1/2",
                      "¼" : "1/4",
                      "⅛" : "1/8",
                      "  ": " "}

  files = list(FILE_DIR.rglob("*.xls*"))
  for file in files:
      wb = openpyxl.load_workbook(file)
      for ws in wb.worksheets:
          for row in ws.iter_rows():
              for cell in row:
                  if cell.value in find_and_replace.keys():
                      cell.value = find_and_replace.get(cell.value)
      wb.save(FILE_DIR / f"{file.stem}_Cleaned.xlsx")


def ImageTool(file_path):
    IMAGES_DIR = Path(settings.MEDIA_ROOT) / "Images"
    IMAGES_DIR.mkdir(parents=True, exist_ok=True)

    # Load the file into a DataFrame
    if file_path.suffix in ['.xls', '.xlsx']:
        df = pd.read_excel(file_path)
    elif file_path.suffix == '.csv':
        df = pd.read_csv(file_path)
    else:
        raise ValueError("Unsupported file type")

    # Check if the required columns exist
    if 'SKU' not in df.columns or 'Images' not in df.columns:
        raise ValueError("The file must contain 'SKU' and 'Images' columns")

    notificationlist = []

    for index, row in df.iterrows():
        sku = row['SKU']
        image_url = row['Images']
        try:
            response = requests.head(image_url)
            if response.headers.get('content-type') == 'image/jpeg':
                notificationlist.append(f'Row {index+1} with SKU {sku} is an Image')
                img_data = requests.get(image_url).content
                img_path = IMAGES_DIR / f'{sku}_Row{index+1}.jpg'
                with open(img_path, 'wb') as handler:
                    handler.write(img_data)
            else:
                notificationlist.append(f'Row {index+1} with SKU {sku} is not an Image')
        except requests.RequestException:
            notificationlist.append(f'Row {index+1} with SKU {sku} is not an Image')

    # Save the notification list to a text file
    notifications_path = IMAGES_DIR / 'notifications.txt'
    with open(notifications_path, 'w') as f:
        for notification in notificationlist:
            f.write(f"{notification}\n")

    return IMAGES_DIR, notifications_path

def zip_directory(directory_path):
    zip_path = Path(f"{directory_path}.zip")
    shutil.make_archive(str(directory_path), 'zip', root_dir=directory_path)
    return zip_path