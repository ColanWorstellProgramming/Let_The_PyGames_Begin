import pygame
import spritesheet
from player import Player
import random

inGame = pygame.display.set_mode([1920, 1080])
fightScene = pygame.display.set_mode([1920, 1080])

random.seed(5)
rn = random.uniform(0,1)
rn2 = random.uniform(0,1)
rn3 = random.uniform(0,1)

def createWorld():
    # Sprites
    grass = pygame.image.load('sprites/Tilesets/tiles/new/grass.png').convert_alpha()
    grassSheet = spritesheet.SpriteSheet(grass)
    bg = grassSheet.get_image(16, 16, 16, 16, 120, 67.5, (0, 0, 0))

    inGame.blit(bg, (0, 0))

    #Grass - use only for slide show errors bloopers

    GrassSprite = pygame.image.load('sprites/Tilesets/tiles/new/grasshills.png').convert_alpha()
    GrassImg = spritesheet.SpriteSheet(GrassSprite)
    GrassTexture = GrassImg.get_image(16, 16, 0, 80, 4, 4, (0, 0, 0))

def createFight():
    BG = pygame.image.load('sprites/bg/backdrop.png').convert_alpha()
    inGame.blit(BG, (0, 0))

    GrassSprite = pygame.image.load('sprites/Tilesets/tiles/new/grasshills.png').convert_alpha()
    GrassImg = spritesheet.SpriteSheet(GrassSprite)
    GrassTexture = GrassImg.get_image(48, 48, 0, 0, 4, 4, (0, 0, 0))

    inGame.blit(GrassTexture, (448, 600))
    inGame.blit(GrassTexture, (1280, 600))

    cloudModel3_4 = pygame.image.load('sprites/Characters/Cloud.png').convert_alpha()
    cloud3_4Sheet = spritesheet.SpriteSheet(cloudModel3_4)
    cloud3_4 = cloud3_4Sheet.get_image(47, 30, 0, 0, 2.8, 2.8, (0, 0, 0))

    inGame.blit(cloud3_4, (1310, 645))

    char = pygame.image.load('sprites/Characters/char.png').convert_alpha()
    charSheet = spritesheet.SpriteSheet(char)
    bunny = charSheet.get_image(48, 48, 0, 0, 4, 4, (0, 0, 0))

    inGame.blit(bunny, (448, 580))


    bgBattle = pygame.image.load('sprites/battle/bgBattle.png').convert_alpha()
    bgBattleSheet = spritesheet.SpriteSheet(bgBattle)
    bgBattlePaste = bgBattleSheet.get_image(48, 20, 0, 0, 20, 14, (0, 0, 0))

    inGame.blit(bgBattlePaste, (480, 800))


    #Attacks
    fight = pygame.image.load('sprites/battle/fight.png').convert_alpha()
    fightSheet = spritesheet.SpriteSheet(fight)
    fightText = fightSheet.get_image(31, 5, 0, 0, 10, 10, (0, 0, 0))

    inGame.blit(fightText, (514, 834))

    run = pygame.image.load('sprites/battle/fight.png').convert_alpha()
    runSheet = spritesheet.SpriteSheet(run)
    runText = runSheet.get_image(14, 5, 0, 6, 10, 10, (0, 0, 0))

    inGame.blit(runText, (908, 834))

    panic = pygame.image.load('sprites/battle/fight.png').convert_alpha()
    panicSheet = spritesheet.SpriteSheet(panic)
    panicText = panicSheet.get_image(22, 5, 0, 12, 10, 10, (0, 0, 0))

    inGame.blit(panicText, (1184, 834))

    con1 = pygame.image.load('sprites/battle/fight.png').convert_alpha()
    con1Sheet = spritesheet.SpriteSheet(con1)
    con1Text = con1Sheet.get_image(61, 5, 0, 18, 10, 10, (0, 0, 0))

    inGame.blit(con1Text, (684, 924))

    con2 = pygame.image.load('sprites/battle/fight.png').convert_alpha()
    con2Sheet = spritesheet.SpriteSheet(con2)
    con2Text = con2Sheet.get_image(61, 5, 0, 24, 10, 10, (0, 0, 0))

    inGame.blit(con2Text, (724, 994))

    #Display All
    pygame.display.update()

