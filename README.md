# Voting_Software

### Made by Sivadithiyan

## Goal: 
To create a tkinter based program to create custom polling scenarios and allowing the user/voters to cast their votes to the users/people they willing to vote for

## Important note:
### Use test_trigger.ipynb to run the code since main.py hasn't been updated. Check the final folder for the most stable version

#### Please take a note that i'm not an expert in tkinter and this is a mini project i did during my free time. So i didnt put much efforts on the looks but the functionality for the most part can sustain a stable working environment.

## Features:
1. A Login logic with 2 different account tyoes (@voter and @operator) (for operator username: @operator password: operator123*)
2. A Register system to register the user details and create an voter account (Note: Some of these fields are region specific eg: Aadhar number which is specific to India, which can be altered with no pressure)
3. A stable database which can store and retrieve all the interactions and information happens within the application. This is a native database and it doesnt link to any public host 3rd party server
4. A operator panel with info modifying perms
5. Operator can create,modify and delete polls 
6. Operator can also modify user details
7. Operator can grant and revoke voting permission to the users all at once or for a specific user/voter
8. Operator has the ability to set a particular poll as default so whenever someone opens the application, the default or the currently active poll set by operator will appear and all the functionalities will work according to it
9. Operator can conclude a poll by simply clicking a button which removes voting permissions momentarily 
10. Voters can log in with their credentials and access the voter page
11. Voters are allowed to vote once per username/account and the app provides a special tag to the voters who are interacting with the application
12. If the voter is found to be using the application to vote twice using the same account, the permission to the vote casting page will be blocked
13. Only the operator can allow the voters t vote again after altering their status
14. Voters can see the current poll details, their status and the results on their voter page
15. Voter must contact the operator inorder to change any detail otherwise there is no way for the user to modify the details


## Future Plans:

1. Including custom tkinter module to beautify the GUI
2. Light and Dark mode
3. Better database management(As of the last update, its kinda messy and unclear)
4. Move from function based system to class based system for better dataflow and security
5. Creating widget to display various screens instead of creating multiple windows (more like tabs)
6. Converting this code into a standalone exe file which can run on its own

Feel free to use this code for any personal use (you can use this wherever you want but dont claim that you made this from scratch. Be a good sport :) )and If any one of you watching have any decent insights and recommendations please leave a comment below i will see them and will possibly update it as time goes.
