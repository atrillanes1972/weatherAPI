filenames = ["1.Raw Data.txt","2.Presentations.txt","3.Reports.txt"]

for filename in filenames:
    filename = filename.replace('.','-',1)
    print(filename)