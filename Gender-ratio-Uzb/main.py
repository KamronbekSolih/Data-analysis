import matplotlib.pyplot as  plt
from ExcelConvert import men,women

x = men.values()
y = women.values() 
years = men.keys()

plt.plot(years,x,label = "Men")
plt.plot(years,y,label = "Women")
plt.title("Men and Women births of Uzbekistan")
plt.xlabel("Years")
plt.ylabel("Number of births")
plt.legend()
plt.show()