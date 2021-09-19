# code = """a = 6+5
# print(a)"""
# exec(code)

# --------------------------------------------
#exit codes:
    # 2-files haven't been downloaded
    # 1-file has been downloaded, deletes the files



try:
    print('Loading pre-requisites')
    exit_code=2
    import time, os, urllib.request, platform
    from urllib.parse import urlparse
    file_being_downloaded=''

    def view_error(error):
        answer=input('Would you like to view the verbose error message(y/n)?')
        if answer=='y' or answer=='Y' or answer=='':
            print(error)
            

    def get_answer(__message__):
        y=False
        while y==False:
            x=input(f'''{__message__}\ny/n:  ''')
            if x.lower()=='n':
                z=False
            else:
                z=True
            y=True
        return z, x
            
    def open_file(location, file_name):
        open_file, open_file_string=get_answer("Would you like to open the file?  ")
        ofg=open_file_string#making the funny
        if open_file:
            # command1="cd "+str(location)
            # command2=".\\"+str(file_name)
            # os.system(command1)
            # os.system(command2)
            try:
                plat=platform.system()
                if plat=='Windows':
                    os.startfile(location+'\\'+file_name)
                else:
                    print(f'Your platform, {plat}, does not support this\nYour file is located at:  {location}/{file_name}')
                # os.startfile(location+'\\'+file_name)
            except AttributeError as error:
                print(f'os.startfile not present\nThis issue can arise in linux or possibly mac\n Your file is located at:   location')
                view_error(error)

        else:
            print()
        return ofg
    
            
    
    def get_name(url):
        url=url
        try:
            parsed= urlparse(url)
        except ValueError:
            print("'"+url+"'  Is an invalid URL")
            url=input("Please enter a valid URl")
        get_name.url=url
        x=parsed.path.rpartition('/')[2]
        get_name.name=x

    def create_name(url):
        file_name_tmp=input('Please enter the name of the file you wish to save it to or leave blank to use the original file name:  ')
        if len(file_name_tmp)==0:
            print('Using original file name')
            create_name.file_name=get_name.name

        else:
            print("Using custom file name")
            create_name.file_name=file_name_tmp

    #all modules loaded and functions defined
    print("This program will eventually be used as a base for an install wizard and part of a backdoor")
    print('Note:  Some html files will be broken in that the links to images will not display, this will be fixed soon')
    url=input('Please enter the URL of the file you wish to download:  ')
    get_name(url)
    url=get_name.url
    create_name(url)
    file_name=create_name.file_name #___________________________________________________________________________
    if len(file_name)<1:
        print("Please choose a url with a valid file name")
        time.sleep(2.5)
        print('Quitting in 5.')
        time.sleep(1)
        print('Quitting in 4..')
        time.sleep(1)
        print('Quitting in 3...')
        time.sleep(1)
        print('Quitting in 2....')
        time.sleep(1)
        print('Quiting in 1.....')
        os.startfile('downloader.py')
        exit() 
    answer0=''
    if os.path.exists(file_name):
        print('File already exists')
        answer0=input("Would you like to replace the old file with the new one(y/n)?:  ")
    
    else:
        print('')
    
    if answer0=='n':
        print("Closing Program")
        input('Press Enter to quit:  ')
        exit()
    # elif 
    exit_code=1
    urllib.request.urlretrieve(url, file_name)
    location=os.path.dirname(os.path.realpath(__file__))
    print('File saved to:  ')
    time.sleep(0.1)
    print(location)
    print(file_name)
    time.sleep(2)
    exit=open_file(location, file_name)
    exit_code=2

except KeyboardInterrupt:
    if exit_code==1:
        print('Closing Program')
        print("Deleting Downloaded File")
        if os.path.exists(file_name):
            os.remove(file_name)
            print('File Deleted')
        else:
            print("File Does Not Exist") 
        print(file_name)
    elif exit_code==2:
        print("Closing Program")
except urllib.error.HTTPError as error_1:
    print('No such file or server')
except urllib.error.URLError as error_2:
    print('Invalid Protocol(http, https, ftp, etc.), or you are attempting to access a server which requires authentication')

if exit=='ydelete' or exit=='ndelete':
    if exit=='ydelete':
        time.sleep(2)
    os.remove(file_name)
#-Joseph
