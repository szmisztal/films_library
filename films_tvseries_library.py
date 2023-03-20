class Films():
    def __init__(self, title, publication_date, genre):
        self.title = title
        self.publication_date = publication_date
        self.genre = genre

        self.current_plays = 0

    def play(self, step = 1):
        self.current_plays += step

    def __str__(self):
        return f"{self.title}, ({self.publication_date})"

class TVSeries():
    def __init__(self, title, publication_date, genre):
        self.title = title
        self.publication_date = publication_date
        self.genre = genre

        self.current_plays = 0
        self.episode_number = 1
        self.season_number = 1

    def play(self, step = 1):
        self.current_plays += step
        self.episode_number += step
        if self.episode_number == 13:
            self.episode_number = 1
            self.season_number += step

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
        movies.extend([title for title in self.titles if isinstance(title, Films)])
        return print(movies)
    
    def get_series(self):
        series = []
        series.extend([title for title in self.titles if isinstance(title, TVSeries)])
        return print(series)

pulp_fiction = Films("Pulp Fiction", 1994, "Criminal")
the_walking_dead = TVSeries("The Walking Dead", 2010, "Horror")
django = Films("Django", 2012, "Western")
breaking_bad = TVSeries("Breaking Bad", 2008, "Crime Drama")
the_hateful_eight = Films("The Hateful Eight", 2015, "Western")
print(the_hateful_eight)
print(the_walking_dead)

library = Library()
library.add_title(pulp_fiction)
library.add_title(the_walking_dead)
library.add_title(django)
library.add_title(breaking_bad)
library.add_title(the_hateful_eight)
print(library.titles)
library.get_movies()
library.get_series()




