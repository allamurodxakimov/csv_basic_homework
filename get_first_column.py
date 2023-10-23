from csv import reader
def get_first_column(data):
    """
    Get the first column from a CSV file.
    Args:
        data(str): csv file.
    Return:
        list: First column.
    """
    f=open("data.csv")
    data=reader(f)
    for i in data:
        print(i[0])
print(get_first_column("data.csv"))
    
# Read the csv file