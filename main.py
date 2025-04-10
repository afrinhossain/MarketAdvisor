import os
import smtplib
import ssl
from email.message import EmailMessage
from dotenv import load_dotenv
import openai
from openai import OpenAI

load_dotenv()

EMAIL_ADDRESS = os.getenv("EMAIL_ADDRESS")
EMAIL_PASSWORD = os.getenv("EMAIL_PASSWORD")
RECEIVER_EMAIL = os.getenv("RECEIVER_EMAIL")
OPENAI_API_KEY = os.getenv("OPENAI_API_KEY")

openai.api_key = OPENAI_API_KEY


def market_advice():
    prompt = """
    Act like a financial advisor but dumb it down.
    Give me:
    - 5 stocks to buy
    - 5 ETFs to buy
    - 5 stocks to sell
    - 5 ETFs to sell
    Given the current market trends, economic outlook, news and other financial advisor blogs.
    Include a short paragraph of reasoning at the end.
    Keep it clean and readable.
    """

    client = OpenAI(api_key=OPENAI_API_KEY)

    response = client.chat.completions.create(
        model="gpt-3.5-turbo",
        messages=[{
            "role": "user",
            "content": prompt
        }],
        # slightly creative but still grounded
        temperature=0.7,
        max_tokens=500)

    return response['choices'][0]['message']['content']


def send_email(subject, content):
    msg = EmailMessage()
    msg['From'] = EMAIL_ADDRESS
    msg['To'] = RECEIVER_EMAIL
    msg['Subject'] = subject
    msg.set_content(content)

    context = ssl.create_default_context()
    with smtplib.SMTP_SSL('smtp.gmail.com', 465, context=context) as smtp:
        smtp.login(EMAIL_ADDRESS, EMAIL_PASSWORD)
        smtp.send_message(msg)
        print("Email sent!")


advice = market_advice()
send_email("Market Advisor Picks - courtesy of our bestie GPT", advice)
