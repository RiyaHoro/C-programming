import pickle
from pathlib import Path
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import LabelEncoder
from sklearn.tree import DecisionTreeClassifier
from sklearn.metrics import classification_report

BASE_DIR = Path(__file__).resolve().parent.parent
DATASET_PATH = BASE_DIR / 'datasets' / 'career_dataset.csv'
MODEL_PATH = BASE_DIR / 'ml_model' / 'career_model.pkl'
ENCODER_PATH = BASE_DIR / 'ml_model' / 'encoders.pkl'


def main():
    df = pd.read_csv(DATASET_PATH)
    encoders = {}

    for col in ['education', 'interest', 'work_preference', 'primary_skill', 'career']:
        le = LabelEncoder()
        df[col] = le.fit_transform(df[col].str.lower())
        encoders[col if col != 'work_preference' else 'work'] = le

    x = df[['age', 'education', 'interest', 'work_preference', 'primary_skill']]
    y = df['career']

    x_train, x_test, y_train, y_test = train_test_split(
        x, y, test_size=0.2, random_state=42, stratify=y
    )

    model = DecisionTreeClassifier(max_depth=6, random_state=42)
    model.fit(x_train, y_train)

    y_pred = model.predict(x_test)
    print(classification_report(y_test, y_pred, zero_division=0))

    with open(MODEL_PATH, 'wb') as model_file:
        pickle.dump(model, model_file)

    with open(ENCODER_PATH, 'wb') as encoder_file:
        pickle.dump(
            {
                'education': encoders['education'],
                'interest': encoders['interest'],
                'work': encoders['work'],
                'skill': encoders['primary_skill'],
                'career': encoders['career'],
            },
            encoder_file,
        )


if __name__ == '__main__':
    main()
