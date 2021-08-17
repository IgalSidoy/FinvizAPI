base_url = "https://finviz.com/"
sub_url_stock_details = "quote.ashx?"
sub_url_screener = "screener.ashx?"
_del = "&"
headers = {'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/75.0.3770.142 Safari/537.36'}
params = {
 "get_ticker": {
                "t": "",
                "ty": "c",
                "p": "d",
                "b":"1" 
              }
          }

def get_url_ticker_data(ticker):
  _params = params["get_ticker"]
  _params["t"] = ticker
  params_res = ""
  for p in _params:
      params_res+=p+'='+_params[p]+_del
  params_res = params_res[:-1]
  url = base_url+sub_url_stock_details+params_res
  return url
  #

