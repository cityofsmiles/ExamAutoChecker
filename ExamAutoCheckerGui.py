#!/usr/bin/env python
 

import PySimpleGUI as sg      
import os
import examautochecker_module as ex

def get_input():     
    left_col = [[sg.Text('Outputs Folder:', size=(16, 1)), sg.InputText(key='OUTDIR')],[sg.Text('Assessment Type:', size=(16, 1)), sg.InputText(key='ASSESSMENT')],
                [sg.Text('Answer Key:', size=(16, 1)), sg.InputText(key='ANSKEY')],
                [sg.Text('Enter the student\'s infos and answers.')],      
                 [sg.Multiline(size=(60,20), key='ANSWERS', autoscroll=True)],      
                 [sg.Submit(), sg.Save(), sg.Exit()]]   
    
    right_col = [[sg.Text('Results:')],      
                 [sg.Multiline(size=(40,25), key='-OUTPUT-', autoscroll=True)]]

    layout = [[sg.Column(left_col, element_justification='c'), sg.VSeperator(),sg.Column(right_col, element_justification='c')]]
    
    window = sg.Window('Exam Auto-Checker', layout, resizable=True)    

    while True:
        event, values = window.read()  
        if event in (None, "Exit"):
            break
        if event == "Submit":
            output_dir = values['OUTDIR']
            assessment_type = values['ASSESSMENT']
            ans_key = values['ANSKEY']
            student_input = values['ANSWERS']
            checked_items, temp_file, student_code, student_lastname, section_output_dir, output_file, student_input, score, total_items = ex.check_answers(output_dir, assessment_type, ans_key, student_input)
            window['-OUTPUT-'].update(checked_items)
        
        if event == "Save":
            ex.save_results(temp_file, output_dir, student_code, student_lastname, section_output_dir, output_file, assessment_type, student_input, score, total_items)
            window['-OUTPUT-'].update('')
            window['ANSWERS'].update('')
            

if __name__ == '__main__':
    get_input()
