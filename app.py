import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
from scipy.stats import pearsonr, linregress, t

st.title("Student Food Spending")
st.write("Statistical and Probability Analysis")

st.header("Our Research")

st.header("Research Question")

st.write(
    "How much do university students spend on food and drinks "
    "during their university days?"
)

st.write(
    "This project investigates how much university students "
    "spend on food and drinks during their university days."
)

st.write(
    "We collected anonymous data from students and used "
    "statistical and probability methods to analyze their spending."
)

st.header("Student Data")

data = {
    "Student": list(range(1, 41)),

    "Days at University": [
        5, 4, 5, 3, 4, 5, 4, 5, 3, 5,
        4, 5, 3, 4, 5, 4, 5, 3, 4, 5,
        5, 3, 4, 5, 4, 5, 3, 4, 5, 4,
        5, 4, 3, 5, 4, 5, 3, 4, 5, 4
    ],

    "Daily Spending": [
        1500, 1050, 1800, 950, 1400, 2200, 1250, 1900, 1100, 2500,
        1350, 2100, 900, 1600, 2300, 1200, 1750, 1000, 1450, 2600,
        2000, 1150, 1550, 1850, 1300, 2400, 950, 1700, 2250, 1350,
        1900, 1250, 1050, 2150, 1500, 1800, 1000, 1600, 2350, 1400
    ],

    "Coffee/Drinks": [
        500, 550, 500, 0, 500, 550, 500, 550, 0, 500,
        500, 550, 0, 500, 550, 500, 500, 0, 500, 550,
        500, 0, 500, 550, 500, 550, 0, 500, 550, 500,
        550, 500, 0, 550, 500, 500, 0, 500, 550, 500
    ],

    "Lunch Spending": [
        1000, 500, 1300, 950, 900, 1650, 750, 1350, 1100, 2000,
        850, 1550, 900, 1100, 1750, 700, 1250, 1000, 950, 2050,
        1500, 1150, 1050, 1300, 800, 1850, 950, 1200, 1700, 850,
        1350, 750, 1050, 1600, 1000, 1300, 1000, 1100, 1800, 900
    ]
}

df = pd.DataFrame(data)

df["Weekly Spending"] = (
    df["Daily Spending"] * df["Days at University"]
)

st.dataframe(df)

st.header("Basic Statistics")

total_students = len(df)
average = df["Daily Spending"].mean()
median = df["Daily Spending"].median()
minimum = df["Daily Spending"].min()
maximum = df["Daily Spending"].max()
std = df["Daily Spending"].std()

st.write("Number of students:", total_students)

st.write("Average daily spending:", round(average), "₸")
st.write("Median daily spending:", round(median), "₸")
st.write("Minimum daily spending:", minimum, "₸")
st.write("Maximum daily spending:", maximum, "₸")
st.write("Standard deviation:", round(std), "₸")

st.header("Confidence Interval")

mean = df["Daily Spending"].mean()
std = df["Daily Spending"].std()
n = len(df)

confidence_level = 0.95
degrees_of_freedom = n - 1

t_value = t.ppf(
    (1 + confidence_level) / 2,
    degrees_of_freedom
)

margin_of_error = t_value * (std / (n ** 0.5))

lower_bound = mean - margin_of_error
upper_bound = mean + margin_of_error

st.write(
    "95% Confidence Interval for average daily spending:"
)

st.subheader(
    f"{lower_bound:.0f} ₸ — {upper_bound:.0f} ₸"
)

st.write(
    "We are 95% confident that the true average daily "
    "food spending of students is within this interval."
)

st.header("Probability Calculator")

st.subheader("Daily Spending")

daily_amount = st.selectbox(
    "Choose a daily spending amount:",
    [1000, 1500, 2000, 2500]
)

daily_above = (df["Daily Spending"] > daily_amount).sum()

daily_probability = daily_above / len(df)

st.write(
    f"Number of students spending more than {daily_amount} ₸: "
    f"{daily_above}"
)

st.write(
    f"Probability of spending more than {daily_amount} ₸ per day:"
)

st.subheader(f"{daily_probability * 100:.1f}%")


st.subheader("Weekly Spending")

