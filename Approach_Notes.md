# Approach Notess

## Next Steps for fetch_data.py:

- Add more stock tickers dynamically.
- Include technical indicators like SMA, EMA, RSI, MACD.
- Automate daily commits with GitHub Actions.

## Technical Implementation Plan

### Add Technical Indicators to fetch_data.py

Start with Simple Moving Averages (SMA): Calculate 10-day and 50-day SMA.

Add Exponential Moving Average (EMA): Implement 20-day EMA.

Include Relative Strength Index (RSI): Calculate 14-day RSI for overbought/oversold signals.

## Enhance Data Visualization

Plot stock prices along with SMA and EMA indicators.

Add RSI as a subplot for better clarity.

## Automate Daily Data Fetching and Commits

Use GitHub Actions to run fetch_data.py daily.

After running, automatically commit and push updated CSVs and plots.
