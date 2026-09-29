import os
import streamlit as st 
import funcs.func as gf 

####----Start Of Fixed Snippets----####
#-- CSS Style Configuration --#
gf.cssStyle()
#-- Page Configuration --#
gf.pageConfig(
    page_title="EDA-Airbnb NYC Dataset",
    page_icon=":bar_chart:",
    layout="wide"
)
#--Embedding icon On Top-Left Sidebar --#
icon_path = os.path.join(os.getcwd(),"deployment","imgs","icon.png")
gf.sidebarLogoConfig(icon_path)
#--Creating top Animated Bar-#
gf.animatedLine()
#--Creating Top Buttons Bar As Navigation--#
st.session_state.page_name = '' #- Avioding Founding Error When Page Is Reloaded
working_path = os.getcwd()
buttons = ["🏛️ Home","📋Overview", "📊EDA", "💡Insights", "🧠Modelling"]
gf. showTopButtons(buttons)
if st.session_state.page_name == "🏛️ Home":
    st.switch_page(os.path.join(working_path,"deployment","Main.py"))
if st.session_state.page_name == "📋Overview":
    st.switch_page(os.path.join(working_path,"deployment","pages","Overview.py"))
if st.session_state.page_name == "📊EDA":
    st.switch_page(os.path.join(working_path,"deployment","pages","EDA.py"))
if st.session_state.page_name == "💡Insights":
    st.switch_page(os.path.join(working_path,"deployment","pages","Insights.py"))
if st.session_state.page_name == "🧠Modelling":
    st.switch_page(os.path.join(working_path,"deployment","pages","Modelling.py"))
#--Creating bottom Animated Bar-#
gf.animatedLine()
#-- Setting Background Color Of Page --#
if 'background_color' not in st.session_state:
    st.session_state.background_color=''
if st.session_state.background_color:
    gf.changeBackgroundColor(st.session_state.background_color)

#- Title Of Page --#
page_title  = "Overview"
color_title = "#00E5FF"
bg_color=st.session_state.background_color
gf.createTopTitleHeader(page_title, color_title,bg_color)
####----End Of Fixed Snippets ----####


######################################
######################################
###################################### 
####----Start Of What EDA Page Contains---####

# -----------------------------
# first text snippet (Glance)
# -----------------------------
title_card="🏢 Business Understanding"
text_card="<div class='imformation-cd-subtitle'>At A Glance ⓘ</div>\
            <strong>Airbnb</strong> is an online platform that allows people\
            to rent out homes, apartments, rooms, or other accommodations\
            to travelers.<br/>\
            <strong>Airbnb</strong> is an online marketplace that connects hosts offering accommodations\
             with guests searching for places to stay.<br/>Hosts publish listings containing information such as \
            location, room type, price, availability, and reviews,<br/> while guests use the platform to discover \
            and book suitable accommodations.<br/>\
            more info about <strong>Airbnb</strong> app : <a href='https://www.airbnb.com/'>Read more</a>\
            "
gf.showInfoCard(title_card,text_card)
# -------------------------------------
# Second text snippet (airbnb workflow)
# -------------------------------------
title_card="🏢 Business Understanding"
text_card=" <div class='imformation-cd-subtitle'>Airbnb Workflow ⚙️</div>\
       -   🏠 A person owns an apartment in New York.<br/>\
       -   👤 They list it on Airbnb.<br/>\
       -   🧳 A traveler searches for a place to stay.<br/>\
       -   💰 The traveler pays to stay there for a certain number of nights.<br/>\
       -   ⭐ After the stay, the traveler can leave a review."
gf.showInfoCard(title_card,text_card)
# -----------------------------------------------
# Third text snippet (Intent Of Initializing EDA)
# ------------------------------------------------
title_card="🏢 Business Understanding"
text_card="<div class='imformation-cd-subtitle'>Intent Of Initialzing EDA 🔬📊</div>\
           - Excuting And Performing Exploratory Data Analysis On <strong>NYC Airbnb dataset</strong> By Using Python Libraries \
            Helping In Understanding Data  And Cleaning That Data To Be Ready For Modelling And\
            Gaining Best Performance Can Be Expected In User Work Environment.</br>\
            - <strong>NYC Airbnb dataset</strong>  Consists Of Instances Or Operations Applied On \
            <strong>Airbnb</strong> Platform In Only <strong>New Work City</strong>"
