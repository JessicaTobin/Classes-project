from time import sleep
class Monster:   #makes a class called Mon
    #stats
    health = 10  
    stamina = 15

    #things it can do
    def getsHit(self):
        self.health=self.health-2

    def sayHealth(self):
        print("Health is now " + str(self.health))

    def attacks(self):
        self.stamina=self.stamina-2

    def sayStam(self):
        print("Stamina is now " + str(self.stamina))


#the monsters that appear including player so I could show the health of the player
you = Monster()
egg = Monster()
soup = Monster()

print("The monster Egg appears")
sleep(1)
print("If your stamina runs out you cannot attack")
sleep(1)
print("This computer will tell you your stamina and health")
sleep(1)
choice = input("Choose your attack: Sword or Punch")

if choice=="Sword" or "sword":
    print ("You hit the monster with a sword")
    egg.getsHit()
    sleep(1)
    print("Egg says:")
    egg.sayHealth()
    sleep(1)
    print("You loose stamina")
    you.attacks()
    sleep(1)
    print("Computer says:")
    you.sayStam()

elif choice=="Punch" or "punch":
    print("You attempt to punch the monster but fail")
    sleep(1)
    print("Egg attacks you")
    egg.attacks()
    sleep(1)
    print("You loose health")
    you.sayHealth()

else:
    print("You try something not offered and fail")
    sleep(1)
    print("Egg attcks you with a critical hit")
    egg.attacks()
    egg.attacks()
    egg.attacks()
    egg.attacks()
    egg.attacks()
    sleep(1)
    print("You have lost all your health")
    sleep(1)
    you.sayHealth()
    print("GAME OVER")
    break
    
    
    
    #if they chose sword:
    #The monster Egg appears
#If your stamina runs out you cannot attack
#This computer will tell you your stamina and health
#Choose your attack: Sword or Punchsword
#You hit the monster with a sword
#Egg says:
#Health is now 8
#You loose stamina
#Computer says:
#Stamina is now 13
    
    #if they choose punch:
    #this part actually doesnt work but I can't figure out why. It just shows the response for sword
    #the resposnse should look like:
    #The monster Egg appears
#If your stamina runs out you cannot attack
#This computer will tell you your stamina and health
#Choose your attack: Sword or Punchpunch
#You attempt to punch the monster but fail
#Egg attacks you
#You loose health
#Computer says:
#Health is now 8


    #if they type anything else:
    #again doesnt work
    #should look like this:    
    #The monster Egg appears
#If your stamina runs out you cannot attack
#This computer will tell you your stamina and health
#Choose your attack: Sword or Punchegg
#You try something not offered and fail
#Egg attcks you with a critical hit
#You have lost all your health
#Health is now 0
#GAME OVER
