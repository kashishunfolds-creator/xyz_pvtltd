import streamlit as st

st.set_page_config(page_title="Urban Threads", layout="wide")

# ─────────────────────────────────────────────
# SESSION STATE
# ─────────────────────────────────────────────
if "page" not in st.session_state:
    st.session_state.page = "Home"

if "category" not in st.session_state:
    st.session_state.category = "All"

if "selected_product" not in st.session_state:
    st.session_state.selected_product = None

# ─────────────────────────────────────────────
# GLOBAL CSS + GSAP
# ─────────────────────────────────────────────
st.markdown("""
<style>

/* BACKGROUND */
body {
    background-color: #0e1117;
}

/* HERO */
.hero {
    height: 85vh;
    background: linear-gradient(rgba(0,0,0,0.5), rgba(0,0,0,0.7)),
    url("https://images.unsplash.com/photo-1490481651871-ab68de25d43d");
    background-size: cover;
    background-position: center;
    display:flex;
    flex-direction:column;
    align-items:center;
    justify-content:center;
    color:white;
    text-align:center;
}

.hero h1 {
    font-size:70px;
    font-weight:900;
}

.hero p {
    font-size:22px;
    color:#ddd;
}

/* STREAMLIT BUTTON STYLE */
div.stButton > button {
    border-radius: 30px;
    padding: 10px 25px;
    font-weight: 600;
    border: none;
    background: linear-gradient(45deg,#ff416c,#ff4b2b);
    color: white;
    transition: 0.3s;
}

div.stButton > button:hover {
    transform: scale(1.08);
}

/* PRODUCT CARD */
.product-card {
    background:#1c1f26;
    padding:15px;
    border-radius:15px;
    text-align:center;
    height:420px;
    display:flex;
    flex-direction:column;
    justify-content:space-between;
    transition:0.3s;
}

.product-card:hover {
    transform: translateY(-10px);
}

.product-card img {
    height:220px;
    object-fit:cover;
    border-radius:10px;
}

</style>

<script src="https://cdnjs.cloudflare.com/ajax/libs/gsap/3.12.2/gsap.min.js"></script>

<script>
document.addEventListener("DOMContentLoaded", function() {
    gsap.from(".hero h1", {y:-80, opacity:0, duration:1});
    gsap.from(".hero p", {opacity:0, duration:1, delay:0.5});
    gsap.from(".product-card", {opacity:0, y:30, stagger:0.2});
});
</script>
""", unsafe_allow_html=True)

# ─────────────────────────────────────────────
# SIDEBAR NAV
# ─────────────────────────────────────────────
menu = st.sidebar.radio(
    "Menu",
    ["Home", "Products"],
    index=0 if st.session_state.page == "Home" else 1
)
st.session_state.page = menu

# ─────────────────────────────────────────────
# HOME PAGE
# ─────────────────────────────────────────────
if st.session_state.page == "Home":

    # HERO (visual only)
    st.markdown("""
    <div class="hero">
        <h1>URBAN THREADS</h1>
        <p>Style that defines you</p>
    </div>
    """, unsafe_allow_html=True)

    st.markdown("###")

    # FUNCTIONAL BUTTONS
    col1, col2, col3, col4 = st.columns([2,1,1,1])

    with col1:
        if st.button("🛍️ Shop Now"):
            st.session_state.page = "Products"

    with col2:
        if st.button("👕 Men"):
            st.session_state.category = "Men"
            st.session_state.page = "Products"

    with col3:
        if st.button("👗 Women"):
            st.session_state.category = "Women"
            st.session_state.page = "Products"

    with col4:
        if st.button("🧒 Kids"):
            st.session_state.category = "Kids"
            st.session_state.page = "Products"

# ─────────────────────────────────────────────
# PRODUCT DATA
# ─────────────────────────────────────────────
products = [
    {"name":"Classic Hoodie","price":"₹1,499","cat":"Men",
     "img":"https://images.unsplash.com/photo-1602810318383-e386cc2a3ccf",
     "desc":"Premium cotton hoodie with relaxed fit."},

    {"name":"Denim Jacket","price":"₹2,499","cat":"Men",
     "img":"https://images.unsplash.com/photo-1520975916090-3105956dac38",
     "desc":"Stylish rugged denim jacket."},

    {"name":"Summer Dress","price":"₹1,799","cat":"Women",
     "img":"https://images.unsplash.com/photo-1496747611176-843222e1e57c",
     "desc":"Lightweight elegant summer dress."},

    {"name":"Oversized Tee","price":"₹999","cat":"Men",
     "img":"https://images.unsplash.com/photo-1585386959984-a4155224a1ad",
     "desc":"Comfortable oversized t-shirt."},

    {"name":"Kids Hoodie","price":"₹799","cat":"Kids",
     "img":"https://images.unsplash.com/photo-1503919545889-aef636e10ad4",
     "desc":"Warm hoodie for kids."},

    {"name":"Casual Shirt","price":"₹1,299","cat":"Women",
     "img":"https://images.unsplash.com/photo-1593030761757-71fae45fa0e7",
     "desc":"Perfect casual wear shirt."}
]

# ─────────────────────────────────────────────
# PRODUCTS PAGE
# ─────────────────────────────────────────────
if st.session_state.page == "Products":

    st.title(f"🛍️ {st.session_state.category} Collection")

    filtered = [
        p for p in products
        if st.session_state.category == "All" or p["cat"] == st.session_state.category
    ]

    cols = st.columns(3)

    for i, p in enumerate(filtered):
        with cols[i % 3]:
            st.markdown(f"""
            <div class="product-card">
                <img src="{p['img']}"/>
                <h4>{p['name']}</h4>
                <p>{p['price']}</p>
            </div>
            """, unsafe_allow_html=True)

            if st.button("View Details", key=i):
                st.session_state.selected_product = p

# ─────────────────────────────────────────────
# PRODUCT DETAIL VIEW
# ─────────────────────────────────────────────
if st.session_state.selected_product:

    p = st.session_state.selected_product

    st.markdown("---")
    st.subheader(p["name"])

    col1, col2 = st.columns(2)

    with col1:
        st.image(p["img"], use_container_width=True)

    with col2:
        st.write(f"### {p['price']}")
        st.write(p["desc"])

        st.button("Proceed to Checkout")

        if st.button("Close"):
            st.session_state.selected_product = None