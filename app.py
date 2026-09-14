from pathlib import Path
import pandas as pd
import streamlit as st


def render_markup(body, unsafe_allow_html=False):
    if unsafe_allow_html:
        # Indented lines after blank lines become Markdown code blocks.
        body = "\n".join(line.lstrip() for line in body.splitlines())
    return st.markdown(body, unsafe_allow_html=unsafe_allow_html)


# =========================================================
# PAGE CONFIG
# =========================================================
st.set_page_config(
    page_title="Partner Hub",
    page_icon="🤝",
    layout="wide"
)


# =========================================================
# PATHS
# =========================================================
BASE_DIR = Path(__file__).resolve().parent
DATA_FILE = BASE_DIR / "data" / "partners.xlsx"


# =========================================================
# LOAD DATA
# =========================================================
@st.cache_data
def load_partners():

    if not DATA_FILE.exists():
        return pd.DataFrame(
            columns=[
                "category",
                "partner_name",
                "country",
                "description",
                "advantages",
                "website"
            ]
        )

    return pd.read_excel(DATA_FILE).fillna("")


df = load_partners()


# =========================================================
# SESSION STATE
# =========================================================
if "presentation" not in st.session_state:
    st.session_state.presentation = False


# =========================================================
# GLOBAL CSS
# =========================================================
render_markup(
    """
    <style>

    /* ===========================
       MAIN BACKGROUND
    =========================== */

    .stApp {
        background:
            radial-gradient(
                circle at top right,
                rgba(0, 180, 216, 0.10),
                transparent 25%
            ),
            linear-gradient(
                135deg,
                #07111f 0%,
                #0b1728 45%,
                #0d1928 100%
            );

        color: white;
    }


    /* ===========================
       MAIN CONTAINER
    =========================== */

    .block-container {
        max-width: 1450px;
        padding-top: 2rem;
        padding-bottom: 4rem;
    }


    /* ===========================
       SIDEBAR
    =========================== */

    [data-testid="stSidebar"] {
        background:
            linear-gradient(
                180deg,
                #081321 0%,
                #0d1a2b 100%
            );

        border-right:
            1px solid rgba(255,255,255,0.07);
    }


    [data-testid="stSidebar"] * {
        color: #ffffff;
    }


    /* ===========================
       HERO
    =========================== */

    .hero {

        padding: 38px 42px;

        border-radius: 26px;

        background:
            linear-gradient(
                120deg,
                #0066ff,
                #00a9d6
            );

        margin-bottom: 32px;

        box-shadow:
            0px 20px 50px
            rgba(0, 110, 255, 0.20);

        position: relative;

        overflow: hidden;
    }


    .hero:after {

        content: "";

        position: absolute;

        width: 320px;
        height: 320px;

        right: -100px;
        top: -150px;

        border-radius: 50%;

        background:
            rgba(255,255,255,0.10);
    }


    .hero h1 {

        margin: 0;

        font-size: 46px;

        font-weight: 800;

        letter-spacing: -1px;
    }


    .hero p {

        margin-top: 12px;

        margin-bottom: 0;

        font-size: 18px;

        opacity: 0.92;
    }


    /* ===========================
       SECTION TITLE
    =========================== */

    .section-title {

        font-size: 29px;

        font-weight: 750;

        margin-top: 25px;

        margin-bottom: 20px;
    }


    /* ===========================
       CATEGORY CARD
    =========================== */

    .category-card {

        background:
            linear-gradient(
                145deg,
                rgba(20,39,64,0.96),
                rgba(10,23,40,0.96)
            );

        border:
            1px solid rgba(255,255,255,0.07);

        padding: 25px;

        border-radius: 21px;

        min-height: 155px;

        margin-bottom: 18px;

        transition: 0.25s ease;

        box-shadow:
            0px 10px 30px rgba(0,0,0,0.15);
    }


    .category-card:hover {

        transform: translateY(-5px);

        border-color:
            rgba(0,180,216,0.40);

        box-shadow:
            0px 18px 40px rgba(0,0,0,0.25);
    }


    .category-icon {

        font-size: 34px;

        margin-bottom: 15px;
    }


    .category-title {

        font-size: 21px;

        font-weight: 700;

        margin-bottom: 7px;
    }


    /* ===========================
       PARTNER CARD
    =========================== */

    .partner-card {

        background:
            linear-gradient(
                145deg,
                rgba(20,35,57,0.97),
                rgba(10,22,38,0.97)
            );

        border:
            1px solid rgba(255,255,255,0.07);

        padding: 28px;

        border-radius: 22px;

        margin-bottom: 18px;

        box-shadow:
            0px 10px 30px rgba(0,0,0,0.16);
    }


    .partner-card:hover {

        border-color:
            rgba(0,180,216,0.25);
    }


    .partner-name {

        font-size: 26px;

        font-weight: 750;

        margin-bottom: 8px;
    }


    .badge {

        display: inline-block;

        padding: 5px 12px;

        border-radius: 50px;

        background:
            rgba(0,180,216,0.13);

        border:
            1px solid rgba(0,180,216,0.22);

        color: #65dcff;

        font-size: 13px;

        margin-right: 8px;
    }


    .country {

        color: #b1bfd0;

        font-size: 14px;

        margin-top: 13px;
    }


    .small-text {

        color: #aab8c9;

        font-size: 14px;
    }


    .description {

        margin-top: 20px;

        line-height: 1.7;

        color: #dbe4ee;

        font-size: 15px;
    }


    /* ===========================
       METRICS
    =========================== */

    div[data-testid="stMetric"] {

        background:
            linear-gradient(
                145deg,
                rgba(21,39,62,0.96),
                rgba(11,24,41,0.96)
            );

        border:
            1px solid rgba(255,255,255,0.07);

        padding: 20px;

        border-radius: 19px;

        box-shadow:
            0px 10px 25px rgba(0,0,0,0.12);
    }


    [data-testid="stMetricValue"],
    [data-testid="stMetricValue"] * {
        color: #ffffff !important;
    }

    [data-testid="stMetricLabel"],
    [data-testid="stMetricLabel"] * {
        color: #dbe4ee !important;
    }


    /* ===========================
       INPUTS
    =========================== */

    div[data-baseweb="select"] > div {

        background-color:
            rgba(255,255,255,0.04);

        border-radius: 12px;
    }


    div[data-testid="stTextInput"] input {

        background-color:
            rgba(255,255,255,0.04);

        border-radius: 12px;

        color: white;
    }


    /* ===========================
       BUTTONS
    =========================== */

    .stButton > button {

        border-radius: 12px;

        border:
            1px solid rgba(255,255,255,0.10);

        background:
            linear-gradient(
                120deg,
                #1266e8,
                #019bc3
            );

        color: white;

        font-weight: 600;

        transition: .2s;
    }


    .stButton > button:hover {

        transform: translateY(-2px);

        border-color: #5edaff;
    }


    /* ===========================
       PRESENTATION CARD
    =========================== */

    .presentation-card {

        margin-top: 25px;

        padding: 55px;

        border-radius: 30px;

        background:
            linear-gradient(
                135deg,
                rgba(20,45,75,0.98),
                rgba(8,17,31,0.99)
            );

        border:
            1px solid rgba(255,255,255,.10);

        box-shadow:
            0px 25px 70px rgba(0,0,0,.25);
    }


    .presentation-partner {

        font-size: 52px;

        line-height: 1.1;

        font-weight: 850;

        letter-spacing: -1.5px;
    }


    .presentation-subtitle {

        color: #5ed9ff;

        margin-top: 14px;

        font-size: 19px;
    }


    .presentation-description {

        margin-top: 40px;

        font-size: 21px;

        line-height: 1.75;

        color: #dce5ef;
    }


    .presentation-heading {

        margin-top: 40px;

        margin-bottom: 14px;

        font-size: 25px;

        font-weight: 750;
    }


    .presentation-advantage {

        font-size: 19px;

        line-height: 1.8;

        color: #e8eef5;
    }


    </style>
    """,
    unsafe_allow_html=True
)


