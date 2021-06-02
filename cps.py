import pygame
import json
import os, sys

pygame.init()

main_path = os.getcwd()

screen = pygame.display.set_mode((200, 200))

font = pygame.font.SysFont("Arial", 45)
best_font = pygame.font.SysFont("Arial", 27)
best_font_ever = pygame.font.SysFont("Arial", 20)

with open (os.path.join(os.path.dirname(sys.argv[0]), "est_score.json"), "r") as f:
        data = json.load(f)
        dico = data

bg = pygame.image.load(open(os.path.join(os.path.dirname(__file__), "gb.png")))
print("attention!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!")
print("relancez l'app pour voir votre nouveau score affiché! ;)")

def revrite(number):

    dico["best_score"] = number

    with open (os.path.join(os.path.dirname(sys.argv[0]), "est_score.json"), "w") as fi:
        json.dump(dico, fi, indent = 4, ensure_ascii=False, sort_keys=False)

best_score_ever = data["best_score"]
click_nbr = 0
finalcps = 0
cps = 0

bestScore = 0

time = 0
seconds = 0

running = True

while running:

    screen.blit(bg, (0, 0))

    score_text = font.render(f"score : {finalcps}",1,(255,0,0))
    higher_score_text = best_font.render(f"meilleur score : {bestScore}",1,(255,0,0))
    best_score_text = best_font_ever.render(f"meilleur score ever : {best_score_ever}",1,(255,0,0))
    screen.blit(score_text,(10,0))
    screen.blit(higher_score_text, (10, 80))
    screen.blit(best_score_text, (10, 150))

    clock = pygame.time.Clock()

    if bestScore > best_score_ever:
        revrite(bestScore)

    time += 0.03125

    if time >= 1:
        seconds += 1
        time = 0

        if click_nbr > bestScore:
            bestScore = click_nbr
            if bestScore > best_score_ever:
                revrite(bestScore)

        finalcps = click_nbr
        click_nbr = 0

    clock.tick(32)

    for event in pygame.event.get():
        if event.type == pygame.MOUSEBUTTONDOWN:
            click_nbr += 1
        elif event.type == pygame.QUIT:
            running = False
    
    pygame.display.flip()

pygame.quit