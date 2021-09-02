from get import scan_stocks
from filter_invest_report import filter
file_name = input("enter name for reuslt file:")
if file_name == '':
    scan_stocks()
else:
    file_name = './data/'+file_name+'.csv'
    scan_stocks(file_name)
    filter(file_name)
