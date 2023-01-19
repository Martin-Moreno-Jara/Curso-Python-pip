import matplotlib.pyplot as plt

def generate_bar_chart(labels,values,name):
  fig, ax = plt.subplots()
  ax.bar(labels,values)
  plt.savefig(f"./img/{name}.png")

def generate_pie_chart(labels,values):
  fig, ax = plt.subplots()
  ax.pie(values,labels=labels)
  ax.axis("equal")
  plt.savefig("./img/pie.png")

if __name__ == "__main__":
  labels = ["A","B","C","D"]
  values = [67,80,45,100]
  #generate_bar_chart(["A","Z"],[4,6])
  generate_pie_chart(labels,values)