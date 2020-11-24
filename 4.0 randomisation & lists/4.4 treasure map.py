# 🚨 Don't change the code below 👇
row1 = ["⬜️","⬜️","⬜️"]
row2 = ["⬜️","⬜️","⬜️"]
row3 = ["⬜️","⬜️","⬜️"]
map = [row1, row2, row3]
print(f"{row1}\n{row2}\n{row3}")
position = input("Where do you want to put the treasure? ")
# 🚨 Don't change the code above 👆

#Write your code below this row 👇

column = int(position[0])
row = int(position[1])

selected_row = map[row - 1]
selected_row[column - 1] = "X"


# if column == "1" and row == "1":
#   map[0][0] = "X"
# if column == "1" and row == "2":
#   map[1][0] = "X"
# if column == "1" and row == "3":
#   map[2][0] = "X"

# if column == "2" and row == "1":
#   map[0][1] = "X"
# if column == "2" and row == "2":
#   map[1][1] = "X"
# if column == "2" and row == "3":
#   map[2][1] = "X"

# if column == "3" and row == "1":
#   map[0][2] = "X"
# if column == "3" and row == "2":
#   map[1][2] = "X"
# if column == "3" and row == "3":
#   map[2][2] = "X"


#Write your code above this row 👆

# 🚨 Don't change the code below 👇
print(f"{row1}\n{row2}\n{row3}")