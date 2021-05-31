import pytesseract
from PIL import Image
import pandas as pd

t_filepath = str(input("What is the filepath to your tesseract installation?"))
s_filepath = str(input("What is the filepath to your screenshots?"))

# direct pytesseract to your command path
pytesseract.pytesseract.tesseract_cmd = t_filepath
# create the excel writer
writer = pd.ExcelWriter('demog_tables.xlsx', engine='xlsxwriter')

# anticipating up to 4 tables so 4 screenshots
for i in range(1,5):
    try:
        filename = "\Screenshot_" + str(i) + ".png" # name of screenshots, numbered sequentially
        tex = pytesseract.image_to_string(Image.open(s_filepath + filename), config="digits") # opening from saved location
        df = pd.DataFrame([tex.split(' ') for tex in tex.split('\n')]).dropna()
        df.to_excel(writer, sheet_name='Sheet_' + str(i), index=False)
        print("Table " + str(i) + " done")
    except: 
        print("No more screenshots found")

writer.save()
print("Images Converted")