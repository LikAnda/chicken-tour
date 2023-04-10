# GOAL: récupérer des œufs en picorant les plantes et les vendres à l'échoppe

# ========[FEATURES]=========
# - se déplacer dans toutes les directions (+ animation)
# - les plantes grandissent automatiquement
# - récupérer des œufs en picorant les plantes (+ animation)
# - vendre les œufs à un magasin pour obtenir des pièces (valeur d'un œufs aléatoirelent choisie)
# - tirer un œuf dans les quatres directions (devant, gauche, derrière, droite)
# - achievements: 10 œuf récupérés / 50 pièces obetnues
# ========[FEATURES]=========

# ==========[KEYS]===========
# Z, Q, S, D = Devant, Gauche, Derrière, Droite
# E = Picorer une plante (poule doit être sur une plante)
# T = Trade à l'échoppe (poule doit être sur le magasin)
# F = Tirer un œuf dans la direction où le joueur regarde (œufs nécessaires pour tirer)
# ==========[KEYS]===========

from tkinter import *
from PIL import Image
from random import randint
from tkinter import messagebox

# compter le nombre de pièces
def coinsCount(coinsValue):
    global ca, window, coinCounterLabel, coinNumber

    coinNumber = coinNumber + coinsValue
    coinCounterLabel.config(text=f"{coinNumber} pièces")

# compter le nombre d'œufs
def eggsCount(eggsValue):
    global ca, window, eggCounterLabel, eggNumber

    eggNumber = eggNumber + eggsValue
    eggCounterLabel.config(text=f"{eggNumber} œufs")

# shoot = tire un œuf dans la direction où regarde le joueur
def shoot():
    global ca, window, player, eggNumber, eggBullet, eggBulletImg, shootInProgress, shootDirection

    xWindow = window.winfo_width()
    yWindow = window.winfo_height()

    if shootInProgress == True:
        xEggBullet, yEggBullet = ca.coords(eggBullet)

        if shootDirection == 0:
            xEggBullet += 10
        elif shootDirection == 1:
            xEggBullet -= 10
        elif shootDirection == 2:
            yEggBullet += 10
        elif shootDirection == 3:
            yEggBullet -= 10

        ca.delete(eggBullet)
        eggBullet = ca.create_image(xEggBullet, yEggBullet, image=eggBulletImg)

    if "xEggBullet" in globals() or "yEggBullet" in globals(): # vérifie si la variable existe
        if xEggBullet < 0:
            shootInProgress = False
        if xEggBullet > xWindow:
            shootInProgress = False
        if yEggBullet < 0:
            shootInProgress = False
        if yEggBullet > yWindow:
            shootInProgress = False

    window.after(20, shoot)

# trade = échanger des œufs contre des pèces au magasin
def trade():
    print("TRADE")
    global ca, window, player, eggNumber, coinNumber
    global xMarket, yMarket

    xPlayer, yPlayer = ca.coords(player)

    if (xMarket-50< xPlayer < xMarket+50) and (yMarket-50< yPlayer < yMarket+50 and eggNumber > 0):
        eggsCount(-1)
        coinToEarn = randint(3, 7)
        coinsCount(coinToEarn)
        print(f"Trade Accepted: coinToEarn = {coinToEarn}")
    else:
        print("Trade Declined")
    
    if coinNumber >= 50:
        messagebox.showerror(title="Succès Déverrouiller", message="Vous avez obetnue plus de 50 pièces !")

# peckAnimation = anime le picorage des plantes
def peckAnimation():
    global ca, window, player
    global rowIndex, compteurSprite, peckSpriteCount

    xPlayer, yPlayer = ca.coords(player)

    peckSpriteCount += 1
    ca.delete(player)
    player = ca.create_image(xPlayer, yPlayer, image = principalSpriteList[rowIndex][peckSpriteCount])
    if peckSpriteCount < 2:
        window.after(300, peckAnimation)

