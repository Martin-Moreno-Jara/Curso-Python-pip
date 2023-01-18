def get_population():
  keys = ["Colombia","Argentina"]
  values = [50887844,4500000]
  return keys,values

mamaguebo = lambda nombre:f"{nombre} mamaguebaso"

def population_per_country(data,country):
  result = list(filter(lambda item:item["country"]==country,data))
  return result