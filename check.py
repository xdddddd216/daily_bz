import os

from download_form import download_form

def check():
    for i in list(os.walk(os.path.join(os.getcwd(),'bz')))[0][1]:
        os.system('aria2c --conf-path=./config/aria2.conf -d '+os.path.join(os.getcwd(),'bz',i)+' -i '+os.path.join(os.getcwd(),'bz',i,'file.txt'))
        download_form(i)

if __name__ == "__main__":
    check()