import unittest
import base64
import subprocess
from PIL import Image
import os
import requests
from playwright.sync_api import expect, sync_playwright  # 1.37.0


class Test(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.p = sync_playwright().start()
        cls.browser = cls.p.chromium.launch()
        cls.context = cls.browser.new_context()
        cls.context.set_default_timeout(5_000)

    def setUp(self):
        self.page = Test.context.new_page()

    def tearDown(self):
        self.page.close()

    @classmethod
    def tearDownClass(cls):
        cls.context.close()
        cls.browser.close()
        cls.p.stop()

    def perform_ocr(image_path):
        return 
        
    def test_challenge_open(self):
        self.page.goto("http://challenge01.root-me.org/programmation/ch8/")
        expect(self.page.locator("form")).to_have_text("Try")

    def test_download_image(self):
        page = self.page
        page.goto("http://challenge01.root-me.org/programmation/ch8/")
        img = page.get_by_role("img")
        image_b64 = img.evaluate("""element => {
            var cnv = document.createElement('canvas');
            cnv.width = element.naturalWidth;
            cnv.height = element.naturalHeight;
            cnv.getContext('2d').drawImage(element, 0, 0, element.naturalWidth, element.naturalHeight);
            return cnv.toDataURL().substring(22)
        }""")

        folder = './img/'
        name = 'to_solve.png'
        full_path = os.path.join(folder, name)
        os.makedirs(folder, exist_ok=True)
        with open(full_path, 'wb') as f:
            f.write(base64.b64decode(image_b64))

        img = Image.open(full_path)
        img = img.convert("RGBA")
        pixdata = img.load()
        for y in range(img.size[1]):
            for x in range(img.size[0]):
                if pixdata[x, y] == (0, 0, 0, 255):
                    pixdata[x, y] = (255, 255, 255, 255)

        width, height = img.size
        new_size = width*8, height*8
        img = img.resize(new_size, Image.LANCZOS)
        img = img.convert('L')
        img = img.point(lambda x: 0 if x < 155 else 255, '1')
        img.save("./img/to_solve_filtered.png")
        command = f'tesseract ./img/to_solve_filtered.png solved 2>/dev/null  && cat solved.txt'
        result = subprocess.run(command, shell=True, capture_output=True, text=True)

        if result.returncode == 0:
            print(f"Texte : {result.stdout}")
            url = 'http://challenge01.root-me.org/programmation/ch8/'
            brr = result.stdout
            donnees = {'cametu': brr}
            print(donnees)
            request = requests.post(url, data=donnees)            
            print(request.text)
        else:
            print("Fuck, here we go again") 
        


if __name__ == "__main__":
    unittest.main(verbosity=2)