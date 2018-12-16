# PUBG
PUBG: Player's Winning Placement Prediction 


1) Download the training dataset from the given link
https://www.kaggle.com/c/pubg-finish-placement-prediction/data 
Change the path of the training dataset in dataset.py
2) Install all the dependencies by typing the following command in the terminal:
pip install -r requirements.txt
3) Model training:
Type the following command to train the model using Random Forest Algorithm.
python pubg.py
This process will take time as the dataset is very large. 
4) To run the application, type the following command in the terminal. 
python app.py
The server is running on http://127.0.0.1:8080/
Copy and paste the above link in the browser. 
The web page will redirect to the homepage after 4 seconds. 
5) Click on choose file, and select solo1.csv. Click predict to check the winning placement of a player. 
The given input file located in the root directory of the project
6) Repeat step 5 for any input in .csv format.

