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

#-- Setting Background Color Of Page --#
if st.session_state.background_color:
    gf.changeBackgroundColor(st.session_state.background_color)


#- Title Of Page --#
page_title  = "Modelling"
color_title = "#00E5FF"
bg_color=st.session_state.background_color
gf.createTopTitleHeader(page_title, color_title,bg_color)

#--Content Of Page--# 
st.info("upcomming Soon")
#--End Of Page Content--#