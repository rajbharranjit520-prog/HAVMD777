import streamlit as st
import numpy as np
import matplotlib.pyplot as plt
import pandas as pd

# Simulation Function (SIR Model)
def simulate_awareness(population, initial_viewers, beta, gamma, days):
    S = population - initial_viewers
    I = initial_viewers
    R = 0

    S_list, I_list, R_list = [], [], []

    for t in range(days):
        new_engaged = beta * S * I / population
        new_dropped = gamma * I

        S -= new_engaged
        I += new_engaged - new_dropped
        R += new_dropped

        S_list.append(S)
        I_list.append(I)
        R_list.append(R)

    return S_list, I_list, R_list


# Page Config
st.set_page_config(page_title="Health Awareness Model", layout="centered")

# Title
st.title("📢 Health Awareness Video Modeling Dashboard")
st.write("Model: Awareness Spread using SIR Approach")

# Sidebar Inputs
st.sidebar.header("⚙️ Input Parameters")

population = st.sidebar.slider("Total Population", 1000, 100000, 50000)
initial_viewers = st.sidebar.slider("Initial Viewers", 10, 1000, 100)
beta = st.sidebar.slider("Sharing Rate (β)", 0.01, 1.0, 0.3)
gamma = st.sidebar.slider("Drop Rate (γ)", 0.01, 1.0, 0.1)
days = st.sidebar.slider("Simulation Days", 30, 180, 60)

topic = st.sidebar.selectbox(
    "Health Topic",
    ["Vaccination", "Mental Health", "Hygiene", "Nutrition"]
)

# Topic Effect
if topic == "Vaccination":
    beta *= 1.2
elif topic == "Mental Health":
    gamma *= 1.2
elif topic == "Hygiene":
    beta *= 1.1

# Overview
st.markdown("""
## 📌 Project Overview

This model predicts how a **health awareness video spreads** among a population using:

- 📈 Social sharing behavior  
- 📊 Audience drop-off  
- 📉 Awareness decay  

It helps in:

- Understanding campaign effectiveness  
- Predicting peak awareness  
- Planning awareness strategies  
""")

# Simulation
S_list, I_list, R_list = simulate_awareness(population, initial_viewers, beta, gamma, days)

# Graph
st.subheader("📈 Awareness Spread Over Time")

fig, ax = plt.subplots(figsize=(6,4))
ax.plot(range(days), S_list, label="Unaware")
ax.plot(range(days), I_list, label="Engaged")
ax.plot(range(days), R_list, label="Dropped")

ax.set_xlabel("Days")
ax.set_ylabel("People")
ax.legend()

plt.tight_layout()
st.pyplot(fig)

# Data Table
st.subheader("📊 Awareness Data Table")

df = pd.DataFrame({
    "Day": list(range(days)),
    "Unaware": np.round(S_list, 0),
    "Engaged": np.round(I_list, 0),
    "Dropped": np.round(R_list, 0)
})

st.dataframe(df, use_container_width=True)

# KPIs
peak_viewers = max(I_list)
peak_day = I_list.index(peak_viewers)
R0 = beta / gamma
reach = max(I_list) + max(R_list)

# Insights
st.subheader("🔍 Key Insights")

col1, col2 = st.columns(2)

with col1:
    st.info(f"""
📊 Peak Engagement  
{int(peak_viewers)} people
""")

with col2:
    st.info(f"""
📅 Peak Day  
Day {peak_day}
""")

# Interpretation
if R0 < 1:
    status = "Low Awareness"
elif R0 < 2:
    status = "Moderate Awareness"
else:
    status = "High Awareness (Viral)"

st.success(f"""
💡 Interpretation:

• R₀ < 1 → Weak spread  
• 1 - 2 → Moderate spread  
• >2 → Strong viral spread  

Current Status: **{status}**
""")

# Strategy Suggestion
st.subheader("🚀 Campaign Recommendation")

if R0 > 2:
    st.success("✅ Strong campaign. Maintain engagement.")
elif R0 > 1:
    st.warning("⚠️ Improve sharing rate for better reach.")
else:
    st.error("🚨 Low awareness. Increase promotion urgently.")

# Mathematical Model
st.subheader("📘 Mathematical Model")

st.latex(r"S_{t+1} = S_t - \beta \cdot \frac{S_t I_t}{N}")
st.latex(r"I_{t+1} = I_t + \beta \cdot \frac{S_t I_t}{N} - \gamma I_t")
st.latex(r"R_{t+1} = R_t + \gamma I_t")

st.markdown("""
**Where:**

• S = Unaware population  
• I = Engaged viewers  
• R = Dropped viewers  
• β = Sharing rate  
• γ = Drop rate  
""")

# Conclusion
st.subheader("📌 Conclusion")

st.write(f"""
🔹 Awareness spreads rapidly initially  

🔹 Peaks at Day **{peak_day}**  

🔹 Maximum engagement: **{int(peak_viewers)} people**  

🔹 Total reach: **{int(reach)} people**  

👉 This model helps design effective health awareness campaigns.
""")