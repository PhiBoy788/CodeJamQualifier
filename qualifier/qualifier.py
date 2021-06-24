from typing import Any, List, Optional
#TODO FORMAT TABLE WITH CONNECTING CHARACTERS
#TODO CREATE LOGIC FOR CENTERED BOOL

def make_table(rows: List[List[Any]], labels: Optional[List[Any]] = None, centered: bool = False) -> str:
    """
    :param rows: 2D list containing objects that have a single-line representation (via `str`).
    All rows must be of the same length.
    :param labels: List containing the column labels. If present, the length must equal to that of each row.
    :param centered: If the items should be aligned to the center, else they are left aligned.
    :return: A table representing the rows passed in.
    """
    ...
    longest_object = longest_item(rows,labels)

    print("Longest Object:", longest_object)
    if labels:
        labels_bool = True
    
    width = sum(longest_object) + 2 + len(rows)

    print("Width = " + str(width))
    print("┌", sep="", end="")
    for i in range(len(longest_object)):
        print("─" * ((longest_object[i] + len(rows[i]) - 1)), end="")
        if i < 2:
            print("┬", end="", sep="")
    print("┐", sep="")




    for i in range(len(rows)):
        for j in range(len(rows[i])):
            item = str(rows[i][j])
            print('│' + " " + item + (" " * (longest_object[j] + 1 - len(item))), end="", sep = "")
        print('│')
        if labels_bool:
            print("├", sep = "", end="")
            for i in range(len(longest_object)):
                print("─" * ((longest_object[i] + len(rows[i]) - 1)), end="")
                if i < 2:
                    print("┼", end="", sep="")
            labels_bool = False
            print("┤", sep="")
    
    
    print("└", sep="", end="")
    for i in range(len(longest_object)):
        print("─" * ((longest_object[i] + len(rows[i]) - 1)), end="")
        if i < 2:
            print("┴", end="", sep="")
    print("┘", sep="")
    
#Counts and returns both the number of rows and columns within a 2D array, respectively.
#Could use logic if a label is not included to give it a blank value or throw an error?
def array_counter(row_list):
    height = len(row_list)
    width = len(row_list[0])
    return height, width

#Returns an array with the value of the longest string in each column
def longest_item(row_list, labels = None):
    longest_array = []
    if labels:
        row_list.insert(0,labels)
    #print(len(row_list))
    for i in range(len(row_list[0])):
        longest = 0
        for j in range(len(row_list)):
            pass
            item_string = str(row_list[j][i])
            #print(item_string)
            current = len(item_string)
            if current > longest:
                longest = current
        longest_array.append(longest)
        #print("Done with Column")
    return longest_array

#Takes the height and width of the table and prints it accordingly
#def printer(row_list,height,width,longest):
    #longest = longest + 2
    #for row in list


#DEBUG CODE
rows=[["Lemon", 18_3285, "Owner"],["Sebastiaan", 18_3285.1, "Owner"],["KutieKatj", 15_000, "Admin"],["Jake", "MoreThanU", "Helper"],["Joe", -12, "Idk Tbh"]]
labels=["User", "Messages", "Role"]


make_table(rows, labels)