import cv2
import numpy as np
import pytesseract
from PIL import Image, ImageDraw, ImageFont
import os

# Укажите путь к tesseract.exe
pytesseract.pytesseract.tesseract_cmd = r'C:\Users\Unicum_Student.MSI\AppData\Local\Programs\Tesseract-OCR\tesseract.exe'


def extract_and_display_text(image_path, lang='rus'):

    try:
        # Проверка существования файла
        if not os.path.exists(image_path):
            raise FileNotFoundError(f"Файл {image_path} не найден!")

        img = cv2.imread(image_path)
        if img is None:
            raise ValueError("Не удалось загрузить изображение. Проверьте формат файла.")

        gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
        gray = cv2.medianBlur(gray, 3)
        gray = cv2.threshold(gray, 0, 255, cv2.THRESH_BINARY | cv2.THRESH_OTSU)[1]


        text = pytesseract.image_to_string(gray, lang=lang)


        text_img = Image.new('RGB', (img.shape[1], img.shape[0]), color=(255, 255, 255))
        draw = ImageDraw.Draw(text_img)

        try:
            font = ImageFont.truetype("arial.ttf", 20)
        except:
            font = ImageFont.load_default()

        y = 10
        for line in text.split('\n'):
            draw.text((10, y), line, font=font, fill=(0, 0, 0))
            y += 25

        text_img_cv = cv2.cvtColor(np.array(text_img), cv2.COLOR_RGB2BGR)


        result = np.hstack((img, text_img_cv))


        height, width = result.shape[:2]
        resized_result = cv2.resize(result, (width // 2, height // 2))


        cv2.imshow('Результат: Исходное изображение | Распознанный текст', resized_result)
        cv2.waitKey(0)
        cv2.destroyAllWindows()

        return text.strip()

    except Exception as e:
        print(f"Ошибка при обработке изображения: {e}")
        return None


if name == "main":
    image_path = '5208459711639316327.jpg'  # Укажите ваш путь

    print(f"Обрабатываем файл: {image_path}")
    result_text = extract_and_display_text(image_path)

    if result_text:
        print("\nРаспознанный текст:")
        print("------------------")
        print(result_text)
    else:
        print("\nНе удалось распознать текст")
