# read the first line of sample letter  and put as line 1 (suse read line once)
with open("../input/letters/starting_letter.txt","r") as f:
    letter= f.read() #read starting letter

# read the name and put on name variable  (use read line with the loop)
with open("../input/names/invited_names.txt","r") as f: # open in read only mode and close it automaticaly
    names =f.readlines() #create a lits of names from file and add extra line after it
    for name in names: # iterate over the name
        striped_name = name.strip() # stripe the name ( avoid new line(space) b4 and after string)
        inserted=letter.replace("[name]", f'\"{striped_name}\"') # replace the name part with picked one
        file_name = f"./redy_to_send/letter_for_{striped_name}" # file name for each letter
        new_f=open(file_name , "w") # open in write if doesn't exit mode
        new_f.write(inserted)# create new file with given file name 
        print(inserted)