# =========================================================
# SIDEBAR
# =========================================================

with st.sidebar:

    render_markup(
        """
        ## 🤝 Partner Hub
        """
    )

    st.caption(
        "Partnyor və məhsul təqdimat platforması"
    )

    st.divider()

    if st.button(
        "🎬 Presentation Mode",
        use_container_width=True
    ):

        st.session_state.presentation = True
        st.rerun()


    page = st.radio(
        "Navigation",
        [
            "🏠 Ana səhifə",
            "🤝 Partnyorlar",
            "📦 Məhsullar",
            "⚖️ Müqayisə",
            "📜 Sertifikatlar"
        ],
        label_visibility="collapsed"
    )


# =========================================================
# PRESENTATION MODE CSS
# =========================================================

presentation_mode = st.session_state.presentation


if presentation_mode:

    render_markup(
        """
        <style>

        /* Hide sidebar */

        [data-testid="stSidebar"] {
            display: none;
        }


        /* Hide default Streamlit UI */

        #MainMenu {
            visibility: hidden;
        }

        footer {
            visibility: hidden;
        }


        /* Presentation viewport */

        .block-container {

            max-width: 1600px;

            padding-top: 1.2rem;

            padding-left: 4rem;

            padding-right: 4rem;
        }


        .hero {

            padding: 48px;

            border-radius: 30px;
        }


        .hero h1 {

            font-size: 60px;
        }


        .hero p {

            font-size: 21px;
        }


        .section-title {

            font-size: 38px;
        }

        </style>
        """,
        unsafe_allow_html=True
    )


    exit_col1, exit_col2 = st.columns(
        [9, 1]
    )

    with exit_col2:

        if st.button(
            "✕ Exit",
            use_container_width=True
        ):

            st.session_state.presentation = False

            st.rerun()


