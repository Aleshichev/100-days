import requests
from twilio.rest import Client

STOCK_NAME = "TSLA"
COMPANY_NAME = "Tesla Inc"

STOCK_ENDPOINT = "https://www.alphavantage.co/query"
NEWS_ENDPOINT = "https://newsapi.org/v2/everything"
STOCK_API_KEY = "your api key"
NEWS_API_KYE = "your key"

account_sid = "your account sid"
auth_token = "your token"
    ## STEP 1: Use https://www.alphavantage.co/documentation/#daily
# When stock price increase/decreases by 5% between yesterday and the day before yesterday then print("Get News").

# Get yesterday's closing stock price.
stock_params = {
    "function": "TIME_SERIES_DAILY",
    "symbol": STOCK_NAME,
    "apikey": STOCK_API_KEY,

}

response = requests.get(STOCK_ENDPOINT, params=stock_params)
data = response.json()["Time Series (Daily)"]
yesterday_closing_price = data['2022-05-24']['4. close']
#[new_item for item in list]
# data_list = [value for (key, value) in data.items()]
# yesterday_data = data_list[0]
# yesterday_closing_price = yesterday_data['4. close']
print(yesterday_closing_price)
# Hint: You can perform list comprehensions on Python dictionaries. e.g. [new_value for (key, value) in dictionary.items()]

#Get the day before yesterday's closing stock price
before_yesterday_closing_price = data['2022-05-23']['4. close']
print(before_yesterday_closing_price)

#Find the positive difference between 1 and 2. e.g. 40 - 20 = -20, but the positive difference is 20. Hint: https://www.w3schools.com/python/ref_func_abs.asp
difference = abs(float(yesterday_closing_price) - float(before_yesterday_closing_price))
print(difference)

#Work out the percentage difference in price between closing price yesterday and closing price the day before yesterday.
diff_precent = (difference / float(yesterday_closing_price)) * 100
print(diff_precent)
#percentage is greater than 5 then print("Get News").

    ## STEP 2: https://newsapi.org/
    # Instead of printing ("Get News"), actually get the first 3 news pieces for the COMPANY_NAME.

# Instead of printing ("Get News"), use the News API to get articles related to the COMPANY_NAME.
if diff_precent > 5:
    news_params = {
        "apikey": NEWS_API_KYE,
        "q": COMPANY_NAME,
    }
    news_response = requests.get(NEWS_ENDPOINT, params=news_params)
    articles = news_response.json()['articles']

# Use Python slice operator to create a list that contains the first 3 articles. Hint: https://stackoverflow.com/questions/509211/understanding-slice-notation
    three_articles = articles[:1]

    ## STEP 3: Use twilio.com/docs/sms/quickstart/python
    #to send a separate message with each article's title and description to your phone number.

# Create a new list of the first 3 article's headline and description using list comprehension.
    formated_articles = [f"Headline: {article['title']}. \nBrief: {article['description']}" for article in three_articles]
# Send each article as a separate message via Twilio.
    print(formated_articles)
    client = Client(account_sid, auth_token)
    for article in formated_articles:
        print(article)
        message = client.messages.create(
                                  from_='+19362377794',
                                  body=article,
                                  to='+380989750736'
                              )

        print(message.status)
    #

#Optional Format the message like this:
"""
TSLA: 🔺2%
Headline: Were Hedge Funds Right About Piling Into Tesla Inc. (TSLA)?. 
Brief: We at Insider Monkey have gone over 821 13F filings that hedge funds and prominent investors are required to file by the SEC The 13F filings show the funds' and investors' portfolio positions as of March 31st, near the height of the coronavirus market crash.
or
"TSLA: 🔻5%
Headline: Were Hedge Funds Right About Piling Into Tesla Inc. (TSLA)?. 
Brief: We at Insider Monkey have gone over 821 13F filings that hedge funds and prominent investors are required to file by the SEC The 13F filings show the funds' and investors' portfolio positions as of March 31st, near the height of the coronavirus market crash.
"""

