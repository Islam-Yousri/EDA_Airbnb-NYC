import os
from num2words import num2words
from datasist.structdata import detect_outliers
import numpy as np 
import pandas as pd 
import matplotlib.pyplot as plt 
import seaborn as sns
import plotly.express as px 
import streamlit as st 
import funcs.func as gf

import warnings
warnings.filterwarnings("ignore")

#-- Page Configuration --#
#-- CSS Style Configuration --#
gf.cssStyle()
gf.pageConfig(
    page_title="EDA-Airbnb NYC Dataset",
    page_icon=":bar_chart:",
    layout="wide"
)
#--Embedding icon On Top-Left Sidebar --#
icon_path = os.path.join(os.getcwd(),"deployment","imgs","icon.png")
gf.sidebarLogoConfig(icon_path)

#--Creating Top Animated Bar-#
gf.animatedLine()
#--Creating Top Buttons Bar As Navigation--#
st.session_state.page_name = '' #- Avioding Founding Error When Page Is Reloaded
working_path = os.getcwd()
buttons = ["🏛️ Home","📋Overview", "📊EDA", "💡Insights", "🧠Modelling"]
gf.showTopButtons(buttons)
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

######################################
######################################
######################################
####----Start Of What EDA Page Contains---####
#-- Title Of Page --#
page_title  = "Exploratory Data Analysis (EDA)" 
color_title = "#00E5FF"
bg_color=st.session_state.background_color
gf.createTopTitleHeader(page_title, color_title,bg_color) 

#--Reading Dataset--# 
data_path=os.path.join(os.getcwd(),"dataset","AB_NYC_2019.csv")
cleaned_data_path=os.path.join(os.getcwd(),"dataset","cleaned_airbnb_NYC.csv")
renting_dataset=gf.load_dataset(data_path)
cleaned_renting_data = gf.load_dataset(cleaned_data_path)
#-- Primary Info About Whole Dataset --#
#- Title Of Primary Info About Whole Dataset 
gf.secTitleName(title_name="Primary Information About \
                Airbnb New York Dataset")
#- Content Of Primary Info About Whole Dataset 
subtitle="At A Glance"
gf.subtitleView(subtitle)
primary_info_set1 = st.columns(4)
primary_info_set2 = st.columns(4)
lst=[
    ("📄 Rows",48895),
    ("🔢 Features",16),
    ("🔢 Numerical",8),
    ("🔤 Categorical",6),
    ("⚠️ Missing Cells",f"{renting_dataset.isna().sum().sum():,}"),
    ("♻️ Duplicates",f"{renting_dataset.duplicated().sum():,}"),
    ("💰 Avg. Price",f"{renting_dataset['price'].mean():.2f}"),
    ("💰 max. Price",f"{renting_dataset['price'].max():,}")
]
#- Show First Four Metrics 
for i in range(0,4):
    with primary_info_set1[i]:
        st.metric(
            f"{lst[i][0]}",
            f"{lst[i][1]}"
        )
#- Show Last Four Metrics 
for i in range(4):
    with primary_info_set2[i]:
        if lst[i+4][0]=='⚠️ Missing Cells':
            st.metric(
                        label=f"{lst[i+4][0]}",
                        value=f"{lst[i+4][1]}",
                        delta=f"out of {renting_dataset.shape[0]*renting_dataset.shape[1]} Cell",
                    )
        else:
            st.metric(
                f"{lst[i+4][0]}",
                f"{lst[i+4][1]}"
            )

#- sidebar options of EDA Page
 #- Show Instancs From Dataset 
st.sidebar.markdown("<font class='sidebar-subtitle'><strong> ⬤ </strong> Primary Options</font><br/>",unsafe_allow_html=True)
sample_case = st.sidebar.radio(label="***Showing Data Samples***",
options=['first 5 element','last 5 element' , 'random 5 element'])

subtitle="View Of Dataset Samples"
gf.subtitleView(subtitle)
with st.expander(f"***Show '{sample_case}' Of Whole Dataset Samples***", expanded=True):
    if sample_case=='first 5 element':st.table(renting_dataset.head(5))
    elif sample_case=='last 5 element':st.table(renting_dataset.tail(5))
    elif sample_case=='random 5 element':st.table(renting_dataset.sample(5))
#- Show Instance Of Insights Set(1)
insight_case = st.sidebar.checkbox(label="***Display Observations***",value=True)
if insight_case :
    subtitle="Insights"
    text_card="- the number of instances In Renting Dataset Is <strong style='padding:0px;'>48895</strong>\
    While The Number Of Features After Droping Non-Necessary Features Is <strong style='padding:0px;'>14</strong><br/>\
    - There Is No Duplicated 'Repeated' Instances In That Data<br/>\
    - Features Has Missing Values Are <strong style='padding:0px;'>name , host_name , last_review  And reviews_per_month</strong>\
    (<strong style='padding:0px;'> 4 features has  And  10 hasn't</strong> )<br/>\
    - There Is <strong style='padding:0px;'>8 Numeric Feature</strong>  And <strong style='padding:0px;'>6 Categorical Feature</strong> \
    "
    gf.subtitleView(subtitle)
    gf.showInfoCard(title_card="insights set (First Glance)",text_card=text_card)

#-- Data Understanding Of Price Feature --#
#- Title Of Understanding Of Price Feature
gf.secTitleName(title_name="Data Understanding Of Price Feature") 
#- Primary Info
subtitle="primary info"
gf.subtitleView(subtitle)
primary_info_set1 = st.columns(3)
primary_info_set2 = st.columns(3)
lst=[
    ("🔢 Feature Type",'int64'),
    ("⚠️ Missing",f"{renting_dataset['price'].isna().sum():,}"),
    ("💰 Avg. Price",f"{renting_dataset['price'].mean():.2f}"),
    ("💰 median Price",f"{renting_dataset['price'].median():.2f}"),
    ("💰 max. Price",f"{renting_dataset['price'].max():,}"),
    ("💰 skewness rate",f"{renting_dataset['price'].skew():.2f}")
]
#- Show First Three Metrics 
for i in range(0,3):
    with primary_info_set1[i]:
        st.metric(
            f"{lst[i][0]}",
            f"{lst[i][1]}"
        )
#- Show Last Three Metrics 
for i in range(3):
    with primary_info_set1[i]:
        st.metric(
            f"{lst[i+3][0]}",
            f"{lst[i+3][1]}"
        )
#- Sidebar price feature Options 
st.sidebar.markdown("<font class='sidebar-subtitle'><strong>\
                     ⬤ </strong> Price Feature Options</font><br/>",
                     unsafe_allow_html=True)
radio_case = st.sidebar.radio(label="***Outliers***",options=["Valid","Inconsistent"]) 
if radio_case=='Valid':
    gf.ftrCardCreater( "Valid Number Of Outliers" , "2972" )
elif radio_case=="Inconsistent":
    gf.ftrCardCreater( "Inconsistent Number Of Outliers" , "11" )
#- Data Analysis
subtitle="Data Analysis"
gf.subtitleView(subtitle)
with st.expander(label="***Visualized Charts***",expanded=True):
    tab1,tab2,tab3 = st.tabs(['boxplot','density-plot','herizontal_barplot'])
    with tab1:
        #- Visualizing Outliers 
        chart_title="Visualizing Outliers"
        chart_desc=" This chart shows Outliers Existing of\
            <span class='chart-description-highlight'>Airbnb listing prices</span>\
            across New York City.\
            It helps To Check If Lower And Upper Outliers"
        gf.chartDesc(chart_title,chart_desc)
        st.plotly_chart(
            px.box(
                data_frame=renting_dataset,
                x='price',
                color_discrete_sequence=['#007DCC']
            )
        )
    with tab2:
        #- Visualizing Distribution Of Price Feature 
        chart_title="Visualizing Prices Spread"
        chart_desc=" This chart shows The Distribution Of \
            <span class='chart-description-highlight'>Airbnb listing prices</span>\
            across New York City.\
            It helps In Showing How Prices Is Spread \
            And If Thier Values Are Normally Spread."
        gf.chartDesc(chart_title,chart_desc)
        skewness_rate = renting_dataset['price'].skew()
        g = sns.displot(
            data=renting_dataset,
            x='price',
            kind='kde',
            color="#007DCC",
            height=4,
            aspect=1.5
        )
        g.set_axis_labels(
            "Price",
            "Density"
        )
        g.ax.legend(
            [f"Skewness Rate: {skewness_rate:.3f}"]
        )
        st.pyplot(g.figure)
    with tab3:
        #- Visualizing groups of prices 
        chart_title="Visualizing Count Groups Of Prices"
        chart_desc=" This Chart Shows\
            <span class='chart-description-highlight'>Airbnb listing prices Groups</span>\
            across New York City.\
            It helps In Show Most Highest Group"
        gf.chartDesc(chart_title,chart_desc)
        #- Give Me Counts Of Instances For Those Groups 
        #. $ 1- 100 
        #. $ 101-200  
        #. $ 201-300
        #. $ 301-400 
        #. $ 401-500 
        #. $ 501-1k
        #. $ 1k-5k
        #. $ 5.1k-10k
        group_1_count = renting_dataset[(renting_dataset['price']>=1) & (renting_dataset['price']<=100)].shape[0]
        group_2_count = renting_dataset[(renting_dataset['price']>=101) & (renting_dataset['price']<=200)].shape[0]
        group_3_count = renting_dataset[(renting_dataset['price']>=201) & (renting_dataset['price']<=300)].shape[0]
        group_4_count = renting_dataset[(renting_dataset['price']>=301) & (renting_dataset['price']<=400)].shape[0]
        group_5_count = renting_dataset[(renting_dataset['price']>=401) & (renting_dataset['price']<=500)].shape[0]
        group_6_count = renting_dataset[(renting_dataset['price']>=501) & (renting_dataset['price']<=1000)].shape[0]
        group_7_count = renting_dataset[(renting_dataset['price']>=1001) & (renting_dataset['price']<=5000)].shape[0]
        group_8_count = renting_dataset[(renting_dataset['price']>=5001) & (renting_dataset['price']<=10000)].shape[0]
        price_ranges = pd.DataFrame({
                "groups" : ["$ 1-100","$ 101-200","$ 201-300","$ 301-400","$ 401-500","$ 501-1k","$ 1k-5k","$ 5.1k-10k"],
                "count"  : [group_1_count,group_2_count,group_3_count,group_4_count,group_5_count,group_6_count,group_7_count,group_8_count]})
        price_ranges=price_ranges.sort_values(by='count')
        #- Visualizing Chart
        st.plotly_chart(
            px.bar(
            data_frame=price_ranges,
            x="count",
            y="groups",
            orientation='h',
            color_discrete_sequence=["#007DCC"]
            )   
        )
 #- Show Instance Of Insights Set(2)
#- Show Instance Of Insights Set(price feature)
insight_case = st.sidebar.checkbox(label="***Display Observations***",value=True,key=2)
if insight_case :
    subtitle="Insights"
    text_card="- <strong style='padding:0px'>Price</strong> Feature Is <strong style='padding:0px'>Positive Integer Numbers</strong>  Such That Minimum Value Is \
        <strong style='padding:0px'>Zero Renting Price</strong> Which It Is Not Logic And Considered As Inconsistent Outliers Must Be Rmoved <br/>\
        - There Are Eleven Inconsistent Outliers Are Valued With zeroe , And They'd been Removed From cleaned DataFrame.<br/>\
        - The mean Of Renting Prices Is <strong style='padding:0px'>152.72</strong> \
        And The median Value Is Only <strong style='padding:0px'>106.0</strong> \
        While The Maximum Value Is <strong style='padding:0px'>10k</strong> \
        Is An Extreme Outlier<br/>\
        - The Distribution Of Price Feature Values has <strong style='padding:0px'>Right-Skewed Spread</strong>\
        With Skewness Rate  <strong style='padding:0px'>19.1</strong> And It's not Suitable For Modelling Predictive\
        AI Algorithm Accurately And It Must Be Normalized Before Modelling Process.<br/>\
        - The Largest Group Is <strong style='padding:0px'> 1 - 100</strong> With <strong style='padding:0px'>23.917k Listings</strong>\
        And Lowest Group Is <strong style='padding:0px'>5.1k - 10k</strong> With <strong style='padding:0px'>20 listings</strong><br/>\
        "
    gf.subtitleView(subtitle)
    gf.showInfoCard(title_card="insights set (Price Feature)",text_card=text_card)

#-- Data Understanding Of name Feature --#
#- Title Of Understanding Of name Feature
gf.secTitleName(title_name="Data Understanding Of name Feature") 
#- Primary Info
subtitle="primary info"
gf.subtitleView(subtitle)
#- Content Of Primary Info About name feature
primary_info_set1 = st.columns(4)
lst=[
    ("🔢 Feature Type",'Object (categorical)'),
    ("⚠️ Missing",f"{renting_dataset['name'].isna().sum():,}"),
    ("✦  Uniques Number",f"{renting_dataset['name'].nunique()}"),
    ("🏆 Most Frequent Accomodation Description","Hillside Hotel","freq : 18"),
]
for i in range(4):
    if len(lst[i])==3:
        with primary_info_set1[i]:
            st.metric(
                f"{lst[i][0]}",
                f"{lst[i][1]}",
                delta=f"{lst[i][2]}"
        )
    else:
        with primary_info_set1[i]:
            st.metric(
                f"{lst[i][0]}",
                f"{lst[i][1]}",
        )
