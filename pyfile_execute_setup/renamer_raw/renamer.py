import ctypes  
import os
path = r'inputs'
files = os.listdir(path)

def renamer_foo(files, path):
    for index, file in enumerate(files):
        if file == None:
            print('There is no file in inputs folder.')
        else:
            os.rename(os.path.join(path, file), os.path.join(path, '00000' + ''.join([str(index),'.png',])))# '00' is zerofill 
            print(file)


def Mbox(title, text, style):
    return ctypes.windll.user32.MessageBoxW(0, text, title, style)


#main
renamer_foo(files, path)
Mbox('Message', 'Completed!', 1)
