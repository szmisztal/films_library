class Films():
    def __init__(self, title, publication_date, genre, number_of_plays):
        self.title = title
        self.publication_date = publication_date
        self.genre = genre
        self.number_of_plays = number_of_plays

        self.current_plays = 0

    def play(self, step = 1):
        self.current_plays += step

    def __str__(self):
        return f"{self.title}, ({self.publication_date})"

class TVSeries(Films):
    def __init__(self, episode_number, season_number, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.episode_number = episode_number
        self.season_number = season_number
    
    def __str__(self):
        season = str(self.season_number).zfill(2)
        episode = str(self.episode_number).zfill(2)
        return f"{self.title} S{season}E{episode}"

class Library():
    def __init__(self):
        self.titles = []

    def add_title(self, title):
        self.titles.append(title)

    def get_movies(self):
        movies = []
        movies.extend[(title for title in self.titles if isinstance(title, Films))]
        sorted_movies = sorted(movies)
        return sorted_movies
    
    def get_series(self):
        series = []
        series.extend([title for title in self.titles if isinstance(title, TVSeries)])
        sorted_series = sorted(series)
        return sorted_series
