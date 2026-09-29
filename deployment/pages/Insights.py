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
#-- Setting Background Color If Not Existed --#
if "background_color" not in st.session_state:
    st.session_state.background_color= "" 
#-- Setting Background Color Of Page --#
if st.session_state.background_color:
    gf.changeBackgroundColor(st.session_state.background_color)

#- Title Of Page --#
page_title  = "Insights" 
color_title = "#00E5FF"
bg_color=st.session_state.background_color
gf.createTopTitleHeader(page_title, color_title,bg_color) 

#-- content of page--#
insights = "- the number of instances In Renting Dataset Is <strong style='padding:0px;'>48895</strong>\
    While The Number Of Features After Droping Non-Necessary Features Is <strong style='padding:0px;'>14</strong><br/>\
    - There Is No Duplicated 'Repeated' Instances In That Data<br/>\
    - Features Has Missing Values Are <strong style='padding:0px;'>name , host_name , last_review  And reviews_per_month</strong>\
    (<strong style='padding:0px;'> 4 features has  And  10 hasn't</strong> )<br/>\
    - There Is <strong style='padding:0px;'>8 Numeric Feature</strong>  And <strong style='padding:0px;'>6 Categorical Feature</strong> \
    - <strong style='padding:0px'>Price</strong> Feature Is <strong style='padding:0px'>Positive Integer Numbers</strong>  Such That Minimum Value Is \
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
    - <strong style='padding:0px;'>name</strong> Feature is A Categorical Feature\
      Have <strong style='padding:0px;'>47905</strong> Variant Descriptions Of\
      Listing On Airbnb Website In New Work City Had Been Done.<br/>\
    - The Most Repeated Characteristics Of Renting Which They Had Been \
    Listed In That Dataset Is  <strong style='padding:0px;'>Hillside Hotel</strong> <br/>\
    -  The Description Of Booking Which It Owned Highest cost Is  \
    <strong style='padding:0px;'>1-BR Lincoln Center , Furnished room in \
    Astoria And Luxury 1 bedroom app.-stunning mangattan views  </strong>\
    - <strong style='padding:0px;'>host_name</strong> Feature is A Categorical Feature\
      Have <strong style='padding:0px;'>11452</strong> Variant Hosts For Renting Accomodation \
      On Airbnb Website In New Work City Had Been Shown.<br/>\
    -   The Most Repeated host On Airbnb In New York City Is <strong style='padding:0px;'>Michael</strong>With\
    <strong style='padding:0px;'>41</strong> Listing<br/>\
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
    - <strong style='padding:0px;'>neighbourhood_night</strong> Feature is A Categorical Feature\
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
    All Boroughs Is  <strong style='padding:0px'>Entire Home/Appartment</strong><br/>\
    - <strong style='padding:0px;'>neighbourhood</strong> Feature is A Categorical Feature\
     Have <strong style='padding:0px'>221 Different Places</strong><br/>\
    - There Is No Missing Values Here In <strong style='padding:0px'>neighbourhood</strong> Feature\
     , Airbnb Activity Is Heavly Concerned In Those Two Previous Boroughs<br/>\
    - The Highest Place In Which Renting Numbers was hugest <strong style='padding:0px'>Williamsburg</strong> \
     Located In <strong style='padding:0px'>Brooklyn Borough</strong> With Average Price <strong style='padding:0px'>143.8</strong><br/>\
    - Highest Five Renting Locations Are  <strong style='padding:0px'>Williamsburg :4500 , Upper West Side/Manhattan:5000 , Bushwick:5000, Harlem:2000 and Bedford-Stuyvesant:10000</strong>\
     And Here The Number Represents Frequency Times.<br/>\
    - The Highest Renting Price Was Paid In Those Places : Location -->  Borough<br/>\
    - Also According To Visualization Chart , The Highest Renting Location Was In <strong style='padding:0px'>Manhattan</strong><br/>\
    - <strong style='padding:0px'>Latitude and Longitude</strong> is Numerical Features Have\
    No Missing Value<br>\
    - The Samples Of This Renting Data Set Is Spread Arroud All Five Boroughs In New York City\
    - <strong style='padding:0px'>room_type</strong>  A Categorical Feature Doesn't Contain\
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
     -<strong style='padding:0px;'>minimum_nights</strong> Feature \
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
    - <strong style='padding:0px'>number_of_reviews</strong> Feature Is A is A Numerical Feature Have <strong style='padding:0px'>364</strong>\
     Unique Postive Integers Such It Represents Number Of Reviews For Each Accomodation Via Airbnb In New York City Ranged From Zero To 629 And There Is Missing Values In That Feature.<br/>\
    -  <strong style='padding:0px'>number_of_reviews</strong> Feature Have  <strong style='padding:0px'>6021</strong>  Outlier Ranged From 59 To 629 Representing 12.31 % Out All Values. And Values \
    Are Not Considered As Non-Outliers Ranged From 0 To 58.<br/> \
    - The Number Of Reviews Which They Are Considered As Outliers , High Precentage  Of Thier Renting Prices Doesn't Extreme <strong style='padding:0px'>1000 dolar</strong><br/>\
    - Approximately , A Large Number Of Accomodations Which They Are More Than 10k Hadn't Any Review (Number Of Reviews Was Zero).<br/> \
    - <style='padding:0px;'>last_reviews Feature</strong> is A Categorical Feature Which It Is Considered As Datetime values <br/> \
    - <style='padding:0px;'>last_reviews</strong> Feature Have <style='padding:0px;'>10052</strong> Missing Values Representing 20.56% Out Of All Values .<br/>\
    - The Date Ranged From 2011 To 2019 Where Highest Number Of Reviews Was In <strong style='padding:0px'>year 2019</strong> And Lowest Was In <strong style='padding:0px'>year 2011</strong>\
    And According To Above Chart , The Number Of Reviews Increase For Each Year From 2011 To 2019.<br/>\
    - <strong style='padding:0px'>reviews_per_month</strong> Feature  is A Numerical Feature whose minimum review rate recieved per month is <strong style='padding:0px'>0.01</strong>\
    nd maximum review rate is <strong style='padding:0px'>58.5</strong>.<br/>\
    -  missing values are existed In <strong style='padding:0px'>number_of_reviews</strong> Feature With over 20 \% \out all values.<br/>\
    - Average number of reviews recieved per month representing review rates , The Most of listing Prices spread highly between the minimum price to 20k and review rates to 20.<br/> \
    - the most description of listing have highest number of reviews <strong style='padding:0px'>Room near JFK Queen Bed</strong> With <strong style='padding:0px'>629</strong>.<br/> \
    - <style='padding:0px;'>calculated_host_listings_count Feature</strong> is A Numerical Feature Whose minimum Number Of listings Which Renting Provider Offered is <br/> \
    - <style='padding:0px;'>1</strong> and maximum number of listings <style='padding:0px;'>327</strong>.<br/>\
    - There Is No Missing Values And Valid Outliers Are Existed.<br/>\
    - Most Number of listings which Each Renting Provider Was Uploaded On Airbnb Is Spread Between <strong style='padding:0px'>1 to 50 And Priced To 2k</strong><br/>\
    -The Name Of Host Which He Inserted Highest Number Of Renting Accomodations Is <strong style='padding:0px'>Sonder (NYC)</strong>\
    With <strong style='padding:0px'>327</strong> Listings And <strong style='padding:0px'>Sonder (NYC)</strong> \
    Is One Of most popular Companies Providing short-term Rentals In New York City In US And From More:<br/> <a href='https://en.wikipedia.org/wiki/Sonder_(company)'>Read More (Sonder[NYC])</a>\
    - <style='padding:0px;'>availability_365 Feature</strong> s A Numerical Feature Whose minimum value is <strong style='padding:0px'>0</strong> Representing <strong style='padding:0px'>Unavailable Renting</strong> \
    While maximum value is <strong style='padding:0px'>365</strong> Representing Fully Year Renting Availability.<br/>\
    - There Is No Missing Values And There Is No Outliers.<br/>\
    - Most Frequent period Is Between Zero And Four with <strong style='paddding:0px'>18.75K</strong> Rentals.<br/>\
    -The Name Of Host Providing Highest Number Of Rentals Along Year Is <strong style='padding:0px'> Ken</strong> and <strong style='padding:0px'>Sonder (NYC)</strong> With <strong style='padding:0px'>4</strong> Times<br/>\
    - The Density Of Description Lengths Is Highly Ranged From <strong style='padding:0px'>3 to 10 words</strong> For Almost All Listings, Even Rentals With High Prices, is ranged between 3 to 10 words. \
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
gf.insightsShow('Whole EDA Insights' , insights)

#- button for downloading powerpoint file 
radio_case = st.sidebar.radio("***Type Of File You Wanna Download***",['powerpoint presentation','PDF presentation'])
if radio_case=='powerpoint presentation':
    current_path = os.getcwd() 
    file_path = os.path.join(current_path,"docs","EDA_Airbnb(NYC).pptx")
    gf.download_file_button(
        file_path=file_path,
        button_text="Download PowerPoint Presentation",
        icon="📊",
        file_name="EDA_Presentation.pptx",
        mime_type="application/vnd.openxmlformats-officedocument.presentationml.presentation"
    )
elif radio_case=='PDF presentation':
    current_path = os.getcwd() 
    file_path = os.path.join(current_path,"docs","EDA_Airbnb(NYC).pdf")
    gf.download_file_button(
        file_path=file_path,
        button_text="Download PDF Presentation",
        icon="📊",
        file_name="EDA_Presentation.pdf",
        mime_type="application/pdf"
    )
#-- End Of Page Content --#
# -------------------------------------------------------
# Last snippet (Utilities)--> (Dependencies) (footer Sec)
# -------------------------------------------------------
gf.footerCreater()