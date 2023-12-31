import random
from datetime import date

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

class TVSeries(Films):
    def __init__(self, title, publication_date, genre, season_number, episode_number):
        super().__init__(title, publication_date, genre)
        self.season_number = season_number
        self.episode_number = episode_number

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
        movies.extend([title for title in self.titles if not isinstance(title, TVSeries)])
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
            print("Nothing`s here.")

    def generate_views(self, amount):
        self.number_of_plays = random.sample(self.titles, amount)
        for title in self.number_of_plays:
            title.play(random.choice(range(1, 100)))

    def top_titles(self, amount, content_type = None):
        if content_type == 'movies':
            content = self.get_movies()
        elif content_type == 'series':
            content = self.get_series()
        else:
            content = self.titles
        self.top_list = sorted(content, key = lambda title: title.current_plays, reverse = True)
        return self.top_list[:amount]

pulp_fiction = Films("Pulp Fiction", 1994, "Criminal")
the_walking_dead = TVSeries("The Walking Dead", 2010, "Horror", 1, 1)
django = Films("Django", 2012, "Western")
breaking_bad = TVSeries("Breaking Bad", 2008, "Crime Drama", 1, 1)
the_hateful_eight = Films("The Hateful Eight", 2015, "Western")
the_last_of_us = TVSeries("The Last of Us", 2023, "Post Apo", 1, 1)
inglourious_basterds = Films("Inglourious Basterds", 2009, "War Film")
kapitan_bomba = TVSeries("Kapitan Bomba", 2007, "Comedy", 1, 1)
alien = Films("Alien", 1979, "Horror")
chernobyl = TVSeries("Chernobyl", 2019, "Drama", 1, 1)

print("MOVIES AND SERIES LIBRARY.")

library = Library()
library.add_title(pulp_fiction)
library.add_title(the_walking_dead)
library.add_title(django)
library.add_title(breaking_bad)
library.add_title(the_hateful_eight)
library.add_title(the_last_of_us)
library.add_title(inglourious_basterds)
library.add_title(kapitan_bomba)
library.add_title(alien)
library.add_title(chernobyl)

library.generate_views(10)

today = date.today()
dd_mm_yyyy = today.strftime("%d/%m/%Y")

top_of_all = library.top_titles(3)
top_of_all_list = []
for title in top_of_all:
    top_of_all_list.append(title.title)
print("The most popular titles today", dd_mm_yyyy, "are: " + ', '.join(top_of_all_list),'.')

top_movies = library.top_titles(3, 'movies')
top_movies_list = []
for title in top_movies:
    top_movies_list.append(title.title)
print("The most popular movies today", dd_mm_yyyy, "are: " + ', '.join(top_movies_list),'.')

top_series = library.top_titles(3, 'series')
top_series_list = []
for title in top_series:
    top_series_list.append(title.title)
print(f"The most popular series today", dd_mm_yyyy, "are: " + ', '.join(top_series_list),'.')




