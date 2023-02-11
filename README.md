# MusicPlayersUpdater
Tool to Update music players. I made this tool for the Test at TouchTunes interview. I don't Use a real API like it was demanded for the test. I do fake calls and responses from the API. I also made a small script called "fake_csv_generator.py" that can generate the input file for you if you do not have one.
# Requirements
1. Having Python 3.10.10 or higher installed  
2. Having request-mock installed https://pypi.org/project/requests-mock/ :
```
pip install requests-mock
```
3. Having you input the CSV file with the mac address of all the music player you want to be updated formatted like this:
![image](https://user-images.githubusercontent.com/14093695/218222948-2525ceec-da1c-452e-af2e-ca9620015ba9.png)
Or you can generate this input file  by using this line:
```
py fake_csv_genretor.py
```
# How to use
Run the command:
```
python PlayerUpdater.py [name of your csv input File]
```
Example:
```
python PlayerUpdater.py music_players.csv 
```
The result you will see will be  in this order
1. The Call to the API
2. The Detailed Response from the API with Status Code
It will look like this: ![image](https://user-images.githubusercontent.com/14093695/218225079-499c01ea-7d00-4454-8b7a-7d6a660f4a29.png)
# Technical decisions and assumptions
## Technical decisions
I decided to make it a simple command line tool so it can be used in the command line or called in other programs. I used request-mock to fake the call and response to the API. I decided that since this is a test, I don't need to handle the fact that the authentification token would expire in real life.

Because this is  a simple tool,  I did not feel there was any place in  the code where it was worth doing unit tests
## Programming Language (Python)
I have chosen to Use Python For 3 main reasons:
1. Python can be used on Windows, MacOS and Linux as long you have it installed on your machine.
2. I can use    to fake API calls and responses in Python without having to code the actual API.
3. It is a good language to do  a simple command line  tool like  this one quickly.
