import requests
from bs4 import BeautifulSoup
from icecream import ic
import re

def get_html(url):
    response = requests.get(url)
    if response.status_code == 200:
        soup = BeautifulSoup(response.text, 'html.parser')
        return soup
    else:
        return None

def extract_number_from_text(soup):
    if not soup:
        return "Error: Invalid BeautifulSoup object provided."
    lines = soup.get_text().split("\n")
    _, suite_first, suite_second = re.findall(r'-?\d\d?', lines[0])
    positif = True if "] + [" in lines[0] else False if "] - [" in lines[0] else None
    u0 = lines[1].replace("U0 = ", "").strip()
    replacements = [
        "You must find U",
        "You have only 2 seconds to send the result with the HTTP GET method (at ",
        "http://challenge01.root-me.org/programmation/ch1/ep1_v.php?result=...)"
    ]
    uX = lines[2]
    for old in replacements:
        uX = uX.replace(old, "").strip()
    return suite_first, suite_second, positif, u0, uX


def calcule(first, second, positive, u0, uX):
    ic(first, second, positive, u0, uX)
    n = 5
    index = 0
    while index <= 5:
        u = u*2           
        index = index + 1

if __name__ == "__main__":
    soup = get_html("http://challenge01.root-me.org/programmation/ch1/")
    if soup:
        Suite_first, Suite_second, Positif, U_zero, U_find = extract_number_from_text(soup)
        calcule(Suite_first, Suite_second, Positif, U_zero, U_find)
    else:
        print("Failed to retrieve HTML content.")
