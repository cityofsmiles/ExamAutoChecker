# Exam Auto-Checker App for Teachers
Automatically check, save, and record student answers obtained from any messaging app.

[pic](https://github.com/cityofsmiles/ExamAutoChecker/blob/assets/autochecker.png)

## Usage
1. Create your worksheet, quiz, or test along with the answer key.
2. Send your worksheet, quiz, or test to your students using any messaging app and let them send you their answers. 
3. Copy their answers from the chat app and paste the answers in the Exam Auto-Checker.
4. In the app, enter the type of activity you want to check. For example: Activity#1, Quiz#1, or Test#1.
5. Click Browse to find the folder where you want to save the outputs and results.
6. Click Browse to find the answer key for the activity. 
7. Click Submit.
8. If there is error in the checking, edit the original student's input. If there is no error, click Save.
9. After clicking Save, the student's output is automatically checked, saved, and recorded in the folder you chose. The scores are recorded in a csv file which you can open using Microsoft Excel or LibreOffice Calc.

_Note:_ the students' input **SHOULD** look like the following:

Bacolod, Jonathan  (Surname, Firstname. The comma is required.)    
8-Hubble           (Grade-Section)  
B1                 (Student code. Optional but strongly recommended. Use B1, B2, etc. for male students and G1, G2, etc. for female students.) 
                         
1. a               (The dot is required. The answers can be any letter, word, or phrase.)  
2. b   (Don't indent the numbers.) 
3. c  
...  
The space between the student code and the first answer is required. Please see the [sample student answer](https://github.com/cityofsmiles/ExamAutoChecker/blob/master/sample-student-answer.txt). 

_Note:_ The answer key should be a simple text file that contains only the correct answers. For example:

1. True
2. a
3. b
4. Perfect Square Trinomial
5. (x-y)

Please see the [sample  answer key](https://github.com/cityofsmiles/ExamAutoChecker/blob/master/sample-answer-key.txt). 

## Installation
* For Windows, click [here](https://github.com/cityofsmiles/ExamAutoChecker/raw/assets/ExamAutoChecker.exe) to download the executable file. Just double click the file to launch the app. Windows will warn you that this file can not be trusted and will discourage you to run it. That is normal. Just click OK to run the program.
* For Linux, click [here](https://github.com/cityofsmiles/ExamAutoChecker/raw/assets/ExamAutoChecker) to download the executable file. Just double click the file to launch the app.
* For Android phones with the architecture arm64-v8a, click [here](https://github.com/cityofsmiles/ExamAutoChecker/raw/assets/ExamAutoChecker-0.1-arm64-v8a-debug.apk) to download the apk file. Other architectures will be supported in the future. If you don't know your phone's architecture, you may install the [CPU Info](https://github.com/kamgurgul/cpu-info) app.

## How to report issues
If you see bugs in the app, please [open a new issue](https://github.com/cityofsmiles/ExamAutoChecker/issues). 

