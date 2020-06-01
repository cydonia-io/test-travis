# To add a new cell, type '# %%'
# To add a new markdown cell, type '# %% [markdown]'
# %% [markdown]
# <h1>Get bitmex price btcusd-perpetual-futures</h1>
# <hr>
# <br>
# &nbsp;&nbsp;&nbsp;Get bitmex price btcusd-perpetual-futures with 1 hour granularity. The data is saved in a csv.
# <br>
# <br>
# &nbsp;&nbsp;&nbsp;Date of the program: Friday, May 15 (Mexico City Zone Time)
# <br>
# <br>
# &nbsp;&nbsp;&nbsp;<a href="https://api.cryptowat.ch/markets/bitmex/btcusd-perpetual-futures/price?apikey=M1SR7D1BZ1Q688SYH30V" style="background-color: rgba(84, 231, 209, 0.3);">Link to Api Rest Cryptowatch Bitmex price btcusd-perpetual-futures</a>
# <br>
# <br> <!--
# <center>
#     <img src="img" alt="" height="1000">
# </center>
# <br>
# <br> -->
# <blockquote>
# Running the program will result in:
#     <br>
#     <br>
#     <code>Writing complete: date </code>&nbsp;&nbsp;&nbsp;Indicates the date of saving data within the CSV
# </blockquote>

# %%
#libraries needed for cryptowatch api rest
import json, time, pandas, requests
from datetime import datetime
import schedule
#Limpiar pantalla
from IPython.display import clear_output
#csv
import csv
import os
import pandas as pd

#path and import 
import sys
sys.path.append("..")
from api.api_rest import *
# %%
#Function get price, extract, tranfor and load into csv

def get_price():    
    
    try:
        #API Rest
        r = requests.get(api_price_bitmex_btcusd)
        
    except:
        #In case error
        print("Server down or incorrect domain")

    else:
        #Extract data 
        result = r.json()

        price = result["result"]["price"]
        ct = datetime.now()

        date_time  = ct.strftime("%Y-%m-%d %H:%M:%S")
        #print(date_time)

        #---------- CSV ----------------

        #Name for our CSV file
        path = '../csv/price_bitmex_btcusd.csv'
        #Columns
        column = ["date", "price", "exchange", "pair"]

        #The number of fields has to match the number of columns - Here the previously saved variables are placed.
        rows = [[date_time, price, "bitmex", "btcusd-perpetual-futures"]]
        #Added to a dataframe
        myDataF = pd.DataFrame(rows, columns=column)

        #Conditional    
        #If the file does not exist, it is created
        if not (os.path.isfile(path) and os.stat(path).st_size != 0):
            try:
                myDataF.to_csv(r''+path+'', index=None, header=True)
                print('Writing complete: ',date_time)

            except:
                print('Error to Writing: ',date_time)

        else:
            #If the file exists, add data
            try:
                myDataF.to_csv(path, index=None, mode="a", header=not os.path.isfile(path))
                clear_output(wait=True)
                print("Writing complete: ",date_time)

            except:
                clear_output(wait=True)
                print("Error to Writing: ",date_time)   


    
#Execute the function  get_price() 
#1 hour
schedule.every(3).seconds.do(get_price)
#schedule.every().hour.do(get_price)

# keeps on running all time. 
while True: 
    # Checks whether a scheduled task  
    schedule.run_pending()
    time.sleep(0)
    


# %%


