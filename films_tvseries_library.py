import random

class Films():
    def __init__(self, title, publication_date, genre):
        self.title = title
        self.publication_date = publication_date
        self.genre = genre

        self.current_plays = 0

    def play(self, step = 1):
        self.current_plays += step

    def __str__(self):
        return f"{self.title} ({self.publication_date})"

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
        sorted_movies = sorted(movies, key = lambda movie: movie.title)
        return sorted_movies
    
    def get_series(self):
        series = []
        series.extend([title for title in self.titles if isinstance(title, TVSeries)])
        sorted_series = sorted(series, key = lambda serie: serie.title)
        return sorted_series
    
    def search(self, title):
        search_title = [title for titles in self.titles if title == titles.title]
        if bool(search_title) == True:
            print(f"Here you are: {search_title}")
        else:
            print("Nothing to do here.")

    def generate_views(self, amount):
        for title in range(amount):
            title = (random.choice(self.titles))
            title_plays = (random.choice(range(1, 100)))
            print(f"{title} - current plays = {title_plays}")

pulp_fiction = Films("Pulp Fiction", 1994, "Criminal")
the_walking_dead = TVSeries("The Walking Dead", 2010, "Horror")
django = Films("Django", 2012, "Western")
breaking_bad = TVSeries("Breaking Bad", 2008, "Crime Drama")
the_hateful_eight = Films("The Hateful Eight", 2015, "Western")
the_last_of_us = TVSeries("The Last of Us", 2023, "Post Apo")

library = Library()
library.add_title(pulp_fiction)
library.add_title(the_walking_dead)
library.add_title(django)
library.add_title(breaking_bad)
library.add_title(the_hateful_eight)
library.add_title(the_last_of_us)

sorted_movies = library.get_movies()
for movie in sorted_movies:
    print(movie)

sorted_series = library.get_series()
for serie in sorted_series:
    print(serie)

library.search("Django")
library.search("Kapitan Bomba")
library.generate_views(10)