#- Sidebar name feature Options
st.sidebar.markdown("<font class='sidebar-subtitle'><strong>\
                     ⬤ </strong> name Feature Options</font><br/>",
                     unsafe_allow_html=True)
data_clean_case = st.sidebar.checkbox(label="***Data Cleaning***",value=True)
#- Data Cleaning Container 
subtitle="Data Cleaning"
gf.subtitleView(subtitle)
title_card="🧹 What Is Happened In Data Cleaning Phase ?"
text_card="<div class='imformation-cd-subtitle'>Performed Steps</div>\
           - Those All Special Literals [ ~ , ! , @ ,  # , $ , % , ^ , & , * , ( , ) , - , _ , + , = , \\ , / ,\
            ? , ',' , '²' , . , New York] Are Existed In Name Descriptions And Therefore All\
            These Previous Literals Had Been Removed From Each Listing Description contained one of them <br/>\
           - converting All numerical form 0,1,2,3,...,n To Textual form zero,one,two,three,...,n"
if data_clean_case:
    lst_info=[
        ("How Many did special Literal '&' appear?",
         "Literal '&' Appeared <strong style='text-decoration:underline;'>3112</strong> Time"),
        ("How Many did special Literal '.' appear?",
         "Literal '.' Appeared <strong style='text-decoration:underline;'>3596</strong> Time"),
        ("How Many did special Literal '-' appear?",
         "Literal '-' Appeared <strong style='text-decoration:underline;'>6047</strong> Time"),
        ("How Many did special Literal '#' appear?",
         "Literal '#' Appeared <strong style='text-decoration:underline;'>546</strong> Time"),
        ("How Many did special Literal '$' appear?",
         "Literal '$' Appeared <strong style='text-decoration:underline;'>88</strong> Time"),
        ("How Many did special Literal '@' appear?",
         "Literal '@' Appeared <strong style='text-decoration:underline;'>179</strong> Time"),
        ("How Many did special Literal '^' appear?",
         "Literal '^' Appeared <strong style='text-decoration:underline;'>8</strong> Time"),
        ("How Many did special Literal '!' appear?",
         "Literal '!' Appeared <strong style='text-decoration:underline;'>6218</strong> Time"),
        ("How Many did special Literal '%' appear?",
         "Literal '%' Appeared <strong style='text-decoration:underline;'>28</strong> Time"),
        ("How Many did word 'New York' appear?",
         "Literal 'New York' Appeared <strong style='text-decoration:underline;'>640</strong> Time"),
        ("How Many Digits Existed In Descriptions",
         "Digits Appeared In <strong style='text-decoration:underline;'>15839</strong> Description Listing")
    ] 
    #- Show Information About Special characters In name feature
    common_row  = st.columns(3)
    special_row = st.columns(2)
    count=0
    for i in range(0,3):
        with common_row[i]:
            gf.ftrCardCreater( lst_info[i][0] ,lst_info[i][1])
    for i in range(0,3):
        with common_row[i]:
            gf.ftrCardCreater( lst_info[i+3][0] ,lst_info[i+3][1])
    for i in range(0,3):
        with common_row[i]:
            gf.ftrCardCreater( lst_info[i+6][0] ,lst_info[i+6][1])
    for i in range(0,2):
        with special_row[i]:
            gf.ftrCardCreater( lst_info[i+9][0] ,lst_info[i+9][1])
gf.showInfoCard(title_card,text_card)
#- Data Analysis
subtitle="Data Analysis"
gf.subtitleView(subtitle)
with st.expander(label="***Visualized Charts***",expanded=True):
    tab1,tab2 = st.tabs(["count plot-1","count plot-2"])
    with tab1:
        chart_title="Check Higher 10 repeated description"
        chart_desc="This Chart Show Most Frequent Repeated 10 Listing Descriptions\
            Where Each Accomation Description Is Varaint From Another"
        gf.chartDesc(chart_title,chart_desc)
        desc_count =  renting_dataset['name'].value_counts()
        most_20_prices = desc_count.sort_values(ascending=False)[:20]
        repeate_names = {
                'listing Description' : most_20_prices.index,
                'Count of Occurances' : most_20_prices.values
            }
        st.plotly_chart(
            px.bar(data_frame = repeate_names , 
                x='listing Description',
                y='Count of Occurances', 
                color_discrete_sequence=["#57B4BA"] )
        )
    with tab2:
        chart_title="Check Higher 20 Priced-Renting Decriptions"
        chart_desc="This Chart Describes Listing Descriptions Priced With highest\
            20 renting price"
        gf.chartDesc(chart_title,chart_desc)
        desc_price = renting_dataset['price'].groupby(renting_dataset['name']).max().sort_values(ascending=False)[:20]
        most_10_desc_price = pd.DataFrame(
            {
            'Description' :desc_price.index,
            'Price':desc_price.values
            }
        )
        st.plotly_chart(
            px.bar(data_frame = most_10_desc_price , 
                x='Description',y='Price',
                labels={"price":"Highest 20 Renting Price"}, 
                color_discrete_sequence=["#57B4BA"]
            )
        )
#- Show Instance Of Insights Set(name feature)
insight_case = st.sidebar.checkbox(label="***Display Observations***",value=True,key=4)
if insight_case :
        subtitle="Insights"
        text_card="- <strong style='padding:0px;'>name</strong> Feature is A Categorical Feature\
              Have <strong style='padding:0px;'>47905</strong> Variant Descriptions Of\
              Listing On Airbnb Website In New Work City Had Been Done.<br/>\
            - The Most Repeated Characteristics Of Renting Which They Had Been \
                Listed In That Dataset Is  <strong style='padding:0px;'>Hillside Hotel</strong> <br/>\
            -  The Description Of Booking Which It Owned Highest cost Is  \
            <strong style='padding:0px;'>1-BR Lincoln Center , Furnished room in \
            Astoria And Luxury 1 bedroom app.-stunning mangattan views  </strong>\
            "
        gf.subtitleView(subtitle)
        gf.showInfoCard(title_card="insights set (name Feature)",text_card=text_card)
#- Data Engineering Container 
subtitle="Data Engineering"
gf.subtitleView(subtitle)
#- Show Instance Of Insights Set(name feature)
date_eng_case = st.sidebar.checkbox(label="***Data Engineering***",value=True)
if date_eng_case:
    feature_names=['desc_len','desc_lang'
                   ,'has_prop_keyword','has_room_keyword',
                   'has_rental_keyword','has_amenity_keyword',
                   'location__keywords','marketing__keywords']
    gf.extractFtrName(feature_names=feature_names)

#-- Data Understanding Of host_name Feature --#
#- Title Of Understanding Of host_name Feature
gf.secTitleName(title_name="Data Understanding Of host_name Feature") 
#- Primary Info
subtitle="primary info"
gf.subtitleView(subtitle)
#- Content Of Primary Info About host_name feature
primary_info_set1 = st.columns(4)
lst=[
    ("🔢 Feature Type",'Categorical'),
    ("⚠️ Missing",f"{renting_dataset['host_name'].isna().sum():,}"),
    ("✦  Uniques Number",f"{renting_dataset['host_name'].nunique()}"),
    ("🏆 Most Frequent host","Michael","freq :  417"),
]
for i in range(4):
    if len(lst[i])==3:
        with primary_info_set1[i]:
            st.metric(
                f"{lst[i][0]}",
                f"{lst[i][1]}",
                delta=f"{lst[i][2]}"
        )
    else:
        with primary_info_set1[i]:
            st.metric(
                f"{lst[i][0]}",
                f"{lst[i][1]}",
        )
st.sidebar.markdown("<font class='sidebar-subtitle'><strong>\
                     ⬤ </strong> host_name Feature Options</font><br/>",
                     unsafe_allow_html=True)
data_clean_case = st.sidebar.checkbox(label="***Data Cleaning***",value=True,key=3)

#- Data Cleaning Container 
subtitle="Data Cleaning"
gf.subtitleView(subtitle)
if data_clean_case:
    lst_info=[
        ("How Many did special Literal ')' appear?",
         "Literal ')' Appeared <strong style='text-decoration:underline;'>379</strong> Time"),
        ("How Many did special Literal '(' appear?",
         "Literal '(' Appeared <strong style='text-decoration:underline;'>381</strong> Time"),
        ("How Many did special Literal '&' appear?",
         "Literal '&' Appeared <strong style='text-decoration:underline;'>1162</strong> Time"),
        ("How Many did special Literal '-' appear?",
         "Literal '-' Appeared <strong style='text-decoration:underline;'>187</strong> Time"),
        ("How Many did special Literal '.' appear?",
         "Literal '.' Appeared <strong style='text-decoration:underline;'>243</strong> Time"),
        ("How Many did special Literal '/' appear?",
         "Literal '/' Appeared <strong style='text-decoration:underline;'>41</strong> Time"),
        ("How Many did special Literal ',' appear?",
         "Literal ',' Appeared <strong style='text-decoration:underline;'>30</strong> Time"),
        ("How Many did special Literal '+' appear?",
         "Literal '+' Appeared <strong style='text-decoration:underline;'>32</strong> Time"),
        ("How Many did special Literal '@' appear?",
         "Literal '@' Appeared <strong style='text-decoration:underline;'>8</strong> Time"),
        ("How Many did word '!' appear?",
         "Literal '!' Appeared <strong style='text-decoration:underline;'>4</strong> Time"),
        ("How Many Digits Existed In host names",
         "Digits Appeared In <strong style='text-decoration:underline;'>44</strong> host names")
    ] 
    #- Show Information About Special characters In name feature
    common_row  = st.columns(3)
    special_row = st.columns(2)
    count=0
    for i in range(0,3):
        with common_row[i]:
            gf.ftrCardCreater( lst_info[i][0] ,lst_info[i][1])
    for i in range(0,3):
        with common_row[i]:
            gf.ftrCardCreater( lst_info[i+3][0] ,lst_info[i+3][1])
    for i in range(0,3):
        with common_row[i]:
            gf.ftrCardCreater( lst_info[i+6][0] ,lst_info[i+6][1])
    for i in range(0,2):
        with special_row[i]:
            gf.ftrCardCreater( lst_info[i+9][0] ,lst_info[i+9][1])

title_card="🧹 What Is Happened In Data Cleaning Phase ?"
text_card="<div class='imformation-cd-subtitle'>Performed Steps</div>\
            - Those All Special Literals [ ~ , ! , @ ,  # , $ , % , ^ , & , * , ( , ) , - , _ , + , = , \\ , / ,\
                ? , ',' , '²' , . , New York] Are Existed In Host Names And Therefore All\
                These Previous Literals Had Been Removed From Each Listing Description contained one of them <br/>\
            - Removing All Numbers From Each Host Name If Existed<br/>\
            - The Instances On Which host_name Contains 'Data' Word Had Been Deleted<br/>\
            - Replacing All Nan Cells In Host Name Feature With 'unknown'\
            "
gf.showInfoCard(title_card,text_card)

