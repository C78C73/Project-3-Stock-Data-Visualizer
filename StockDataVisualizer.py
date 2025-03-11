#import

#variables

#Ask the user to enter the stock symbol for the company they want data for.
stockSymbol = input("Please enter the stock symbol for the company you want data for: ")

#Ask the user for the chart type they would like.
chartType = input("Please enter the chart type you would like: ")

#Ask the user for the time series function they want the api to use.
timeSeries = input("Please enter the time series function you would like the api to use: ")

#Ask the user for the beginning date in YYYY-MM-DD format.
beginningDate = input("Please enter the beginning date in YYYY-MM-DD format: ")

#Ask the user for the end date in YYYY-MM-DD format.
#The end date should not be before the begin date
endDate = input("Please enter the end date in YYYY-MM-DD format: ")
while True:
    if (endDate > beginningDate):
        print("The end date should not be before the begin date.")
        endDate = input("Please enter the end date in YYYY-MM-DD format: ")
    else:
        break


#Generate a graph and open in the user’s default browser.
def GenerateChart(stockSymbol, chartType, timeSeries, beginningDate, endDate):
    print("Generating chart...")
    return