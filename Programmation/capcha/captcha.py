from playwright.sync_api import sync_playwright
import pytesseract
from PIL import Image
import requests
from io import BytesIO

def download_image(image_url):
    im = Image.open("playwright.png")
    im = im.convert("P")
    print(im.histogram())




if __name__ == '__main__':
    download_image