#- Data Analysis
subtitle="Data Analysis"
gf.subtitleView(subtitle)
with st.expander(label="***Visualized Charts***",expanded=True):
    tab1 , tab2 = st.tabs(['bar charts' , 'pie charts']) 
    filtered_1_host,filtered_more_1_host=[],[]
    for name in renting_dataset['host_name']: 
        if len(str(name).split())==1:
            filtered_1_host.append(name)
        else:
            filtered_more_1_host.append(name)
    #- number of each unique value Sorted As Pandas Series   
    _1_host_occurances  = pd.Series(filtered_1_host  , name='one-host').value_counts() 
    more_1_hosts_occurances = pd.Series(filtered_more_1_host , name='more-one-host').value_counts()
    with tab1:
        with st.expander("single host vs number of accomodations"):
            #- chart description
            chart_title="Check Highest 10 Frequent Host Names"
            chart_desc="This Chart Describes What's The Highest  Frequent 10 Single Host Name, \
            They Provided Rentals"
            gf.chartDesc(chart_title,chart_desc) 
            #- Chart Display
            _1host_listings = pd.DataFrame(
                    {
                        'host_names'    : _1_host_occurances.index,
                        'listing_count' :  _1_host_occurances.values
                    }
            )
            #- Visualizing highest 10 listings At Airbnb From New-York City (mone host added accomodation Rent)
            st.plotly_chart(            
                px.bar(data_frame=_1host_listings[:10] ,y='host_names',x='listing_count',
                text_auto=True ,
                color_discrete_sequence=["#57B4BA"],
              )
            )
        with st.expander("double hosts vs number of accomodations"):
            #- chart description
            chart_title="Check Highest 10 Frequent Host Names"
            chart_desc="This Chart Describes What's The Highest  Frequent 10 Double Host Name, \
            They Provided Rentals"
            gf.chartDesc(chart_title,chart_desc) 
            #- Chart Display 
            _more1host_listings = pd.DataFrame(
                {
                'host_names' : more_1_hosts_occurances.index,
                'listing_count':more_1_hosts_occurances.values
                }
            ).sort_values(by='listing_count',ascending=False)
            #- Visualizing highest 10 listings At Airbnb From New-York City (mone host added accomodation Rent)
            st.plotly_chart(
                px.bar(data_frame=_more1host_listings[:10],y='host_names',
                    x='listing_count',
                    text_auto=True ,
                    color_discrete_sequence=["#57B4BA"],
                )
            )
        with st.expander("single host vs avg. price"):
            #- chart description
            chart_title="Check Highest 10 Average Prices On Single Host Names "
            chart_desc="This Chart Describes Highest ten average prices Which Single Hosts Provided \
            On Airbnb City"
            gf.chartDesc(chart_title,chart_desc) 
            #- vitualing Chart 
             #-single Hosts 
            meanprice_hostname_filter = renting_dataset['price'].groupby(renting_dataset['host_name']).mean()
            filter_desired_1host = round(meanprice_hostname_filter[_1host_listings['host_names']].sort_values(ascending=False),2)
            filter_desired_1host = pd.DataFrame(
                {
                    "host_name"  : filter_desired_1host.index,
                    "avg_prices" : filter_desired_1host.values
                }
            )
            st.plotly_chart(
                #- Visualizing Highest 10 Mean Of costs That One Host Provided
                px.bar(data_frame=filter_desired_1host[:10] ,
                    x="host_name",
                    y="avg_prices",
                    labels={'host_name':'Name Of Host','avg_prices':'Mean Of Prices'},
                    color_discrete_sequence=["#57B4BA"],
                    text_auto=True)
            )
        with st.expander("double host vs avg. price"):
            #- chart description
            chart_title="Check Highest 10 Average Prices On Douple Host Names "
            chart_desc="This Chart Describes Highest ten average prices Which Double Hosts Provided \
            On Airbnb City"
            gf.chartDesc(chart_title,chart_desc) 
            #-double Hosts 
            meanprice_hostname_filter = renting_dataset['price'].groupby(renting_dataset['host_name']).mean()
            filter_desired_more_1_host = round(meanprice_hostname_filter[_more1host_listings['host_names']].sort_values(ascending=False),2)
            filter_desired_more_1_host = pd.DataFrame(
                {
                    "host_name"  : filter_desired_more_1_host.index,
                    "avg_prices" : filter_desired_more_1_host.values
                }
            )
            st.plotly_chart(
                #- Visualizing Highest 10 Mean Of costs That double Host Provided
                px.bar(data_frame=filter_desired_more_1_host[:10] ,
                    x="host_name",
                    y="avg_prices",
                    labels={'host_name':'Name Of Host','avg_prices':'Mean Of Prices'},
                    color_discrete_sequence=["#57B4BA"],
                    text_auto=True)
            )
    with tab2:
        with st.expander("Precentage Of Room Types Rented By (michaeal)"):
            #- What's The Types Of Room That 'Michael' Listed Them For Renting 
            filter_michael_room_types = cleaned_renting_data[cleaned_renting_data['host_name']=='michael']['room_type'] 
            st.plotly_chart(
                #-what's the precentage of each room type which Micheal Had provided For Renting In That Data 
                px.pie(data_frame=pd.DataFrame({'room_type_micheal' :filter_michael_room_types.values }),
                names='room_type_micheal',
                color_discrete_sequence=['cyan','blue','red'],
                title='Precentages Of Room Types Which host "Micheal" Provided For Renting')
            )
        with st.expander("Precentage Of Room Types Rented By (mike)"):
            #- What's The Types Of Room That 'mike' Listed Them For Renting  
            filter_mike_room_types = cleaned_renting_data[cleaned_renting_data['host_name']=='mike']['room_type'] 
            #-what's the precentage of each room type which Micheal Had provided For Renting In That Data 
            px.pie(data_frame=pd.DataFrame({'room_type_mike' :filter_mike_room_types.values }),
            names='room_type_mike',color_discrete_sequence=['cyan','blue'],
            title='Precentages Of Room Types Which host name "Mike" Provided For Renting')
        with st.expander("Precentage Of Room Types Rented By (sonder NYC)"):
            #- What's The Types Of Room That 'sonder  and nyc' Listed Them For Renting 
            filter_sonder_nyc_room_types = cleaned_renting_data[cleaned_renting_data['host_name']=='sonder  and nyc']['room_type']
            st.plotly_chart(
                #-what's the precentage of each room type which sonder and nyc ( ) Had provided For Renting In That Data 
                #- Sonder (NYC) refers to a Selected collection of design-led apartment-style stays and boutique hotels in New York City.
                px.pie(data_frame=pd.DataFrame({'room_type_sonder_nyc' :filter_sonder_nyc_room_types.values }),
                names='room_type_sonder_nyc',color_discrete_sequence=['cyan','blue'],title='Precentages Of Room Types Which "sonder nyc" Provided For Renting')
            )
        with st.expander("Precentage Of Room Types Rented By (pi and leo)"):
            #- What's The Types Of Room That 'pi and leo' Listed Them For Renting 
            filter_pi_leo_room_types = cleaned_renting_data[cleaned_renting_data['host_name']=='pi and leo']['room_type']
            st.plotly_chart(
                #-what's the precentage of each room type which pi and leo Had provided For Renting In That Data 
                px.pie(data_frame=pd.DataFrame({'room_type_pi_leo' :filter_pi_leo_room_types.values }),
                names='room_type_pi_leo',color_discrete_sequence=['cyan','blue'],title='Precentages Of Room Types Which shared host names "pi and leo" Provided For Renting')
            )
        with st.expander("Precentage Of Room Types Rented By (wesly and jessica)"):
            #- What's The Types Of Room That wesly and jessica Listed Them For Renting 
            filter_wesly_jessica_room_types = cleaned_renting_data[cleaned_renting_data['host_name']=='wesly and jessica']['room_type']
            st.plotly_chart(
                #-what's the precentage of each room type which wesly and jessica Had provided For Renting In That Data 
                px.pie(data_frame=pd.DataFrame({'room_type_wesly and jessica' :filter_wesly_jessica_room_types.values }),
                names='room_type_wesly and jessica',color_discrete_sequence=['cyan','blue'],title='Precentages Of Room Types Which "wesly and jessica" Provided For Renting')
            )
#- Show Instance Of Insights Set(host_name feature)
insight_case = st.sidebar.checkbox(label="***Display Observations***",value=True,key=5)
if insight_case :
        subtitle="Insights"
        text_card="- <strong style='padding:0px;'>host_name</strong> Feature is A Categorical Feature\
              Have <strong style='padding:0px;'>11452</strong> Variant Hosts For Renting Accomodation \
              On Airbnb Website In New Work City Had Been Shown.<br/>\
            -   The Most Repeated host On Airbnb In New York City Is <strong style='padding:0px;'>Michael</strong>With\
            <strong style='padding:0px;'>417</strong> Listing<br/>\
            -  Number Of Hostings Which One Host had Provided Are  <strong style='padding:0px;'>46758</strong> Are While they Have More One Host Are  \
            <strong style='padding:0px;'>2137</strong><br/>\
            - The Most Repeated Ten Hosts In That Dataset Provided Renting Of Thier Houses And Was Just Individual Persons (one \
            host Raised renting On Airbnb Website From New York City In Us) \
            Presented In <strong style='padding:0px;'>Previous Charts In Section Data Analysis</strong> where highest Hostings\
             Was Are Provided By <strong style='padding:0px;'>micheal</strong> With <strong style='padding:0px;'>417</strong> \
            Hostings And Lowest Ones By <strong style='padding:0px;'>Mike</strong> with <strong style='padding:0px;'>194</strong><br/>\
            - The Type Of Listings Which  <strong style='padding:0px;'>Michael</strong> Offered For Renting In That Data Are \
             <strong style='padding:0px;'>Entire Home</strong> With  <strong style='padding:0px;'>60.2 %</strong> Out Of \
            Number Of Listings Was Offered By Host <strong style='padding:0px;'>Michael</strong>  \
            ,Shared Room With <strong style='padding:0px;'>36.5 %</strong> And Private Room With <strong style='padding:0px;'>3.36%</strong><br/> \
            - The Type Of Listings Which <strong style='padding:0px;'>Mike</strong> Offered For Renting \
            In That Data Are <strong style='padding:0px;'>Entire Home</strong> \
            With 72.7 % Out Of Number Of Listings Was Offered By Host <strong style='padding:0px;'>Mike</strong> \
            And Private Room With  <strong style='padding:0px;'>27.3%</strong>\
            - The Most Repeated Ten Hosts In That Dataset Provided Renting Of Thier\
            Houses And Was shared Persons (more than one host Raise renting On Airbnb Website From New York City In\
            Us) Presented In <strong style='padding:0px'>Previous Chart In Data Analysis Section</strong> where highest Hostings Was Are Provided By\
            <strong style='padding:0px'>Sonder and Nyc</strong> With <strong style='padding:0px'>327</strong><br/>\
            Hostings And Lowest Ones By <strong style='padding:0px'>(pi and leo),(charlie and selena) , \
            (jess and ana) And (wesly and jessica)</strong> With <strong style='padding:0px'>8</strong><br/>\
            -  The Type Of Listings Which <strong style='padding:0px'>sonder  and nyc</strong>\
             Offered For Renting In That Data Are <strong style='padding:0px'>Entire Home</strong>\
            With <strong style='padding:0px'>25.0 % </strong> Out Of Number Of Listings Was Offered \
            By Host <strong style='padding:0px'>sonder  and nyc</strong> And Private Room With <strong style='padding:0px'>75%</strong><br/> \
            - The Type Of Listings Which <strong style='padding:0px'>pi and leo</strong>\
             Offered For Renting In That Data Are <strong style='padding:0px'>Entire Home</strong>\
             With <strong style='padding:0px'>87.5 %</strong> Out Of Number Of Listings Was\
             Offered By Host <strong style='padding:0px'>pi and leo</strong> And Private Room\
             With <strong style='padding:0px'>12.5%</strong><br/>\
             -  <strong style='padding:0px'>jess and ana</strong> \
            Offered Only Just Shared Room For Renting In All Cases \
            In That Data<br/> \
            - The Type Of Listings Which <strong style='padding:0px'>wesly and jessica</strong>\
            Offered For Renting In That Data Are <strong style='padding:0px'>Entire Home</strong>\
            With <strong style='padding:0px'>75 %</strong> Out Of Number Of Listings Was Offered By\
            Host <strong style='padding:0px'>wesly and jessica</strong> \
            And <strong style='padding:0px'>Private Room</strong> With <strong style='padding:0px'>25 %</strong><br/>\
            - The Highest Ten Renting Averages Provided From Individual Persons \
            (one host Raised renting On Airbnb Website From New York City In Us)  \
            Where Largest Average Provided By <strong style='padding:0px'>olson</strong>\
            With <strong style='padding:0px'>9.999 K</strong> While Less Average By \
            <strong style='padding:0px'>viberlyn</strong> With <strong style='padding:0px'>2995</strong><br/>\
            -  <strong style='padding:0px'>Olson</strong> Offered Only Just Entire Home \
            For Renting In All his Cases In That Data.<br/> \
            -  <strong style='padding:0px'>viberlyn</strong> Offered Only Just Entire Home For \
            Renting In All his Cases In That Data .<br/>\
            - The Highest Ten Renting Averages Provided From shared \
            Persons (more one host Raised renting On Airbnb Website From New York City In Us)\
            Where Largest Average Provided By <strong style='padding:0px'>Jay and Liy</strong>\
            With <strong style='padding:0px'>6000</strong> While Less Average\
            By <strong style='padding:0px'>jeff and kelly</strong> With <strong style='padding:0px'>949</strong><br/>\
            -  <strong style='padding:0px'>Jay and Liy</strong> Offered Only Just Entire home For \
            Renting In All thier Cases In That Data.<br/>\
            -  <strong style='padding:0px'>jeff and kelly</strong> Offered Only Just Private \
            room For Renting In All thier Cases In That Data.\
            "
        gf.subtitleView(subtitle)
        gf.showInfoCard(title_card="insights set (host_name Feature)",text_card=text_card)
#- Data Engineering Container 
subtitle="Data Engineering"
gf.subtitleView(subtitle)
#- Show  Set (News feature)
date_eng_case = st.sidebar.checkbox(label="***Data Engineering***",value=True,key=7)
if date_eng_case:
    feature_names=['hosts_count']
    gf.extractFtrName(feature_names=feature_names)

#-- Data Understanding Of nighbourhood_group Feature --#
#- Title Of Understanding Of nighbourhood_group Feature
gf.secTitleName(title_name="Data Understanding Of neighbourhood_group Feature")
#- Primary Info
subtitle="primary info"
gf.subtitleView(subtitle)
#- Content Of Primary Info About name feature
primary_info_set1 = st.columns(4)
lst=[
    ("🔢 Feature Type",'Object'),
    ("⚠️ Missing",f"{renting_dataset['neighbourhood_group'].isna().sum():,}"),
    ("✦  Uniques Number",f"{renting_dataset['neighbourhood_group'].nunique()}"),
    ("🏆 Most Frequent borough","Manhattan","freq : 21661"),
]
for i in range(4):
    if len(lst[i])==3:
        with primary_info_set1[i]:
            st.metric(
                f"{lst[i][0]}",
                f"{lst[i][1]}",
                delta=f"{lst[i][2]}"
        )
    else:
        with primary_info_set1[i]:
            st.metric(
                f"{lst[i][0]}",
                f"{lst[i][1]}",
        )
#- Sidebar name feature Options
st.sidebar.markdown("<font class='sidebar-subtitle'><strong>\
                     ⬤ </strong> neighbourhood_group Feature Options</font><br/>",
                     unsafe_allow_html=True)
