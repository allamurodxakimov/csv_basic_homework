#Define function,Get coloumn names from a csv file
from csv import reader
def get_column_names(data):
    """ 
    Get column names from a csv file
    Parameters:
        data(str): csv file
    Returns:
        column_names: list of column names
    """
    f=open("data.csv")
    r=reader(f)
    ls=[]
    for i in r:
        ls.append(i)
    return ls[0]
print(get_column_names("data.csv"))
    
# Read the csv fileg