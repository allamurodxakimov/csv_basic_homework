from csv import reader
def find_number_of_columns(data):
    """
    Find the number of columns in CSV.
    Args:
        data(str): csv file.
    Return:
        int: Number of columns.
    """
    f=open("data.csv")
    row=reader(f)
    ls=[]
    for i in row:
        ls.append(i[0])
    return len(ls)
print(find_number_of_columns("data,csv"))

# Read the csv file