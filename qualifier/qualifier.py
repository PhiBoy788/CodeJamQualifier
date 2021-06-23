from typing import Any, List, Optional


def make_table(rows: List[List[Any]], labels: Optional[List[Any]] = None, centered: bool = False) -> str:
    """
    :param rows: 2D list containing objects that have a single-line representation (via `str`).
    All rows must be of the same length.
    :param labels: List containing the column labels. If present, the length must equal to that of each row.
    :param centered: If the items should be aligned to the center, else they are left aligned.
    :return: A table representing the rows passed in.
    """
    ...
    longest_object = longest_item(rows)
    if labels:
        longest_label = longest_item(labels)
        if longest_label > longest_object:
            longest_object = longest_label

    #longest_object += 2

    #print("┌" + ("─" * (longest_object + 2)) + "┐")

    for i in range(len(rows)):
        for j in range(len(rows[i])):
            item = str(rows[i][j])
            print("|" + " " + item + (" " * (longest_object + 1 - len(item))), end="")
        print("|")
    
    
    #print("└" + ("─" * (longest_object + 2)) + "┘")
    
#Counts and returns both the number of rows and columns within a 2D array, respectively.
#Could use logic if a label is not included to give it a blank value or throw an error?
def array_counter(row_list):
    height = len(row_list)
    width = len(row_list[0])
    return height, width

#Counts longest item within 2D array, can be used for labels as well.
def longest_item(row_list):
    longest = 0
    for row in row_list:
        for item in row:
            item_string = str(item)
            current = len(item_string)
            if current > longest:
                longest = current
    return longest

#Takes the height and width of the table and prints it accordingly
#def printer(row_list,height,width,longest):
    #longest = longest + 2
    #for row in list


#DEBUG CODE
rows=[["Lemon", 18_3285, "Owner"],["Sebastiaan", 18_3285.1, "Owner"],["KutieKatj", 15_000, "Admin"],["Jake", "MoreThanU", "Helper"],["Joe", -12, "Idk Tbh"]]

make_table(rows)

