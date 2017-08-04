import webbrowser


# This is the Class of which the instances from \
# instancemovie.py will initialize from


class Projectmovie():
    def __init__(
        self, title_movie, description_movie, year_movie, category_movie,
        duration_movie, poster_movie, trailer_movie): 
        self.title = title_movie
        self.description = description_movie
        self.year = year_movie
        self.category = category_movie
        self.duration = duration_movie
        self.poster_image_url = poster_movie
        self.trailer_youtube_url = trailer_movie

# this method opens the youtube movie trailer
    def trailer_movie(): webbrowser.open(self.trailer_youtube_url)
