import PyPDF2
import string

pdf_file = open('./A1GermanWords.pdf', 'rb')
pdf_reader = PyPDF2.PdfReader(pdf_file)

word_list = []
for page_num in range(len(pdf_reader.pages)):
    page = pdf_reader.pages[page_num]
    words = page.extract_text().split()
    for word in words:
        #''.join(e for e in word if e.isalnum())
        #import re
        #re.sub('\W+','', word)
        word = word.strip(string.punctuation)
        if not word.isupper() and word.isalpha() and len(word)>1: # avoid abbreviations which are all upper case
            word_list.append(word.lower())

pdf_file.close()

word_set_A1 = set(word_list)

with open('./goethe_German_Word_List_A1.txt', 'w',encoding='UTF-8') as output_file:
    for word in word_set_A1:
        output_file.write(word + '\n')


pdf_file = open('./A2GermanWords.pdf', 'rb')
pdf_reader = PyPDF2.PdfReader(pdf_file)

word_list_A2 = []
for page_num in range(len(pdf_reader.pages)):
    page = pdf_reader.pages[page_num]
    words = page.extract_text().split()
    for word in words:
        #''.join(e for e in word if e.isalnum())
        #import re
        #re.sub('\W+','', word)
        word = word.strip(string.punctuation)
        if not word.isupper() and word.isalpha() and len(word)>1: # avoid abbreviations which are all upper case
            if not word.lower() in word_set_A1:
                word_list_A2.append(word.lower())

pdf_file.close()

word_set_A2 = set(word_list_A2)

with open('./goethe_German_Word_List_A2.txt', 'w',encoding='UTF-8') as output_file:
    for word in word_set_A2:
        output_file.write(word + '\n')