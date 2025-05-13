# -test
Итоговый проект по информатике. 
название: scanner.
инструкция по запуску: 
1. скопировать код из файла проекта.
2. скачать необходимые библиотеки: 
по отдельности: 
pip install opencv-python ,
pip install numpy ,
pip install pytesseract,
pip install python-docx ,
pip install requests ,
сразу все: 
pip install opencv-python numpy pytesseract python-docx requests .
Tesseract OCR - должен быть установлен отдельно на вашей системе.скачать его можно на оффициальном сайте: 
https://github.com/UB-Mannheim/tesseract/wiki после установки Tesseract OCR нужно написать путь к нему, в коде проекта нужно исправить эту строчку: pytesseract.pytesseract.tesseract_cmd = r'путь к Tesseract.exe'
4. загрузить фото текстового документа ,из которого необходимо извлеч текст,в папку с проектом и написать в коде путь к фото.
необходимо исправить эту строчку image_path = 'путь к фото.jpg'
5. запустить проект. должен появится файл формата docx в папке проекта, в нем содерится весь извлеченный с картинки текст


