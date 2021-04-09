# Internship-QM-Telegram-API

# Creating BOT in Telegram App:

1. Search for this Username on Telegram: `@BotFather`.
2. To create a new bot: type `/newbot` and click on send.
3. Set a Name for your Bot(This is the Display Name).
4. Now, Set a unique Username(The username should end with 'bot'. For example: 'Tetris_bot' or 'tetrisbot').
5. Now the bot has been created and the bot link is generated. This link can be used to access and chat with the bot.
6. With this link, the Bot Token gets generated. (Note: Keep your token secure and store it safely, it can be used by anyone to control the bot).

# Installing necessary dependencies:

1. Installing MongoDB: `sudo apt install mongodb`.
2. Clone this repository: `git clone https://github.com/skynet-05/Internship-QM-Telegram-API.git`.
3. Go into the folder: `cd Internship-QM-Telegram-API`.
4. Installing python dependencies all at once: `pip3 install -r requirements.txt` (If this step gives an error continue with steps 5, 6 and 7 else not required)
5. Installing Python package of MongoDB: `pip3 install pymongo`.
6. Installing Python package of Telegram: `pip3 install telegram`.
7. Installing Python requests package: `pip3 install requests`

# Controlling the bot using the code in this repository:

3. Now save the bot token in config.py file. Replace `PUT YOUR BOT TOKEN HERE` with the generated token.
5. Full code is on `final_telegram_code.py` file.
6. Few changes have to be made in `final_telegram_code.py` file.
7. Replace `GIVE A NAME FOR YOUR DATABASE` in `final_telegram_code.py` file with a name for your DataBase.
8. Replace `GIVE A NAME FOR THE COLLECTIONS` in `final_telegram_code.py` file with a name for your collections in the DataBase.
9. Now save the file.
10. Run the file by using this command `python3 final_telegram_code.py`. This code is now running and your bot is online.
11. You can now send messages to your bot using the bot link from any phone and and the messages can be replied back to the user from terminal where the code is running.
12. All messages sent to bot from a user is store in the MongoDB database created.
13. Code can be stopped by pressing `ctrl + c` from keyboard.

# Accessing MongDB database created to save the messages:

1. Open a new terminal
2. Type `mongo` and press enter.
3. To list all DataBases created: `show dbs`.
4. Now you should be able to see the database name you had given in `final_telegram_code.py` file.
5. To access the database: `use <NAME OF YOUR DATABASE>` (Note: do not include '<' '>').
6. To list all collections in the database: `show collections`.
7. To print all data in the collection: `db.<NAME OF THE COLLECTION>.find().pretty()` (Note: do not include '<' '>').
8. Now all data stored in the collection is printed and can be viewed.
9. More MongoDB functionality can be found here -> https://docs.mongodb.com/manual/

# Issues:

If any issues, it can be addressed here -> https://github.com/skynet-05/Internship-QM-Telegram-API/issues