weekly_amount = st.selectbox(
    "Choose a weekly spending amount:",
    [5000, 10000, 15000]
)

weekly_above = (df["Weekly Spending"] > weekly_amount).sum()

weekly_probability = weekly_above / len(df)

st.write(
    f"Number of students spending more than {weekly_amount} ₸ per week: "
    f"{weekly_above}"
)

st.write(
    f"Probability of spending more than {weekly_amount} ₸ per week:"
)

st.subheader(f"{weekly_probability * 100:.1f}%")

st.header("Distribution of Daily Spending")

st.write(
    "This histogram shows how daily food spending is distributed among students."
)

fig, ax = plt.subplots()

ax.hist(df["Daily Spending"], bins=5)

ax.set_xlabel("Daily Spending (₸)")
ax.set_ylabel("Number of Students")
ax.set_title("Distribution of Daily Food Spending")

st.pyplot(fig)
st.header("Days at University and Food Spending")

st.write(
    "This scatter plot shows the relationship between the number of days "
    "students spend at university and their daily food spending."
)

fig2, ax2 = plt.subplots()

ax2.scatter(
    df["Days at University"],
    df["Daily Spending"]
)

ax2.set_xlabel("Days at University")
ax2.set_ylabel("Daily Spending (₸)")
ax2.set_title("Days at University vs Daily Spending")

st.pyplot(fig2)

st.header("Correlation Analysis")

correlation = df["Days at University"].corr(df["Daily Spending"])

st.write(
    "Correlation between days at university and daily food spending:"
)

st.subheader(f"r = {correlation:.2f}")

st.write(
    "The result shows a strong positive correlation. "
    "Students who spend more days at university tend to spend more money on food."
)

st.write(
    "However, correlation does not mean causation. "
    "Other factors may also affect food spending."
)

st.header("Linear Regression")

x = df["Days at University"]
y = df["Daily Spending"]

slope, intercept, r_value, p_value_reg, std_err = linregress(x, y)

st.write(
    f"Regression equation: Daily Spending = "
    f"{slope:.2f} × Days at University + {intercept:.2f}"
)

st.write(
    f"Slope: {slope:.2f}"
)

st.write(
    f"R² = {r_value**2:.2f}"
)

st.write(
    "The regression shows how daily food spending changes "
    "with the number of days students spend at university."
)

fig3, ax3 = plt.subplots()

ax3.scatter(x, y)

ax3.plot(
    x,
    intercept + slope * x
)

ax3.set_xlabel("Days at University")
ax3.set_ylabel("Daily Spending (₸)")
ax3.set_title("Linear Regression: Days at University vs Daily Spending")

st.pyplot(fig3)

st.header("Hypothesis Testing")

r, p_value = pearsonr(
    df["Days at University"],
    df["Daily Spending"]
)

alpha = 0.05

st.write("Null hypothesis (H₀): There is no significant correlation.")
st.write("Alternative hypothesis (H₁): There is a significant correlation.")
st.write("Significance level (α): 0.05")

st.write(f"Pearson correlation: r = {r:.2f}")
st.write(f"P-value: {p_value:.6f}")

if p_value < alpha:
    st.write(
        "Result: Reject H₀. The correlation is statistically significant."
    )
else:
    st.write(
        "Result: Fail to reject H₀. The correlation is not statistically significant."
    )

st.header("Conclusion")

st.write(
    f"The average student spends about {round(average):,} ₸ per day on food."
)

st.write(
    f"The probability of spending more than 2,000 ₸ per day is "
    f"{(df['Daily Spending'] > 2000).mean() * 100:.1f}%."
)

st.write(
    f"The correlation between days at university and daily food spending "
    f"is strong (r = {correlation:.2f})."
)

st.write(
    f"The hypothesis test gives a p-value of {p_value:.4f}, "
    "which is less than 0.05. Therefore, we reject the null hypothesis."
)

st.write(
    f"The linear regression model has an R² value of {r_value**2:.2f}, "
    "which shows how much of the variation in daily food spending "
    "is explained by the number of days at university."
)

st.write(
    "This means that there is a statistically significant relationship "
    "between the number of days students spend at university and their "
    "daily food spending. However, correlation does not prove causation."
)