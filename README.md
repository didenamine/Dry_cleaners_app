# Dry cleaners application 
This app is coded using Tkinter and sqlite3 -> python and it aims to help the dry cleaners to organize their clients commands and get rid of the boring paper use.
__________________________________________________________

The app is very user friendly so it contain only 3 inputs :<br />
1 - Name of the client <br />
2 - Prename of the client <br />
3 - and then the number which can be phone number or the ranking number(because some owners work with the rank of the clients for example client number 1 will have the number 1 and 2 will take 2 and so on...
_________________________________________________________
there is an option where you can choose the clothe name and under it the quantity 
then there is the add to the command which will add the chosen clothe to the total command but it won't be commited 
until the whole commande is done which is the function of the last button after the paid Yes or No option       
________________________________________________________
The other buttons are <br />
1 show all records of the clients 'that paid'<br /> 
2 show all records of the clients 'that didn't pay'<br />
3 show the prices and there is an option there to modify a price <br />
4 search about a client threw the number it was given while writting the commande -> phone number or rank<br /> 
5 delete a client from the data base which is only accessible by the owner threw a password <br />

## Downlaoding way (not obligatory) : 
just download the files as zip or clone them inside a file <br /> 
In order to make the app an .exe <br/> :
open cmd inside that file and do the following commandes(It is recommended to have python>3.7 inside the pc )<br/>
1 - pip install pyinstaller  <that will download the pyinstaller library inside the pc > <br />
2 - pyinstaller -w --onefile Pressing_code.py # "that will take some time"  <br />
3 - go to the dist file that will be added to the files and bring the .exe file to the main file 'outside the dist file' <br />
4 - Done ! <br/>

