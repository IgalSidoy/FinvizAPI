import get
from datetime import datetime




print("start ------------------------------ " + str(datetime.now()))

print(get.get_ticker_data("EDIT"))
print("########################################################################################")
print(get.get_ticker_data("KRMD"))
print("########################################################################################")
print(get.get_ticker_data("NKTX"))
print("########################################################################################")
print(get.get_ticker_data("NAOV"))
print("end ------------------------------ " + str(datetime.now()))


