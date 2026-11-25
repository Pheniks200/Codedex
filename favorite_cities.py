# Write code below 💖

class City:
  def __init__(self,name, country, population, landmarks, nickname, founding_year, mayor):
    self.name = name
    self.country = country
    self.population = round(population,-3)
    self.landmarks = landmarks
    self.nickname = nickname
    self.founding_year = int(founding_year)
    self.mayor = mayor

bielsko = City('Bielsko', "Poland", 168083, ["zamek", 'ratusz'], 'bialka', 1412, 'prezydent')

print(vars(bielsko))