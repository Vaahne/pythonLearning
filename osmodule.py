import os
import datetime
file_name = "novel.txt"

# if os.path.exists(file_name):
#     os.remove(file_name)
# else:
#     print("File not found")

dir = "test1"
# os.mkdir(dir) # to make a directory
# os.chdir(dir) # to change to a directory
# os.getcwd()   # to know the current working directory
# os.rmdir(dir) # to remove directory
# os.listdir(dir) # to list the content inside dir


for name in os.listdir(dir):
    fullname = os.path.join(dir, name) #it creates a string containing cross-platform concatenated directories.
    if os.path.isdir(fullname):
        print("{} is a directory".format(fullname))
    else:
        print("{} is a file".format(fullname))

print("/n ====Time stamp ====\n")
timestamp = os.path.getmtime(file_name)
print(datetime.datetime.fromtimestamp(timestamp))


print("\n ===absolute and relative path ===\n")
import os
def parent_directory():
  # Create a relative path to the parent 
  # of the current working directory 
  relative_parent = os.path.join(os.getcwd(), os.pardir)

  # Return the absolute path of the parent directory
  return os.path.abspath(relative_parent)

print(parent_directory())