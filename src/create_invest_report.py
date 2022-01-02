from get import scan_stocks
file_name = input("enter name for reuslt file:")
if file_name == '':
    scan_stocks()
else:
    file_name = './data/'+file_name+'.csv'
    scan_stocks(file_name)
