# Exercise 2

# Satellites:
sat_database = {"METEOSAT" : 3000,
                "LANDSAT"  : 30,
                "MODIS"    : 500                
               }
print(sat_database)
# The dictionary above contains the names and spatial resolutions of some satellite systems.

# 1) Add the "GOES" and "worldview" satellites with their 2000/0.31m resolution to the dictionary [2P]
sat_database["GOES"]= 2000
sat_database["worldview"]= 0.31

print("I have the following satellites in my database:")
print(sat_database)

# 2) print out all satellite names contained in the dictionary [2P]
print(sat_database.keys())

# 3) Ask the user to enter the satellite name from which she/he would like to know the resolution [2P]
answer = input ("About which satellite would like to know the resolution?")

if answer == "METEOSAT":
    print(" The  resolution of METEOSAT is 3000 m.")
elif answer == "LANDSAT":
    print("The  resolution of LANDSAT is 30 m.")
elif answer == "MODIS":
    print(" The  resolution of MODIS is 500 m. ")
elif answer == "GOES":
    print("The  resolution of GOES is 2000 m.") 
elif answer == "worldview":
    print("The  resolution of worldview is 0.31 m.")
else:
    print("I did not understand your answer! Please check your entry for the correct spelling.")
    
# 4) Check, if the satellite is in the database and inform the user, if it is not [2P]
if answer in sat_database:
    print ("The satellite is registered in the database.")
else: 
    print ("The satellite is not registered in the database.")

# 5) If the satellite name is in the database, print a meaningful message containing the satellite name and it's resolution [2P] 
ans=answer
reso=(sat_database.get(answer))

if answer in sat_database:
    print ("In the database the satellite {ans} is registered and {reso} m is its resolution".format(ans=ans, reso=reso))
else: 
    print ("The satellite is not registered in the database.")
    
    
    
    
