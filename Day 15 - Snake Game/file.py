# with open("high_score") as file:
#     contents = file.read()
#     print(contents)

with open("high_score", mode="a") as file:
    file.write("\nNew Text.")