# peck = picorer les plantes pour obtenir des oeufs
def peck():
    print("PECK")
    global ca, window, player, peckSpriteCount, peckCount, peckInProgress
    global crop1, crop2, crop3, crop4, crop1Image, crop2Image, crop3Image, crop4Image
    global xCrop1, yCrop1, xCrop2, yCrop2, xCrop3, yCrop3, xCrop4, yCrop4, crop1State, crop2State, crop3State, crop4State

    xPlayer, yPlayer = ca.coords(player)

    if (xCrop1-30< xPlayer < xCrop1+30) and (yCrop1-30< yPlayer < yCrop1+30 and crop1State == 4):
        crop1State = 0
        ca.delete(crop1)
        peckAnimation()
        peckSpriteCount = 0
        crop1 = ca.create_image(xCrop1, yCrop1, image=principalCropsList[0][crop1State])
        eggsCount(1)
        peckCount += 1
    
    if (xCrop2-30< xPlayer < xCrop2+30) and (yCrop2-30< yPlayer < yCrop2+30 and crop2State == 4):
        crop2State = 0
        ca.delete(crop2)
        peckAnimation()
        peckSpriteCount = 0
        crop2 = ca.create_image(xCrop2, yCrop2, image=principalCropsList[0][crop2State])
        eggsCount(1)
        peckCount += 1

    if (xCrop3-30< xPlayer < xCrop3+30) and (yCrop3-30< yPlayer < yCrop3+30 and crop3State == 4):
        crop3State = 0
        ca.delete(crop3)
        peckAnimation()
        peckSpriteCount = 0
        crop3 = ca.create_image(xCrop3, yCrop3, image=principalCropsList[0][crop3State])
        eggsCount(1)
        peckCount += 1

    if (xCrop4-30< xPlayer < xCrop4+30) and (yCrop4-30< yPlayer < yCrop4+30 and crop4State == 4):
        crop4State = 0
        ca.delete(crop4)
        peckAnimation()
        peckSpriteCount = 0
        crop4 = ca.create_image(xCrop4, yCrop4, image=principalCropsList[0][crop4State])
        eggsCount(1)
        peckCount += 1
    
    peckInProgress = False

    if peckCount == 10:
        messagebox.showinfo(title="Succès Déverrouiller", message="Vous avez picoré des plantes 10 fois !")

# growCrops = fait grandir les plantations
def growCrops():
    global ca, window
    global crop1, crop2, crop3, crop4, crop1Image, crop2Image, crop3Image, crop4Image
    global xCrop1, yCrop1, xCrop2, yCrop2, xCrop3, yCrop3, xCrop4, yCrop4
    global crop1State, crop2State, crop3State, crop4State

    cropsNumberAchieved = 0
    cropsNumber = randint(0, 2) # nombre de plantes à faire grandir
    growTime = randint(2500, 6500) # temps avant de faire grandir de nouvelles plantes

    # "pass" utilisé pour facilité la fonction "peck"
    while cropsNumberAchieved < cropsNumber: # faire grandir une ou plusieurs plantes à la fois
        cropToGrow = randint(1, 4)
        if cropToGrow == 1:
            if crop1State >= 4:
                pass
            else:
                crop1State += 1
                ca.delete(crop1)
                crop1 = ca.create_image(xCrop1, yCrop1, image=principalCropsList[0][crop1State])
                print(f"Crop 1 state = {crop1State}")
        elif cropToGrow == 2:
            if crop2State >= 4:
                pass
            else:
                crop2State += 1
                ca.delete(crop2)
                crop2 = ca.create_image(xCrop2, yCrop2, image=principalCropsList[0][crop2State])
                print(f"Crop 2 state = {crop2State}")
        elif cropToGrow == 3:
            if crop3State >= 4:
                pass
            else:
                crop3State += 1
                ca.delete(crop3)
                crop3 = ca.create_image(xCrop3, yCrop3, image=principalCropsList[0][crop3State])
                print(f"Crop 3 state = {crop3State}")
        elif cropToGrow == 4:
            if crop4State >= 4:
                pass
            else:
                crop4State += 1
                ca.delete(crop4)
                crop4 = ca.create_image(xCrop4, yCrop4, image=principalCropsList[0][crop4State])
                print(f"Crop 4 state = {crop4State}")

        cropsNumberAchieved += 1 # pour la boucle qui fait grandir plusieurs plantes
    
    window.after(growTime, growCrops)

# borderProcess = empeche le joueur de ne pas dépasser la zone de jeu
def borderProcess():
    global ca, player, principalSpriteList, rowIndex, compteurSprite
    xPlayer, yPlayer = ca.coords(player)
    xWindow = window.winfo_width()
    yWindow = window.winfo_height()

    if xPlayer < 0:
        xPlayer = xWindow
    if xPlayer > xWindow:
        xPlayer = 0
    if yPlayer < 0:
        yPlayer = yWindow
    if yPlayer > yWindow:
        yPlayer = 0
    
    ca.delete(player)
    player = ca.create_image(xPlayer, yPlayer, image = principalSpriteList[rowIndex][compteurSprite])

