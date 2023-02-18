Linking Deviant to Bybit via Heroku

What you will need:

- A **TradingView** account

*Use our referral link to get a discount on your pro/premium subscription: [https://www.tradingview.com/?aff_id=107886f_sub=alyavalley*](https://www.tradingview.com/?aff_id=107886%E2%81%A1f_sub=alyavalley)*

- **Opal Deviant**

ALYA NFT holders get automatic access to Opal indicators and trading bot Deviant. You can mint a ALYA NFT on our website: <https://www.alyavalley.com/Mint>

Once your verify your asset in our discord, you will be able to submit your trading view ID to get access to the indicators and the algos.

- A **ByBit account**

*Use our affiliate link to open a new account: [https://partner.bybit.com/b/alyavalley*](https://partner.bybit.com/b/alyavalley)*

- A **Heroku** account to host your webhook app

[*www.heroku.com*](http://www.heroku.com)

Programs to install:

- **Visual Studio Code**: <https://code.visualstudio.com/>
- **Heroku CLI:** <https://devcenter.heroku.com/articles/heroku-cli>
- **Git** : <https://git-scm.com/downloads>`
1. OPAL scripts setup

Download the code repository to create the Deviant webhooks from ALYA github: <https://github.com/AlyaValley/Opal-Deviant-webhook>

![](Aspose.Words.b770a670-acbb-4025-81b7-868627666454.001.jpeg)

Click on Code, then either select Open with Github if you are familiar with git, or simply download the ZIP file.

Open *Visual Studio Code*, open the Environment tab and click on Open Folder:

![](Aspose.Words.b770a670-acbb-4025-81b7-868627666454.002.jpeg)

Go inside the folder *Opal\_deviant\_webhook* and click on open:

![](Aspose.Words.b770a670-acbb-4025-81b7-868627666454.003.jpeg)

Agree to trust the authors of this code ;)

2. ByBit API setup

Go to your bybit account, Click on your profile logo, and go to API

![](Aspose.Words.b770a670-acbb-4025-81b7-868627666454.004.jpeg)

Click on Create New Key

![](Aspose.Words.b770a670-acbb-4025-81b7-868627666454.005.jpeg)

Select the following options and click submit:

![](Aspose.Words.b770a670-acbb-4025-81b7-868627666454.006.png)

Write down your secret key and copy it.

In Visual Studio Code, open the file *bybitconfig.py* with your API keys and a passphrase:

![](Aspose.Words.b770a670-acbb-4025-81b7-868627666454.007.jpeg)

IMPORTANT : setup for BTCUSDT on byBit

If you link deviant to byBit to for BTCUSDT, you need to make sure you are in one-way mode, not hedge mode, otherwise each alert will open 2 position - one short one long !!

![](Aspose.Words.b770a670-acbb-4025-81b7-868627666454.008.png) ![](Aspose.Words.b770a670-acbb-4025-81b7-868627666454.009.png)

3. Heroku setup

Create an account on [www.heroku.com ](http://www.heroku.com)Click on New and create new app:

![](Aspose.Words.b770a670-acbb-4025-81b7-868627666454.010.png)

Choose a name and create your app:

![](Aspose.Words.b770a670-acbb-4025-81b7-868627666454.011.jpeg)

4. Push the deviant webhook code to heroku

In *Visual Studio Code*, right click on *TV\_deviant\_heroku\_bybit* and click open in integrated terminal:

![](Aspose.Words.b770a670-acbb-4025-81b7-868627666454.012.jpeg)

In the terminal, type the following command (press enter after each command). First let’s check that git is properly installed:

git --version

You should get something like

![](Aspose.Words.b770a670-acbb-4025-81b7-868627666454.013.png)

If you get an error message there is probably a problem with your git installation.

If you have never used git before you will need to set your user name and email: git config –global user.name “your user name”

Git config –global user.mail youremail@mail.com

Then login in Heroku:

Heroku login

The terminal will ask you to press any key, and open your internet browser to connect to your heroku account. After that go back to Visual Studio Code Terminal and enter the command:

git init

heroku git:remote -a *name-of-your-bot-set-on-heroku*

git add .

git commit -m “pushing my bot to heroku”

git push heroku main

You will see a bunch of code line passing on the terminal, and it should end with something like:

![](Aspose.Words.b770a670-acbb-4025-81b7-868627666454.014.png)

Copy the https address of your app which is in the form https://name-of-your-bot.herokuapp.com/  (in the example above: https://deviant-bybit-m15-221006.herokuapp.com ).

**The address of your webhook will be with webhook added at the end : <https://name-of-your-bot.herokuapp.com/webhook>**

5. Setup an alert in Trading View and end it to Bybit via your app

In Visual Studio code, open the file *tradingview\_webhook\_payload\_format.txt* and change “YOUR PASSPHRASE” for the passphrase you have set up in the *bybitconfig.py* file.

![](Aspose.Words.b770a670-acbb-4025-81b7-868627666454.015.jpeg)

In TradingView, choose an asset on Bybit and a time frame.

Open deviant and set up your strategy. Make sure your strategy is correct using the strategy tester tool. We give suggestions of strategies preset to ALYA NFT holders in our discord: <https://discord.gg/alyavalley>

Once your strategy is setup, create an alert :

![](Aspose.Words.b770a670-acbb-4025-81b7-868627666454.016.png)

In *Condition* select *OPAL deviant*, choose the alerts you want to receive.![](Aspose.Words.b770a670-acbb-4025-81b7-868627666454.017.jpeg)

Click *Webhook URL*, and copy the address of your heroku webhook (remember to add /webhook at the end of the address).

In *Message*, copy the content of the file *tradingview\_webhook\_payload\_format.txt* (with your actual passphrase).

Click Create, and **VOILA** ! you have set up a webhook that will send deviant alerts to your heroku app, to bybit API which will automatically take the trades deviant finds.

**WARNING**:

Opal Deviant  will always send Stop Loss, Entry and Take Profits signals from TradingView to your broker for every trade if your strategy is well managed. <https://www.tradingview.com/x/N9QVZL0q/>

When you are looking to turn off a current trade from OPAL Deviant which is running on your broker (e.g. taking too long to close, not satisfy, you are content with your win etc.), you will need to manage the trade on your broker (adapt stop loss, exit market, changing limit order, …).

BUT TradingView will keep sending alerts via the webhook and mess up your broker account, so you need to delete the alert of the specific strategy on your TradingView account to stop sending calls to your API key.

Then before turning back on the strategy with the alert, you will need to wait for Opal Deviant to be out of every position on the same strategy: no pending  stop loss, entry, take profit and exit or that will send a new order to your broker.

Here we are out of a trade for ex:

<https://www.tradingview.com/x/eoVRd33o/>

We recommend you to turn off the algos during big economic news days and sessions when the volatility will increase when bigger boys are killing others' algos.

Soon we will release Opal Deviant for FTX.

You can use our link as well to get 5% reduced fees: <https://ftx.com/referrals#a=alyavalley>

**DISCLAIMER**

ALYA does not host your API keys.

ALYA cannot interfere with your TradingView account, Heroku access and your broker. Alya team and associates will always be there to assist you in case of any issue.

All trades suggestions and ideas from Alya website, twitter, discord, youtube, including trade setups  from our different algos and indicators, are given for educational purposes only. Over 95% of traders never win and actually lose money.

Trading is risky and there are NO guarantees that you will actually win the trade.

If you follow any setups, you do so at your own risk and take full responsibility for your actions. The information should not be construed as investment / trading advice and is not meant to be a solicitation or recommendation to buy, sell or hold any securities, Crypto or coins mentioned.

All content is for entertainment and education ONLY. No financial advice.

Past performance is no guarantee of future results.

Alya, its employees or associates are NOT liable for your trading wins or losses. Do your own research.

All information provided is a general market commentary and does not constitute investment or financial advice.

We are not financial advisors and this information is for entertainment purposes only.
