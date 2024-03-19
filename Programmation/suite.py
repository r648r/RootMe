import requests
from bs4 import BeautifulSoup
from icecream import ic
import re

def get_html(url):
    cookies = {
        'PHPSESSID': '6d5bf2cb5ee8cac56ad6ce7b3ba1bf08',
    }

    response = requests.get(url, cookies=cookies)
    if response.status_code == 200:
        soup = BeautifulSoup(response.text, 'html.parser')
        return soup
    else:
        return None

def extract_number_from_text(soup):
    if not soup:
        return "Error: Invalid BeautifulSoup object provided."
    formula = soup.get_text().split("\n")
    print("===================================================================================")
    ic(formula[:2:])
    _, suite_first, suite_second = re.findall(r'-?\d\d?', formula[0])
    positif = True if "] + [" in formula[0] else False if "] - [" in formula[0] else None
    u0 = int(formula[1].replace("U0 = ", "").strip())
    replacements = [
        "You must find U",
        "You have only 2 seconds to send the result with the HTTP GET method (at ",
        "http://challenge01.root-me.org/programmation/ch1/ep1_v.php?result=...)"
    ]
    number_of_round = formula[2].strip()
    for old in replacements:
        number_of_round = number_of_round.replace(old, "").strip()
    return int(suite_first), int(suite_second), bool(positif), int(u0), int(number_of_round)


def calcule(first, second, positive, u0, i_final):
    print("===================================================================================")
    ic(first, second, positive, u0, i_final)
    print("===================================================================================")
    i = 0
    Un_plus_1 = u0
    while i <= i_final -1:
        if positive:
            Un_plus_1 = (first + Un_plus_1) + (i * second)
        else:
            Un_plus_1 = (first + Un_plus_1) - (i * second)
        i+=1
    print("===================================================================================")
    ic(Un_plus_1)
    print("===================================================================================")
    return Un_plus_1

if __name__ == "__main__":
    soup = get_html("http://challenge01.root-me.org/programmation/ch1/")
    if soup:
        Suite_first, Suite_second, Positif, U_zero, U_find = extract_number_from_text(soup)
        awnser = str(calcule(Suite_first, Suite_second, Positif, U_zero, U_find))
        ic(get_html(f"http://challenge01.root-me.org/programmation/ch1/ep1_v.php?result={awnser}"))
    else:
        print("Failed to retrieve HTML content.")
