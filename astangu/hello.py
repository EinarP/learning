# -----------------------------------------------------------------------------
# File handing with base python only:
# https://www.w3schools.com/python/python_file_handling.asp
# -----------------------------------------------------------------------------

# Open title_basics.csv file (UTF-8 encoding)
print("Here I am, opening the file!")
# input_file = open("data/title_basics.csv", encoding="utf8")
input_file = open("data\\title_basics.csv", encoding="utf8")

# input_file = open(
#    "C:/Users/einar/OneDrive/Development/astangu/data/title_basics.csv",
#    encoding="utf8"
#)

# Count and print out the number of lines in the file
print("Number of lines in the file:", input_file)

# Print out and write to title_basics_head.csv file first 10 lines
print("Now writing first lines to the output file")

# Close the files
print("Closing both files")

print("Ilmar Põder aka \"poro\"\t387\\a12\nAksel Roos aka \"axl\"\t456\\b13")
