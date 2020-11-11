"""
create by: a5892731
date: 2020-11-11

V2.0

"""

#import openpyxl
#import os
#from time import sleep
from os import listdir, getcwd, chdir, walk
from openpyxl import Workbook

wb = Workbook()
ws = wb.active



class Log_Folder:
    list_of_files = []
    list_of_folders = []
    local_ardes = ''


# ----------------------------------------------------------------
def Create_xml_file():

    ws.title = "Arkusz 1"
    columns = ['A', 'B']
    for column in range(len(columns)):
        ws.column_dimensions[columns[column]].width = 80
    ws.append(('Lokalizacja folderu docelowego:', getcwd()))
    ws.append(('-----------------', '-----------------'))
    ws.append(('Plik:', ('Folder: ' + '> > >')))
    #ws.cell(row=3, column=max(bufor_column)+1, value='Pełny adres:')


def printing(list1=[], adres = ''):


    if list1 == []:
        return False

    for i in range(len(list1)):

            if list1[i] is not None:
                ws.append((list1[i] , adres,))


def Logger_machine(main_adres):


    list_of_files = []
    list_of_folders = []
    local_ardes = ''
    list_of_objects = listdir()

    if list_of_folders != None:




        for path, subfiles, files in walk(main_adres):

            if len(files):
                printing(files, path)



# ----------------------------------------------------PROGRAM------------------------------------------------------


print('*' * 70)
print('Wpisz poniżej adres folderu z plikami których chcesz zrobić liste')
print('*' * 70)
main_adres = input('Podaj adres: ')
print('*' * 70)


program_adres = getcwd()


print('Źródło listy: ' + main_adres)
print('*' * 70)

chdir(main_adres)

Create_xml_file()



Logger_machine(main_adres)


chdir(program_adres)
wb.save('LIST OF FILES.xlsx')
wb.close()
print('end of files')
print('')
input('press enter to end program: ')






