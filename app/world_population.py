import csv
import matplotlib.pyplot as plt
import app.charts

def get_dictionary_from_csv(path): #Obtener del csv una lista de diccionarios de los paises
  with open(path,"r+") as csv_file:
    reader = csv.reader(csv_file,delimiter=",")
    header = next(reader)
    dict_list = []
    for row in reader:
      combined_files = zip(header,row)
      dictionary = {key:value for key,value in combined_files}
      dict_list.append(dictionary)
  return dict_list

def get_country(dict_list,country): # Obtener la información del pais seleccionado
  dic = {}
  for i in dict_list:
    if i["Country/Territory"]==country:
      dic = i
  return dic
  

def get_population(country_dict):
  copy_dict = country_dict.copy()
  keys = ["2022 Population","2020 Population","2015 Population","2010 Population","2000 Population","1990 Population","1980 Population","1970 Population"]
  for i in country_dict.keys():
    if i not in keys:
      copy_dict.pop(i)
  copy_dict["2022"] = int(copy_dict.pop("2022 Population"))
  copy_dict["2020"] = int(copy_dict.pop("2020 Population"))
  copy_dict["2015"] = int(copy_dict.pop("2015 Population"))
  copy_dict["2010"] = int(copy_dict.pop("2010 Population"))
  copy_dict["2000"] = int(copy_dict.pop("2000 Population"))
  copy_dict["1990"] = int(copy_dict.pop("1990 Population"))
  copy_dict["1980"] = int(copy_dict.pop("1980 Population"))
  copy_dict["1970"] = int(copy_dict.pop("1970 Population"))
  
  return copy_dict

def separate_values(data):
  labels = list(data.keys())
  values = []
  for i in data:
    values.append(data[i])
  return labels[::-1], values[::-1]

'''def bar_char(labels,values):
  fig, ax = plt.subplots()
  ax.bar(labels,values)
  plt.show()'''
      
if __name__ == "__main__":
  csv_dictionary = get_dictionary_from_csv("./app/data.csv")
  #print(csv_dictionary[0])
  print(type(csv_dictionary))
  pais = input("Qúe pais: ")
  new_dict = get_country(csv_dictionary,pais)
  #print(new_dict)
 # print()
  only_population = get_population(new_dict)
  #print(only_population)
  labels, values = separate_values(only_population)

  print(labels)
  print(values)
  charts.generate_bar_chart(labels,values)