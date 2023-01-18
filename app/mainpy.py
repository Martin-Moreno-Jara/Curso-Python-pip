import utils
lista = [{"country":"Colombia","population":11044},
           {"country":"Argentina","population":8885}]
def run():

  
  countries,population = utils.get_population()
  print(f"{countries}\n{population}")
  
  mamaguebaso = utils.mamaguebo("Ernesto")
  print(mamaguebaso)
  
  print()
  
  result = utils.population_per_country(lista,"Colombia")
  print(result)

if __name__ == "__main__":
  run() 