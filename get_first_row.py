from csv import reader
def get_first_row(data):   
   """
   Get the first row from a CSV file.
    Args:
        data(str): csv file.
    Return:
        list: First row.
    """
   f=open("data.csv")
   data=reader(f)
   ls=[]
   for i in data:
        ls.append(i)
   return ls[1]
print(get_first_row("data.csv"))
# Read the csv file