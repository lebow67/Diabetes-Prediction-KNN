import gradio as gr
import pandas as pd
import joblib

# Load saved files
model = joblib.load("diabetes_model.pkl")
scaler = joblib.load("scaler.pkl")
expected_columns = joblib.load("columns.pkl")


def predict(
    pregnancies,
    glucose,
    blood_pressure,
    skin_thickness,
    insulin,
    bmi,
    diabetes_pedigree,
    age,
):

    row = {
        "Pregnancies": pregnancies,
        "Glucose": glucose,
        "BloodPressure": blood_pressure,
        "SkinThickness": skin_thickness,
        "Insulin": insulin,
        "BMI": bmi,
        "DiabetesPedigreeFunction": diabetes_pedigree,
        "Age": age,
    }

    input_df = pd.DataFrame([row])

    # Keep feature order correct
    input_df = input_df[expected_columns]

    # Scale
    scaled = scaler.transform(input_df)

    # Predict
    prediction = model.predict(scaled)[0]

    # Confidence
    confidence = model.predict_proba(scaled)[0].max() * 100

    if prediction == 1:
        result = f"""
# 🔴 Diabetic

### Confidence: **{confidence:.2f}%**
"""
    else:
        result = f"""
# 🟢 Not Diabetic

### Confidence: **{confidence:.2f}%**
"""

    return result


with gr.Blocks(theme=gr.themes.Soft(), title="Diabetes Prediction") as demo:

    gr.Markdown(
        """
# 🩺 Diabetes Prediction using K-Nearest Neighbors

Enter the patient's medical information below and click **Predict**.

This model was trained using the **Pima Indians Diabetes Dataset**.
"""
    )

    with gr.Row():

        with gr.Column():

            pregnancies = gr.Slider(
                0, 17, value=2, step=1,
                label="Pregnancies"
            )

            glucose = gr.Slider(
                0, 200, value=120,
                label="Glucose"
            )

            blood_pressure = gr.Slider(
                0, 130, value=70,
                label="Blood Pressure"
            )

            skin_thickness = gr.Slider(
                0, 100, value=20,
                label="Skin Thickness"
            )

        with gr.Column():

            insulin = gr.Slider(
                0, 900, value=80,
                label="Insulin"
            )

            bmi = gr.Slider(
                0.0, 70.0,
                value=25.0,
                step=0.1,
                label="BMI"
            )

            diabetes_pedigree = gr.Slider(
                0.0,
                3.0,
                value=0.5,
                step=0.01,
                label="Diabetes Pedigree Function"
            )

            age = gr.Slider(
                18,
                90,
                value=30,
                step=1,
                label="Age"
            )

    predict_btn = gr.Button("🔍 Predict", variant="primary")

    output = gr.Markdown()

    predict_btn.click(
        fn=predict,
        inputs=[
            pregnancies,
            glucose,
            blood_pressure,
            skin_thickness,
            insulin,
            bmi,
            diabetes_pedigree,
            age,
        ],
        outputs=output,
    )

demo.launch()