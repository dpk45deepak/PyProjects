import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# ------------------ PAGE CONFIG ------------------
st.set_page_config(
    page_title="Food Delivery Dashboard",
    page_icon="🍔",
    layout="wide"
)

# ------------------ LOAD DATA ------------------
@st.cache_data
def load_data():
    return pd.read_csv("src/data/dataset.csv")

df = load_data()

# ------------------ SIDEBAR ------------------
st.sidebar.title("🔎 Filters")

selected_gender = st.sidebar.multiselect(
    "Select Gender",
    df["Gender"].unique(),
    default=df["Gender"].unique()
)

selected_occupation = st.sidebar.multiselect(
    "Select Occupation",
    df["Occupation"].unique(),
    default=df["Occupation"].unique()
)

age_range = st.sidebar.slider(
    "Select Age Range",
    int(df["Age"].min()),
    int(df["Age"].max()),
    (int(df["Age"].min()), int(df["Age"].max()))
)

# Apply Filters
filtered_df = df[
    (df["Gender"].isin(selected_gender)) &
    (df["Occupation"].isin(selected_occupation)) &
    (df["Age"].between(age_range[0], age_range[1]))
]

# ------------------ HEADER ------------------
st.markdown(
    """
    <h1 style='text-align:center; color:#ff4b4b'>
    🍔 Online Food Delivery Customer Analytics Dashboard
    </h1>
    """,
    unsafe_allow_html=True
)

st.markdown("---")

# ------------------ KPI SECTION ------------------
st.subheader("📊 Key Insights")

col1, col2, col3, col4 = st.columns(4)

col1.metric("👥 Total Customers", len(filtered_df))

col2.metric(
    "😊 Satisfaction Rate",
    f"{round(filtered_df['Output'].value_counts(normalize=True)['Yes']*100,1)}%"
)

col3.metric(
    "🎓 Student Users",
    f"{round(filtered_df['Occupation'].value_counts(normalize=True).get('Student',0)*100,1)}%"
)

col4.metric(
    "👨 Male Users",
    f"{round(filtered_df['Gender'].value_counts(normalize=True).get('Male',0)*100,1)}%"
)

st.markdown("---")

# ------------------ DEMOGRAPHICS ------------------
st.subheader("👥 Customer Demographics")

col1, col2 = st.columns(2)

with col1:
    fig, ax = plt.subplots(figsize=(6,4))
    sns.histplot(filtered_df["Age"], bins=20, color="#ff4b4b", ax=ax)
    ax.set_title("Age Distribution")
    st.pyplot(fig)

with col2:
    fig, ax = plt.subplots(figsize=(6,4))
    filtered_df["Gender"].value_counts().plot(
        kind="pie", autopct="%1.1f%%", colors=["#ff4b4b","#4CAF50"], ax=ax
    )
    ax.set_ylabel("")
    st.pyplot(fig)

# ------------------ OCCUPATION ------------------
st.subheader("💼 Occupation Analysis")

fig, ax = plt.subplots(figsize=(8,4))
filtered_df["Occupation"].value_counts().plot(
    kind="bar", color="#4CAF50", ax=ax
)
ax.set_title("Occupation Distribution")
st.pyplot(fig)

# ------------------ INCOME ------------------
st.subheader("💰 Income Distribution")

fig, ax = plt.subplots(figsize=(8,4))
filtered_df["Monthly Income"].value_counts().plot(
    kind="bar", color="#ff9800", ax=ax
)
ax.set_title("Income Categories")
st.pyplot(fig)

# ------------------ MOTIVATION ------------------
st.subheader("🔥 Reasons for Using Food Delivery")

reasons = [
    "Ease and convenient",
    "Time saving",
    "More restaurant choices",
    "Easy Payment option"
]

cols = st.columns(2)

for i, reason in enumerate(reasons):
    with cols[i % 2]:
        fig, ax = plt.subplots(figsize=(6,4))
        filtered_df[reason].value_counts().plot(
            kind="bar", color="#2196F3", ax=ax
        )
        ax.set_title(reason)
        st.pyplot(fig)

# ------------------ SATISFACTION ------------------
st.subheader("😊 Customer Satisfaction")

fig, ax = plt.subplots(figsize=(5,5))
filtered_df["Output"].value_counts().plot(
    kind="pie",
    autopct="%1.1f%%",
    colors=["#4CAF50","#ff4b4b"],
    ax=ax
)
ax.set_ylabel("")
st.pyplot(fig)

st.markdown("---")

# ------------------ FOOTER ------------------
st.markdown(
    """
    <p style='text-align:center; color:gray'>
    Built with ❤️ using Streamlit | Data Analytics Project
    </p>
    """,
    unsafe_allow_html=True
)