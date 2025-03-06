import streamlit as st

# Hide the sidebar and set up a global font
st.markdown("""
<style>
@import url('https://fonts.googleapis.com/css2?family=Poppins:wght@300;400;600&display=swap');

/* Hide sidebar + header */
section[data-testid="stSidebar"] {
    display: none;
}
header, .stAppHeader {
    display: none;
}

/* Global background color */
* {
    background-color: #433633;
    margin: 0; /* Remove default browser margin */
    padding: 0;
    font-family: 'Poppins', sans-serif;
}

/* Container centers its content in a column layout */
.container {
    display: flex;
    flex-direction: column;
    align-items: center; /* Center horizontally */
    text-align: center;
    width: 100%;
    box-sizing: border-box;
}

/* Header bar styling */
.header {
    background-color: #92D1C3;
    display: flex;
    justify-content: center;
    width: 95%;
    padding: 20px;
    margin: 40px 0;
    cursor: pointer;
    border-radius: 30px;
    border-bottom:6px solid black;
}

/* Title (left side) */
.a {
    color: #433633;
    flex: 3;
    font-weight: 600;
    background: transparent;
    font-size: 1.5rem;
}

/* Subtitle (right side) */
.b {
    color: #433633;
    background: transparent;
    font-size: 1rem;
}

/* Example container for 2-column layout */
.box-container {
    display: flex;
    height: 500px;
    width: 80%;
 
    margin-bottom: 40px;
    flex :2 1;
    gap:20px;
}

/* Left and right boxes */
.left-box {
    border-radius:20px;
    flex: 1;
    background-color: #A39B8B;
    display: flex;
    justify-content: center;
    align-items: center;
    padding:20px;
     transition: transform 0.3s ease; 
        border-bottom:6px solid black;
}
.left-box:hover{
  
  transform: scale(1.3); /* Scales 1.5 times bigger */
}
.right-box {
    flex: 1;
    display: flex;
    flex-direction: column;
    
}
.right-box .top,
.right-box .bottom {
    flex: 1;
    border: 2px solid #ccc;
    display: flex;
    justify-content: center;
    align-items: center;
    transition: transform 0.3s ease; 
    flex-direction: column;
    margin:10px;
    border-radius:5px;
       border-bottom:6px solid white;
}
.right-box .top:hover{
    
  transform: scale(1.5); /* Scales 1.5 times bigger */
}
.right-box .bottom:hover{
    
  transform: scale(1.5); /* Scales 1.5 times bigger */
}



/* Example custom class for special text or container */
.st {
    font-family: 'Press Start 2P', cursive;
    display: flex;
    align-items: center; /* Fix spelling */
    justify-content: center;
    height: 100px;
    width: 80%;
    font-size: 30px;
    margin: 30px auto;
    border: 4px solid white;
}
.bottom p{
    padding:8px;
}
ul.skills {
  list-style-type: none;
  padding: 0;
  margin: 0 auto;
  max-width: 300px; /* Adjust as needed */
}

ul.skills li {
  background-color: #8F857D; /* Card background */
  color: #1B2021;           /* Text color */
  margin: 10px 0;
  padding: 10px;
  border-radius: 8px;
  font-weight: 500;
  font-family: 'Poppins', sans-serif; /* Ensure you've imported the font */
cursor:pointer;
}
ul.skills li:hover {
background-color:#A39B8B;
}
</style>
""", unsafe_allow_html=True)

# HTML layout
st.markdown("""
<div class="container">
  <div class="header">
    <div class="a">My Projects</div>
    <div class="b">2021-2025</div>
  </div>

  <div class="box-container">
    <div class="left-box">
    <img src="https://static.vecteezy.com/system/resources/previews/027/517/373/original/pixel-art-cartoon-office-man-character-png.png">
      </img>
          </div>
    <div class="right-box">
      <div class="top">
       Skills  :
        <ul className="skills">
      <li>Machine Learning</li>
      <li>Web Dev</li>
      <li>Dsa</li>
      </ul>
      </div>
      <div class="bottom">
        <p>"Talk is cheap. Show me the code."</p>
      </div>
    </div>
  </div>
</div>
""", unsafe_allow_html=True)


st.markdown(
    """
    <style>
    /* Target the text input */
    div[data-testid="stTextInput"] input[type="text"] {
        background-color: #92D1C3 !important; /* Light teal background */
        color: black !important;           /* Dark text color */
        border: 2px solid #92D1C3 !important;/* Dark border */
        border-radius: 6px !important;
        padding: 8px !important;
    }
    /* Style the placeholder text */
    div[data-testid="stTextInput"] input[type="text"]::placeholder {
        color: black !important; /* Placeholder color */
        opacity: 1 !important;
        font-weight:300;
    }
    </style>
    """,
    unsafe_allow_html=True
)

search_query = st.text_input(
    label="",
    placeholder="Search the Technology",
    key="search_query"
)

if search_query:
    st.write("You searched for:", search_query)
         # Switch to the page whose title is "Next Page"
    st.switch_page("./pages/next_page.py")