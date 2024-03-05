from pathlib import Path
import openpyxl

BASE_DIR = Path(__file__).parent
INPUT_DIR = BASE_DIR / "Files"
OUTPUT_DIR = BASE_DIR / "Output"

OUTPUT_DIR.mkdir(parents=True, exist_ok=True)

find_and_replace = {'special double quote' : '"', 'special single quote': "'", "°" : " Degrees", "™" : "", "®" : "", "©" : "", "pie" : "applie_pie"}

files = list(INPUT_DIR.rglob("*.xls*"))
for file in files:
    wb = openpyxl.load_workbook(file)
    for ws in wb.worksheets:
        for row in ws.iter_rows():
            for cell in row:
                if cell.value in find_and_replace.keys():
                    cell.value = find_and_replace.get(cell.value)
    wb.save(OUTPUT_DIR / f"{file.stem}_Cleaned.xlsx")
