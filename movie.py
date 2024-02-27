current_movies = {
  'The Grinch': '11:00am',
  "Bad Santa": '11:30am',
  "Kill Bill": '1:00pm',
  "Dune": '3:20pm'
}

print("We're showing the following movies:")
for key in current_movies:
  print(key)

movie = input('What movie would you like the showtime for?\n')

showtime = current_movies.get(movie.capitalize())

if showtime == None:
  print("Requested movie isn't playing")
else:
  print(showtime)