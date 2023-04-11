# -----------------------------------------------------------------------------
# File handing with base python only:
# https://www.w3schools.com/python/python_file_handling.asp
# -----------------------------------------------------------------------------

# Open title_basics.csv file (UTF-8 encoding)
f = open("data/title_basics.csv", encoding="utf8")

# Count and print out the number of lines in the file
line_count = 0
for x in f:
  line_count += 1
  
print("Number of lines:", line_count)

# Print out and write to title_basics_head.csv file first 10 lines
fw = open("title_basics_head.csv", "w")

f.seek(0)
for index in range(0,10):
    line = f.readline()
    print(line)
    fw.write(line)

# Close the files
fw.close()
f.close()