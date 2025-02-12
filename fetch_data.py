"""Importing modules with alias"""
import yfinance as yf
import pandas as pd
import matplotlib.pyplot as plt
import os
from datetime import datetime

TICKERS = ["AAPL", "MSFT", "GOOGL", "TSLA"] # Assigns a list, with tickers of interest


START_DATE = "2024-01-01" # Assigns a string, with the start date
END_DATE = datetime.today().strftime('%Y-%m-%d') # Formatting for the end date

DATA_DIR = "stock_data" # Assigns a name to the data directory
os.makedirs(DATA_DIR, exist_ok=True) # Creates the directory DATA_DIR, if it doesn't exist already

def fetch_stock_data(ticker):
    """Fetch historical stock data for a given ticker from Yahoo Finance."""

    print(f"Fetching data for {ticker}...")
    try:
        stock_data = yf.download(ticker, start=START_DATE, end=END_DATE) # Fetches Yahoo Finance data, for each ticker listed, over the date interval speciified by START_DATE and END_DATE
        if not stock_data.empty: # stock_data has been fetched
            file_path = os.path.join(DATA_DIR, f"{ticker}_prices.csv") # Creates a file path within the DATA_DIR directory, for the ticker's data
            stock_data.to_csv(file_path) # Saves the ticker's data in a CSV file
            print(f"Data saved: {file_path}")
        else:
            print(f"No data found for {ticker}")
    except Exception as e: # Catches any kind of error and prevents the script from crashing
        print(f"Error fetching {ticker}: {e}")

if __name__ == "__main__":
    for ticker in TICKERS: # Loops through all tickers in the TICKERS array
        fetch_stock_data(ticker) # Calls function, fetch_stock_data, to fetch and save data
    print("All stock data fetched successfully!")
