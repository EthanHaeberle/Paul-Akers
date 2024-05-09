
from flask import Flask, request, render_template
from pdfminer.high_level import extract_text
import os

app = Flask(__name__)

UPLOAD_FOLDER = 'uploads'
if not os.path.exists(UPLOAD_FOLDER):
    os.makedirs(UPLOAD_FOLDER)

def count_word_occurrences(pdf_text, word):
    return pdf_text.lower().count(word.lower())

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/upload', methods=['POST'])
def upload_file():
    if 'file' not in request.files:
        return 'No file part'

    file = request.files['file']
    if file.filename == '':
        return 'No selected file'

    if file:
        filename = os.path.join(UPLOAD_FOLDER, file.filename)
        file.save(filename)
        
        # Execute your Python script on the uploaded file here
        with open(filename, 'rb') as f:
            pdf_text = extract_text(f)

def count_word_occurrences(file_path, word):
    count = 0
    with open(file_path, 'rb') as f:
        pdf_text = extract_text(f)
        count += pdf_text.lower().count(word.lower())
    return count


inch_occ = count_word_occurrences(L, "part number")
inch_and_quarter_occ = count_word_occurrences(L, "PIPE80PE1.25")
twoinch_occ = count_word_occurrences(L, "PIPE80PE2.00")
threeinch_occ = count_word_occurrences(L, "PIPE80PE3.00")
skotchkote_occ = count_word_occurrences(L, "part number")
tape_occ = count_word_occurrences(L, "TT33")
dope_occ = count_word_occurrences(L, "part number")
thirty_inch_nipple = count_word_occurrences(L, "ENIP300X3000")
air_fitting_kit = count_word_occurrences(L, "AIRFK-1")


if inch_occ >= 1:
    inch_by_close = count_word_occurrences(L, "part number")
    inch_by_two = count_word_occurrences(L, "part number")
    inch_by_three = count_word_occurrences(L, "part number")
    inch_by_four = count_word_occurrences(L, "part number")
    inch_by_six = count_word_occurrences(L, "part number")
    
    inch_elbows = count_word_occurrences(L, "part number")
    inch_tees = count_word_occurrences(L, "part number")
    inch_unions = count_word_occurrences(L, "part number")
    inch_couplings = count_word_occurrences(L, "part number")
    inch_ubolt = count_word_occurrences(L, "part number")
    
    inch_list = [inch_by_close, inch_by_two, inch_by_three, inch_by_four, inch_by_six,
            inch_elbows, inch_tees, inch_unions, inch_couplings, inch_ubolt]
   
    inch_word_list = ['inch_by_close', 'inch_by_two', 'inch_by_three', 
                      'inch_by_four', 'inch_by_six',
            'inch_elbows', 'inch_tees', 'inch_unions', 'inch_couplings', 'inch_ubolt' ]
    
    for word, count in zip(inch_word_list, inch_list):
        if count == 0:
            print(f'No occurrences of "{word}" found.')
        else:
            print(f'{count} occurrences of "{word}" found.')
   
else:   
    print(' 1" - This job does not include any 1" fittings or pipe')
    
if inch_and_quarter_occ >= 1:
    inch_and_quarter_by_close = count_word_occurrences(L, "SMNIP125X0000")
    inch_and_quarter_by_two = count_word_occurrences(L, "SMNIP125X0200")
    inch_and_quarter_by_three = count_word_occurrences(L, "SMNIP125X0300")
    inch_and_quarter_by_four = count_word_occurrences(L, "SMNIP125X0400")
    inch_and_quarter_by_six = count_word_occurrences(L, "SMNIP125X0600")
    inch_and_quarter_by_eight = count_word_occurrences(L, "SMNIP125X0800")
    inch_and_quarter_by_ten = count_word_occurrences(L, "SMNIP125X1000")
    inch_and_quarter_by_twelve = count_word_occurrences(L, "SMNIP125X1200")
    
    inch_and_quarter_elbows = count_word_occurrences(L, "EELL125")
    inch_and_quarter_tees = count_word_occurrences(L, "ETEE125")
    inch_and_quarter_unions = count_word_occurrences(L, "EUNN125")
    inch_and_quarter_coup = count_word_occurrences(L, "ECPL125")
    
    inch_and_quarter_ubolt = count_word_occurrences(L, "U-BOLT 125")
    
    inch_and_quarter_list = [inch_and_quarter_by_close, inch_and_quarter_by_two, 
                             inch_and_quarter_by_three, inch_and_quarter_by_four, inch_and_quarter_by_six ,
            inch_and_quarter_elbows , inch_and_quarter_tees , inch_and_quarter_unions, inch_and_quarter_coup,  inch_and_quarter_ubolt ]
    
    inch_and_quarter_word_list = ['inch_and_quarter_by_close', 'inch_and_quarter_by_two', 
                             'inch_and_quarter_by_three', 'inch_and_quarter_by_four', 'inch_and_quarter_by_six' ,
            'inch_and_quarter_elbows' , 'inch_and_quarter_tees' , 'inch_and_quarter_unions', 'inch_and_quarter_coup', ' inch_and_quarter_ubolt' ]
    
    for word, count in zip(inch_and_quarter_word_list, inch_and_quarter_list):
        if count == 0:
            print(f'No occurrences of "{word}" found.')
        else:
            print(f'{count} occurrences of "{word}" found.')
   
