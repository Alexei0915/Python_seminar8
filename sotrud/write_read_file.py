def write_file(data):
    with open('database.csv','a') as file:
        file.writelines(data)
          
def read_file():
    with open('database.csv','r') as file:
        return file.readlines()
    