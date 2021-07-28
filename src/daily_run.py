from get import daily_automate
start_date = input('enter date from where to start fetch ( format =  yyyy-mm-dd | example : 2021-07-18 ) :')
if start_date =='':
   start_date = '2021-01-01' 
result = input("Fetch latest prices? y/n:")
if result == 'y':
    fetch = True
else:
    fetch=False
daily_automate(start_date,fetch)