#Fight Logic
def fightLogic(theGame):

    # BackDrops
    fight = pygame.image.load('sprites/battle/drop.png').convert_alpha()
    fightSheet = spritesheet.SpriteSheet(fight)
    fightText = fightSheet.get_image(33, 7, 0, 0, 10, 10, (0, 0, 0))

    run = pygame.image.load('sprites/battle/drop.png').convert_alpha()
    runSheet = spritesheet.SpriteSheet(run)
    runText = runSheet.get_image(16, 7, 0, 8, 10, 10, (0, 0, 0))

    panic = pygame.image.load('sprites/battle/drop.png').convert_alpha()
    panicSheet = spritesheet.SpriteSheet(panic)
    panicText = panicSheet.get_image(25, 7, 0, 16, 10, 10, (0, 0, 0))

    con1 = pygame.image.load('sprites/battle/drop.png').convert_alpha()
    con1Sheet = spritesheet.SpriteSheet(con1)
    con1Text = con1Sheet.get_image(64, 16, 0, 24, 10, 10, (0, 0, 0))

    #White Drop
    fight2 = pygame.image.load('sprites/battle/whiteDrop.png').convert_alpha()
    fightSheet2 = spritesheet.SpriteSheet(fight2)
    fightText2 = fightSheet2.get_image(33, 7, 0, 0, 10, 10, (0, 0, 0))

    run2 = pygame.image.load('sprites/battle/whiteDrop.png').convert_alpha()
    runSheet2 = spritesheet.SpriteSheet(run2)
    runText2 = runSheet2.get_image(16, 7, 0, 8, 10, 10, (0, 0, 0))

    panic2 = pygame.image.load('sprites/battle/whiteDrop.png').convert_alpha()
    panicSheet2 = spritesheet.SpriteSheet(panic2)
    panicText2 = panicSheet2.get_image(25, 7, 0, 16, 10, 10, (0, 0, 0))

    con12 = pygame.image.load('sprites/battle/whiteDrop.png').convert_alpha()
    con1Sheet2 = spritesheet.SpriteSheet(con12)
    con1Text2 = con1Sheet2.get_image(64, 16, 0, 24, 10, 10, (0, 0, 0))

    #Fight Button Logic

    #Cloud Speak
    bgBattle = pygame.image.load('sprites/battle/bgBattle.png').convert_alpha()
    bgBattleSheet = spritesheet.SpriteSheet(bgBattle)
    bgBattlePaste = bgBattleSheet.get_image(48, 20, 0, 0, 10, 7, (0, 0, 0))

    #Font
    font = pygame.font.Font('freesansbold.ttf', 32)

    # Hard Code Logic

    cloudHealth = 10
    cloudAttack = [2, 3, 4]

    playerHealth = 40
    playerMaxHealth = 40
    playerAttack = 6
    playerPanic = 1
    playerConstruct = 2
    playerRun = False

    fighting = True

    while(fighting):

        if cloudHealth <= 0:
            theGame.setFlip(1)
            theGame.setFlap(1)
            fighting = False

        for event in pygame.event.get():
            if ( event.type == pygame.QUIT ):
                done = True
            if event.type == pygame.MOUSEBUTTONDOWN:

                hit = cloudAttack[random.randrange(0, 2)]

                if 504 <= mouse[0] <= 814 and 804 <= mouse[1] <= 854: # Attack
                    cloudHealth = cloudHealth - playerAttack

                    #Cloud Fight Back
                    playerHealth = playerHealth - hit

                    #Cloud Speak
                    text = font.render('That was very effective!', True, (0, 0, 0))

                    inGame.blit(bgBattlePaste, (1130, 400))
                    inGame.blit(text, (1170, 450))

                    #Bunny Speak
                    text = font.render('Ouch! I have {} Health Left!'.format(playerHealth), True, (0, 0, 0))

                    inGame.blit(bgBattlePaste, (400, 400))
                    inGame.blit(text, (420, 450))

                if 901 <= mouse[0] <= 1040 and 804 <= mouse[1] <= 852: # Run
                    theGame.setFlip(1)
                    theGame.setFlap(1)
                    playerRun = True
                    fighting = False

                if 1178 <= mouse[0] <= 1396 and 804 <= mouse[1] <= 854: # Panic
                    #Cloud Taking Damage
                    cloudHealth = cloudHealth - playerPanic

                    #Cloud Fight Back
                    playerHealth = playerHealth - hit

                    #Cloud Speak
                    text = font.render("Not very effective..", True, (0, 0, 0))

                    inGame.blit(bgBattlePaste, (1130, 400))
                    inGame.blit(text, (1170, 450))

                    #Bunny Speak
                    text = font.render('Ouch! I have {} Health Left!'.format(playerHealth), True, (0, 0, 0))

                    inGame.blit(bgBattlePaste, (400, 400))
                    inGame.blit(text, (420, 450))

                if 676 <= mouse[0] <= 1286 and 894 <= mouse[1] <= 1014: # Construct
                    #Cloud Taking Damage
                    cloudHealth = cloudHealth - playerConstruct

                    #Cloud Speak
                    text = font.render("Hurts just a little :')", True, (0, 0, 0))

                    inGame.blit(bgBattlePaste, (1130, 400))
                    inGame.blit(text, (1170, 450))

                    #Cloud Fight Back
                    playerHealth = playerHealth - cloudAttack[random.randrange(0, 2)]

                    #Bunny Speak
                    text = font.render('Ouch! I have {} Health Left!'.format(playerHealth), True, (0, 0, 0))

                    inGame.blit(bgBattlePaste, (400, 400))
                    inGame.blit(text, (420, 450))

        mouse = pygame.mouse.get_pos()

        #Attack
        if 504 <= mouse[0] <= 814 and 804 <= mouse[1] <= 854:
            #Attack Logic

            #Print Backdrop
            inGame.blit(fightText, (504, 824))
        else:
            inGame.blit(fightText2, (504, 824))

        #Run
        if 901 <= mouse[0] <= 1040 and 804 <= mouse[1] <= 852:
            #Run Logic

            #Print Backdrop
            inGame.blit(runText, (898, 824))
        else:
            inGame.blit(runText2, (898, 824))

        #Panic
        if 1178 <= mouse[0] <= 1396 and 804 <= mouse[1] <= 854:
            #Panic Logic

            #Print Backdrop
            inGame.blit(panicText, (1174, 824))
        else:
            inGame.blit(panicText2, (1174, 824))


        #Constructive Criticism
        if 676 <= mouse[0] <= 1286 and 894 <= mouse[1] <= 1014:
            #Constructive Logic

            #Print Backdrop
            inGame.blit(con1Text, (674, 914))
        else:
            inGame.blit(con1Text2, (674, 914))

        pygame.display.update()
