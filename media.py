import webbrowser


#the Movie object
class Movie():
    def __init__(self, movie_title, movie_storyline, movie_poster_url, movie_youtube_url):
        self.title = movie_title
        self.storyline = movie_storyline
        self.poster_image_url = movie_poster_url
        self.trailer_youtube_url = movie_youtube_url

#the function to call to visualize the trailers in the webpage
        def showTrailer(self):
            webbrowser.open(self.trailer_youtube_url)
