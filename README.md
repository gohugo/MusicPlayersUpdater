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
