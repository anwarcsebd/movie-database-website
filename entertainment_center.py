import  media
import fresh_tomatoes

# movie object
toy_story = media.Movie("Toy Story", "A story of a boy and a toy that come to life",
	"https://upload.wikimedia.org/wikipedia/en/1/13/Toy_Story.jpg", "https://www.youtube.com/watch?v=4KPTXpQehio")


avatar = media.Movie("Avatar", "A marine on an alien planet", 
	"http://upload.wikimedia.org/wikipedia/id/b/b0/Avatar-Teaser-Poster.jpg","http://www.youtube.com/watch?v=-9ceBgWV8io")


wall_e = media.Movie("WALL-E", "WALL-E is set in the far future where humans have left Earth on a giant ship called the Axiom because of all the garbage pile-up",
	"https://vignette.wikia.nocookie.net/disney/images/f/f2/Walleposter.jpg/revision/latest?cb=20150214194124",
	"https://www.youtube.com/watch?v=alIq_wG9FNk")


school_of_rock = media.Movie("School of Rock", "Storyline", "http://upload.wikimedia.org/wikipedia/en/1/11/School_of_Rock_Poster.jpg",
	"https://www.youtube.com/watch?v=3PsUJFEBC74") 


ratatouille = media.Movie("Ratatouille", "Storyline", "http://upload.wikimedia.org/wikipedia/en/5/50/RatatouillePoster.jpg",
	"https://www.youtube.com/watch?v=c3sBBRxDAqk")


hunger_games = media.Movie("Honger Games", "Storyline", "http://upload.wikimedia.org/wikipedia/en/4/42/HungerGamesPoster.jpg",
	"https://www.youtube.com/watch?v=PbA63a7H0bo") 


#the list of movie objects to be displayed in the webpage

movies = [toy_story, avatar, wall_e, school_of_rock, ratatouille, hunger_games]

fresh_tomatoes.open_movies_page(movies)

