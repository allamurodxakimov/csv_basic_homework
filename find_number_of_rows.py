from csv import reader
def find_number_of_rows(data):
    """
    Find the number of rows in CSV.
    Args:
        data(str): csv file.
    Return:
        int: Number of rows.
    """
    f=open("data.csv")
    l=reader(f)
    for i in l:
        print(len(i))
print(find_number_of_rows("data.csv"))
