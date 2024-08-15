# Iris Classifier Web Application

This web application predicts the species of iris flower based on user input for sepal length, sepal width, petal length, and petal width. It uses the famous Iris dataset and is connected to the back end via Anvil. This project demonstrates how to build a basic machine learning model and integrate it with a web app interface using Anvil.

## Features

- **Iris Species Prediction**: Users input the four features of an iris flower (sepal length, sepal width, petal length, and petal width), and the app predicts the species of the flower.
- **Interactive UI**: A user-friendly interface built using Anvil's framework, allowing seamless interaction with the machine learning model.
- **Server-side Integration**: The model is hosted on the server and predictions are made using `anvil.server.call()` function.

## How It Works

1. **User Input**: The user provides the values for the four attributes: sepal length, sepal width, petal length, and petal width.
2. **Prediction**: Once the user submits the data by clicking the button, the app sends a request to the backend server to run the `predict_iris` function.
3. **Display Results**: The app returns the predicted iris species and displays it in the UI.


## Project Structure

- **Frontend**: Built with Anvil Designer, this includes the user interface for collecting input and displaying the prediction.
- **Backend**: A server-side script (not provided here) that contains the machine learning model to predict the iris species.

## How to Run

1. Clone this repository or open it in Anvil's app editor.
2. Define the server function `predict_iris` on the server-side. You can create this using Python and a pre-trained iris classification model.
3. Input values for sepal length, sepal width, petal length, and petal width in the form fields.
4. Click the "Predict" button to get the iris species.

## Dependencies

- [Anvil](https://anvil.works/)
- Python (Anvil environment)