else:   
    print(' 1 1/4" - This job does not include any 1 1/4" fittings or pipe')  

if twoinch_occ >= 1:
    
    two_by_close = count_word_occurrences(L, "SMNIP200X0000")
    two_by_three = count_word_occurrences(L, "SMNIP200X0300")
    two_by_four = count_word_occurrences(L, "SMNIP200X0400")
    two_by_six = count_word_occurrences(L, "SMNIP200X0600")
    two_by_8 = count_word_occurrences(L, "SMNIP200X0800")
    two_by_10 = count_word_occurrences(L, "SMNIP200X1000")
    two_by_12 = count_word_occurrences(L, "SMNIP200X1200")
    
    two_inch_elbows = count_word_occurrences(L, "EELL200")
    two_inch_tees = count_word_occurrences(L, "ETEE200")
    two_inch_unions = count_word_occurrences(L, "EUNN200")
    two_inch_coup = count_word_occurrences(L, "ECPL200")
    two_inch_ubolt = count_word_occurrences(L, "U-BOLT 200")
    
    two_inch_list = [two_by_close, two_by_three,  two_by_four, two_by_six, two_by_8, two_by_10,
                      two_by_12, two_inch_elbows, two_inch_tees, two_inch_unions, two_inch_coup, two_inch_ubolt]
    
    two_inch_word_list = [ 'two_by_close' , 'two_by_three',  'two_four', 'two_by_six', 'two_by_8', 'two_by_10',
                      'two_by_12', 'two_inch_elbows', 'two_inch_tees', 'two_inch_unions', 'two_inch_coup', 'two_inch_ubolt' ]
    
    for word, count in zip(two_inch_word_list, two_inch_list):
        if count == 0:
            print(f'No occurrences of "{word}" found.')
        else:
            print(f'{count} occurrences of "{word}" found.')
   
else:   
    print(' 2" - This job does not include any 2" fittings or pipe')   
    
if threeinch_occ >= 1:
    
    three_by_three = count_word_occurrences(L, "SMNIP300X0300")
    three_by_four = count_word_occurrences(L, "SMNIP300X0400")
    three_by_six = count_word_occurrences(L, "SMNIP300X0600")
    three_by_8 = count_word_occurrences(L, "SMNIP300X0800")
    three_by_10 = count_word_occurrences(L, "SMNIP300X1000")
    three_by_12 = count_word_occurrences(L, "SMNIP300X1200")
    three_inch_elbows = count_word_occurrences(L, "EELL300")
    three_inch_tees = count_word_occurrences(L, "ETEE300")
    three_inch_unions = count_word_occurrences(L, "part number")
    three_inch_coup = count_word_occurrences(L, "ECPL300")
    three_inch_ubolt = count_word_occurrences(L, "U-BOLT 300")
    
    three_inch_list = [three_by_three,  three_by_four, three_by_six, three_by_8, three_by_10,
                      three_by_12, three_inch_elbows, three_inch_tees, three_inch_unions, three_inch_coup, three_inch_ubolt ]
    
    three_inch_word_list = ['three_by_three',  'three_four', 'three_by_six', 'three_by_8', 'three_by_10',
                      'three_by_12', 'three_inch_elbows', 'three_inch_tees', 'three_inch_unions', 'three_inch_coup', 'three_inch_ubolt' ]
    
    for word, count in zip(three_inch_word_list, three_inch_list):
        if count == 0:
            print(f'No occurrences of "{word}" found.')
        else:
            print(f'{count} occurrences of "{word}" found.')
   
else:   
    print(' 3" - This job does not include any 3" fittings or pipe')   
    
if tape_occ == 0 :
    print("This job does not contain tape was that intentional?")
if air_fitting_kit == 0 :
    print("This job does not contain an air fitting kit, was this intentional? ")
if thirty_inch_nipple == 0 :
    print('This job does not contain a 30" nipple, was that intentional' )
            

if __name__ == '__main__':
    app.run(debug=True)
