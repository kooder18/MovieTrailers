import webbrowser

class Movie():
    def __init__(self, movie_title, movie_storline, poster_image, trailer_youtube, actors):
        self.title = movie_title
        self.storyline = movie_storline
        self.poster_image_url = poster_image
        self.trailer_youtube_url = trailer_youtube
        self.actor_list = actors


    def show_trailer(self):
        webbrowser.open(self.trailer_youtube_url)