# move = déplace le sprite du personnage
def move(event):
    global ca, player, principalSpriteList, compteurSprite, rowIndex
    global shootInProgress, eggBullet, eggBulletImg, shootDirection, eggNumber, peckInProgress

    # effectuer d'autres actions en cas de presse de touche autres que z, q, s, d
    if  event.char == 'z' or event.char == 's' or event.char == 'q' or event.char == 'd':
        if peckInProgress != True:
            compteurSprite += 1

            if compteurSprite == 7:
                compteurSprite = 2
            x, y = ca.coords(player)

            if event.char == 'z':
                ca.delete(player)
                rowIndex = 3
                player = ca.create_image(x, y-10, image = principalSpriteList[rowIndex][compteurSprite])
            elif event.char == 's':
                ca.delete(player)
                rowIndex = 2
                player = ca.create_image(x, y+10, image = principalSpriteList[rowIndex][compteurSprite])
            elif event.char == 'q':
                ca.delete(player)
                rowIndex = 1
                player = ca.create_image(x-10, y, image = principalSpriteList[rowIndex][compteurSprite])
            elif event.char == 'd':
                ca.delete(player)
                rowIndex = 0
                player = ca.create_image(x+10, y, image = principalSpriteList[rowIndex][compteurSprite])
            borderProcess()

    elif event.char == 'e':
        peckInProgress = True
        peck()
    elif event.char == 'f':
        if eggNumber > 0:
            x, y = ca.coords(player)
            if "eggBullet" in globals(): # vérifie si la vriable existe pour supprimer l'ancien œuf
                print("eggBullet exist")
                ca.delete(eggBullet)
            eggBullet = ca.create_image(x, y, image=eggBulletImg)
            if rowIndex == 0:
                shootDirection = 0
            elif rowIndex == 1:
                shootDirection = 1
            elif rowIndex == 2:
                shootDirection = 2
            elif rowIndex == 3:
                shootDirection = 3
            eggsCount(-1)
            shootInProgress = True
    elif event.char == 't':
        trade()

compteurSprite = 2
peckSpriteCount = 0
eggNumber = 0
coinNumber = 5
peckCount = 0
peckInProgress = False

window = Tk()
window.title("Chicken Tour")
window.geometry("1002x678")

ca = Canvas (width=1002,height=678)
ca.place(x=0,y=0)

imageMap = PhotoImage(file="./images/map.png") # map
map = ca.create_image(500, 338,  image=imageMap)

imagePlayer = PhotoImage(file="./images/first-chicken-sprite.png") # joueur
player = ca.create_image(275, 380, image=imagePlayer)

eggCounterImage = PhotoImage(file="./images/egg-counter.png")
eggCounter =  ca.create_image(40, 40, image=eggCounterImage)
eggCounterLabel = Label(window, text=f"{eggNumber} œufs", font=("Arial", 15), background="#20A80A")
eggCounterLabel.place(x=70, y=28) # compteur d'œuf

coinCounterImage = PhotoImage(file="./images/coin-counter.png")
coinCounter =  ca.create_image(190, 42, image=coinCounterImage)
coinCounterLabel = Label(window, text=f"{coinNumber} pièces", font=("Arial", 15), bg="#DEE50E")
coinCounterLabel.place(x=220, y=28)# compteur de pièces

window.bind("<Any-KeyPress>", move)

# ===========[sprites]=========== #
sprite = Image.open("./images/chicken-sprite.png") # sprite du joueur
principalSpriteList = []
for i in range(0, 4):
    listTemp = []
    for j in range(0, 7):
        img = sprite.crop([j*47, i*47, j*47+47, i*47+47])
        img = img.save("./images/temp.png")
        imgTemp = PhotoImage(file="./images/temp.png")
        listTemp.append(imgTemp)
    principalSpriteList.append(listTemp)

spriteCrops = Image.open("./images/crops.png") # sprite des plantes
principalCropsList = []
for i in range(0, 1):
    listTempCrops = []
    for j in range(0, 5):
        imgCrops = spriteCrops.crop([j*39, i*90, j*39+39, i*90+90])
        imgCrops = imgCrops.save("./images/tempCrops.png")
        imgTempCrops = PhotoImage(file="./images/tempCrops.png")
        listTempCrops.append(imgTempCrops)
    principalCropsList.append(listTempCrops)

# =========[coordonnées]========= #
xCrop1, yCrop1 = 115, 90
xCrop2, yCrop2 = 740, 350
xCrop3, yCrop3 = 220, 540
xCrop4, yCrop4 = 660, 490

xMarket, yMarket = 460, 185

# ============[props]============ #
crop1 = ca.create_image(xCrop1, yCrop1, image=principalCropsList[0][0])
crop1State = 0

crop2 = ca.create_image(xCrop2, yCrop2, image=principalCropsList[0][1])
crop2State = 1

crop3 = ca.create_image(xCrop3, yCrop3, image=principalCropsList[0][2])
crop3State = 2

crop4 = ca.create_image(xCrop4, yCrop4, image=principalCropsList[0][4])
crop4State = 4

marketImage = PhotoImage(file="./images/market.png")
market = ca.create_image(xMarket, yMarket, image=marketImage)

eggBulletImg = PhotoImage(file="./images/egg-bullet.png")

shootInProgress = False
shoot()
window.after(4000, growCrops)

window.mainloop()