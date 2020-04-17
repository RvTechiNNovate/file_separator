#GUI of file seprator

from tkinter import *
from tkinter import filedialog
import os
import shutil as sh

def browse():
    dir_path=filedialog.askdirectory()
    entry_browse.insert(0,dir_path)
    
def reset():
    #print('this is reset button') #prints msg on console
    s=entry_browse.get()
    ln=len(s)
    entry_browse.delete(0,ln) #to clear username text field

    s=entry_key.get()
    ln=len(s)
    entry_key.delete(0,ln)

    text_box.delete('1.0',END)

def file_finder(file_extension):
    folder_path=entry_browse.get()
    files=[]
    for file in os.listdir(folder_path):
        for extension in file_extension:
            if file.endswith(extension):
                files.append(file)
    return files


def submit():
    folderpath=entry_browse.get()
    dict={
            'image__extensions':('.png','.jpeg','.jpg'),
            'audio__extensions':('.mp3','.m4a','.wav','.flac'),
            'video__extensions':('.mp4','.mkv','.flv','.mpeg'),
            'document__extensions':('.doc','.pdf','.txt'),}
    for extension_type,extensiontuple in dict.items():
    #print(file_finder(folderpath,extensiontuple))
        folder_name=extension_type.split('_')[0]+' files'
        nfolder_path=os.path.join(folderpath,folder_name)
        os.mkdir(nfolder_path)
        for item in (file_finder(extensiontuple)):
                     item_path=os.path.join(folderpath,item)
                     nitem_path=os.path.join(nfolder_path,item)
                     sh.move(item_path,nitem_path)
    print("done")



root=Tk()
root.state('zoomed')
bgc='skyblue'
root.configure(bg=bgc)
root.resizable(width=False,height=False)
root.title("Welcome window")

lbl_title=Label(root,text='WELCOME TO file Seprator',font=('cambria',25,'bold'),bg=bgc,fg='white')
lbl_title.pack(pady=10)

lbl_browse=Label(root,text="Directory Path",font=('cambria',22,'italic'),bg=bgc,fg="white")
lbl_browse.place(x=280,y=220)

entry_browse=Entry(root,font=('cambria',20),bg='black',fg='white',bd=5)
entry_browse.place(x=550,y=220)

btn_browse=Button(root,command=browse,text='Browse',font=('Book Antiqua',20),bg='dark olive green',fg='white')
btn_browse.place(x=900,y=220)

btn_sbmt=Button(root,command=submit,text='submit',font=('Book Antiqua',15),bg='dark olive green',fg='white')
btn_sbmt.place(x=400,y=380)

btn_rst=Button(root,command=reset,text='Reset',font=('Book Antiqua',15),bg='dark olive green',fg='white')
btn_rst.place(x=550,y=380)



root.mainloop()