# =========================================================
# HERO
# =========================================================

render_markup(
    """
    <div class="hero">

        <h1>Partner Hub</h1>

        <p>
        Partnyorlar, məhsullar, üstünlüklər və təqdimat
        materialları vahid platformada.
        </p>

    </div>
    """,
    unsafe_allow_html=True
)


# =========================================================
# HOME PAGE
# =========================================================

if page == "🏠 Ana səhifə":

    render_markup(
        '<div class="section-title">Ümumi baxış</div>',
        unsafe_allow_html=True
    )


    col1, col2, col3 = st.columns(3)


    with col1:

        st.metric(
            "🤝 Partnyor sayı",
            len(df)
        )


    with col2:

        category_count = (
            df["category"].nunique()
            if not df.empty
            else 0
        )

        st.metric(
            "📦 Kateqoriya sayı",
            category_count
        )


    with col3:

        country_count = (
            df.loc[df["country"].astype(str).str.strip().ne(""), "country"].nunique()
            if not df.empty
            else 0
        )

        st.metric(
            "🌍 Ölkə sayı",
            country_count
        )


    render_markup(
        '<div class="section-title">Kateqoriyalar</div>',
        unsafe_allow_html=True
    )


    if df.empty:

        st.warning(
            "Məlumat yoxdur. "
            "`data/partners.xlsx` faylını əlavə edin."
        )


    else:

        categories = (
            df["category"]
            .dropna()
            .unique()
        )


        cols = st.columns(3)


        icons = [
            "❄️",
            "🎨",
            "🧱",
            "⚙️",
            "🔧",
            "🏗️"
        ]


        for i, category in enumerate(categories):

            category_df = df[
                df["category"] == category
            ]


            count = len(category_df)


            icon = icons[
                i % len(icons)
            ]


            with cols[i % 3]:

                render_markup(
                    f"""
                    <div class="category-card">

                        <div class="category-icon">
                            {icon}
                        </div>

                        <div class="category-title">
                            {category}
                        </div>

                        <div class="small-text">
                            {count} partnyor mövcuddur
                        </div>

                    </div>
                    """,
                    unsafe_allow_html=True
                )


# =========================================================
# PARTNERS PAGE
# =========================================================

