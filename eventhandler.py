import time
import os
import shutil
from watchdog.observers import Observer
from watchdog.events import FileSystemEventHandler
source=r'C:\Users\HP LAPTOP\Downloads'
destination=r'C:\Users\HP LAPTOP\Downloads\bill 1_files\python'
dir_three={"Image_Files": ['.jpg', '.jpeg', '.png', '.gif', '.jfif'],
           "Video_Files": ['.mpg', '.mp2', '.mpeg', '.mpe', '.mpv', '.mp4', '.m4p', '.m4v', '.avi', '.mov'],
           "Document_Files": ['.ppt', '.xls', '.xlsx' '.csv', '.pdf', '.txt'],
           "Setup_Files":['.exe', '.bin', '.cmd', '.msi', '.dmg']}
class FileMovementHandler(FileSystemEventHandler):
     def on_created(self, event):
          name, extension=os.path.splitext(event.src_path)
          for key,value in dir_three.items():
               if extension in value:
                    file_name=os.path.basename(event.src_path)
                    path1=source+'/'+file_name
                    path2=destination+'/'+key
                    path3=destination+'/'+key+'/'+file_name
                    time.sleep(3)
                    if os.path.exists(path2):
                        print('moving')
                        shutil.move(path1,path3)
                    else:
                       os.makedirs(path2)
                       print('move it')
                       shutil.move(path1,path3)
          print(event)
event_handler=FileMovementHandler()
observer=Observer()
observer.schedule(event_handler, source, recursive=True)
observer.start
while True:
     time.sleep(2)
     print('running')
     
