from typing import Any, List, Optional
import math

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

    #Creates an Array of the longest string in both the columns of the given rows list and labels(if given)
    longest_object = longest_item(rows,labels)

    #Creates a boolean to handle table printing with or without labels.
    if labels:
        labels_bool = True
    else:
        labels_bool = False
    
    #Prints the top line of the table, spacing characters according 
    #to the length of the longest string in the column
    print("┌", sep="", end="")
    for i in range(len(longest_object)):
        offset = 2
        print("─" * (longest_object[i] + 2), end="")
        if i < longest_object[i] and i < len(longest_object) - 1:
            print("┬", end="", sep="")
            offset += i + i
    print("┐", sep="")

    #Prints the middle portion of the table and formats it with or without labels
    for i in range(len(rows)):
        for j in range(len(rows[i])):
            item = str(rows[i][j])
            item_length = len(item)
            item_left = item_length / 2
            item_right = item_length / 2
            spacing_left = longest_object[j] / 2
            spacing_right = longest_object[j] / 2

            if type(item_left) is float:
                item_left = math.floor(item_left)
                item_right = math.ceil(item_right)

            if type(spacing_left) is float:
                spacing_left = math.floor(spacing_left)
                spacing_right = math.ceil(spacing_right)

            if centered == False:
                print('│' + " " + item + (" " * (longest_object[j] + 1 - item_length)), end="", sep = "")
            else:
                print('│' + (" " * (spacing_left + 1 - item_left)) + item + (" " * (spacing_right + 1 - item_right)), end="", sep = "")                
        print('│')
        if labels_bool:
            print("├", sep = "", end="")
            for i in range(len(longest_object)):
                print("─" * (longest_object[i] + 2), end="")
                if i < longest_object[i] and i < len(longest_object) - 1:
                    print("┼", end="", sep="")
            labels_bool = False
            print("┤", sep="")
    
    #Prints bottom line of table using similar logic as the top line
    #TODO possible refactor to consolidate into one function? 
    print("└", sep="", end="")
    for i in range(len(longest_object)):
        print("─" * (longest_object[i] + 2), end="")
        if i < longest_object[i] and i < len(longest_object) - 1:
            print("┴", end="", sep="")
    print("┘", sep="")


#Returns an array with the value of the longest string in each column of a given 2D array
def longest_item(row_list, labels = None):
    longest_array = []
    if labels:
        row_list.insert(0,labels)
    for i in range(len(row_list[0])):
        longest = 0
        for j in range(len(row_list)):
            pass
            item_string = str(row_list[j][i])
            current = len(item_string)
            if current > longest:
                longest = current
        longest_array.append(longest)
    return longest_array


#DEBUG CODE
#rows=[["Lemon", 18_3285, "Owner"],["Sebastiaan", 18_3285.1, "Owner"],["KutieKatj", 15_000, "Admin"],["Jake", "MoreThanU", "Helper"],["Joe", -12, "Idk Tbh"]]
#labels=["User", "Messages", "Role"]

#Centered
#rows=[["Ducky Yellow", 3],["Ducky Dave", 12],["Ducky Tube", 7],["Ducky Lemon", 1]]
#labels=["Name", "Duckiness"]
#centered=True


#make_table(rows, labels, True)