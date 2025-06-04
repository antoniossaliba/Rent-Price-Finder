🏘️ RentFinder: Automated Rental Listing Aggregator
RentFinder is a Python-based web automation project that scrapes rental listings from a housing website based on user-defined criteria (e.g., location, price range, etc.), extracts relevant information such as price, location, and listing URL, and then submits this data to a connected Google Sheet via a Google Form using Selenium.

🚀 Features
🔍 Scrapes rental listings matching user-defined search filters

📍 Extracts prices, locations, and listing links

🧠 Uses BeautifulSoup for HTML parsing and Selenium for automation

📝 Submits the results to a Google Sheet through a Google Form

⚙️ Fully customizable for different rental websites and Google Form structures

🛠️ Tech Stack
Python 3.x

BeautifulSoup – HTML parsing

Selenium – Browser automation

Google Forms – Submission backend

Dependencies include:

beautifulsoup4

selenium

requests

lxml or html.parser🛡️ Disclaimer
Make sure to comply with the Terms of Service of any website you scrape.

Frequent scraping or automation may lead to being blocked by some sites.

Always test with small datasets before scaling up.

📈 Future Improvements
Add multi-site support

Integrate with Google Sheets API (instead of Forms)

Add GUI for easier configuration

Deploy on a server with scheduled scraping

📄 License
This project is licensed under the MIT License. See LICENSE for details.

🙌 Contributing
Feel free to fork the repo and submit a pull request. Feedback and improvements are welcome!
