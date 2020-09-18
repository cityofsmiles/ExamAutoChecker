import os
from csv import writer
import io
import re

def save_student_input(output_dir, student_input):   
    os.chdir(output_dir)
    temp_file = "temp.txt"
    f= open(temp_file,"w+")
    f.write(student_input)
    f.close()
    return temp_file


def parse_infos(temp_file, output_dir):
    os.chdir(output_dir)
    f=open(temp_file, "r")
    student_name = str(f.readlines(1))
    student_lastname, student_firstname = student_name.split(',')
    student_lastname = student_lastname[2:]
    student_firstname = student_firstname[1:-4]
    section = str(f.readlines(2))
    section = section[2:-4]
    section = section.replace(" ", "")
    student_code = str(f.readlines(3))
    student_code = student_code.replace(" ", "")
    student_code = student_code.replace("[", "")
    student_code = student_code.replace("'", "")
    student_code = student_code.replace(",", "")
    student_code = student_code.replace("]", "")
    student_code = student_code.replace('\\', "")
    student_code = student_code.replace('n', "")
    student_code = student_code.rstrip()
    return student_code, student_lastname, student_firstname, section


def create_output_file(output_dir, student_code, student_lastname, student_firstname, section, assessment_type):
    output_file = student_code + "-" + student_lastname + ".txt"
    section_output_dir = os.path.join(output_dir, section, assessment_type)
    if os.path.isdir(section_output_dir) == False:
        os.makedirs(section_output_dir)
    os.chdir(section_output_dir)
    f= open(output_file,"w+")
    f.write(student_lastname + ", " + student_firstname + "\n")
    f.write(section + "\n")
    f.write(student_code + "\n")
    f.write(assessment_type + "\n\n")
    f.close()
    return section_output_dir, output_file


def simplecount(filename):
    lines = 0
    for line in open(filename):
        lines += 1
    return lines


def check_items(temp_file, ans_key, output_dir, assessment_type, section_output_dir, output_file):  
    os.chdir(output_dir)
    num_lines = simplecount(temp_file)
    file_temp = open(temp_file)
    try:
        answer_file = open(ans_key)
    except FileNotFoundError:
        print("Answer key does not exist!")
    all_lines = file_temp.readlines()
    answer_lines = answer_file.readlines()
    score = 0
    mistake = 0
    os.chdir(section_output_dir)
    f = io.open(output_file, "a+", encoding='utf8')
    for i in range(5, num_lines+1):
        j = i - 4
        item = all_lines[i - 1]
        if "." in item:
            item_num, item_answer = item.split('.')
        item_answer = item_answer.strip()
        item_answer = re.sub(' +', ' ', item_answer)
        item_answer = item_answer.lower()
        answer = answer_lines[j - 1]
        if "." in answer:
            answer_num, correct_answer = answer.split('.')
        correct_answer = correct_answer.strip()
        correct_answer = re.sub(' +', ' ', correct_answer)
        correct_answer = correct_answer.lower()
        
        if item_answer == correct_answer:
            comment = "Correct" 
            score += 1
        else:
            comment = "Wrong"  
            mistake += 1
        
        f.write(item_num + ". " + item_answer + " (" + correct_answer + ") " + comment + "\n")
    total_items = score + mistake
    f.write("\n\nScore = " + str(score) + "\n")
    f.write("Mistake = " + str(mistake) + "\n")
    f.write("Total = " + str(total_items))
    return score, total_items


def read_output(section_output_dir, output_file):
    os.chdir(section_output_dir)
    with io.open(output_file,'r',encoding='utf8') as f:
        checked_items = f.read()
    return checked_items


def clean_up(temp_file, output_dir, student_code, student_lastname, section_output_dir, output_file, assessment_type, score):
    os.chdir(section_output_dir)
    new_output_file = student_code + "-" + student_lastname + "-" + str(score) + ".txt"
    os.rename(output_file, new_output_file) 
    os.chdir(output_dir)
    os.remove(temp_file)
    return new_output_file


def append_list_as_row(file_name, list_of_elem):
    # Open file in append mode
    with open(file_name, 'a+', newline='') as write_obj:
        # Create a writer object from csv module
        csv_writer = writer(write_obj)
        # Add contents of list as last row in the csv file
        csv_writer.writerow(list_of_elem)


def record_score(section_output_dir, assessment_type, student_code, score, total_items):
    record_csv = assessment_type + '-Scores.csv'
    os.chdir(section_output_dir)
    try:
        f = open(record_csv)
    except IOError:
        f= open(record_csv,"w")
        f.write("Code," + str(total_items) + "\n")
        f.close()
    finally:
        f.close()
    row_contents = [student_code, score]
    append_list_as_row(record_csv, row_contents)
    


def check_answers(output_dir, assessment_type, ans_key, student_input):
    temp_file = save_student_input(output_dir, student_input)
    
    student_code, student_lastname, student_firstname, section = parse_infos(temp_file, output_dir)
    
    section_output_dir, output_file = create_output_file(output_dir, student_code, student_lastname, student_firstname, section, assessment_type)
    
    score, total_items = check_items(temp_file, ans_key, output_dir, assessment_type, section_output_dir, output_file)

    checked_items = read_output(section_output_dir, output_file)
    
    return checked_items, temp_file, student_code, student_lastname, section_output_dir, output_file, student_input, score, total_items
    
            
def save_results(temp_file, output_dir, student_code, student_lastname, section_output_dir, output_file, assessment_type, student_input, score, total_items):
    
    clean_up(temp_file, output_dir, student_code, student_lastname, section_output_dir, output_file, assessment_type, score)
    
    record_score(section_output_dir, assessment_type, student_code, score, total_items)
    











