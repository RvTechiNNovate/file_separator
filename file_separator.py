import os
import shutil
dict={
'audio_extensions':('.mp3','.m4a','.wav','.flac'),
'video-extensions':('.mp4','.mkv','.flv','.mpeg'),
'document_extensions':('.doc','.pdf','.txt'),
}
folderpath=input("enter the path of the where you want to do sepration")
print()
def file_finder(folder_path,file_extension):
    files=[]
    for file in os.listdir(folder_path):
        for extension in file_extension:
            if file.endswith(extension):
                files.append(file)
    return files
for extension_type,extensiontuple in dict.items():
    #print(file_finder(folderpath,extensiontuple))
    folder_name=extension_type.split('_')[0]+'files'
    nfolder_path=os.path.join(folderpath,folder_name)
    os.mkdir(nfolder_path)
    for item in (file_finder(folderpath,extensiontuple)):
                 item_path=os.path.join(folderpath,item)
                 nitem_path=os.path.join(nfolder_path,item)
                 shutil.move(item_path,nitem_path)
                 
    

    
