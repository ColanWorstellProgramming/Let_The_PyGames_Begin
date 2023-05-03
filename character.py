import pygame, config


## -------------------------------- Player's Character Class
class char:
    def __init__(self):
        self.playerMaxHealth = 40
        self.playerHealth = 40
        self.playerAttackOption1 = 6 # Main Attack - (Attack)
        self.playerAttackOption2 = 1 # Secondary Attack - (Panic)
        self.playerAttackOption3 = 2 # Tertiary Attack - (Constructive Crit)


    def getPlayerMaxHealth(self):
        return self.playerMaxHealth

    def setPlayerMaxHealth(self, x):
        self.playerMaxHealth = x

    def getPlayerHealth(self):
        return self.playerHealth

    def setPlayerHealth(self, x):
        self.playerHealth = x

    def getPlayerAttackOption1(self):
        return self.playerAttackOption1

    def setPlayerAttackOption1(self, x):
        self.playerAttackOption1 = x

    def getPlayerAttackOption2(self):
        return self.playerAttackOption2

    def setPlayerAttackOption2(self, x):
        self.playerAttackOption2 = x

    def getPlayerAttackOption3(self):
        return self.playerAttackOption3

    def setPlayerAttackOption3(self, x):
        self.playerAttackOption3 = x


## -------------------------------- Default Enemies Class
class enemy:
    def __init__(self):
        self.cloudHealth = -1
        self.cloudAttack = -1


    def getEnemyHealth(self):
        return self.cloudHealth

    def setEnemyHealth(self, x):
        self.cloudHealth = x

    def getEnemyAttack(self):
        return self.cloudAttack

    def setEnemyAttack(self, x):
        self.cloudAttack = x
