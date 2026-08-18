import streamlit as st
import joblib
import pandas as pd
from datetime import date, time


# ============================================================
# 1. PAGE CONFIGURATION
# ============================================================

st.set_page_config(
    page_title="Flight Delay Estimator",
    page_icon="✈️",
    layout="centered",
    initial_sidebar_state="collapsed"
)


# ============================================================
# 2. CUSTOM CSS
# ============================================================

st.markdown("""
<style>

    /* =========================
       MAIN PAGE
       ========================= */

    .stApp {
        background:
            radial-gradient(
                circle at top right,
                #17365d 0%,
                #0b1f38 35%,
                #061426 100%
            );

        color: white;
    }


    /* =========================
       REMOVE DEFAULT TOP SPACE
       ========================= */

    .block-container {
        max-width: 900px;
        padding-top: 3rem;
        padding-bottom: 4rem;
    }


    /* =========================
       HEADER
       ========================= */

    .hero {
        text-align: center;
        padding: 20px 0 35px 0;
    }

    .hero-icon {
        font-size: 55px;
        margin-bottom: 5px;
    }

    .hero-title {
        font-size: 44px;
        font-weight: 800;
        letter-spacing: -1px;
        color: white;
        margin-bottom: 8px;
    }

    .hero-subtitle {
        font-size: 17px;
        color: #a9bbd1;
        max-width: 650px;
        margin: auto;
        line-height: 1.6;
    }


    /* =========================
       SECTION TITLES
       ========================= */

    .section-title {
        font-size: 22px;
        font-weight: 700;
        color: white;
        margin-top: 25px;
        margin-bottom: 15px;
    }


    /* =========================
       LABELS
       ========================= */

    label {
        color: #dbe7f5 !important;
        font-weight: 600 !important;
    }


    /* =========================
       INPUT BOXES
       ========================= */

    div[data-baseweb="input"],
    div[data-baseweb="select"] > div {

        background-color: #ffffff !important;

        border-radius: 10px !important;

        border: 1px solid #d5dfeb !important;
    }


    input {
        color: #10243d !important;
    }


    div[data-baseweb="select"] span {
        color: #10243d !important;
    }


    /* =========================
       NUMBER INPUT BUTTONS
       ========================= */

    button[data-testid="stNumberInputStepDown"],
    button[data-testid="stNumberInputStepUp"] {
        color: #10243d !important;
    }


    /* =========================
       PREDICT BUTTON
       ========================= */

    .stButton > button {

        width: 100%;

        background: linear-gradient(
            90deg,
            #ffffff,
            #dcecff
        );

        color: #09203b;

        border: none;

        border-radius: 12px;

        padding: 14px;

        font-size: 17px;

        font-weight: 800;

        margin-top: 25px;

        transition: all 0.2s ease;
    }


    .stButton > button:hover {

        transform: translateY(-2px);

        box-shadow:
            0px 8px 25px rgba(0, 0, 0, 0.30);

        background: white;

        color: #061a31;
    }


    /* =========================
       ROUTE CARD
       ========================= */

    .route-card {

        background: rgba(255, 255, 255, 0.06);

        border: 1px solid rgba(255, 255, 255, 0.12);

        border-radius: 16px;

        padding: 20px;

        margin-top: 20px;

        text-align: center;

        backdrop-filter: blur(10px);
    }


    .route-label {

        font-size: 12px;

        color: #91a8c2;

        letter-spacing: 2px;

        margin-bottom: 8px;
    }


    .route {

        font-size: 25px;

        font-weight: 800;

        color: white;
    }


    /* =========================
       PREDICTION RESULT
       ========================= */

    .prediction-card {

        background: white;

        border-radius: 20px;

        padding: 30px;

        margin-top: 30px;

        text-align: center;

        box-shadow:
            0px 15px 45px rgba(0, 0, 0, 0.30);
    }


    .prediction-label {

        color: #60748b;

        font-size: 15px;

        font-weight: 600;

        margin-bottom: 5px;
    }


    .prediction-value {

        color: #0a2340;

        font-size: 48px;

        font-weight: 900;

        margin: 5px 0;
    }


    .prediction-description {

        color: #60748b;

        font-size: 15px;
    }


    /* =========================
       FOOTER
       ========================= */

    .footer {

        text-align: center;

        color: #7189a4;

        font-size: 13px;

        margin-top: 45px;

        padding-top: 20px;

        border-top:
            1px solid rgba(255,255,255,0.08);
    }


    /* =========================
       SMALL SCREEN
       ========================= */

    @media (max-width: 600px) {

        .hero-title {
            font-size: 34px;
        }

        .hero-subtitle {
            font-size: 15px;
        }

        .prediction-value {
            font-size: 38px;
        }

    }

</style>
""", unsafe_allow_html=True)


# ============================================================
# 3. LOAD TRAINED MODEL
# ============================================================

model = joblib.load(
    r"C:\Users\Dell\Desktop\yasmin.python\ai.huawei\project\Flight Delay project\flight_delay_model.joblib"
)