elif page == "🤝 Partnyorlar":


    # =====================================================
    # PRESENTATION MODE
    # =====================================================

    if presentation_mode:


        render_markup(
            '<div class="section-title">Partnyor təqdimatı</div>',
            unsafe_allow_html=True
        )


        if df.empty:

            st.warning(
                "Partnyor məlumatı yoxdur."
            )


        else:

            partner_list = sorted(
                df["partner_name"]
                .dropna()
                .unique()
                .tolist()
            )


            selected_partner = st.selectbox(
                "Təqdimat üçün partnyor seçin",
                partner_list
            )


            partner_df = df[
                df["partner_name"]
                == selected_partner
            ]


            row = partner_df.iloc[0]


            category = row.get(
                "category",
                ""
            )


            country = row.get(
                "country",
                ""
            )


            description = row.get(
                "description",
                ""
            )


            advantages = row.get(
                "advantages",
                ""
            )


            render_markup(
                f"""
                <div class="presentation-card">

                    <div class="presentation-partner">

                        {selected_partner}

                    </div>


                    <div class="presentation-subtitle">

                        {category}
                        &nbsp;&nbsp;•&nbsp;&nbsp;
                        🌍 {country}

                    </div>


                    <div class="presentation-description">

                        {description}

                    </div>


                    <div class="presentation-heading">

                        ⭐ Niyə bu brend?

                    </div>


                    <div class="presentation-advantage">

                        {advantages}

                    </div>


                </div>
                """,
                unsafe_allow_html=True
            )


            website = row.get(
                "website"
            )


            if (
                pd.notna(website)
                and str(website).strip()
            ):

                st.write("")

                st.link_button(
                    "🌐 Rəsmi sayt",
                    str(website)
                )


    # =====================================================
    # NORMAL MODE
    # =====================================================

    else:


        render_markup(
            '<div class="section-title">Partnyorlarım</div>',
            unsafe_allow_html=True
        )


        col_filter, col_search = st.columns(
            [1, 2]
        )


        with col_filter:

            categories = sorted(
                df["category"]
                .dropna()
                .unique()
                .tolist()
            )


            selected_category = st.selectbox(
                "Kateqoriya",
                ["Hamısı"] + categories
            )


        with col_search:

            search_text = st.text_input(
                "Axtarış",
                placeholder="Məsələn: Mitsubishi"
            )


        filtered_df = df.copy()


        if selected_category != "Hamısı":

            filtered_df = filtered_df[
                filtered_df["category"]
                == selected_category
            ]


        if search_text:

            filtered_df = filtered_df[
                filtered_df["partner_name"]
                .astype(str)
                .str.contains(
                    search_text,
                    case=False,
                    na=False
                )
            ]


        st.caption(
            f"{len(filtered_df)} partnyor tapıldı"
        )


        for _, row in filtered_df.iterrows():


            partner_name = row.get(
                "partner_name",
                ""
            )


            category = row.get(
                "category",
                ""
            )


            country = row.get(
                "country",
                ""
            )


            description = row.get(
                "description",
                ""
            )


            advantages = row.get(
                "advantages",
                ""
            )


            render_markup(
                f"""
                <div class="partner-card">


                    <div class="partner-name">

                        {partner_name}

                    </div>


                    <span class="badge">

                        {category}

                    </span>


                    <div class="country">

                        🌍 {country}

                    </div>


                    <div class="description">

                        <b>Haqqında</b>

                        <br><br>

                        {description}

                    </div>


                    <div class="description">

                        <b>⭐ Əsas üstünlüklər</b>

                        <br><br>

                        {advantages}

                    </div>


                </div>
                """,
                unsafe_allow_html=True
            )


            website = row.get(
                "website"
            )


            if (
                pd.notna(website)
                and str(website).strip()
            ):

                st.link_button(
                    "🌐 Rəsmi sayta keç",
                    str(website)
                )


# =========================================================
# PRODUCTS
# =========================================================

elif page == "📦 Məhsullar":

    render_markup(
        '<div class="section-title">📦 Məhsullar</div>',
        unsafe_allow_html=True
    )


    st.info(
        "Bu bölmədə partnyorların məhsulları, "
        "şəkilləri və texniki göstəriciləri olacaq."
    )


# =========================================================
# COMPARISON
# =========================================================

elif page == "⚖️ Müqayisə":

    render_markup(
        '<div class="section-title">⚖️ Məhsul müqayisəsi</div>',
        unsafe_allow_html=True
    )


    st.info(
        "Bu bölmədə iki və ya daha çox məhsulu "
        "yan-yana müqayisə edəcəyik."
    )


# =========================================================
# CERTIFICATES
# =========================================================

elif page == "📜 Sertifikatlar":

    render_markup(
        '<div class="section-title">📜 Sertifikatlar</div>',
        unsafe_allow_html=True
    )


    st.info(
        "Bu bölmədə sertifikatlar, PDF kataloqlar "
        "və texniki sənədlər olacaq."
    )
