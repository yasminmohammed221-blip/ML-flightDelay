import streamlit as st
from datetime import date, time


# ============================================================
# PAGE CONFIGURATION
# ============================================================

st.set_page_config(
    page_title="Flight Delay Estimator",
    page_icon="✈️",
    layout="centered",
    initial_sidebar_state="collapsed"
)


# ============================================================
# CUSTOM CSS
# ============================================================

st.markdown("""
<style>

    /* ---------- Main Page ---------- */

    .stApp {
        background-color: #071A33;
        color: white;
    }

    .main {
        background-color: #071A33;
    }

    /* ---------- Remove Streamlit Top Space ---------- */

    .block-container {
        padding-top: 2rem;
        padding-bottom: 3rem;
        max-width: 850px;
    }

    /* ---------- Title ---------- */

    .title {
        text-align: center;
        color: white;
        font-size: 42px;
        font-weight: 800;
        margin-bottom: 5px;
    }

    .subtitle {
        text-align: center;
        color: #B8C7DC;
        font-size: 17px;
        margin-bottom: 35px;
    }

    /* ---------- Section Titles ---------- */

    .section-title {
        color: white;
        font-size: 21px;
        font-weight: 700;
        margin-top: 20px;
        margin-bottom: 15px;
    }

    /* ---------- Input Labels ---------- */

    label {
        color: #EAF1FA !important;
        font-weight: 600 !important;
    }

    /* ---------- Input Boxes ---------- */

    div[data-baseweb="input"] {
        background-color: white;
        border-radius: 10px;
    }

    div[data-baseweb="select"] > div {
        background-color: white;
        border-radius: 10px;
    }

    input {
        color: #071A33 !important;
    }

    /* ---------- Selectbox Text ---------- */

    div[data-baseweb="select"] span {
        color: #071A33 !important;
    }

    /* ---------- Button ---------- */

    .stButton > button {
        width: 100%;
        background-color: white;
        color: #071A33;
        border: none;
        border-radius: 12px;
        padding: 13px;
        font-size: 17px;
        font-weight: 700;
        margin-top: 20px;
        transition: 0.2s;
    }

    .stButton > button:hover {
        background-color: #DCE7F5;
        color: #071A33;
        border: none;
    }

    /* ---------- Route Card ---------- */

    .route-card {
        background-color: #102B4C;
        border: 1px solid #29476A;
        border-radius: 14px;
        padding: 18px;
        text-align: center;
        margin-top: 10px;
        margin-bottom: 20px;
    }

    .route-label {
        color: #AFC0D6;
        font-size: 13px;
        margin-bottom: 5px;
    }

    .route {
        color: white;
        font-size: 20px;
        font-weight: 700;
    }

    /* ---------- Prediction Card ---------- */

    .prediction-card {
        background-color: white;
        border-radius: 18px;
        padding: 28px;
        text-align: center;
        margin-top: 30px;
        box-shadow: 0px 8px 25px rgba(0, 0, 0, 0.25);
    }

    .prediction-title {
        color: #071A33;
        font-size: 18px;
        font-weight: 700;
        margin-bottom: 8px;
    }

    .prediction-number {
        color: #071A33;
        font-size: 42px;
        font-weight: 800;
        margin: 5px;
    }

    .prediction-text {
        color: #52657D;
        font-size: 15px;
    }

    /* ---------- Footer ---------- */

    .footer {
        text-align: center;
        color: #7F94AE;
        font-size: 13px;
        margin-top: 40px;
    }

</style>
""", unsafe_allow_html=True)


# ============================================================
# HEADER
# ============================================================

st.markdown(
    '<div class="title">✈️ Flight Delay Estimator</div>',
    unsafe_allow_html=True
)

st.markdown(
    '<div class="subtitle">'
    'Predict the expected arrival delay of your flight'
    '</div>',
    unsafe_allow_html=True
)


# ============================================================
# FLIGHT INFORMATION
# ============================================================

st.markdown(
    '<div class="section-title">📋 Flight Information</div>',
    unsafe_allow_html=True
)

# Flight date
flight_date = st.date_input(
    "📅 Flight Date",
    value=date.today()
)


# Scheduled departure
departure_time = st.time_input(
    "🕐 Scheduled Departure Time",
    value=time(12, 0)
)


# ============================================================
# FLIGHT DETAILS
# ============================================================

st.markdown(
    '<div class="section-title">🛫 Flight Details</div>',
    unsafe_allow_html=True
)

col1, col2 = st.columns(2)

with col1:

    distance = st.number_input(
        "📏 Distance (miles)",
        min_value=0.0,
        value=500.0,
        step=10.0
    )

with col2:

    scheduled_duration = st.number_input(
        "⏱️ Scheduled Duration (minutes)",
        min_value=1,
        value=120,
        step=5
    )


# ============================================================
# AIRLINE
# ============================================================

airlines = [
    "American Airlines",
    "Delta Air Lines",
    "United Airlines",
    "Southwest Airlines",
    "JetBlue Airways",
    "Alaska Airlines"
]

airline = st.selectbox(
    "✈️ Airline",
    airlines
)


# ============================================================
# AIRPORTS
# ============================================================

col1, col2 = st.columns(2)

with col1:

    origin_airports = [
        "JFK - New York",
        "LAX - Los Angeles",
        "ORD - Chicago",
        "ATL - Atlanta",
        "DFW - Dallas",
        "SFO - San Francisco"
    ]

    origin = st.selectbox(
        "🛫 Origin Airport",
        origin_airports
    )


with col2:

    destination_airports = [
        "JFK - New York",
        "LAX - Los Angeles",
        "ORD - Chicago",
        "ATL - Atlanta",
        "DFW - Dallas",
        "SFO - San Francisco"
    ]

    destination = st.selectbox(
        "🛬 Destination Airport",
        destination_airports
    )


# ============================================================
# ROUTE
# ============================================================

route = f"{origin}  →  {destination}"

st.markdown(
    f"""
    <div class="route-card">
        <div class="route-label">SELECTED ROUTE</div>
        <div class="route">{route}</div>
    </div>
    """,
    unsafe_allow_html=True
)


# ============================================================
# PREDICTION BUTTON
# ============================================================

predict = st.button(
    "🔮 Estimate Flight Delay"
)


# ============================================================
# PREDICTION
# ============================================================

if predict:

    # --------------------------------------------------------
    # TEMPORARY VALUE
    # --------------------------------------------------------
    # This is ONLY for testing the interface.
    # We will replace this with your ML model.
    
    estimated_delay = 23


    # --------------------------------------------------------
    # DISPLAY RESULT
    # --------------------------------------------------------

    st.markdown(
        f"""
        <div class="prediction-card">

            <div class="prediction-title">
                ✈️ Estimated Arrival Delay
            </div>

            <div class="prediction-number">
                {estimated_delay} minutes
            </div>

            <div class="prediction-text">
                This flight is expected to arrive approximately
                {estimated_delay} minutes late.
            </div>

        </div>
        """,
        unsafe_allow_html=True
    )


# ============================================================
# FOOTER
# ============================================================

st.markdown(
    """
    <div class="footer">
        Flight Delay Estimator • Machine Learning Project
    </div>
    """,
    unsafe_allow_html=True
)
