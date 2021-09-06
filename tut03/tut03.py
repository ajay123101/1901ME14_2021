import os
 
 
def write_to_file(data, file_name):
    """Writes list of lists into CSV file"""
    with open(file_name, "w") as f:
        for row in data:
            f.write("\n".join((",".join(row))))
 
 
def output_by_subject():
    roll = {}
    DIRECTORY = "output_by_subject"
 
    with open("regtable_old.csv", "r") as f:
        for row in f:
            row = row.strip().split(",")
            rollno, register_sem, _, subno, _, _, _, _, sub_type = row
            if rollno not in roll:
                roll[rollno] = []
            roll[rollno].append([rollno, register_sem, subno, sub_type])
 
    if not os.path.exists(DIRECTORY):
        os.makedirs(DIRECTORY)
 
    for rollno in roll:
        write_to_file(roll[rollno], os.path.join(DIRECTORY, rollno + ".csv"))
 
 
def output_individual_roll():
    subject = {}
    DIRECTORY = "output_individual_roll"
 
    with open("regtable_old.csv", "r") as f:
        for row in f:
            row = row.strip().split(",")
            rollno, register_sem, _, subno, _, _, _, _, sub_type = row
            if subno not in subject:
                subject[subno] = []
            subject[subno].append([rollno, register_sem, subno, sub_type])
 
    if not os.path.exists(DIRECTORY):
        os.makedirs(DIRECTORY)
 
    for subno in subject:
        write_to_file(subject[subno], os.path.join(DIRECTORY, subno + ".csv"))
 
 

output_by_subject()
output_individual_roll()