# ============================================================
# 4. HEADER
# ============================================================

st.markdown("""
<div class="hero">

    <div class="hero-icon">
        ✈️
    </div>

    <div class="hero-title">
        Flight Delay Estimator
    </div>

    <div class="hero-subtitle">
        Predict the expected arrival delay of a flight
        using machine learning and scheduled flight information.
    </div>

</div>
""", unsafe_allow_html=True)


# ============================================================
# 5. DATE
# ============================================================

st.markdown(
    '<div class="section-title">📅 Flight Date</div>',
    unsafe_allow_html=True
)

flight_date = st.date_input(
    "Select flight date",
    value=date(2008, 1, 1)
)

year = flight_date.year
month = flight_date.month
day_of_month = flight_date.day

day_of_week = flight_date.weekday() + 1


# ============================================================
# 6. SCHEDULED TIMES
# ============================================================

st.markdown(
    '<div class="section-title">🕐 Scheduled Flight Times</div>',
    unsafe_allow_html=True
)

col1, col2 = st.columns(2)

with col1:

    departure_time = st.time_input(
        "Scheduled departure",
        value=time(12, 0)
    )

with col2:

    arrival_time = st.time_input(
        "Scheduled arrival",
        value=time(14, 0)
    )


crs_dep_time = (
    departure_time.hour * 100
    + departure_time.minute
)

crs_arr_time = (
    arrival_time.hour * 100
    + arrival_time.minute
)


# ============================================================
# 7. AIRLINE
# ============================================================

st.markdown(
    '<div class="section-title">✈️ Airline</div>',
    unsafe_allow_html=True
)

airlines = [
    "AA",
    "AS",
    "CO",
    "DL",
    "EA",
    "HP",
    "NW",
    "PA",
    "PI",
    "TW",
    "UA",
    "US",
    "WN"
]

unique_carrier = st.selectbox(
    "Select airline",
    airlines
)


# ============================================================
# 8. ROUTE
# ============================================================

st.markdown(
    '<div class="section-title">🛫 Flight Route</div>',
    unsafe_allow_html=True
)

col1, col2 = st.columns(2)

with col1:

    origin = st.text_input(
        "Origin airport code",
        value="LAX",
        max_chars=3
    ).upper()

with col2:

    destination = st.text_input(
        "Destination airport code",
        value="JFK",
        max_chars=3
    ).upper()


st.caption(
    "Enter the 3-letter airport codes used in the dataset, "
    "such as LAX, JFK, ATL, ORD, etc."
)


# ============================================================
# 9. FLIGHT DETAILS
# ============================================================

st.markdown(
    '<div class="section-title">📊 Flight Details</div>',
    unsafe_allow_html=True
)

col1, col2 = st.columns(2)

with col1:

    distance = st.number_input(
        "Distance (miles)",
        min_value=1.0,
        value=500.0,
        step=10.0
    )

with col2:

    scheduled_duration = st.number_input(
        "Scheduled duration (minutes)",
        min_value=1.0,
        value=120.0,
        step=5.0
    )


# ============================================================
# 10. ROUTE PREVIEW
# ============================================================

st.markdown(
    f"""
    <div class="route-card">

        <div class="route-label">
            SELECTED ROUTE
        </div>

        <div class="route">
            {origin} &nbsp; ✈️ &nbsp; {destination}
        </div>

    </div>
    """,
    unsafe_allow_html=True
)


# ============================================================
# 11. PREDICTION BUTTON
# ============================================================

predict = st.button(
    "🔮 Estimate Arrival Delay"
)


# ============================================================
# 12. MAKE PREDICTION
# ============================================================

if predict:

    input_data = pd.DataFrame({

        "Year": [year],

        "Month": [month],

        "DayofMonth": [day_of_month],

        "DayOfWeek": [day_of_week],

        "CRSDepTime": [crs_dep_time],

        "CRSArrTime": [crs_arr_time],

        "UniqueCarrier": [unique_carrier],

        "CRSElapsedTime": [scheduled_duration],

        "Origin": [origin],

        "Dest": [destination],

        "Distance": [distance]

    })


    prediction = model.predict(input_data)[0]


    # ========================================================
    # DISPLAY RESULT
    # ========================================================

    if prediction < 0:

        message = (
            f"The flight is expected to arrive "
            f"{abs(prediction):.1f} minutes early."
        )

    else:

        message = (
            f"The flight is expected to arrive "
            f"{prediction:.1f} minutes late."
        )


    st.markdown(
        f"""
        <div class="prediction-card">

            <div class="prediction-label">
                ESTIMATED ARRIVAL DELAY
            </div>

            <div class="prediction-value">
                {prediction:.1f} min
            </div>

            <div class="prediction-description">
                {message}
            </div>

        </div>
        """,
        unsafe_allow_html=True
    )


# ============================================================
# 13. FOOTER
# ============================================================

st.markdown(
    """
    <div class="footer">

        Flight Delay Estimator
        • Machine Learning Project
        • Gradient Boosting

    </div>
    """,
    unsafe_allow_html=True
)