#- Data Analysis
subtitle="Data Analysis"
gf.subtitleView(subtitle)
with st.expander(label="***Visualized Charts***",expanded=True):
    tab1 , tab2 ,tab3 , tab4 = st.tabs(tabs=["chart-1","chart-2","chart-3","chart-4"])
    with tab1:
        #- chart description
        chart_title="Counting Of Each Label In neighbourhood_group"
        chart_desc="This Chart Describes What's The  Frequency Of Each Borough inseted In This Dataset,\
        Which Help In Clearing Which Borough Had Been Occured Highly"
        gf.chartDesc(chart_title,chart_desc) 
        #- Chart Display
        st.plotly_chart(
            px.histogram(data_frame=renting_dataset,x="neighbourhood_group",text_auto=True
             ,color_discrete_sequence=["#57B4BA"]).update_xaxes(categoryorder="max descending")
        )
        with tab2:
            #- chart description
            chart_title="Most 10 Maximum Prices In Which Borough"
            chart_desc="This Chart Describes What's The Maximum Renting Price Was In Any Borough"
            gf.chartDesc(chart_title,chart_desc) 
            #- Chart Display
            filter_maxprice_borough = renting_dataset['price'].groupby(renting_dataset['neighbourhood_group']).max().sort_values(ascending=False)
            filter_maxprice_borough  = pd.DataFrame({
                "Borough"   :filter_maxprice_borough.index ,
                "Max_Price" :filter_maxprice_borough.values
            })
            st.plotly_chart(
                    px.bar(filter_maxprice_borough,x="Borough",y="Max_Price"
                           ,text_auto=True,color_discrete_sequence=["#57B4BA"]) 
                )
        with tab3:
            #- chart description
            chart_title="Average Prices Is Paied For Each Borough "
            chart_desc="This Chart Describes The Average Renting Prices Of Each Borough"
            gf.chartDesc(chart_title,chart_desc) 
            #- Chart Display
            fltr_avgprice_borough = round(renting_dataset['price'].groupby(renting_dataset['neighbourhood_group']).mean().sort_values(ascending=False),2)
            fltr_avgprice_borough = pd.DataFrame({
                    "Borough": fltr_avgprice_borough.index,
                    "Average Prices" :fltr_avgprice_borough.values
            })
            st.plotly_chart(
                    px.bar(
                        data_frame = fltr_avgprice_borough,
                        x = "Borough",
                        y="Average Prices",
                        text_auto=True,
                        color_discrete_sequence=["#57B4BA"]
                    ) 
            )
        with tab4:
            #- chart description
            chart_title="Coordinates For Each Stay On A Map"
            chart_desc="This Chart Describes How Stay Coordinates Is Found On A Global Map"
            gf.chartDesc(chart_title,chart_desc) 
            #- Inserting A Map(display Char)
            st.plotly_chart(
                px.scatter_map(renting_dataset,lat="latitude",lon="longitude",color='neighbourhood_group',
                    color_discrete_sequence=["#76ABAE","#D10056","#003049","#2C687B","#E7D283"])
            )
#- Show Instance Of Insights Set(host_name feature)
insight_case = st.sidebar.checkbox(label="***Display Observations***",value=True,key=6)
if insight_case :
        subtitle="Insights"
        text_card="- <strong style='padding:0px;'>neighbourhood_night</strong> Feature is A Categorical Feature\
            Have <strong style='padding:0px'>Five Different Boroughs</strong> Are Brooklyn , Manhattan ,Queens , Staten_Island and Bronx<br/>\
            - most two boroughs have largest number of listings Are   \
            <strong style='padding:0px'>Manhattan and Broklyn</strong> And Therefore\
            , Airbnb Activity Is Heavly Concerned In Those Two Previous Boroughs<br/>\
            - There Is No Missing Values Here In This Column<br/>\
            - The Most Frequent Borough Where Renting Is Highest Is <strong style='padding:0px'>Manhattan</strong>\
            While Lowest Number Of Booking  Renting Is In <strong style='padding:0px'>Bronx</strong><br/>\
            - The Maximum Renting Price Was In <strong style='padding:0px'>Manhatta , Broklyn And  Queens </strong> And All Those Boroughs Are Coastal Cities.<br/>\
            - The Most Three Average Prices Of Renting Was In <strong style='padding:0px'>Manhattan , Broklyn And  Staten Island </strong> <br/>\
            - The Hugest Type Of Rooms Was Renting In All Boroughs Is <strong style='padding:0px'>Shared Rooms</strong> While Lowest Type Of Rooms Was Renting In \
            All Boroughs Is  <strong style='padding:0px'>Entire Home/Appartment</strong><br/>"
        gf.subtitleView(subtitle)
        gf.showInfoCard(title_card="insights set (neighbourhood_night Feature)",text_card=text_card)

#-- Data Understanding Of neigbourhood Feature --#
#- Title Of Understanding Of neigbourhood Feature
gf.secTitleName(title_name="Data Understanding Of neigbourhood Feature")
#- Primary Info
subtitle="primary info"
gf.subtitleView(subtitle)
#- Content Of Primary Info About neighbourhood feature
primary_info_set1 = st.columns(4)
lst=[
    ("🔢 Feature Type",'Object (categorical)'),
    ("⚠️ Missing",f"{renting_dataset['neighbourhood'].isna().sum():,}"),
    ("✦  Uniques Number",f"{renting_dataset['name'].nunique()}"),
    ("🏆 Most Frequent Accomodation Description","Williamsburg","freq : 3920"),
]
for i in range(4):
    if len(lst[i])==3:
        with primary_info_set1[i]:
            st.metric(
                f"{lst[i][0]}",
                f"{lst[i][1]}",
                delta=f"{lst[i][2]}"
        )
    else:
        with primary_info_set1[i]:
            st.metric(
                f"{lst[i][0]}",
                f"{lst[i][1]}",
        )
st.sidebar.markdown("<font class='sidebar-subtitle'><strong>\
                     ⬤ </strong> neighbourhood Feature Options</font><br/>",
                     unsafe_allow_html=True)
data_clean_case = st.sidebar.checkbox(label="***Data Cleaning***",value=True,key=8)
#- Data Cleaning Container 
subtitle="Data Cleaning"
gf.subtitleView(subtitle)
if data_clean_case:
    lst_info=[
        ("How Many did special Literal '-' appear?",
         "Literal '-' Appeared <strong style='text-decoration:underline;'>4247</strong> Time"),
        ("How Many did special Literal '.' appear?",
         "Literal '.' Appeared <strong style='text-decoration:underline;'>124</strong> Time"),
        ("How Many did special Literal ',' appear?",
         "Literal ',' Appeared <strong style='text-decoration:underline;'>2</strong> Time"),
    ] 
    #- Show Information About Special characters In name feature
    common_row  = st.columns(3)
    for i in range(0,3):
        with common_row[i]:
            gf.ftrCardCreater( lst_info[i][0] ,lst_info[i][1])
title_card="🧹 What Is Happened In Data Cleaning Phase ?"
text_card="<div class='imformation-cd-subtitle'>Performed Steps</div>\
            - Those All Special Literals [ '-' , '.' , ','] Are Existed In Host Names And Therefore All\
                These Previous Literals Had Been Removed From Each Listing Description contained one of them <br/>\
            - <strong style='padding:0px'>326</strong> Value in neighbourhood Feature Has Borough name And All Sequences\
            Appeared In Those Value Had Been Removed<br/> \
            "
gf.showInfoCard(title_card,text_card)
#- Data Analysis
subtitle="Data Analysis"
gf.subtitleView(subtitle) 
with st.expander("**visualized Charts**" , expanded=True):
    #- chart description
    chart_title="Counting Of Highest 1-hundred Priced Places"
    chart_desc="This Chart Is Used To Describe Count Each Place\
        In All Boroughs Which Representing Highest 1-hundred Renting Prices\
        And Show As Group Bars."
    gf.chartDesc(chart_title,chart_desc) 
    #- Chart Display
    max_ten_prices = cleaned_renting_data.sort_values(by="price" , ascending=False).head(100)
    borough_place_price = max_ten_prices[["neighbourhood_group","neighbourhood","price"]]
    default_colors = px.colors.qualitative.Plotly
    st.plotly_chart(
        px.histogram(data_frame=borough_place_price,
             x="neighbourhood_group",
             color="neighbourhood", 
             barmode="group",
             color_discrete_sequence=default_colors
        )
    )
#- Show Instance Of Insights Set(host_name feature)
insight_case = st.sidebar.checkbox(label="***Display Observations***",value=True,key=9)
if insight_case :
        subtitle="Insights"
        text_card="- <strong style='padding:0px;'>neighbourhood</strong> Feature is A Categorical Feature\
            Have <strong style='padding:0px'>221 Different Places</strong><br/>\
           - There Is No Missing Values Here In <strong style='padding:0px'>neighbourhood</strong> Feature\
            , Airbnb Activity Is Heavly Concerned In Those Two Previous Boroughs<br/>\
           - The Highest Place In Which Renting Numbers was hugest <strong style='padding:0px'>Williamsburg</strong> \
            Located In <strong style='padding:0px'>Brooklyn Borough</strong> With Average Price <strong style='padding:0px'>143.8</strong><br/>\
           - Highest Five Renting Locations Are  <strong style='padding:0px'>Williamsburg :4500 , Upper West Side/Manhattan:5000 , Bushwick:5000, Harlem:2000 and Bedford-Stuyvesant:10000</strong>\
            And Here The Number Represents Frequency Times.<br/>\
           - The Highest Renting Price Was Paid In Those Places : Location -->  Borough<br/>\
           - Also According To Visualization Chart , The Highest Renting Location Was In <strong style='padding:0px'>Manhattan</strong><br/>"
        gf.subtitleView(subtitle)
        gf.showInfoCard(title_card="insights set (neighbourhood Feature)",text_card=text_card)

#-- Data Understanding Of Latitude And Longitude Feature --#
#- Title Of Understanding Of Latitude And Longitude Feature
gf.secTitleName(title_name="Data Understanding Of Latitude And Longitude Feature")
#- Primary Info
subtitle="primary info"
gf.subtitleView(subtitle)
#- Content Of Primary Info About neighbourhood feature
primary_info_set1 = st.columns(4)
lst=[
    ("🔢 Latitude Type",'float'),
    ("🔢 Longitude Type",'float'),
    ("⚠️ Latitude Missing",f"{renting_dataset['latitude'].isna().sum() :,}"),
    ("⚠️ Longitude Missing",f"{renting_dataset['longitude'].isna().sum() :,}"),
]
for i in range(4):
    with primary_info_set1[i]:
        st.metric(
            f"{lst[i][0]}",
             f"{lst[i][1]}",
        )
st.sidebar.markdown("<font class='sidebar-subtitle'><strong>\
                     ⬤ </strong> Latitude And Longitude Feature Options</font><br/>",
                     unsafe_allow_html=True)
#- Data Analysis
subtitle="Data Analysis"
gf.subtitleView(subtitle)
with st.expander("**visualized Charts**" , expanded=True):
    #- chart description
    chart_title="Plotting Scatter Between Latitude And Longitude"
    chart_desc="This Chart Is Used To Describe How Those Points Is Spread\
       Which It Clears Where Stays Are"
    gf.chartDesc(chart_title,chart_desc)
    #- display chart 
    #- Splitting The Graph Representing The Locations Spread According To Number Of Boroughs
    filter_manhattan = renting_dataset[renting_dataset['neighbourhood_group']=="Manhattan"][["latitude","longitude"]] 
    filter_Brooklyn  = renting_dataset[renting_dataset['neighbourhood_group']=="Brooklyn"][["latitude","longitude"]] 
    filter_Queens    = renting_dataset[renting_dataset['neighbourhood_group']=="Queens"][["latitude","longitude"]]
    filter_Staten_Is = renting_dataset[renting_dataset['neighbourhood_group']=="Staten Island"][["latitude","longitude"]] 
    filter_Bronx     = renting_dataset[renting_dataset['neighbourhood_group']=="Bronx"][["latitude","longitude"]] 
    fig, ax = plt.subplots(figsize=(8, 6))
    # Plot each neighbourhood group
    ax.scatter(
            filter_manhattan['latitude'],
            filter_manhattan['longitude'],
            color="#8C56D4",
            label="Manhattan"
        )
    ax.scatter(
            filter_Brooklyn['latitude'],
            filter_Brooklyn['longitude'],
            color="#3A86FF",
            label="Brooklyn"
        )
    ax.scatter(
            filter_Queens['latitude'],
            filter_Queens['longitude'],
            color="#45A9A9",
            label="Queens"
        )
    ax.scatter(
            filter_Staten_Is['latitude'],
            filter_Staten_Is['longitude'],
            color="#F375C2",
            label="Staten Island"
        )
    ax.scatter(
            filter_Bronx['latitude'],
            filter_Bronx['longitude'],
            color="#441752",
            label="Bronx"
        )
    ax.set_title("Latitude vs Longitude")
    ax.set_xlabel("Latitude")
    ax.set_ylabel("Longitude")
    ax.legend()
    plt.tight_layout()
    st.pyplot(fig) 
#- Show Instance Of Insights Set(lat and long feature)
insight_case = st.sidebar.checkbox(label="***Display Observations***",value=True,key=10)
if insight_case:
        subtitle="Insights"
        text_card="- <strong style='padding:0px'>Latitude and Longitude</strong> is Numerical Features Have\
        No Missing Value<br>\
        - The Samples Of This Renting Data Set Is Spread Arroud All Five Boroughs In New York City"
        gf.subtitleView(subtitle)
        gf.showInfoCard(title_card="insights set (Latitude And Longitude Feature)",text_card=text_card)
