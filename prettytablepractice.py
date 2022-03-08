import prettytable
from prettytable import PrettyTable

PrettyTable()
table = PrettyTable()
table.field_names = ["Pokemon", "Type",]
table.add_rows(
[
["Bulbasaur" , "Grass"],
["Pikachu", "Electric"],
["Squirtle", "Water"],
["Charmandar", "Fire"]
])

table.align = "l"


print(table)
