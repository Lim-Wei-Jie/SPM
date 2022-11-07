## Definition of Done (DoD)
#### For a feature to be considered done, it has to fulfil the following criteria:
* Fulfil acceptance criteria defined in the User Story
* Pass all test-cases created for the User Story
## Test-Driven Development (TDD)
* Python TDD framework: Unittest
## Branching Strategy
* Feature-based, each branch is for each feature
* When a feature fulfils DoD, merge the feature branch into the main branch for other branches to merge main branch into their branch, so that they know that the feature fulfils DoD and they can access the features
* Refactoring of code can be done after
## Merge Conflict rule
In the instance where the merging of a branch to the main branch results in a merge conflict
1. The person doing the merging will open the file with the merge conflict via github desktop
2. Screenshot the conflicting codes and send to the telegram groupchat
3. The person who coded the codes in the conflict will let the other person know whether to 'Accept Current Change', 'Accept Incoming Change', or 'Accept Both Changes'
4. If required, conduct a zoom call for better communication

Setup: 
1. Install global Vue 3 CLI using the following command in Command Prompt
    ``` npm install -g @vue/cli ```
2. Restart your VM
1. Unzip the project folder
2. Open the project window in visual studio code
3. Before running the LJPS system please ensure that the following vue libraries are installed.
    Run these commands in the terminal:
    1. cd frontend
    2. npm install 
4. Before running the LJPS system please ensure that the following python libraries are installed.
    Run these commands in the terminal:
    1. cd ..
    2. cd backend
    3. pip install Flask
    4. pip install Flask-Cors
    5. pip install flask-sqlalchemy
    6. pip install Flask-Testing
    7. pip install mysql-connector-python
5. Run Wamp Server
6. Using Phpmyadmin interface
7. Import the "schema.sql" in the backend folder
8. In "db.py" please change the database connection string in line 10 to the one local to your computer
9. In the terminal type: "cd backend" 
10. In the terminal type "python routes.py"
11. In the terminal type "cd .." then "cd frontend"
12. in the terminal type "npm run dev"
13. The project is now running 
