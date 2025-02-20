# 📈 Daily Stock Data Analysi

## 🔍 Project Overview
This project automates the daily fetching, analysis, and visualization of stock prices using **Yahoo Finance (`yfinance`)**. The data is stored in CSV format and updated daily using **GitHub Actions**.

## 🚀 Features
- 📊 **Fetches stock data** from Yahoo Finance
- 📈 **Generates daily price charts** using Matplotlib
- 📅 **Automates daily updates** with GitHub Actions
- 📂 **Stores historical stock data** in CSV format

## 🛠️ Technologies Used
- **Python** (Pandas, NumPy, Matplotlib, yfinance)
- **GitHub Actions** (for daily automation)
- **Yahoo Finance API** (for stock data)

## 📥 Installation & Setup
### Clone the repository:
```sh
git clone https://github.com/YOUR-USERNAME/daily-stock-analysis.git
cd daily-stock-analysis
```

### Create a virtual environment (optional but recommended):
```sh
python -m venv venv
source venv/bin/activate  # macOS/Linux
venv\Scripts\activate  # Windows
```

### Install dependencies:
```sh
pip install -r requirements.txt
```

### Run the script manually:
```sh
python fetch_stock_data.py
```

## 📌 How It Works
1. **The script fetches stock price data** for selected stocks.
2. **It generates daily closing price charts** using Matplotlib.
3. **The data & plots are stored in `data/` and `plots/` directories.**
4. **GitHub Actions runs the script every day at 12:00 UTC.**

## ⚡ Automating with GitHub Actions
- The project includes a GitHub Actions workflow that runs daily.
- The workflow fetches new stock data, updates the CSV files, and commits the changes.
- You can manually trigger the workflow if needed.

## 📊 Example Chart
![Example Chart](plots/AAPL_price.png)
*(Example visualization of Apple's stock price)*

## 🏗️ Future Improvements
- Add **more technical indicators** (RSI, MACD, Moving Averages)
- Store data in **a database instead of CSV**
- Build an **interactive web dashboard** with Streamlit

## 📝 Contributing
Feel free to **fork this repository**, submit issues, or suggest improvements!

## 📜 License
This project is open-source and available under the **MIT License**.

---
✨ Happy Coding! 🚀