#- Data Engineering Container 
subtitle="Data Engineering"
gf.subtitleView(subtitle)
#- Show  Set (News feature)
date_eng_case = st.sidebar.checkbox(label="***Data Engineering***",value=True,key=11)
if date_eng_case:
    feature_names=['distance_km']
    gf.extractFtrName(feature_names=feature_names)

#-- Data Understanding Of room_type Feature --#
#- Title Of Understanding Of room_type Feature
gf.secTitleName(title_name="Data Understanding Of room_type Feature")
#- Primary Info
subtitle="primary info"
gf.subtitleView(subtitle)
#- Content Of Primary Info About neighbourhood feature
primary_info_set1 = st.columns(4)
lst=[
    ("🔢 Latitude Type",'category'),
    ("⚠️ Missing",f"{renting_dataset['room_type'].isna().sum() :,}"),
    ("✦  Uniques Number",f"{renting_dataset['room_type'].nunique()}"),
    ("🏆 Most Frequent host","Entire Home/apt","freq :  25409"),
]
for i in range(4):
    if len(lst[i])==3:
        with primary_info_set1[i]:
            st.metric(
                f"{lst[i][0]}",
                f"{lst[i][1]}",
                delta=f"{lst[i][2]}"
        )
    else:
        with primary_info_set1[i]:
            st.metric(
                f"{lst[i][0]}",
                f"{lst[i][1]}",
        )
st.sidebar.markdown("<font class='sidebar-subtitle'><strong>\
                     ⬤ </strong>room_type Feature Options</font><br/>",
                     unsafe_allow_html=True) 
#- Data Cleaning Container 
subtitle="Data Cleaning"
gf.subtitleView(subtitle)
if data_clean_case:
    lst_info=[
        ("How Many did special Literal '/' appear?",
         "Literal '/' Appeared <strong style='text-decoration:underline;'>25409</strong> Time"),
    ] 
    #- Show Information About Special characters In name feature
    common_row  = st.columns(1)
    for i in range(0,1):
        with common_row[i]:
            gf.ftrCardCreater( lst_info[i][0] ,lst_info[i][1])
title_card="🧹 What Is Happened In Data Cleaning Phase ?"
text_card="<div class='imformation-cd-subtitle'>Performed Steps</div>\
            -  All Room Types Consisting of '/' Special Character Must Be Cleaned From This Literal<br/>\
            "
gf.showInfoCard(title_card,text_card)
#- Data Analysis
subtitle="Data Analysis"
gf.subtitleView(subtitle)
with st.expander("**visualized Charts**" , expanded=True):
    tab1,tab2,tab3,tab4 = st.tabs(['count plot','Average Prices','Maximum Prices','Minimum Prices'])
    with tab1:
        #- chart description
        chart_title="Number Of Each Type Room"
        chart_desc="This Chart Is Used To Count Renting Listings For Each Type Room"
        gf.chartDesc(chart_title,chart_desc)
        #- display chart 
        #- Counting Of Each Category In room_type Feature
        st.plotly_chart(
            px.histogram(
            data_frame=cleaned_renting_data,
            x='room_type',
            color_discrete_sequence=["#57B4BA"],
            text_auto=True 
        ).update_xaxes(categoryorder="max descending")
        )
    with tab2:
        #- chart description
        chart_title="Average Prices For Each Room Type"
        chart_desc="This Chart Is Used To Show The Average Price Of Each Group Of\
        Renting Listings For Each Type Room"
        gf.chartDesc(chart_title,chart_desc)
        #- display chart
        avg_prices = round(cleaned_renting_data['price'].groupby(cleaned_renting_data['room_type']).mean(),2)
        fig , ax = plt.subplots(figsize=(8,4))  
        ax.bar(avg_prices.index , avg_prices.values,color="#57B4BA")
        ax.set_title("Room Type Vs Price Average")
        ax.set_xlabel("Room Type")
        ax.set_ylabel("Price Average") 
        st.pyplot(fig)
    with tab3:
        #- chart description
        chart_title="Maximum Price For Each Room Type"
        chart_desc="This Chart Is Used To Show The Maximum Price Of Each Group Of\
        Renting Listings For Each Type Room"
        gf.chartDesc(chart_title,chart_desc)
        #- display chart
        max_prices = round(cleaned_renting_data['price'].groupby(cleaned_renting_data['room_type']).max(),2)
        fig , ax = plt.subplots(figsize=(8,4))  
        ax.bar(max_prices.index,max_prices.values,color="#57B4BA")
        ax.set_title("Room Type Vs Price Average")
        ax.set_xlabel("Room Type")
        ax.set_ylabel("Price Average") 
        st.pyplot(fig)
    with tab4:
        #- chart description
        chart_title="Minimum Price For Each Room Type"
        chart_desc="This Chart Is Used To Show The Mimimum Price Of Each Group Of\
        Renting Listings For Each Type Room"
        gf.chartDesc(chart_title,chart_desc)
        #- display chart
        min_prices = round(cleaned_renting_data['price'].groupby(cleaned_renting_data['room_type']).min(),2)
        fig , ax = plt.subplots(figsize=(8,4))  
        ax.bar(max_prices.index,max_prices.values,color="#57B4BA")
        ax.set_title("Room Type Vs Price Average")
        ax.set_xlabel("Room Type")
        ax.set_ylabel("Price Average") 
        st.pyplot(fig)
#- Show Instance Of Insights Set(lat and long feature)
insight_case = st.sidebar.checkbox(label="***Display Observations***",value=True,key=12)
if insight_case:
        subtitle="Insights"
        text_card="- <strong style='padding:0px'>room_type</strong>  A Categorical Feature Doesn't Contain\
            Missing Values Have Three Types Of Rooms: <br/><strong style='padding-left:15px;text-decoration:underline;font-size:14px;'>1. Entire Home / Apt</strong><br>\
            <strong style='padding-left:15px;text-decoration:underline;font-size:14px;'>2. Private Room</strong><br>\
            <strong style='padding-left:15px;text-decoration:underline;font-size:14px;'>3. shared Room</strong><br>\
            - The Maximum Renting Price For Each Room Type Is:<br/>\
            <strong style='padding-left:15px;text-decoration:underline;font-size:14px;'> 1. Entire Home : 10k  USA Dolar</strong><br>\
            <strong style='padding-left:15px;text-decoration:underline;font-size:14px;'> 2. Private Room: 10k  USA Dolar</strong><br>\
            <strong style='padding-left:15px;text-decoration:underline;font-size:14px;'> 3. Shared Room : 1.8k USA Dolar</strong><br> \
            - The Minimum Renting Price For Each Room Type Is<br/>\
            <strong style='padding-left:15px;text-decoration:underline;font-size:14px;'> 1. Entire Home  : 10 USA Dolar</strong><br>\
            <strong style='padding-left:15px;text-decoration:underline;font-size:14px;'> 2. Private Room : 10 USA Dolar</strong><br>\
            <strong style='padding-left:15px;text-decoration:underline;font-size:14px;'> 3. Shared Room : 10 USA Dolar</strong><br> \
            - The Average Renting Price For Each Room Type Is<br/>\
            <strong style='padding-left:15px;text-decoration:underline;font-size:14px;'> 1. Entire  Home  : 212.81 USA Dolar</strong><br>\
            <strong style='padding-left:15px;text-decoration:underline;font-size:14px;'> 2. Private Room  : 89.81  USA Dolarr</strong><br>\
            <strong style='padding-left:15px;text-decoration:underline;font-size:14px;'> 3. Shared  Room  : 70.25  USA Dolar</strong><br> \
            "
        gf.subtitleView(subtitle)
        gf.showInfoCard(title_card="insights set (room_type Feature)",text_card=text_card)

#-- Data Understanding Of minimum_neighs Feature --#
#- Title Of Understanding Of minimum_neighs Feature
gf.secTitleName(title_name="Data Understanding Of minimum_neighs Feature")
#- Primary Info
subtitle="primary info"
gf.subtitleView(subtitle)
#- Content Of Primary Info About neighbourhood feature
primary_info_set1 = st.columns(4)
lst=[
    ("🔢 Latitude Type",f"{str(renting_dataset['minimum_nights'].dtype)}"),
    ("⚠️ Missing",f"{renting_dataset['minimum_nights'].isna().sum() :,}"),
    ("✦  Uniques Number",f"{renting_dataset['minimum_nights'].nunique()}"),
    ("💰 median",f"{renting_dataset['minimum_nights'].median()}"),
]
for i in range(4):
    with primary_info_set1[i]:
        st.metric(
            f"{lst[i][0]}",
            f"{lst[i][1]}",
        )
st.sidebar.markdown("<font class='sidebar-subtitle'><strong>\
                     ⬤ </strong>minimum_nights Feature Options</font><br/>",
                     unsafe_allow_html=True) 
#- show outliers 
radio_case = st.sidebar.radio(label="***Outliers***",options=["Valid"],key=13) 
if radio_case=='Valid':
    gf.ftrCardCreater( "Valid Number Of Outliers" , "6605" )
#- Data Analysis
subtitle="Data Analysis"
gf.subtitleView(subtitle)
with st.expander("**visualized Charts**" , expanded=True):
    #- Preparing Data To Be Shown 
        #- filtering Data On minimum nights  ( Not Outliers ) 
    q1 = renting_dataset['minimum_nights'].quantile(0.25)
    q3 = renting_dataset['minimum_nights'].quantile(0.75)
    IQR = q3-q1
    lower_bound = q1-1.5*IQR 
    upper_bound = q3+1.5*IQR 
        #- filtering Data On minimum nights  ( Not Outliers ) 
    cond_1 = (renting_dataset['minimum_nights']>=lower_bound) 
    cond_2 = (renting_dataset['minimum_nights']<=upper_bound)
    filter_min_nights = renting_dataset[cond_1 & cond_2] 
    filter_nights  = filter_min_nights['minimum_nights'].value_counts(ascending=False) 
        #- Max Price For Each Minimum Night From one To Eleven 
    night_maxprice={}
    nights=list(filter_nights.index) 
    for n in nights: 
        num = num2words(n)
        night_maxprice[f"{num} night"] = int(cleaned_renting_data[cleaned_renting_data['minimum_nights']==n]['price'].max())
        #- Min Price For Each Minimum Night From one To Eleven 
    night_minprice={}
    nights=list(filter_nights.index) 
    for n in nights: 
        num = num2words(n)
        night_minprice[f"{num} night"] = int(cleaned_renting_data[cleaned_renting_data['minimum_nights']==n]['price'].min())
        #- Mean Price For Each Minimum Night From one To Eleven 
    night_avgprice={}
    nights=list(filter_nights.index) 
    for n in nights: 
        num = num2words(n)
        night_avgprice[f"{num} night"] = int(cleaned_renting_data[cleaned_renting_data['minimum_nights']==n]['price'].mean())   
        #- Creating A Dictionary That Hode 
        #- keys-values Expressions : 
            #- nights are not outliers
            #- maximum Price Paied For Each Unique Number Of Nights
            #- minimum Price Paied For Each Unique Number Of Nights 
            #- average Price Paid For Each Unique Number Of Nights
    nights_prices = pd.DataFrame(
        {
            "Non-Outlier Nights" : night_maxprice.keys(),
            "Maximum Price"      : night_maxprice.values(),
            "Minimum Price"      : night_minprice.values(),
            "Average Price"      : night_avgprice.values()
        }
        )
    charts = [f"chart-{i+1}" for i in range(6)] 
    tab1,tab2,tab3,tab4,tab5,tab6 = st.tabs(charts)
    with tab1:
        #- chart description
        chart_title="Relationship Between Price And Minimum Nights"
        chart_desc="This Chart Is Used To Show How The Renting \
        Prices Affect Minimum nights ."
        gf.chartDesc(chart_title,chart_desc)
        #- display chart 
        #- Determine How Minimum_nights Feature Is Spread With price Feature
        st.plotly_chart(
            px.scatter(
                data_frame=renting_dataset,
                x= "minimum_nights",
                y="price",
                labels={"minimum_nights":"Number Of Nights Must Be Booked" , "price":"Listing Price"},
                title="Renitng Nights Vs Renting Price (including Outliers)",
                color_discrete_sequence=["#57B4BA"]
            )
        )
    with tab2:
        #- chart description
        chart_title="Progress Line"
        chart_desc="- This Chart Is Used To Show Progress Line Between Unique \
        Booked Nights Versus Maximum Price.<br>\
        - A Line Chart Describing Non-Outliers Of Minimum Nights Must Be Booked\
        And Maximum Renting Price Was Paid For Each Non-Abnormal Valid Value."
        gf.chartDesc(chart_title,chart_desc)
        #- display chart
        st.plotly_chart(
            px.line(data_frame=nights_prices,x="Non-Outlier Nights",y=["Maximum Price"],
            markers=True,
            color_discrete_sequence=["#57B4BA"],
            title="Nights Vs Maximum Price")
        )
    with tab3:
        #- chart description
        chart_title="Minimum Nights Vs Maximum And Average Price"
        chart_desc="- Progress Line Between Unique Booked Nights Versus Average And Minimum Price.<br/>\
        - This Chart Is Used To Show How Minimum Renting Price And Also Average\
        Was Affected By Number Of Minimum Nights Must Be Rented."
        gf.chartDesc(chart_title,chart_desc)
        #- display chart
        st.plotly_chart(
            px.line(data_frame=nights_prices,x="Non-Outlier Nights",y=["Minimum Price","Average Price"],
                    markers=True,
                    color_discrete_sequence=["#57B4BA","#90CAF9"],
                title="Nights Vs Minimum/Avg Price")
        )
    with tab4:
        #- chart description
        chart_title="Non-outlier Nights Vs number of bookings For Each Borough"
        chart_desc="- Visualizing Nights Vs Boroughs In Where Non-Outlier Nights Was Booked<br/>\
        - This Chart Describes the Count Of Each Non-Abnormal Minimum Night Must Be Booked\
        For Each Borough<br/>"
        gf.chartDesc(chart_title,chart_desc)
        #- display chart
        filter_nights_boroughs = renting_dataset[cond_1 & cond_2]
        min_prices = round(cleaned_renting_data['price'].groupby(cleaned_renting_data['room_type']).min(),2)
        st.plotly_chart(
            px.histogram(
                data_frame=filter_nights_boroughs,
                x="minimum_nights",
                color="neighbourhood_group" ,
                labels={"minimum_nights" : "nights"},
                barmode="group",
                color_discrete_sequence=["#E63946","#2196F3","#547792","#239BA7","#4635B1"],
                title="Non-Outlier Nights Vs Number Of Bookings For Each Borough"
            )
        )
    with tab5:
        #- chart description
        chart_title="Non-outlier Nights Vs number of bookings For Each Room Type"
        chart_desc="- Visualizing Nights Vs Room Type In Where Non-Outlier Nights Was Booked<br/>\
        - This Chart Describes the Count Of Each Non-Abnormal Minimum Night Must Be Booked\
        For Each Room Type<br/>"
        gf.chartDesc(chart_title,chart_desc)
        #- display chart
        filter_nights_boroughs = renting_dataset[cond_1 & cond_2]
        st.plotly_chart(
            px.histogram(
                data_frame=filter_nights_boroughs,
                x="minimum_nights",
                color="room_type",
                labels={"minimum_nights":"nights"},
                barmode="group",
                color_discrete_sequence=["#E63946" ,"#2196F3" ,"#547792"] ,
                title="Non-Outlier Nights Vs Number Of Bookings For Each Room Type"
            )
        )
    with tab6:
        #- chart description
        chart_title="he Relations Between Outliers Of Minimum Nights And Prices"
        chart_desc="-Visualizing The Relationship Between Minimum Nights Are Outliers And\
        Renting Prices.<br/>"
        gf.chartDesc(chart_title,chart_desc)
        #- display chart
        #-Dealing With Valid Oultliers 
        idx_outliers = detect_outliers(data=renting_dataset,n=0,features=['minimum_nights'])
        filter_outliers = renting_dataset.loc[idx_outliers] 
        fig , ax = plt.subplots(figsize=(6,5))
        ax.scatter(x=filter_outliers['minimum_nights'],y=filter_outliers['price'],color="#427AB5")
        ax.set_title("Relationship  Between Minimum Night Versus Price (Outliers)")
        ax.set_xlabel("Minimum Nights")
        ax.set_ylabel("Price")
        st.plotly_chart(fig)