gf.showInfoCard(title_card,text_card)
#--Airbnb Banner Image--#
airbnb_img_path = os.path.join(os.getcwd(),"deployment","imgs","overview_imgs","banner.png")   
img_base64 = gf.imgAsBase64(airbnb_img_path)
st.markdown(
    f"""
    <div style="
        width: 80%;
        margin:10px auto;
        height: 200px;
        background-image: url('data:image/png;base64,{img_base64}');
        background-size: contain;
        background-position: center;
        background-repeat: repeat;
        border-radius: 8px;
    "></div>
    """,unsafe_allow_html=True
)
#- 
# -----------------------------------------------
# Fourth text snippet (Predictors Show)
# ------------------------------------------------
#- animated bar 
gf.animatedLine()
sec_name='Predictors'
gf.secTitleName(sec_name)
lst_ftr_desc=[
    ('id' , 'Unique identifier for each Airbnb listing.'),
    ('name' , 'Name/title of the Airbnb listing.'),
    ('host_id' , 'Unique identifier of the host who owns/manages the listing.'),
    ('host_name' , 'Name of the host.'),
    ('neighbourhood_group' , 'The larger NYC Place(Neighbourhood) where the listing is located: Manhattan, Brooklyn, Queens, Bronx, or Staten Island.'),
    ('neighbourhood' , 'The specific neighborhood where the listing is located.'),
    ('latitude' , 'Geographic latitude of the listing.'),
    ('longitude' , 'Geographic longitude of the listing.'),
    ('room_type' , 'Type of accommodation offered: Entire home/apt, Private room, or Shared room.'),
    ('minimum_nights' , 'Minimum number of nights that a guest must book.'),
    ('number_of_reviews' , 'Total number of reviews received by the listing.'),
    ('last_review' , 'Date of the most recent review for the listing.'),
    ('reviews_per_month' , 'Average number of reviews received per month.'),
    ('calculated_host_listings_count' , ' Number of Airbnb listings associated with that host.'),
    ('availability_365' , 'Number of days during the year that the listing is available for booking, from 0 to 365.'),
    ('price', 'Pric of the listing per night in USD.')
]
cols = st.columns(3)
ftr_count = 0
for i in range(3):
    with cols[i]:
        gf.ftrCardCreater(lst_ftr_desc[ftr_count][0],lst_ftr_desc[ftr_count][1])
    ftr_count+=1;
for i in range(3):
    with cols[i]:
        gf.ftrCardCreater(lst_ftr_desc[ftr_count][0],lst_ftr_desc[ftr_count][1])
    ftr_count+=1;
for i in range(3):
    with cols[i]:
        gf.ftrCardCreater(lst_ftr_desc[ftr_count][0],lst_ftr_desc[ftr_count][1])
    ftr_count+=1;
for i in range(3):
    with cols[i]:
        gf.ftrCardCreater(lst_ftr_desc[ftr_count][0],lst_ftr_desc[ftr_count][1])
    ftr_count+=1;
for i in range(3):
    with cols[i]:
        gf.ftrCardCreater(lst_ftr_desc[ftr_count][0],lst_ftr_desc[ftr_count][1])
    ftr_count+=1;
# -----------------------------------------------
# Fifth text snippet (Target Feature Show)
# ------------------------------------------------
sec_name='Target Feature'
gf.secTitleName(sec_name)
gf.ftrCardCreater(lst_ftr_desc[-1][0],lst_ftr_desc[-1][1])



# -------------------------------------------------------
# Last snippet (Utilities)--> (Dependencies) (footer Sec)
# -------------------------------------------------------
gf.footerCreater()
####---- End Of What EDA Page Contains---####