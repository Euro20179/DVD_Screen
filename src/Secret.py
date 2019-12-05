import pygame
import tkinter as tk
from tkinter import messagebox
from Main import mainInit
from os import listdir
import random
import time
from statistics import mean
from Dvds import DVDS

def mouseChks(event, DVDSDict):
    global gotten
    keys = pygame.key.get_pressed()
    MPos = pygame.mouse.get_pos()
    if event.button == 1:
        for DVD in DVDSDict.values():
            if MPos[0] > DVD.SX and MPos[0] < DVD.SX + DVD.SW and MPos[1] > DVD.SY and MPos[1] < DVD.SY + DVD.SH:
                if DVD.Move: gotten += 1; DVD.Move = False
                else: gotten -= 1; DVD.Move = True


def main(count, sh, sw, winWidth, winHeight):
    global gotten

    pygame.init(); pygame.mixer.init(); pygame.font.init()

    with open(r".\src\txt_files\High_Score!!.txt", "r") as File: #finds the high score from the "High_Score!!.txt" text file
        scores = File.read().split("\n")
        tuples = [x.split(" ") for x in scores]
        tuples.pop(0)
        scores = [float(x[0]) for x in tuples]
        highScore = max(scores)
        avgScore = mean(scores)

    MClicks = 0
    gotten = 0
    start = time.time()
    root = tk.Tk(); root.withdraw()
    messagebox.showinfo("YOU DESCOVERED THE SECRET", "the secret minigame!\n(press esc to go back at any time)")

    Run = True
    path = "./DVD_Logos"
    sw, sh = int(sw), int(sh)
    logos = [str(f'{path}/{x}') for x in listdir(path)]
    DVD_Logos = [pygame.image.load(x) for x in logos]

    DVDSDict = {}
    mainFont = pygame.font.SysFont("AR DESTINE", 25)

    for x in range(count): DVDSDict[x] = DVDS(winWidth, winHeight, DVD_Logos, sh, sw)

    win = pygame.display.set_mode((winWidth, winHeight), pygame.FULLSCREEN)

    pygame.display.set_caption("SECRET GAME")

    clock = pygame.time.Clock()

    timeLim = 0
    for x in range(0, len(DVDSDict)): #increases the time limit a bit for each DVD
        timeLim += random.gauss(3, .5)

    while (Run := True):
        clock.tick(120)
        
        if time.time() - start >= timeLim:
            r = tk.Tk(); r.withdraw()
            messagebox.showinfo("GAME OVER", "you ran out of time")
            pygame.display.quit()
            mainInit(winWidth, winHeight, sh, sw)
        for event in pygame.event.get():
            if event.type == pygame.QUIT: pygame.display.quit(); pygame.quit(); Run = False; break
            if event.type == pygame.MOUSEBUTTONDOWN: MClicks += 1; mouseChks(event, DVDSDict)

        for DVD in DVDSDict.values(): #checks if all are frozen
            if DVD.Move: break   
        else: #if they are, do this
            end = time.time()
            score = round(len(DVDSDict) / (end - start) * timeLim - (MClicks - len(DVDSDict)), 2)
            pygame.mixer.Sound(".\src\Sounds\Clap.wav").play()
            messagebox.showinfo("YOU WIN", f"FINAL SCORE: {score}\nClicks: {MClicks}\nDVDS: {len(DVDSDict)}\nAccuracy: {len(DVDSDict) / MClicks * 100}")
            pygame.display.quit()
            with open(r".\src\txt_files\High_Score!!.txt", "a") as File: #saves the stats from this game
                File.write(f'\n{score} {MClicks} {len(DVDSDict)}')
            mainInit(winWidth, winHeight, sh, sw)

        keys = pygame.key.get_pressed()
        if keys[pygame.K_ESCAPE]:
            pygame.display.quit()
            mainInit(winWidth, winHeight, sh, sw)

        win.fill((0, 0, 0))
        for DVD in DVDSDict.values(): 
            if DVD.Move: DVD(winWidth, winHeight, DVD_Logos)               
            win.blit(DVD.currentLogo, (DVD.SX, DVD.SY))

        score = round(len(DVDSDict) / (time.time() - start) * timeLim - (MClicks - len(DVDSDict)), 2)
        win.blit(mainFont.render(f'Gotten: {gotten}/{len(DVDSDict)}', False, (255, 255, 255)), (0, 0))
        win.blit(mainFont.render(f'Time left: {timeLim}', False, (255, 255, 255)), (0, 40))
        win.blit(mainFont.render(f'Score: {score}', False, (255, 255, 255)), (0, 60))
        win.blit(mainFont.render(f'Mouse Clicks: {MClicks}', False, (255, 255, 255)), (0, 20))
        win.blit(mainFont.render(f'High Score: {highScore}', False, (255, 255, 255)), (0, 80))
        win.blit(mainFont.render(f'Avg score: {avgScore}', False, (255, 255, 255)), (0, 100))

        pygame.display.update()