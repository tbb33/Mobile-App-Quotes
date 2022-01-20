# Mobile-App-Quotes
 
## This mobile app (which can be used on desktop, android, and iOS) will provide the user with a quote based on how the user is feeling. 
### Install Kivy library (pip install kivy) before executing this program.

### Explanation of each file:

1. main.py - run this to execute the app. It contains logic of the app written in python.
2. design.kv - GUI of the app in kivy language. Kivy works as hierarchy of objects.
3. users.json - database containing users information for the app including username, password, and datetime created in dictionary format.
4. quotes folder - containes .txt files for respective feelings. In each .txt file are quotes for that feeling. 
   - Currently the app only has quotes for 3 feelings, but this can easily be expanded by adding more quotes to a .txt file, naming the .txt file for the feelings, and adding the file to the "quotes" folder.

6. hoverable.py - sub-module to implement hoverable behavior.

7. logout_nothover.png and logout_hover.png - 2 images for the hover/nonhover behavior for logout button. 

