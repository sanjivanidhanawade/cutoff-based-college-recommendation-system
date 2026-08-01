# Cut-Off Based College Recommendation System

A desktop application (Tkinter GUI) that predicts/recommends colleges to students based on their academic cut-off marks, using machine learning classification models.

## Features

- User registration and login (SQLite-backed)
- College admission prediction using multiple ML models:
  - Support Vector Machine (SVM)
  - Random Forest Classifier
  - Decision Tree Classifier
- Model training pipeline with accuracy/classification reports (`train.py`)
- Simple, animated Tkinter GUI with video splash screen

## Tech Stack

- Python, Tkinter (GUI)
- scikit-learn (SVM, Random Forest, Decision Tree)
- pandas, numpy
- SQLite (user auth)
- OpenCV / tkvideo (video playback), Pillow (images)

## Project Structure

```
GUI_main.py          Entry point - launches the main GUI
login.py              Login screen
registration.py       User registration screen
train.py               Model training (SVM / RF / DT)
Check_Prediction.py   Runs prediction using trained models
*.joblib               Pre-trained model files
Admission_Predict.csv  Dataset
dataset.csv
train.csv
assets/                 UI images
demo/                   Demo videos
```

## Getting Started

```bash
pip install -r requirements.txt
python GUI_main.py
```

## Demo

See the `demo/` folder for a walkthrough of the application in action.
