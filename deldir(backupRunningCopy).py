import datetime
import logging
import os
import sys
import tarfile
import yaml

#Tool setup variables here
archive_name="test.tar"

#Init and logging config section
def __init__(self, log_path):
    self.root_path = log_path

    logging.basicConfig(
        #filename=<filename-format here>,
        format='%(asctime)s [%(levelname)s]: %(message)s',
        encoding=self.CHAR_ENCODING,
        level=logging.DEBUG
    )

# For archiving use
def create_tar_ball(self, file_list, name):
    with tarfile.open(name, "w") as tar:
        for name in file_list:
            tar.add(name)

#Test for logging function
logging_path= "./tmp/deldir/"#'Enter your log directory path here'

#making a log directory at given path(if exists then it will skip)
if os.path.isdir(logging_path):
    print("Directory already exists")
else:
    os.mkdir(logging_path)

#creating a log file with date
file=open(logging_path+datetime.datetime.today().strftime('%d-%m-%Y')+'.txt','a')

def del_older_files(directory):
  N=90 # Enter number of old file you want to delete
  if not os.path.exists(directory):# if input path not exist then it will show below error
    print("Please provide valid path")
    sys.exit(1)
  if os.path.isfile(directory):# if the given file path is file then it will show below error
    print("Please provide dictionary path")
    sys.exit(2)
  today=datetime.datetime.now()# it will get currunt datetime and transfer to variable(today)
  for each_file in os.listdir(directory):
    each_file_path=os.path.join(directory,each_file)
    if os.path.isfile(each_file_path):
      file_cre_date=datetime.datetime.fromtimestamp(os.path.getctime(each_file_path))# Here, fortimestamp will get the date of file created 
      # Testing the date settings, line below is temp disabled
      #dif_days=(today-file_cre_date).days
      dif_days=(today)
      if dif_days:# Testing for settings 'now',line below is temp disabled.
      #if dif_days > N:# if the age(N) of file is older then 90 days then conditions becomes True and remove that file
        currentdir = os.getcwd()
        os.remove(each_file_path)
        os.chdir(logging_path)
        file.write(os.path.join(directory,each_file)+ ' deleted '+str(dif_days)+' days ago\n')
        os.chdir(currentdir)
        print(each_file_path,dif_days)

#Archiving function
def arc_older_files(directory):
  with tarfile.open(archive_name,"w") as tar:
    N=90 # Enter number of old file you want to delete
    if not os.path.exists(directory):# if input path not exist then it will show below error
      print("Please provide valid path")
      sys.exit(1)
    if os.path.isfile(directory):# if the given file path is file then it will show below error
      print("Please provide dictionary path")
      sys.exit(2)
    today=datetime.datetime.now()# it will get currunt datetime and transfer to variable(today)
    for each_file in os.listdir(directory):
      each_file_path=os.path.join(directory,each_file)
      if os.path.isfile(each_file_path):
        file_cre_date=datetime.datetime.fromtimestamp(os.path.getctime(each_file_path))# Here, fortimestamp will get the date of file created
      # Testing the date settings, line below is temp disabled
      #dif_days=(today-file_cre_date).days
        dif_days=(today)
        if dif_days:# Testing for settings 'now',line below is temp disabled.
      #if dif_days > N:# if the age(N) of file is older then 90 days then conditions becomes True and remove that file
          currentdir = os.getcwd()
        # Archive function code here
        # Should include code to process file list or array
          tar.add(each_file_path)
          os.chdir(logging_path)
          file.write(os.path.join(directory,each_file)+ ' archived '+str(dif_days)+' days ago\n')
          os.chdir(currentdir)
          print(each_file_path,dif_days)

# Config file for directory to process
#with open('./tmp/dirprocess.txt', 'r') as f:  # Open file for read
#    for directory in f:           # Read line-by-line,contains dir each line
#        directory = directory.strip()
#        del_older_files(directory)

#with open('./tmp/dirarchive.txt', 'r') as f:  # Open file for read
#    for directory in f:           # Read line-by-line,contains dir each line
#        directory = directory.strip()
#        arc_older_files(directory)

# Testing YAML config reading
with open('testconfig.yaml') as f:
    config = yaml.load(f, Loader=yaml.FullLoader)
    #print(config)
    for key,value in (config[0]).items():
        #print(values)
        listing = list(value.values())
        #print(listing)
        for directory in listing:
            directory = directory.strip()
            del_older_files(directory)

with open('testconfig.yaml') as f2:
    config = yaml.load(f2, Loader=yaml.FullLoader)
    #print(config)
    for key,value in (config[1]).items():
        #print(values)
        listing = list(value.values())
        #print(listing)
        for directory in listing:
            directory = directory.strip()
            arc_older_files(directory)
