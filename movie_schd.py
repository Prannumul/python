current_movies={"Transformer's":"3:00pm",
                    "Indiana Jones":"7:00 pm",
                    "Lego movie":"4:00 pm"}

print("We are showing the following mvoies")
for key in current_movies:
    print(key) # print the keys
    #print(current_movies[key]) #print values

movie=input("What movie would you like the showtime for?\n")
showtime= current_movies.get(movie)
#showtime= current_movies[movie]
if showtime == None:
    print("Requested movie isn't playing")
else:
    print(movie,"is playing at",showtime)