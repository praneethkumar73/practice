cities = """ The city of love Paris
    The city of dreams Mumbai
    The golden city Amritsar"""

# {'Paris':'The city of love','Mumbai':'The city of dreams','Amritsar':'The golden city'}
output={}
for city in cities.split("\n"):
    key = city.strip().split(" ")[-1]
    value = " ".join(city.strip().split(" ")[0:-1])
    output[key] = value
    print(output)
