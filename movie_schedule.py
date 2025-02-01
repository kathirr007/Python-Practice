current_movies = {
    'The Grinch': '11:00am',
    'Moana 2': '2:00pm',
    'Master 2': '4:00pm',
    'Bad Boys III': '6:00pm',
}

print("We are showing the following movies: \n")

for key in current_movies:
    print(key)

movie = input("Which movie you would like to know the show time?\n")

show_time = current_movies.get(movie)

if show_time == None:
    print(f"Sorry..! The requested movie {movie} is not available.")
else:
    print(f"Movie {movie} is playing at {show_time}.")


