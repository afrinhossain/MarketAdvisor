# MarketAdvisor

A simple AI-powered tool that uses OpenAI’s ChatGPT to suggest:

- 5 stocks to buy  
- 5 stocks to sell  
- 5 ETFs to buy  
- 5 ETFs to sell  

This is done using current market trends, economic outlook, news and other financial advisor blogs.
All suggestions are emailed to you using Gmail. The goal was to get simple advice for myself due to my interest in building a stock portfolio without having to actually read relevant market trends. The next step will be to automate this to be run once a day.

---

## Built With
- Python
- OpenAI API (GPT-3.5)
- Replit
- SMTP (for sending emails)

---

## How to Use

 Add a `.env` file with the following:

```env
EMAIL_ADDRESS=yourgmail@gmail.com
EMAIL_PASSWORD=your_app_password
RECEIVER_EMAIL=you@example.com
OPENAI_API_KEY=sk-...

and run script :) 
