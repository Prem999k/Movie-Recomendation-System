import streamlit as st
import pickle
import pandas as pd
from sklearn.metrics.pairwise import cosine_similarity
import warnings
warnings.filterwarnings("ignore")

# =============================
# LOAD DATA
# =============================
df = pickle.load(open("df.pkl", "rb"))
tfidf_matrix = pickle.load(open("tfidf_matrix.pkl", "rb"))

indices = pd.Series(df.index, index=df['title']).drop_duplicates()

# =============================
# RECOMMEND FUNCTION (SAFE)
# =============================
def recommend(movie):
    if movie is None or movie not in indices:
        return pd.DataFrame()

    idx = indices[movie]

    sim_scores = cosine_similarity(tfidf_matrix[idx], tfidf_matrix).flatten()
    sim_indices = sim_scores.argsort()[::-1][1:11]

    # Safety check
    sim_indices = [i for i in sim_indices if i < len(df)]

    return df.iloc[sim_indices]

# =============================
# PAGE CONFIG
# =============================
st.set_page_config(page_title="Movie Recommender", page_icon="🎬")

# =============================
# CLEAN PROFESSIONAL THEME 🎨
# =============================
st.markdown("""
<style>
/* Title */ .main-title { font-size: 45px; font-weight: 600; color: #ffff0f; text-align: center; margin-bottom: 5px; } 
/* Subtitle */ .subtitle { text-align: center; color: #94a3b8; font-size: 20px; margin-bottom: 30px; }
/* Inputs */ .stTextInput input, .stSelectbox div[data-baseweb="select"] 
{ background-color: #111827 !important; color: white !important; border-radius: 8px !important; }
/* Button */ .stButton>button { background-color: #2563eb; color: white; border-radius: 8px; font-weight: 500; }
/* Results */ .result-item { padding: 14px; margin-bottom: 10px; border-radius: 10px; background-color: #111827; 
color: #e5e7eb; font-size: 16px; border: 1px solid rgba(255,255,255,0.05); } /* Top result highlight */ .top1 
{ background-color: #1e293b; font-weight: 600; }
</style>
""", unsafe_allow_html=True)

# =============================
# HEADER
# =============================
st.markdown("<div class='main-title'>🎬 Movie Recommender</div>", unsafe_allow_html=True)
st.markdown("<div class='subtitle'>Get similar movies instantly</div>", unsafe_allow_html=True)

# =============================
# SEARCH
# =============================
search = st.text_input("Search movie")

filtered = df[df['title'].str.contains(search, case=False)] if search else df

# Handle empty search result
if len(filtered) == 0:
    st.warning("No movies found. Try another search.")
    st.stop()

selected_movie = st.selectbox("Select movie", filtered['title'].values)

# =============================
# BUTTON
# =============================
if st.button("Recommend"):

    if not selected_movie:
        st.warning("Please select a movie")
        st.stop()

    recs = recommend(selected_movie)

    if recs.empty:
        st.warning("No recommendations found")
        st.stop()

    st.markdown("### Top Recommendations")

    # Top-to-bottom display
    for i, row in enumerate(recs['title']):
        if i == 0:
            st.markdown(
                f"<div class='result-item top1'>⭐ {row}</div>",
                unsafe_allow_html=True
            )
        else:
            st.markdown(
                f"<div class='result-item'>{row}</div>",
                unsafe_allow_html=True
            )
