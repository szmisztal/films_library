class Films():
    def __init__(self, title, publication_date, genre, number_of_plays):
        self.title = title
        self.publication_date = publication_date
        self.genre = genre
        self.number_of_plays = number_of_plays

        self.current_plays = 0

    def __str__(self):
        return f"{self.title}, {self.publication_date}, {self.genre}, {self.number_of_plays}"
    
    def play(self, step = 1):
        self.current_plays += step

class TVSeries(Films):
    def __init__(self, episode_number, season_number, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.episode_number = episode_number
        self.season_number = season_number
    
    def __str__(self):
        return super(). __str__ + f"{self.episode_number}, {self.season_number}"
