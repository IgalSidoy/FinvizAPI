# FinvizAPI - developer helper functions for data extractions - with no limits
### Scraper for : [Finviz](https://www.finviz.com) (website) market data 

#### basic usage:
```python
import get
result = get.get_ticker_data("AAPL")
print(result)
{'P/E': '31.41', 
 'EPS(ttm)': '4.46', 
 'InsiderOwn': '0.07%', 
 'SharesOutstanding': '16.75B', 
 'Performance_Week': '5.15%', 
 'MarketCapitalization': '2290.71B', 
 'Forward_P/E': '26.18', 
 'EPS_Next_Year': '3.30%',
 'Insider_Transactions': '-2.79%', 
 'Shares_Float': '16.68B', 
 'Performance_Month': '13.29%',
 'Income(ttm)': '76.31B', 
 'PEG': '1.75', 
 'EPS_Next_Quarter': '0.99',
 'Institutional_Ownership': '58.60%',
 'Short_Float': '0.65%',
 'Performance_Quarter': '11.17%',
 'Sales': '325.41B', 'P/S': '7.04', 
 'EPS_This_Year': '10.20%',
 'Inst_Trans': '-',
 'Short_Ratio': '1.32', 
 'Performance_Half_Year': '5.48%', 
 'Book/Share': '4.13', 
 'P/B': '33.89', 
 'Return_On_Assets_ttm': '22.90%',
 'Target_Price': '159.46',
 'Performance_Year': '53.76%',
 'Cash/Share': '4.27',
 'P/C': '32.80',
 'EPS_Next_5Years': '17.93%',
 'return_on_equity_ttm': '111.80%',
 '52W Range': '89.14 - 145.09',
 'Performance_Year_To_Date': '5.48%',
 'Dividend_Annual': '0.88',
 'P/FCF': '30.04', 
 'EPS_Past_5_Years': '7.30%', 
 'ROI': '31.70%', 
 '52W_High': '-3.54%',
 'Beta': '1.20',
 'Dividend_Yield_Annual': '0.63%',
 'Quick_Ratio': '1.10', 
 'Sales_Past_5_Years': '3.30%', 
 'Gross_Margin_ttm': '39.90%',
 '52W_Low': '57.00%',
 'ATR': '1.94',
 'Employees': '147000', 
 'Current_Ratio': '1.10', 
 'Sales Q/Q': '53.60%', 
 'Operation_Margin': '27.30%',
 'RSI_14': '75.58', 
 'Volatility_Week/Month': '1.39% 1.51%',
 'Optionable': 'Yes', 
 'Total_Debt_To_Equity': '1.76',
 'EPS Q/Q': '118.60%',
 'Profit_Margin': '23.50%',
 'Relative_Volume': '0.96', 
 'Previous_Close': '137.27',
 'Shortable': 'Yes', 
 'LT_Debt/Eq': '1.57', 
 'Earnings_Date': 'Jul 27 AMC',
 'dividend_payout_ratio_ttm': '18.20%', 
 'Payout': '18.20%', 
 'Average_Volume_3_Months': '82.26M', 
 'Price': '139.96', 
 "Analysts' mean recommendation (1=Buy 5=Sell)": '2.00',
 'SMA_20': '6.70%', 
 'SMA50': '8.23%', 
 'SMA200': '8.23%', 
 'Volume': '78,945,568', 
 'Change_Today': '1.96%'
 }
```
#### get collection of screeners from main page:(example)
```python
import get
result = get.get_screeners()
{'ticker': 'SQBG', 'name': 'Sequential Brands Group, Inc.', 'industry': 'Apparel Manufacturing ', 'market_cap': '13.66M', 'last': '15.70', 'change': '89.16%', 'volume': '28044052', 'signal': 'Top Gainers'}
{'ticker': 'ALEC', 'name': 'Alector, Inc.', 'industry': 'Biotechnology ', 'market_cap': '1.79B', 'last': '35.21', 'change': '57.12%', 'volume': '39132116', 'signal': 'Top Gainers'}
{'ticker': 'BLIN', 'name': 'Bridgeline Digital, Inc.', 'industry': 'Software - Infrastructure ', 'market_cap': '37.14M', 'last': '8.97', 'change': '56.00%', 'volume': '144081088', 'signal': 'Top Gainers'}
{'ticker': 'TATT', 'name': 'TAT Technologies Ltd.', 'industry': 'Aerospace & Defense ', 'market_cap': '52.56M', 'last': '8.45', 'change': '42.62%', 'volume': '34354388', 'signal': 'Top Gainers'}
{'ticker': 'OSG', 'name': 'Overseas Shipholding Group, Inc.', 'industry': 'Oil & Gas Midstream ', 'market_cap': '182.39M', 'last': '2.88', 'change': '37.14%', 'volume': '18763940', 'signal': 'Top Gainers'}
{'ticker': 'MRIN', 'name': 'Marin Software Incorporated', 'industry': 'Software - Application ', 'market_cap': '165.36M', 'last': '20.29', 'change': '34.55%', 'volume': '121334016', 'signal': 'Top Gainers'}
{'ticker': 'IDT', 'name': 'IDT Corporation', 'industry': 'Telecom Services ', 'market_cap': '1.10B', 'last': '45.38', 'change': '15.38%', 'volume': '1253213', 'signal': 'New High'}
{'ticker': 'JAX', 'name': "J. Alexander's Holdings, Inc.", 'industry': 'Restaurants ', 'market_cap': '185.06M', 'last': '13.80', 'change': '12.56%', 'volume': '2753090', 'signal': 'New High'}
{'ticker': 'JRSH', 'name': 'Jerash Holdings (US), Inc.', 'industry': 'Apparel Manufacturing ', 'market_cap': '74.90M', 'last': '7.23', 'change': '9.38%', 'volume': '426782', 'signal': 'New High'}
{'ticker': 'RFL', 'name': 'Rafael Holdings, Inc.', 'industry': 'Biotechnology ', 'market_cap': '961.96M', 'last': '60.01', 'change': '10.52%', 'volume': '77317', 'signal': 'New High'}
{'ticker': 'BLIN', 'name': 'Bridgeline Digital, Inc.', 'industry': 'Software - Infrastructure ', 'market_cap': '37.14M', 'last': '8.97', 'change': '56.00%', 'volume': '144081088', 'signal': 'Overbought'}
{'ticker': 'TATT', 'name': 'TAT Technologies Ltd.', 'industry': 'Aerospace & Defense ', 'market_cap': '52.56M', 'last': '8.45', 'change': '42.62%', 'volume': '34354388', 'signal': 'Overbought'}
{'ticker': 'TATT', 'name': 'TAT Technologies Ltd.', 'industry': 'Aerospace & Defense ', 'market_cap': '52.56M', 'last': '8.45', 'change': '42.62%', 'volume': '34354388', 'signal': 'Unusual Volume'}
{'ticker': 'STAF', 'name': 'Staffing 360 Solutions, Inc.', 'industry': 'Staffing & Employment Services ', 'market_cap': '24.20M', 'last': '4.99', 'change': '34.50%', 'volume': '85384920', 'signal': 'Unusual Volume'}
{'ticker': 'JAX', 'name': "J. Alexander's Holdings, Inc.", 'industry': 'Restaurants ', 'market_cap': '185.06M', 'last': '13.80', 'change': '12.56%', 'volume': '2753090', 'signal': 'Unusual Volume'}
{'ticker': 'WIZ', 'name': 'Alpha Architect Merlyn.AI Bull-Rider Bear-Fighter ETF', 'industry': 'Exchange Traded Fund ', 'market_cap': '-', 'last': '36.14', 'change': '0.28%', 'volume': '1313644', 'signal': 'Unusual Volume'}
{'ticker': 'PNC', 'name': 'The PNC Financial Services Group, Inc.', 'industry': 'Banks - Regional ', 'market_cap': '81.46B', 'last': '192.79', 'change': '0.55%', 'volume': '1599243', 'signal': 'Upgrades'}
{'ticker': 'ITRM', 'name': 'Iterum Therapeutics plc', 'industry': 'Biotechnology ', 'market_cap': '410.20M', 'last': '1.42', 'change': '-37.99%', 'volume': '83008152', 'signal': 'Top Losers'}
{'ticker': 'ARWR', 'name': 'Arrowhead Pharmaceuticals, Inc.', 'industry': 'Biotechnology ', 'market_cap': '8.84B', 'last': '63.13', 'change': '-25.69%', 'volume': '7344481', 'signal': 'Top Losers'}
{'ticker': 'PBTS', 'name': 'Powerbridge Technologies Co., Ltd.', 'industry': 'Software - Application ', 'market_cap': '82.53M', 'last': '1.80', 'change': '-19.28%', 'volume': '2592665', 'signal': 'Top Losers'}
{'ticker': 'WTT', 'name': 'Wireless Telecom Group, Inc.', 'industry': 'Communication Equipment ', 'market_cap': '79.30M', 'last': '2.97', 'change': '-18.85%', 'volume': '1273973', 'signal': 'Top Losers'}
{'ticker': 'ATHE', 'name': 'Alterity Therapeutics Limited', 'industry': 'Biotechnology ', 'market_cap': '46.90M', 'last': '1.75', 'change': '-18.22%', 'volume': '22721772', 'signal': 'Top Losers'}
{'ticker': 'CTXR', 'name': 'Citius Pharmaceuticals, Inc.', 'industry': 'Biotechnology ', 'market_cap': '352.19M', 'last': '2.15', 'change': '-17.31%', 'volume': '43215964', 'signal': 'Top Losers'}
{'ticker': 'PLSE', 'name': 'Pulse Biosciences, Inc.', 'industry': 'Medical Instruments & Supplies ', 'market_cap': '550.97M', 'last': '17.25', 'change': '-17.15%', 'volume': '365570', 'signal': 'Top Losers'}
{'ticker': 'ATOS', 'name': 'Atossa Therapeutics, Inc.', 'industry': 'Biotechnology ', 'market_cap': '648.82M', 'last': '5.37', 'change': '-16.09%', 'volume': '27924132', 'signal': 'Top Losers'}
{'ticker': 'KTRA', 'name': 'Kintara Therapeutics, Inc.', 'industry': 'Biotechnology ', 'market_cap': '75.00M', 'last': '1.93', 'change': '-16.09%', 'volume': '1355675', 'signal': 'Top Losers'}
{'ticker': 'ZME', 'name': 'Zhangmen Education Inc.', 'industry': 'Education & Training Services ', 'market_cap': '2.06B', 'last': '11.12', 'change': '-14.98%', 'volume': '945421', 'signal': 'New Low'}
{'ticker': 'YQ', 'name': '17 Education & Technology Group Inc.', 'industry': 'Education & Training Services ', 'market_cap': '642.51M', 'last': '3.15', 'change': '-5.41%', 'volume': '2183847', 'signal': 'New Low'}
{'ticker': 'CVM', 'name': 'CEL-SCI Corporation', 'industry': 'Biotechnology ', 'market_cap': '369.74M', 'last': '8.05', 'change': '-6.94%', 'volume': '6941967', 'signal': 'New Low'}
{'ticker': 'PHVS', 'name': 'Pharvaris N.V.', 'industry': 'Biotechnology ', 'market_cap': '577.02M', 'last': '16.30', 'change': '-6.48%', 'volume': '10187', 'signal': 'New Low'}
{'ticker': 'SQBG', 'name': 'Sequential Brands Group, Inc.', 'industry': 'Apparel Manufacturing ', 'market_cap': '13.66M', 'last': '15.70', 'change': '89.16%', 'volume': '28044052', 'signal': 'Most Volatile'}
{'ticker': 'BLIN', 'name': 'Bridgeline Digital, Inc.', 'industry': 'Software - Infrastructure ', 'market_cap': '37.14M', 'last': '8.97', 'change': '56.00%', 'volume': '144081088', 'signal': 'Most Volatile'}
{'ticker': 'BLIN', 'name': 'Bridgeline Digital, Inc.', 'industry': 'Software - Infrastructure ', 'market_cap': '37.14M', 'last': '8.97', 'change': '56.00%', 'volume': '144081088', 'signal': 'Most Active'}
{'ticker': 'SPCE', 'name': 'Virgin Galactic Holdings, Inc.', 'industry': 'Aerospace & Defense ', 'market_cap': '10.40B', 'last': '44.94', 'change': '4.05%', 'volume': '135686528', 'signal': 'Most Active'}
{'ticker': 'KEYS', 'name': 'Keysight Technologies, Inc.', 'industry': 'Scientific & Technical Instruments ', 'market_cap': '28.29B', 'last': '153.15', 'change': '-0.27%', 'volume': '836646', 'signal': 'Downgrades'}
{'ticker': 'FLEX', 'name': 'Flex Ltd.', 'industry': 'Electronic Components ', 'market_cap': '8.69B', 'last': '17.87', 'change': '0.51%', 'volume': '1657623', 'signal': 'Insider Selling'}
```
