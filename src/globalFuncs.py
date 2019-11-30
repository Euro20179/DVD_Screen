import sys
import pygame
import wikipedia
import webbrowser
import random
import bs4 as bs
import requests
import pandas as pd
import tkinter as tk
from tkinter import messagebox
from DVD_Screen import Menu

def randDisMov():
    try:
        avoid = {"Animation", "Disney", "Studios", "Nationsal Geographic", "ESPN", "Fox", "Productions", "Pictures", "Digital", "ABC", "Films", "shorts", "series", "films", "Ltd", "Robert Simonds", "BAM"}
        disMoves = {x for x in wikipedia.WikipediaPage("List_of_Walt_Disney_Pictures_films").links if not set(x.split(" ")) & avoid}
        webbrowser.open(f"https://en.wikipedia.org/wiki/{random.choice(list(disMoves))}")
    except:
        root = tk.Tk(); root.withdraw()
        messagebox.showinfo("ERROR", "ERROR")

def randPixMov():
    try:
        page = requests.get("https://en.wikipedia.org/wiki/List_of_Pixar_films").text

        soup = bs.BeautifulSoup(page, "html.parser")
        table = soup.find('table').tbody
        rows = table.find_all('tr')

        columns = [x for x in rows[0].find('th')]
    
        df = pd.DataFrame(columns=columns)
        movies = []
        for i in range(0, len(rows)):
            if len(tds := rows[i].find_all("a")) >= 1:
                if "]" not in tds[0].text: movies.append(tds[0].text)

        webbrowser.open(f'https://en.wikipedia.org/wiki/{random.choice(movies)}')
    except:
        root = tk.Tk(); root.withdraw()
        messagebox.showinfo("ERROR", "ERROR")