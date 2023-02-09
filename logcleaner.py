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
        logger.info('Deleted one file: %s',os.path.join(directory,each_file))
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
          tar.add(each_file_path)
          logger.info('Archived one file: %s', os.path.join(directory, each_file))
          print(each_file_path,dif_days)

# For archiving use
def create_tar_ball(self, file_list, name):
    with tarfile.open(name, "w") as tar:
        for name in file_list:
            tar.add(name)