#- Show Instance Of Insights Set(lat and long feature)
insight_case = st.sidebar.checkbox(label="***Display Observations***",value=True,key=14)
if insight_case:
        subtitle="Insights"
        text_card="-<strong style='padding:0px;'>minimum_nights</strong> Feature \
            is A Numerical Feature Have <strong style='padding:0px'>109</strong>\
            Unique Postive Integers   Such It Represents Nights Was Been Booked Via Airbnb.<br/>\
            - There is no Missing Values/User Input Errors<br/>\
            - There Are Outliers In This Feature Values Such That The Variance Between maximum And Minimum Value\
            Is Very Hugh  (min , 1 ) And (max , 1250)<br/>\
            - There Are <strong style='padding:0px;'>6605 Outliers/Abnormal Values</strong>\
            From Total 48895 Instance Representing <strong style='padding:0px;'>13.51%</strong> \
            Out All Data Instances.<br/>\
            - After Caculating Interquantile Range To Determine Which Values Are Not Represented As Outliers\
            <strong style='padding:0px'>From 1 night To 11 night</strong><br/>\
            -  Number of Nights For Which Maximum Renting Price Was Paid<br/>\
            <strong style='padding-left:15px;text-decoration:underline;font-size:14px;'>- 3 night </strong> , maximum price paid For <strong style='padding-left:15px;text-decoration:underline;font-size:14px;'> 10k </strong><br>\
            <strong style='padding-left:15px;text-decoration:underline;font-size:14px;'>- 5 night </strong> , maximum price paid For <strong style='padding-left:15px;text-decoration:underline;font-size:14px;'> 10k </strong><br>\
            -  Number of Nights For Which Minimum Renting Price Was Paid<br/>\
            <strong style='padding-left:15px;text-decoration:underline;font-size:14px;'>- one night </strong> , minimum price paid For <strong style='padding-left:15px;text-decoration:underline;font-size:14px;'> 10 </strong><br>\
            <strong style='padding-left:15px;text-decoration:underline;font-size:14px;'>- two night </strong> , minimum price paid For <strong style='padding-left:15px;text-decoration:underline;font-size:14px;'> 10 </strong><br>\
            <strong style='padding-left:15px;text-decoration:underline;font-size:14px;'>- five night </strong> , minimum price paid For <strong style='padding-left:15px;text-decoration:underline;font-size:14px;'> 10 </strong><br> \
            <strong style='padding-left:15px;text-decoration:underline;font-size:14px;'>- seven night </strong> , minimum price paid For <strong style='padding-left:15px;text-decoration:underline;font-size:14px;'> 10 </strong><br>\
            - Number of Nights  Which Highest Average Renting Price Was Paid<br/>\
            <strong style='padding-left:15px;text-decoration:underline;font-size:14px;'>- One night </strong> , minimum borough Provided one night For Renting :<strong style='padding-left:15px;text-decoration:underline;font-size:14px;'> Staten Island </strong> While\
            maximum Borough Provided One Night For Renting : <strong style='padding-left:15px;text-decoration:underline;font-size:14px;'> Manhattan </strong>.<br/>\
            <strong style='padding-left:15px;text-decoration:underline;font-size:14px;'>- Two   night </strong> , minimum borough Provided two night For Renting :<strong style='padding-left:15px;text-decoration:underline;font-size:14px;'> Staten Island </strong> While\
            maximum Borough Provided One Night For Renting : <strong style='padding-left:15px;text-decoration:underline;font-size:14px;'> Brooklyn </strong>.<br/>\
            <strong style='padding-left:15px;text-decoration:underline;font-size:14px;'>- Three night </strong> , minimum borough Provided three night For Renting :<strong style='padding-left:15px;text-decoration:underline;font-size:14px;'> Staten Island </strong> While\
            maximum Borough Provided Three Night For Renting : <strong style='padding-left:15px;text-decoration:underline;font-size:14px;'> Brooklyn </strong>.<br/>\
            <strong style='padding-left:15px;text-decoration:underline;font-size:14px;'>- Four  night </strong>  , minimum borough Provided four night For Renting :<strong style='padding-left:15px;text-decoration:underline;font-size:14px;'> Bronx </strong> While\
            maximum Borough Provided four Night For Renting :<strong style='padding-left:15px;text-decoration:underline;font-size:14px;'> Manhattan </strong>.<br/>\
            - None Outlier Values Is Ranged From One To Eleven Night Where Any Type Of Room Was Been Booked (Most Frequent Type Of Room For Each Non-Abnormal Outliers).<br/>\
            <strong style='padding-left:15px;text-decoration:underline;font-size:14px;'>- One night </strong> , Most Frequent Type Of Room Was Booked For One Night : <strong style='padding-left:15px;text-decoration:underline;font-size:14px;'> Private Room </strong><br/>\
            <strong style='padding-left:15px;text-decoration:underline;font-size:14px;'>- Two night </strong> , Most Frequent Type Of Room Was Booked For One Night : <strong style='padding-left:15px;text-decoration:underline;font-size:14px;'> Entire Home </strong><br/>\
            <strong style='padding-left:15px;text-decoration:underline;font-size:14px;'>- Three night </strong> , Most Frequent Type Of Room Was Booked For One Night : <strong style='padding-left:15px;text-decoration:underline;font-size:14px;'> Entire Home </strong><br/> \
            - There Are <strong style='padding:0px'>98</strong> Unique Numbers Considered As Outliers<br/>\
            - The Lowest  Of  Minimum Nights Was Booked And Considered As Valid Outlier <strong style='padding:0px'>12</strong> Which Repeated \
            <strong style='padding:0px'>91</strong> Time.<br/>\
            - The Highest Of  Minimum Nights Was Booked And Considered As iInvalid Outlier \
            <style='padding:0px;'>1250</strong>  Which Repeated <strong style='padding:0px;'>Only one</strong>\
            Time And It Represent Input Error.<br/>\
            "
        gf.subtitleView(subtitle)
        gf.showInfoCard(title_card="insights set (minimum_nights Feature)",text_card=text_card)
#- Show  Set (News feature)
date_eng_case = st.sidebar.checkbox(label="***Data Engineering***",value=True,key=15)
if date_eng_case:
    feature_names=['guest_intent']
    gf.extractFtrName(feature_names=feature_names)

#-- Data Understanding Of number_of_reviews Feature --#
#- Title Of Understanding Of number_of_reviews Feature
gf.secTitleName(title_name="Data Understanding Of number_of_reviews Feature")
#- Primary Info
subtitle="primary info"
gf.subtitleView(subtitle)
#- Content Of Primary Info About neighbourhood feature
primary_info_set1 = st.columns(5)
lst=[
    ("🔢 Type Of Data",'int64'),
    ("⚠️ Missing",f"{renting_dataset['number_of_reviews'].isna().sum() :,}"),
    ("✦  Uniques Number",f"{renting_dataset['number_of_reviews'].nunique()}"),
    ("💰 max. number of reviews",f"{int(renting_dataset['number_of_reviews'].agg(['min','max'])['min'])}"),
    ("💰 min. number of reviews",f"{int(renting_dataset['number_of_reviews'].agg(['min','max'])['max'])}")
]
for i in range(5):
    with primary_info_set1[i]:
        st.metric(
            f"{lst[i][0]}",
            f"{lst[i][1]}",
    )
st.sidebar.markdown("<font class='sidebar-subtitle'><strong>\
                     ⬤ </strong>number_of_reviews Feature Options</font><br/>",
                     unsafe_allow_html=True) 
#- show outliers 
radio_case = st.sidebar.radio(label="***Outliers***",options=["Valid"],key=16) 
if radio_case=='Valid':
    gf.ftrCardCreater( "Valid Number Of Outliers" , "6021" )
#- Data Analysis
subtitle="Data Analysis"
gf.subtitleView(subtitle)
with st.expander("**visualized Charts**" , expanded=True):
    #- Intializing Set Of Data Structures 
    reviews_outliers_idx = detect_outliers(data=renting_dataset , n=0,features=['number_of_reviews'])
    filter_outliers = renting_dataset.loc[reviews_outliers_idx] 
    filter_non_outliers = renting_dataset[renting_dataset['number_of_reviews']<59]
    reviews_count = renting_dataset['number_of_reviews'].value_counts().sort_values(ascending=False).reset_index()
    reviewscount_maxprice = renting_dataset['price'].groupby(renting_dataset['number_of_reviews']).max().sort_values(ascending=False).reset_index()
    reviewscount_maxprice = reviewscount_maxprice.sort_values(by="number_of_reviews")
    with st.expander("**Visualization If There Is Outliers**"):
        st.plotly_chart(
            px.box(
                data_frame=renting_dataset,
                x='number_of_reviews',
                color_discrete_sequence=['#0055DA']
                
            )
        )
    with st.expander("**Graphs Clearing Relationships**"):
        tab1 , tab2 , tab3 = st.tabs(['Prices Vs Number Of Reviews','Number Of Reviews(outliers) Vs Prices','Number Of Reviews(Non-Outliers) Vs Prices'])
        with tab1:
            st.plotly_chart(
                #- The Spread Of Price With number Of reviews 
                px.scatter(
                    data_frame=renting_dataset,
                    x='number_of_reviews',
                    y='price',
                    labels={"number_of_reviews":"Number Of Reviews" , "price":"Price"},
                    title="Price Vs Reviews Number",
                    color_discrete_sequence=['#1591DC']     
                )
            )
        with tab2:
            st.plotly_chart(
                #- The Points Spread Between Non-Outliers Of (number_of_reviews) Feature And Price Feature 
                px.scatter(
                    data_frame=filter_outliers ,
                    x="number_of_reviews",
                    y="price",
                    title="Number Of Reviews(outliers) Vs Prices",
                    color_discrete_sequence=['#D92243']
                )
            )
        with tab3:
            st.plotly_chart(
                #- The Points Spread Between Non-Outliers Of (number_of_reviews) Feature And Price Feature 
                px.scatter(
                    data_frame=filter_non_outliers ,
                    x="number_of_reviews",
                    y="price",
                    title="Number Of Reviews(non-outliers) Vs Prices",
                    color_discrete_sequence=['#00C68D']
                )
            )
