import csv
import os

def previous_vote(id_num):
    """
    Checks if the featured ID has already been used.
    
    A message will be displayed if the ID is found, or None is returned if things are okay.
    
    """
    try:
        with open('data.csv', 'r', newline='') as file:
            reader = csv.reader(file)
            next(reader, None)
            for row in reader:
                for number in row:
                    if str(id_num) == row[0]:
                        return "Can not enter a previously saved ID number."
        
    except FileNotFoundError:
        return "An error occurred"
    return None 
    
def new_vote(id_num, vote_choice):
    """The vote will be saved to the file. A header will get added if the file is new."""
    try:
        file_existence = os.path.exists("data.csv") """AI-assisted"""
        with open('data.csv', 'a', newline='') as file:
            writer = csv.writer(file)
            if not file_existence:
                writer.writerow(['ID', 'Vote'])
            writer.writerow([id_num, vote_choice])
                
        return f'Your Vote is: {vote_choice}'
    
    except:
        return "An error occurred while saving the vote."