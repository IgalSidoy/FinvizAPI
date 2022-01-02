from get import get_ticker_data;
from get import calc_stocatics;
from datetime import datetime



def extract_insights(ticker,period=5,spike_triger=20):
    #period - days 
    #spike_triger - percent change trigger
    dic_result = []

    result = get_ticker_data(ticker)
    if result['status']!='200':
        return None

    c = result["data"]["c"]
    l = result["data"]["l"]
    d = result["data"]["d"]

    counter = 1
    for i in range(len(c)-1,0,period*(-1)):
        
        prev_close = float(c[i-1])
        
        close = float(c[i])

        
        change  = round((close-prev_close)/close*100,2)
        abs_change = abs(change)
    
        date = str(datetime.fromtimestamp(int(d[i]))).split(' ')[0]
        split_date = date.split('-')
        delimiter = '/'
        result_date = split_date[2]+delimiter + \
        split_date[1]+delimiter+split_date[0]
        stoc = calc_stocatics(result["data"],result_date,40)

        last = i
        if abs_change >=spike_triger:    
            if i<len(c)-1:
                next_date = str(datetime.fromtimestamp(int(d[i+1]))).split(' ')[0]
                split_date = next_date.split('-')
                delimiter = '/'
                result_date = split_date[2]+delimiter + \
                split_date[1]+delimiter+split_date[0]
                next_stoc = calc_stocatics(result["data"],result_date,40)
                next_low = float(l[i+1])
                next_change = round((next_low-close)/next_low*100,2)
            else:
                next_stoc={"average":-1}
                next_change=""
                next_low=-1

            line = {
            "date":date,
            "change":str(change)+"%",
            "close":close,
            "prev_close":prev_close,
            "next_low":next_low,
            "next_change":str(next_change)+"%",
            "stoc":stoc["average"],
            "next_stoc":next_stoc["average"],
            "insights":{}
            }
            if change>0:
                line['insights']['type']='up'
            else:
                line['insights']['type']='down'

            if next_low>close:
                line['insights']['next_day_effect']='up'
            else:
                line['insights']['next_day_effect']='down'
            if next_low<0:
                line['insights']['next_day_effect']=''
            # print(line)
            dic_result.append(line)
        counter+=1
    insights_result = {
        "ticker":ticker,
        "dic_result":dic_result,
        "correlation":0
    }
    if len(dic_result)==0:
        return insights_result

    correlation_counter = 0
    for line in dic_result:
        if line['insights']['type']==line['insights']['next_day_effect']:
            correlation_counter+=1
    insights_result["correlation"] = round(correlation_counter/len(dic_result),2)
    return insights_result


# print(extract_insights("LVTX",5,10))
