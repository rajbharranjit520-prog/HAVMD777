# 📢 Health Awareness Video Modeling Dashboard

## 📌 Project Overview

This project simulates how a **health awareness video spreads among a population** over time using a mathematical approach inspired by the SIR (Susceptible–Infected–Recovered) model.

The dashboard helps analyze:

* Awareness spread dynamics
* Audience engagement behavior
* Drop-off trends
* Campaign effectiveness

---

## 🎯 Objective

The main objective of this project is to:

* Model the spread of awareness through social sharing
* Predict peak engagement and reach
* Analyze how quickly awareness declines
* Assist in designing better awareness campaigns

---

## 🧠 Methodology

The model is based on a modified SIR framework:

* **S (Unaware Population)** → People who have not seen the video
* **I (Engaged Viewers)** → People actively watching/sharing
* **R (Dropped Viewers)** → People who lost interest

### Mathematical Equations:

S(t+1) = S(t) - β * S * I / N
I(t+1) = I(t) + β * S * I / N - γ * I
R(t+1) = R(t) + γ * I

Where:

* β = Sharing Rate
* γ = Drop Rate
* N = Total Population

---

## ⚙️ Features

### 🔹 Interactive Inputs

* Total Population
* Initial Viewers
* Sharing Rate (β)
* Drop Rate (γ)
* Simulation Days
* Health Topic Selection

---

### 🔹 Dashboard Outputs

* Peak Engagement
* Peak Day
* Awareness Factor (R₀)
* Total Reach
* Campaign Insights

---

### 🔹 Visualizations

* Awareness Spread Line Graph
* Daily Engagement Growth
* Engagement Distribution Histogram

---

### 🔹 Insights & Recommendations

* Awareness level classification (Low / Moderate / High)
* Campaign performance analysis
* Strategic recommendations

---

## 🛠️ Technologies Used

* Python
* Streamlit
* NumPy
* Pandas
* Matplotlib

---

## ▶️ How to Run the Project

### Step 1: Install Dependencies

```bash
pip install streamlit pandas numpy matplotlib
```

### Step 2: Run the Application

```bash
streamlit run app.py
```

### Step 3: Open in Browser

```
http://localhost:8501
```

---

## 📊 Use Cases

* Public health awareness campaigns
* Digital marketing analysis
* Social media engagement prediction
* Educational simulation of information spread

---

## 🚀 Future Enhancements

* Integration with real-world data
* Advanced visualization using Plotly
* AI-based prediction models
* Multi-platform campaign simulation

---

## 📌 Conclusion

This project demonstrates how mathematical modeling can be used to simulate and analyze the effectiveness of health awareness campaigns.

It provides valuable insights into:

* How fast awareness spreads
* When engagement peaks
* How audience interest declines

👉 This can help in planning more effective and impactful awareness strategies.

---

## 👨‍💻 Author

Adityanath Yadav

---

## ⭐ Acknowledgement

This project is developed as part of academic learning in data analytics and simulation modeling.
