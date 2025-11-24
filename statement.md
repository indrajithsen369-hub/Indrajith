Problem Statement:
  The problem this project addresses is the difficulty in quickly estimating house prices based on basic property features without relying on manual market 
  research or real estate experts. Users often need an immediate price prediction using details such as bedrooms, bathrooms, area, and location, but there is no 
  simple tool that can both generate estimates and keep a record for future reference. This project provides a solution by building a machine-learning based system
  that predicts house prices from user-entered inputs and stores each prediction in a database. The system allows users to view past results and make multiple predictions 
  efficiently through an interactive menu, offering a convenient and automated way to estimate housing prices.

Scope of the project :
  The scope of this project is limited to predicting house prices based on four input features: the number of bedrooms, the number of bathrooms, the total area in square feet, 
  and the location category. It focuses on using a predefined sample dataset to train a machine-learning model and does not include real-world or large-scale housing market data. 
  The system operates as a command-line application, allowing users to enter details, receive a predicted price, and save each result into a local SQLite database.The project 
  also includes the ability to view previously stored predictions, which helps users track multiple estimates over time. It is designed for educational and demonstration 
  purposes, showcasing how machine learning, data storage, and user interaction can work together in a simple application. The scope does not extend to features such as live
  data integration, advanced pricing factors, graphical interfaces, or deployment on web or mobile platforms.

Target Users:
  The project is intended for beginners and students who want to learn how machine-learning models can be applied to real-world problems in a simple and 
  interactive way. It is also suitable for developers and learners who are exploring how to integrate prediction systems with a database using Python. Educators 
  can use this project as a teaching example to demonstrate concepts such as data preprocessing, model training, and persistent storage. 

High level features: 
  he project provides an automated house price prediction system that uses a trained machine-learning model to generate estimated prices based on user-entered 
  property details. It includes a data preprocessing pipeline that encodes location values and scales numerical features to improve the accuracy and reliability 
  of predictions. The system stores every prediction along with the input details in a SQLite database, allowing users to maintain a history of all previous 
  results. It offers an interactive, menu-driven interface that enables users to make predictions, view stored records, and exit the application without needing
  any technical knowledge
