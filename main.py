from kivy.app import App
from kivy.lang import Builder
from kivy.uix.screenmanager import ScreenManager, Screen
from kivy.uix.label import Label
from kivy.properties import ObjectProperty
from kivy.uix.textinput import TextInput
import os
import examautochecker-module as ex
from android.permissions import request_permissions, Permission
request_permissions([Permission.READ_EXTERNAL_STORAGE, Permission.WRITE_EXTERNAL_STORAGE])
from android.storage import primary_external_storage_path
primary_ext_storage = primary_external_storage_path()


Builder.load_file('examautochecker.kv')


class Manager(ScreenManager):
    pass


class ScreenOne(Screen):    
    def save_key(self, answer_key):
        os.chdir(output_dir)
        file_ans_key = 'answer-key.txt'
        fob = open(file_ans_key,'w')
        fob.write(answer_key)
        fob.close()
    
    def get_assessment_type(self):
        global assessment_type_str
        assessment_type_str = self.ids.assessment_type_id.text    
        
    
class ScreenTwo(Screen):
    def on_enter(self, *args):
        self.outdir_label_id.text = "Output Folder of " + assessment_type_str + ": " + output_dir
    
        
    def update_values(self):
        self.ids.checked_items_id.text = ExamAutoChecker.get_running_app().checked_items_results
        
    def clear_screens(self):
        self.ids.student_input_id.text = ""
        self.ids.checked_items_id.text = ""


class ExamAutoChecker(App):
    def build(self):
        self.title = "Exam Auto-Checker"
        global output_dir
        output_dir = os.path.join(primary_ext_storage, "ExamAutoChecker")
        if os.path.isdir(output_dir) == False:
            os.makedirs(output_dir)
        return Manager()

    
    def check_now(self, student_input):
        assessment_type = assessment_type_str
        file_ans_key = 'answer-key.txt'
        self.checked_items_results, self.temp_file, self.student_code, self.student_lastname, self.section_output_dir, self.output_file, self.student_input, self.score, self.total_items = ex.check_answers(output_dir, assessment_type, file_ans_key, student_input)
        
        
    def save_results(self):
        temp_file = ExamAutoChecker.get_running_app().temp_file
        student_code = ExamAutoChecker.get_running_app().student_code
        student_lastname = ExamAutoChecker.get_running_app().student_lastname
        section_output_dir = ExamAutoChecker.get_running_app().section_output_dir
        output_file = ExamAutoChecker.get_running_app().output_file
        assessment_type = assessment_type_str
        student_input = ExamAutoChecker.get_running_app().student_input
        score = ExamAutoChecker.get_running_app().score
        total_items = ExamAutoChecker.get_running_app().total_items
        ex.save_results(temp_file, output_dir, student_code, student_lastname, section_output_dir, output_file, assessment_type, student_input, score, total_items)
        
    
        
app = ExamAutoChecker()

app.run()










