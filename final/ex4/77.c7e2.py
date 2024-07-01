user={}

name=input("enter your name:")
age=int(input("enter your age:"))
fav_movies=input("enter fav movies:").split(",") #saprated by comma
fav_songs=input("enter fav songs:").split(",")

user['name']=name
user['age']=age
user['fav_movies']=fav_movies
user['fav_songs']=fav_songs

for key,value in user.items():
    print(f"{key} : {value}")