#- Show Instance Of Insights Set(lat and long feature)
insight_case = st.sidebar.checkbox(label="***Display Observations***",value=True,key=17)
if insight_case:
        subtitle = "Insights"
        gf.subtitleView(subtitle)
        text_card="- <strong style='padding:0px'>number_of_reviews</strong> Feature Is A is A Numerical Feature Have <strong style='padding:0px'>364</strong>\
         Unique Postive Integers Such It Represents Number Of Reviews For Each Accomodation Via Airbnb In New York City Ranged From Zero To 629 And There Is Missing Values In That Feature.<br/>\
        -  <strong style='padding:0px'>number_of_reviews</strong> Feature Have  <strong style='padding:0px'>6021</strong>  Outlier Ranged From 59 To 629 Representing 12.31 % Out All Values. And Values \
        Are Not Considered As Non-Outliers Ranged From 0 To 58.<br/> \
        - The Number Of Reviews Which They Are Considered As Outliers , High Precentage  Of Thier Renting Prices Doesn't Extreme <strong style='padding:0px'>1000 dolar</strong><br/>\
        - Approximately , A Large Number Of Accomodations Which They Are More Than 10k Hadn't Any Review (Number Of Reviews Was Zero).<br/> \
        "
        gf.showInfoCard(title_card="insights set (number of reviews Feature)",text_card=text_card)
#- Show  Set (News feature)
date_eng_case = st.sidebar.checkbox(label="***Data Engineering***",value=True,key=18)
if date_eng_case:
    feature_names=['has_review','review_cateogry']
    gf.extractFtrName(feature_names=feature_names)

#-- Data Understanding Of last_Review Feature --#
#- Title Of Understanding Of last_Review Feature
gf.secTitleName(title_name="Data Understanding Of last_Review Feature")
#- Primary Info
subtitle="primary info"
gf.subtitleView(subtitle) 
#- Content Of Primary Info About neighbourhood feature
primary_info_set1 = st.columns(2)
lst=[
    ("🔢 Type Of Data",'Datetime'),
    ("⚠️ Missing",f"{renting_dataset['last_review'].isna().sum() :,}"),
    ("✦  Uniques Number",f"{renting_dataset['last_review'].nunique()}")
]
for i in range(2):
    with primary_info_set1[i]:
        st.metric(
            f"{lst[i][0]}",
            f"{lst[i][1]}",
    )
st.sidebar.markdown("<font class='sidebar-subtitle'><strong>\
                     ⬤ </strong>last_review Feature Options</font><br/>",
                     unsafe_allow_html=True) 
#- Data Cleaning Container 
subtitle="Data Cleaning"
gf.subtitleView(subtitle)
title_card="🧹 What Is Happened In Data Cleaning Phase ?"
text_card="<div class='imformation-cd-subtitle'>Performed Steps</div>\
            - Firstly , Checking If Datetime Format Consisting Of 3 info day/month/year And It Contains Only Three Those Info<br/> \
            - secondly, Filling All Missing Values In last_review With 'no_date' <br/> \
            "
gf.showInfoCard(title_card,text_card) 
#- Data Analysis
subtitle="Data Analysis"
gf.subtitleView(subtitle)
with st.expander("**visualized Charts**" , expanded=True):
    last_date_review = pd.to_datetime(renting_dataset['last_review'])
    years = last_date_review.dt.year
    years_df = years.value_counts().sort_values(ascending=False).reset_index()
    st.plotly_chart(
        px.line(
            data_frame=years_df,
            x='last_review',
            y='count',
            labels={"last_reviews":'Date Of Writing Reviews' , "count":"The Number Of Reviews Per Year"},
            title="Year  Versus count of All reviews For Each Year",
            markers=True,
            color_discrete_sequence=['#0055DA']
        )
    )
#- Show Instance Of Insights Set(lat and long feature)
insight_case = st.sidebar.checkbox(label="***Display Observations***",value=True,key=19)
if insight_case:
        subtitle="Insights"
        text_card="- <style='padding:0px;'>last_reviews Feature</strong> is A Categorical Feature Which It Is Considered As Datetime values <br/> \
        - <style='padding:0px;'>last_reviews</strong> Feature Have <style='padding:0px;'>10052</strong> Missing Values Representing 20.56% Out Of All Values .<br/>\
        - The Date Ranged From 2011 To 2019 Where Highest Number Of Reviews Was In <strong style='padding:0px'>year 2019</strong> And Lowest Was In <strong style='padding:0px'>year 2011</strong>\
        And According To Above Chart , The Number Of Reviews Increase For Each Year From 2011 To 2019.<br/>\
        "  
        gf.subtitleView(subtitle)
        gf.showInfoCard(title_card="insights set (last_reviews Feature)",text_card=text_card)
#- Show  Set (News feature)
date_eng_case = st.sidebar.checkbox(label="***Data Engineering***",value=True,key=20)
if date_eng_case:
    feature_names=['year','month','days_since_last_review']
    gf.extractFtrName(feature_names=feature_names)

#-- Data Understanding Of reviews_per_month Feature --#
#- Title Of Understanding Of reviews_per_month Feature
gf.secTitleName(title_name="Data Understanding Of reviews_per_month Feature")
#- Primary Info
subtitle="primary info"
gf.subtitleView(subtitle) 
#- Content Of Primary Info About neighbourhood feature
primary_info_set1 = st.columns(4)
lst=[
    ("🔢 Type Of Data",f'{str(renting_dataset['reviews_per_month'].dtype)}'),
    ("⚠️ Missing",f"{renting_dataset['reviews_per_month'].isna().sum() :,}"),
    ("💰 min. avgerage Of Reviews Per Month","0.01"),
    ("💰 max. avgerage Of Reviews Per Month","58.50")
]
for i in range(4):
    with primary_info_set1[i]:
        st.metric(
            f"{lst[i][0]}",
            f"{lst[i][1]}",
    )
st.sidebar.markdown("<font class='sidebar-subtitle'><strong>\
                     ⬤ </strong>reviews_per_month Feature Options</font><br/>",
                     unsafe_allow_html=True) 
#- Data Cleaning Container 
subtitle="Data Cleaning"
gf.subtitleView(subtitle)
title_card="🧹 What Is Happened In Data Cleaning Phase ?"
text_card="<div class='imformation-cd-subtitle'>Performed Steps</div>\
            - Firstly ,The Instances Whose Number Of Reviews Assigned To 0 Is Same Instances Whose Average Number Of Reviews Per Month Is Missing Values. <br/> \
            - secondly, Filling All Missing Values In 'number_of_reviews'  With 0.0 <br/> \
            "
gf.showInfoCard(title_card,text_card) 
#- Data Analysis
subtitle="Data Analysis"
gf.subtitleView(subtitle)
with st.expander("**visualized Charts**" , expanded=True):
    #- Intializing Set Of Data Structures 
    top_10_listings = cleaned_renting_data.sort_values('reviews_per_month',ascending=False).head(10)
    with st.expander("Visualizing If There Are Outliers"):
        st.plotly_chart(
            px.box(
                data_frame=renting_dataset,
                x="reviews_per_month",
                color_discrete_sequence=['#0055DA']
            )
        )
    with st.expander("Relationship Between Reviews_per_month And Price"):
        st.plotly_chart(
            px.scatter(
                data_frame=renting_dataset,
                x='reviews_per_month',
                y='price',
                color_discrete_sequence=['#0055DA']
            )
        )
    with st.expander("Top 10 Listings Has Average Number Of Reviews Per Month"):
        st.plotly_chart(
            px.bar(
                data_frame=top_10_listings,
                x='reviews_per_month',
                y='name',
                labels={'name':'Description Of Accomodation'},
                color_discrete_sequence=['#0055DA']
            )
        )
#- Show Instance Of Insights Set(lat and long feature)
insight_case = st.sidebar.checkbox(label="***Display Observations***",value=True,key=21)
if insight_case:
    subtitle="Insights"
    text_card="- <strong style='padding:0px'>reviews_per_month</strong> Feature  is A Numerical Feature whose minimum review rate recieved per month is <strong style='padding:0px'>0.01</strong>\
    nd maximum review rate is <strong style='padding:0px'>58.5</strong>.<br/>\
    -  missing values are existed In <strong style='padding:0px'>number_of_reviews</strong> Feature With over 20 \% \out all values.<br/>\
    - Average number of reviews recieved per month representing review rates , The Most of listing Prices spread highly between the minimum price to 20k and review rates to 20.<br/> \
    - the most description of listing have highest number of reviews <strong style='padding:0px'>Room near JFK Queen Bed</strong> With <strong style='padding:0px'>629</strong>.<br/> \
    "
    gf.subtitleView(subtitle)
    gf.showInfoCard(title_card="insights set (reviews_per_month Feature)",text_card=text_card)
#- Show  Set (News feature)
date_eng_case = st.sidebar.checkbox(label="***Data Engineering***",value=True,key=22)
if date_eng_case:
    feature_names=["avg_reviews_activity"]
    gf.extractFtrName(feature_names=feature_names)

#-- Data Understanding Of calculated_host_listings_count Feature --#
#- Title Of Understanding Of calculated_host_listings_count Feature
gf.secTitleName(title_name="Data Understanding Of  calculated_host_listings_count Feature")
#- Primary Info
subtitle="primary info"
gf.subtitleView(subtitle)
primary_info_set1 = st.columns(4)
lst=[
    ("🔢 Type Of Data",'int64'),
    ("⚠️ Missing",f"{renting_dataset['calculated_host_listings_count'].isna().sum() :,}"),
    ("min. host's listings","1"),
    ("max. host's Listings","327")
]
for i in range(4):
    with primary_info_set1[i]:
        st.metric(
            f"{lst[i][0]}",
            f"{lst[i][1]}",
    )
st.sidebar.markdown("<font class='sidebar-subtitle'><strong>\
                     ⬤ </strong> calculated_host_listings_count Feature Options</font><br/>",
                     unsafe_allow_html=True) 
#- Data Analysis
subtitle="Data Analysis"
gf.subtitleView(subtitle) 
with st.expander("Visualized Charts",expanded=True):
    #- Intializing Set Of Primitive Instructions 
    top_recent = renting_dataset[["host_name",'calculated_host_listings_count']].sort_values("calculated_host_listings_count",ascending=False).reset_index()
    dict_ = {}
    i = 0 ; limit=5;
    for name in top_recent['host_name']:
        if not(name in dict_.keys()):
            dict_[name] = int(top_recent['calculated_host_listings_count'].loc[i])
            if len(dict_.keys()) == limit:break;
        i+=1
    with st.expander("Check If There Are Outliers Here"):
        st.plotly_chart(
            px.box(
                data_frame=renting_dataset,
                x='calculated_host_listings_count',
                color_discrete_sequence=['#0055DA']
            )
        )
    with st.expander("distribution spread Between prices And Count Of Hosts For Each Renting Provided"):
        st.plotly_chart(
            px.scatter(
                data_frame=renting_dataset,
                x='calculated_host_listings_count',
                y='price',
                color_discrete_sequence=['#0055DA']
            )
        )
    with st.expander("Top 5 Hosts Who They Provided Rentals"):
        st.plotly_chart(
            px.bar(
                data_frame=pd.DataFrame({
                    "Host Name" : dict_.keys(),
                    "Number of Listings" : dict_.values() 
                }),
                x="Host Name",
                y="Number of Listings",
                color_discrete_sequence=['#0055DA']
            )
        )
#- Show Instance Of Insights Set(lat and long feature)
insight_case = st.sidebar.checkbox(label="***Display Observations***",value=True,key=23)
if insight_case:
        subtitle="Insights"
        text_card="- <style='padding:0px;'>calculated_host_listings_count Feature</strong> is A Numerical Feature Whose minimum Number Of listings Which Renting Provider Offered is <br/> \
        - <style='padding:0px;'>1</strong> and maximum number of listings <style='padding:0px;'>327</strong>.<br/>\
        - There Is No Missing Values And Valid Outliers Are Existed.<br/>\
        - Most Number of listings which Each Renting Provider Was Uploaded On Airbnb Is Spread Between <strong style='padding:0px'>1 to 50 And Priced To 2k</strong><br/>\
        -The Name Of Host Which He Inserted Highest Number Of Renting Accomodations Is <strong style='padding:0px'>Sonder (NYC)</strong>\
        With <strong style='padding:0px'>327</strong> Listings And <strong style='padding:0px'>Sonder (NYC)</strong> \
        Is One Of most popular Companies Providing short-term Rentals In New York City In US And From More:<br/> <a href='https://en.wikipedia.org/wiki/Sonder_(company)'>Read More (Sonder[NYC])</a>\
        "  
        gf.subtitleView(subtitle)
        gf.showInfoCard(title_card="insights set (last_reviews Feature)",text_card=text_card)
#- Show  Set (News feature)
date_eng_case = st.sidebar.checkbox(label="***Data Engineering***",value=True,key=24)
if date_eng_case:
    feature_names=['accomodation_count_case']
    gf.extractFtrName(feature_names=feature_names)

#-- Data Understanding Of availability_365 Feature --#
#- Title Of Understanding Of availability_365 Feature
gf.secTitleName(title_name="Data Understanding Of  availability_365 Feature")
#- Primary Info
subtitle="primary info"
gf.subtitleView(subtitle)
primary_info_set1 = st.columns(4)
lst=[
    ("🔢 Type Of Data",'int64'),
    ("⚠️ Missing",f"{renting_dataset['availability_365'].isna().sum() :,}"),
    ("min. avialable period","0.0"),
    ("max. avialable perion","365")
]
for i in range(4):
    with primary_info_set1[i]:
        st.metric(
            f"{lst[i][0]}",
            f"{lst[i][1]}",
    )
st.sidebar.markdown("<font class='sidebar-subtitle'><strong>\
                     ⬤ </strong> availability_365 Feature Options</font><br/>",
                     unsafe_allow_html=True) 
