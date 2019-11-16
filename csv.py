import os.path

excel_path = 'C:\\Users\\usenadu\\Documents\\dumidu-pearson\\google api\\1\\excel_files\\'

f = open ("book1.csv", "r")
f1 = f.readlines()

for address in f1:
    address = address.rstrip() # rstrip - remove the new line
    a = address.split(",")
    excel_file,gsheetid = a[0],a[1]

    #print (a[0])
    #print (a[1])
    
    excel_file_path = os.path.join(excel_path, excel_file)
    print (excel_file_path)
    print (gsheetid)