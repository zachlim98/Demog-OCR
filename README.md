# Demography Table Converter
 A little tool to convert screenshots from pesky demography papers.

### Installation:

Use requirements.txt in order to install all the necessary dependencies. You also need to have tesseract installed which you can find [here](https://digi.bib.uni-mannheim.de/tesseract/tesseract-ocr-setup-3.05.02-20180621.exe). Install the program and then add it to your PATH variable. You can find out how to do it [here](https://medium.com/quantrium-tech/installing-and-using-tesseract-4-on-windows-10-4f7930313f82). Once that's done, you're ready to use this. 

### Usage:

All you need to do is run the file:

```
python app.py
```

It will then ask for the filepath to your tesseract installation. For example `C:\Program Files (x86)\Tesseract-OCR\tesseract.exe` is where my tesseract installation is. 

It will then ask for the filepath to your screenshots. You can have up to 4 screenshots. My screenshots, for instance, are stored at `C:\Users\Username\Desktop`

Your screenshots HAVE to be named **Screenshot_x.png** with x being any digit from 1 to 4. It will then begin to convert your screenshots and you should have an excel file with all the screenshots being in separate sheets. 

### Tips:

For your screenshots, try to screenshot JUST the data, without the headers of the tables. You can always add in the headers later. 