#- Data Analysis
subtitle="Data Analysis"
gf.subtitleView(subtitle) 
with st.expander("Visualized Charts",expanded=True):
    #- Intializing Set Of Primitive Instructions 
    with st.expander("Check If There Are Outliers"):
        st.plotly_chart(
            px.box(
                data_frame=renting_dataset,
                x='availability_365',
                color_discrete_sequence=['#0055DA']
            )
        )
    with st.expander("Distribution Of Data Values Over Prices"):
        st.plotly_chart(
            px.scatter(
                data_frame=renting_dataset,
                x='availability_365',
                y='price',
                color_discrete_sequence=['#0055DA']
            )
        )
    with st.expander("Frequency Of Renting Availability"):
        st.plotly_chart(
            px.histogram(
                data_frame=renting_dataset,
                x='availability_365',
                color_discrete_sequence=['#0055DA']
            )
        )
#- Show Instance Of Insights Set(lat and long feature)
insight_case = st.sidebar.checkbox(label="***Display Observations***",value=True,key=25)
if insight_case:
        subtitle="Insights"
        text_card="- <style='padding:0px;'>availability_365 Feature</strong> s A Numerical Feature Whose minimum value is <strong style='padding:0px'>0</strong> Representing <strong style='padding:0px'>Unavailable Renting</strong> \
        While maximum value is <strong style='padding:0px'>365</strong> Representing Fully Year Renting Availability.<br/>\
        - There Is No Missing Values And There Is No Outliers.<br/>\
        - Most Frequent period Is Between Zero And Four with <strong style='paddding:0px'>18.75K</strong> Rentals.<br/>\
        -The Name Of Host Providing Highest Number Of Rentals Along Year Is <strong style='padding:0px'> Ken</strong> and <strong style='padding:0px'>Sonder (NYC)</strong> With <strong style='padding:0px'>4</strong> Times<br/>\
        "  
        gf.subtitleView(subtitle)
        gf.showInfoCard(title_card="insights set (last_reviews Feature)",text_card=text_card)
#- Show Set (News feature)
date_eng_case = st.sidebar.checkbox(label="***Data Engineering***",value=True,key=26)
if date_eng_case:
    feature_names=["availability_case"]
    gf.extractFtrName(feature_names=feature_names)

#-- EDA Of Extracted Features (New Features) --# 
#- Title Of Understanding Of Extracted Features
gf.secTitleName(title_name="EDA Of Engineered Features")
st.sidebar.markdown(f"""
        <style>
        .animated-line {{
            width: 100%;
            height: 4px;
            margin: 10px auto 25px auto;

            background: linear-gradient(
                90deg,
                #00E5FF,
                #00B8FF,
                #2979FF,
                #651FFF,
                #00E5FF
            );

            background-size: 300% 100%;
            border-radius: 10px;

            animation: lineMove 4s linear infinite;
        }}

        @keyframes lineMove {{
            0% {{
                background-position: 0% 50%;
            }}

            100% {{
                background-position: 300% 50%;
            }}
        }}
        </style>

        <div class="animated-line"></div>
        """
    , unsafe_allow_html=True)
extract_ftrs  = st.sidebar.multiselect(
  "Choose EDA Of Extracted Features",
  options     = ['desc_len','desc_lang', 'has_prop_keyword', 'has_room_keyword', 
             'has_rental_keyword', 'has_amenity_keyword', 'has_loc_keyword',
             'has_market_keyword', 'distance_km', 'guest_intent',
             'review_category' ,'accomodation_count_case', 'availability_case'],
  default     = ['desc_len','desc_lang']
) 
#-Programming Logic Section-# 
if 'desc_len' in extract_ftrs:
    with st.expander("The Relationship Between Description Length And Renting Prices",expanded=True):
        st.plotly_chart(
            #- relationship between description length and price 
            px.scatter(
                data_frame=cleaned_renting_data,
                x='desc_len',
                y='price',
                color_discrete_sequence=['#0055DA'],
            )
        )
if 'desc_lang' in extract_ftrs:
    top_freq_langs = cleaned_renting_data['desc_lang'].value_counts().head(10).reset_index()
    with st.expander("Top Ten Languages Which Listing Descriptions Was Written By",expanded=True):
        fig , ax = plt.subplots(figsize=(3,3))
        sns.barplot(
                data=top_freq_langs,
                x='desc_lang',
                y='count',
                color="#458393",
                ax=ax
            )
        ax.set_xlabel("language which The Listing description Is Written In") 
        ax.set_ylabel("frequency")
        ax.set_title("description language Vs Frequency") 
        st.pyplot(fig)
cond_1 = 'has_prop_keyword'    in extract_ftrs
cond_2 = 'has_room_keyword'    in extract_ftrs 
cond_3 = 'has_rental_keyword'  in extract_ftrs
cond_4 = 'has_amenity_keyword' in extract_ftrs
cond_5 = 'has_loc_keyword'     in extract_ftrs
cond_6 = 'has_market_keyword'  in extract_ftrs
if cond_1 | cond_2 | cond_3 | cond_4 | cond_5 | cond_6:
    with st.expander("Counting Of listings having Special keywords in description(name)"):
        keyword_cols = [
            'has_prop_keyword',
            'has_room_keyword',
            'has_rental_keyword',
            'has_amenity_keyword',
            'has_loc_keyword',
            'has_market_keyword'
        ]
        keyword_percentage = (
            cleaned_renting_data[keyword_cols].mean() * 100
        ).sort_values(ascending=False)
        fig , ax = plt.subplots(figsize=(3,3))
        sns.barplot(
            x=keyword_percentage.values,
            y=keyword_percentage.index,
            ax=ax 
        )
        ax.set_title('Frequency of Description Keywords')
        ax.set_xlabel('Percentage of Listings (%)')
        ax.set_ylabel('Keyword Feature')
        st.pyplot(fig)

if 'distance_km' in extract_ftrs:
    with st.expander("The Relationship Between Distances From Center City And Prices",expanded=True):
        fig , ax = plt.subplots(figsize=(3,3))
        sns.scatterplot(
        data=cleaned_renting_data,
        x='distance_km',
        y='price',
        color="#458393",
        alpha=0.3,
        label=f"corr rate : {cleaned_renting_data[['distance_km','price']].corr()['price']['distance_km']:.3}",
        ax=ax
        )
        ax.set_title("The Relationship Between Distance(KM) And Price($)") 
        ax.set_xlabel("Distance (km)")
        ax.set_ylabel("Price ($)")
        st.pyplot(fig) 
if 'guest_intent' in extract_ftrs:
    with st.expander("counting Of Guest Intents",expanded=True):
        fig , ax = plt.subplots(figsize=(3,3))
        sns.countplot(
            data=cleaned_renting_data,
            y='guest_intent',
            order=cleaned_renting_data['guest_intent'].value_counts(ascending=False).index,
            color="#458393",
            ax=ax
        )
        ax.set_title("Guest Intent For Renting Vs Frequency")
        st.pyplot(fig)
if 'review_category' in extract_ftrs:
    with st.expander("Counting For cases Of Number Of Reviews",expanded=True):
        fig , ax = plt.subplots(figsize=(3,3))
        sns.countplot(
            data=cleaned_renting_data,
            x='review_category',
            order=cleaned_renting_data['review_category'].value_counts().index,
            color="#458393",
            ax=ax
        )
        ax.set_xlabel("Case Of Reviews Number")
        ax.set_ylabel("Number Of Reviews")
        ax.tick_params(axis='x',rotation=95)
        st.pyplot(fig) 
if 'accomodation_count_case' in extract_ftrs:
    with st.expander("case Of accomodation counts Which Each Host Provided",expanded=True):
        fig , ax = plt.subplots(figsize=(3,3))
        sns.countplot(
            data=cleaned_renting_data,
            x='accomodation_count_case',
            order=cleaned_renting_data['accomodation_count_case'].value_counts().index,
            color="#458393",
            label="highest frequent case :providing single listing {32301} ",
            ax=ax
        )
        ax.set_xlabel("provided listings count case") 
        ax.set_ylabel("Number Of Listings") 
        ax.set_title("listings count case Vs count")
        st.pyplot(fig)
if 'availability_case' in extract_ftrs:
    with st.expander("counting Of availability Cases",expanded=True):
        fig , ax = plt.subplots(figsize=(3,3))
        sns.countplot(
            data=cleaned_renting_data,
            x='availability_case',
            order=cleaned_renting_data['availability_case'].value_counts().index,
            color="#458393",
            label="highest frequent case :un-avialable {17530} ",
            ax=ax
        )
        ax.set_xlabel("Renting period") 
        ax.set_ylabel("Number Of Listings") 
        ax.set_title("Renting Period Vs listings count")
        ax.tick_params(axis='x', rotation=95) 
        ax.legend()
        st.pyplot(fig)

#-- Multivariate Analysis Of Numerical Features --#
with st.container(border=True):
    numeric_df = cleaned_renting_data.select_dtypes(['number'])
    fig , ax = plt.subplots(figsize=(12,4))
    corr_matrix = numeric_df.corr() 
    sns.heatmap(
    data=corr_matrix,
    annot=True,
    fmt='0.3f',
    cmap="coolwarm",
    ax=ax
    )
    ax.set_title("Numerical Feature Relationships Level (Multivariate Analysis)")
    st.pyplot(fig)

#- Show Instance Of Insights Set(from all extracted features)
insight_case = st.sidebar.checkbox(label="***Display Observations Of Extracted Features***",value=True,key=27)
if insight_case:
        subtitle="Insights"
        text_card = "- The Density Of Description Lengths Is Highly Ranged From <strong style='padding:0px'>3 to 10 words</strong> For Almost All Listings, Even Rentals With High Prices, is ranged between 3 to 10 words. \
        <br/>- All Single Hosts Provided Prices Ranged From <strong style='padding:0px'>25 to 2500</strong> And All Description Lengths Consist Of Only One Word. \
        <br/>- High Priced Rentals Were Provided From <strong style='padding:0px'>Multiple Hosts</strong>. \
        <br/>- The Median Distance (km) From City Center Is <strong style='padding:0px'>6.391 km</strong>. \
        <br/>- There Is A Weak Negative Relationship Between Distance And Price With <strong style='padding:0px'>-0.173</strong>. Therefore, We Can't Say That The Distance_km Feature Alone Determines The Price. Price Tends To Slowly Decrease As The Distance From The City Center Increases. \
        <br/>- A Huge Number Of Listings (Accommodations) Is Categorized As Few In The Review Category, At A Percentage Of <strong style='padding:0px'>55.67%</strong>. This Could Represent One Of The Following Possibilities: (Newer Listings, Inactive Listings, Listings With Low Booking Activity, Or Listings That Simply Received A Small Number Of Reviews). \
        <br/>- A High Portion Of Listings Have Zero Availability At <strong style='padding:0px'>35.9%</strong> Across All Years From 2011 To 2019, While Other Samples Are Available Throughout All Years Embedded In The Dataset. \
        <br/>- A Huge Portion Of Hosts Provided Or Visited The Renting Platform Only One Time, Which Is Labeled As <strong style='padding:0px'>Single</strong> In The accomodation_count_case Feature. \
        <br/>- Approximate Frequency Of Special Keywords In The Description (Name) Feature: \
        <table style='width:100%; border-collapse:collapse; margin:10px 0; font-size:15px; text-align:left;'> \
        <tr><th style='padding:8px; border-bottom:1px solid #ddd;'>Keyword Feature</th><th style='padding:8px; border-bottom:1px solid #ddd;'>Frequency</th></tr> \
        <tr><td style='padding:8px;'>has_prop_keyword</td><td style='padding:8px;'><strong>74.5%</strong></td></tr> \
        <tr><td style='padding:8px;'>has_market_keyword</td><td style='padding:8px;'><strong>62.6%</strong></td></tr> \
        <tr><td style='padding:8px;'>has_room_keyword</td><td style='padding:8px;'><strong>60.0%</strong></td></tr> \
        <tr><td style='padding:8px;'>has_loc_keyword</td><td style='padding:8px;'><strong>40.3%</strong></td></tr> \
        <tr><td style='padding:8px;'>has_amenity_keyword</td><td style='padding:8px;'><strong>22.4%</strong></td></tr> \
        <tr><td style='padding:8px;'>has_rental_keyword</td><td style='padding:8px;'><strong>2.5%</strong></td></tr> \
        </table> \
        <br/>- Property, market, and room-related terminology appears frequently in listing descriptions, while rental terminology is relatively uncommon. According to this, these features may provide useful information for ML modelling. \
        <br/>- The Dominant Language Is <strong style='padding:0px'>English</strong> With <strong style='padding:0px'>40,828 Listings</strong>. \
        <br/>- English Dominates Listing Descriptions, Although The Dataset Contains Listings Detected In Multiple Other Languages. \
        <br/>- The Dominant Intent Of Guests Is Renting For <strong style='padding:0px'>Weekend</strong> With <strong style='padding:0px'>19,691 Occurrences</strong>. \
        <br/>- Shorter-term/stay-pattern categories Dominate The Dataset, While Monthly-oriented Listings Form A Smaller Group. \
        <br/>- All Numerical Features Have Some Degree Of Correlation With Price.\
        "
        gf.subtitleView(subtitle)
        gf.showInfoCard(title_card="insights set of all extracted features",text_card=text_card)
####-- End Of What EDA Page Contains---####

# -------------------------------------------------------
# Last snippet (Utilities)--> (Dependencies) (footer Sec)
# -------------------------------------------------------
gf.footerCreater()