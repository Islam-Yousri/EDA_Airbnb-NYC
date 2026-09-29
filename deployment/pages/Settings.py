import os
import streamlit as st 
import funcs.func as gf 

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
#- Cheching If Background Color Is Set In Session State, If Not Then Set It To Default --#
#-- Setting Background Color If Not Existed --#
if "background_color" not in st.session_state:
    st.session_state.background_color= "" 


if "background_color" in st.session_state:
    gf.changeBackgroundColor(st.session_state.background_color)


#- Title Of Page --#
page_title  = "Settings"
color_title = "#00E5FF"
bg_color=st.session_state.background_color
gf.createTopTitleHeader(page_title, color_title,bg_color)
#--Creating Background Color change widget--#



with st.expander("***Change Background Color***", expanded=True):
    bg_blue = st.toggle("🔵Blue Mode")
    bg_green = st.toggle("🌳Green Mode")
    default_color = st.button("Click To Reset To Default Color")
    st.session_state.bg_blue = bg_blue
    st.session_state.bg_green = bg_green
    st.session_state.default_color = default_color  

if default_color:
    if bg_green or bg_blue:
        st.warning("Please deselect the other mode before resetting to default color.")
    if not bg_green and not bg_blue:
        gf.changeBackgroundColor("#FFFFFF")
        st.session_state.background_color = "#FFFFFF" 

if bg_blue and bg_green:
    st.warning("Please select only one mode at a time.")
elif bg_blue:
    gf.changeBackgroundColor("#E3F2FD")
    st.session_state.background_color = "#E3F2FD"
elif bg_green:
    gf.changeBackgroundColor("#E7F5EB")
    st.session_state.background_color = "#E7F5EB"

# -------------------------------------------------------
# Last snippet (Utilities)--> (Dependencies) (footer Sec)
# -------------------------------------------------------
gf.footerCreater()  
