import weaponClass as w
import csv


"""
- Create a program that will read the contents of the file 'weapons.txt'. Each record in the file represents the specs to a weapon.
- Create an instance of the weapon object for each record. 
- Create a dictionary that will contain the name of the weapon as the key and the number of bullets as the value. 
- Print out details of each weapon using the object's methods only (as per comments below). 
- Fire all bullets of the weapon and print a countdown of bullets remaining (run exe file to visualize, HINT: use end='\r' in your print statement).
- Print out the name of the weapon and the number of bullets from the dictionary.

HINT: Follow the comments for each line to help with the logic of the problem.
"""


# create a file object to open the file in read mode

outfile = open(
    "/Users/ryanleckich/Desktop/School/AdvancedPython/MIS5322_quiz_1/weapons.csv", "r"
)


# create a csv object from the file object
weapons = csv.reader(outfile)

# skip the header row


next(weapons)
# print(guns)

# create an empty dictionary named 'weapons_dict'


weapons_dict = {}


# use a for loop to iterate through every row of the csv file

for ammo in weapons:
    # if ammo in guns:
    # outfile.write(guns[ammo])
    # else:
    # outfile.write(ammo)
    # use variables for name,speed and range (optional)
    # print(ammo)

    # create an instance of the weapon object using the
    # specs from the csv file (name,speed and range)

    armory = w.Weapon(ammo[0], ammo[1], ammo[2])

    # append the name and bullet count to 'weapons_dict'
    weapons_dict = {"Weapon Name": [0]}, {"Bullet": armory.get_bullets()}

    # print out the name of the weapon using the appropriate method of the object
    print(armory.get_name())

    # print out the speed of the weapon using the appropriate method of the object
    print(armory.get_speed())

    # print out the range of the weapon using the appropriate method of the object
    print(armory.get_range())

    # print out the number of bullets of the weapon using the appropriate method of the object
    print(armory.get_bullets())

    # use an input statement to halt the program and wait for the user -
    input("Press enter to fire the weapon")

    # length = armory.get_bullets()

    # use an appropriate loop to keep firing the weapon until all bullets run out

    for i in range(armory.get_bullets()):

        # call the appropriate method to fire a bullet
        armory.fire_bullet(armory.get_bullets())

        # print out the bullet count every time the weapon is fired
        print(armory.get_bullets())


# using a loop print out the name and number of bullets from the dictionary
for i in weapons_dict:

    print(weapons_dict)
