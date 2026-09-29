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
#-- Setting Background Color If Not Existed --#
if "background_color" not in st.session_state:
    st.session_state.background_color= "" 

#-- Setting Background Color Of Page --#
if st.session_state.background_color:
    gf.changeBackgroundColor(st.session_state.background_color)

#- Title Of Page --#
page_title  = "Home" 
color_title = "#00E5FF"
bg_color=st.session_state.background_color
gf.createTopTitleHeader(page_title, color_title,bg_color)
####----End Of Fixed Snippets ----####


######################################
######################################
###################################### 
####----Start Of What Home Page Contains---####
#-Global vars-# 
head_color="#972525"
head_style="italic"
head_famliy="serif" #- Times New Roman, Georgia 
sub_head_color="#270B0B"
#- What Home Page Consists Of  (Info About Page Content)
with st.container():
    text="1. Intro<br/>\
          2. Info About Analysis Life Cycle<br>\
          3. Info About Machine Learning"
    gf.showInfoCard(title_card="Home Content Table",text_card=text)

#-Intro Section-# 
with st.container():
    #- Title Of Info section
    gf.secTitleName(title_name="Intro (ℹ)")
    #- Content Of Info Section
    text="This website is built around the Airbnb NYC dataset and guides \
             the user through a complete data-to-insight workflow. First, it \
             performs an end to end analysis of the dataset, cleaning and \
             transforming the raw listings data, then displaying interactive\
              visualization charts that reveal patterns in prices, neighborhoods, \
             room types, availability  over time. Second, it provides an\
            <strong>Overview</strong> section that summarizes key information\
            about the data—such as the number of listings, distribution of prices,\
            most popular areas, and main features used in the analysis—so users can\
            quickly understand the context before diving into the details. Finally,\
            the site trains and integrates a machine learning model that learns from\
            historical listing attributes (like location, room type,\
            number of reviews, minimum nights, etc.) to predict the expected\
            rental price for a new Airbnb listing, allowing users to input property\
            details and see an estimated price along\
            with basic explanations of which factors most influence the prediction." 
    gf.showInfoCard(title_card="The Purpose Of Initializing The Webiste",text_card=text)

#-Analysis Info Section-# 
with st.container():
    #- Title Of Info section
    gf.secTitleName(title_name="Info About Analysis File Cycle")
    #- data science image banner
    ds_banner_path = os.path.join(os.getcwd(),"deployment","imgs","home_imgs","datascience_banner.jpg")   
    img_base64 = gf.imgAsBase64(ds_banner_path)
    # Banner Image
    st.markdown( 
    f"""
    <div style="
        width: 100%;
        height: 200px;
        background-image: url('data:image/png;base64,{img_base64}');
        background-size: contain;
        background-position: center;
        background-repeat: repeat;
        border-radius: 8px;
    "></div>
    """,
    unsafe_allow_html=True
    )
    #- Data science Phase 
    title_card="📈 📊🧠 What's Data Science ?!"
    text="- Data science is the practice of extracting insights from data using statistics,\
        programming, and domain knowledge to inform decisions and build predictive models.<br/>\
        - Data science combines statistics, programming, and domain expertise to collect,\
        clean, analyze, and model data, turning raw information into actionable insights\
        and predictions that support decision-making.<br/>\
        - A typical lifecycle Of Data Science is:<br/>\
        <strong>1. Data Gathering</strong><br/>\
        <strong>2. Data Preparation</strong><br/>\
        <strong>3. Data Wrangling</strong><br/>\
        <strong>4. Analysis</strong><br/>\
        <strong>5. Model Training</strong><br/>\
        <strong>6. Testing</strong><br/>\
        <strong>7. Deployment</strong>" 
    gf.showInfoCard(title_card=title_card,text_card=text)
    #- Analysis Phases 
        #- Two Main Important Concepts (Data And Business Understanding)
    title_card=f"📈 📊 What's Analysis?!"
    text="- the Analysis Phase is the stage where you examine prepared data\
          to discover patterns, relationships, trends, anomalies,\
        and insights that can answer the business or project questions.<br/>\
        - The main goal Of Analysis Stage is to answer : \
        “<strong>What does the data tell us?</strong>”<br/>\
        <div class='imformation-cd-subtitle'>Two Main Concepts Are Necessary To Be Known</div>\
        <div style='padding-left:30px'>\
        <strong >- Business Understanding</strong>\
        <p style='padding-left:40px'>Clear What The Problem And The Context Of Workflow Is Followed And understanding the real-world problem that\
          the business or organization wants to solve before working with the data. </p>\
        <strong>-Data Understanding</strong>\
        <p style='padding-left:40px'>Assessing Available Variables And Identify Patterns About Dataset And Its Quality To Model AI Algorithm For Production</p>\
    </div>" 
    gf.showInfoCard(title_card=title_card,text_card=text)
    gf.secTitleName(title_name="Common Steps Of Executing EDA")
    #- 1st Procedure (Importing Utilities Will Be Used For Processing Data)
    with st.expander("***1st Procedure*** : ( Importing Utilities Will Be Used For Processing Data )"):
        st.markdown(
            """
            - **Utilities** are Python Packages (**Python Libraries**) And Also Called **Dependencies**
            
                - Analyzing Datasets For Modelling It Later Using Machine Learning Algorithms It Requires 
                    To Import Set Of **Python Libraries** For Completing The Life Cycle Of Developing Machine Learning System.
                    - ***Pandas And Numpy*** : Numeric Manipulation And Calculations 
                    - ***Matplotlib , seaborn And Plotly*** : Data Visualization"
            """
                 )
        lib_py_path = os.path.join(os.getcwd(),
                        "deployment","imgs","home_imgs","analysis_imgs",
                        "importing_py_libraries.png"
                        )
        byte_file_lib_py = gf.imgAsBase64(lib_py_path)
        st.markdown(
            f"""
            **Python Code Snippet**
            <img src='data:image/png;base64,{byte_file_lib_py}'  style="display:block;margin:auto;width:600px">
            """
            ,unsafe_allow_html=True)
    #- 2nd Procedure*** : ( Reading Data To Be Analyzed )
    with st.expander("***2nd Procedure*** : ( Reading Data To Be Analyzed )"):
        st.markdown(
                """
                - **Reading Data** And **Gain Some Of Generic Information**
                    - The **Pandas** Library Has A Wide Range Of Probabilities For Loading Data Onto
                    Pandas Data Frame 
                    - Common File Types Holding Dataset Can Be Loaded Using Pandas Library Commands 
                        - CSV  File 
                        - Json File 
                        - SQL  File 
                        - XLSX File
                    - Most Of Data Available In Tabular Format Of CSV Files   
                        - CSV File Is Treny And Easy To Access 
                """
                         )
        for i in range(8):

            reading_data_path = os.path.join(os.getcwd(),
                                "deployment","imgs","home_imgs","analysis_imgs",
                                f"ReadingData{i}.png"
                                )
            img_py = gf.imgAsBase64(reading_data_path )
            st.markdown(
                f"""
                **action- {i+1}**
                <img src='data:image/png;base64,{img_py}' style="display:block;margin:auto;width:600px">
                """
                ,unsafe_allow_html=True)
     #- 3rd Procedure*** : ( Reading Data To Be Analyzed )
    with st.expander("***3rd Procedure*** : ( Reducing The Number Of Features )"):
        st.markdown(
                """
                - Some Variables / Columns Con Be Dropped If They Don't Add Value While Performing
                Analysis Life Cycle 
                -Removing Features / Attributes Can't Add Predictive Power In Building Powerful Machine Learning System
                """
             )
        data_reduction_path = os.path.join(os.getcwd(),
                                        "deployment","imgs","home_imgs","analysis_imgs",
                                        "Data_Reduction.png"
                                        )
        img_py = gf.imgAsBase64(data_reduction_path)
        st.markdown(
                f"""
                ****Python Code Snippet****
                <img src='data:image/png;base64,{img_py}' style="display:block;margin:auto;width:600px">
                """
            ,unsafe_allow_html=True)
    #- 4th Procedure*** : (  Feature Engineering )
    with st.expander("***4th Procedure*** : ( Engineering Features)"):
        st.markdown(
                """
                - The Main Goal Is To Create Meaningful Data From Raw Data
                - The Process Of Using Domain Knowledge To Select And Transform \
                    Most Relavant Features From Raw Data While Modelling ML Algorithm Or Using Statistical Modelling  
                    -  It Is Represented In Building New Features From Multi-Informatic Column
                        - Mult-informatic Columns Carries More Than One Info 

                """
             )
        ftr_engineering_path = os.path.join(os.getcwd(),
                                        "deployment","imgs","home_imgs","analysis_imgs",
                                        "feature_engineering1.png"
                                        )
        ftr_engineering_path1 = os.path.join(os.getcwd(),
                                        "deployment","imgs","home_imgs","analysis_imgs",
                                        "feature_engineering1.png"
                                        )
        ftr_engineering_path2 = os.path.join(os.getcwd(),
                                            "deployment","imgs","home_imgs","analysis_imgs",
                                            "feature_engineering2.png"
                                            )
        
        ftr_img_py = gf.imgAsBase64(ftr_engineering_path)
        ftr_img1_py = gf.imgAsBase64(ftr_engineering_path1)
        ftr_img2_py = gf.imgAsBase64(ftr_engineering_path2)
        st.markdown(
                f"""
                ****Python Code Snippet-1****
                <img src='data:image/png;base64,{ftr_img_py}' style="display:block;margin:auto;width:600px">
                """
            ,unsafe_allow_html=True)
        st.markdown(
                f"""
                ****Python Code Snippet-2****
                <img src='data:image/png;base64,{ftr_img1_py}' style="display:block;margin:auto;width:600px">
                """
            ,unsafe_allow_html=True)
        st.markdown(
                f"""
                ****Python Code Snippet-3****
                <img src='data:image/png;base64,{ftr_img2_py}' style="display:block;margin:auto;width:600px">
                """
            ,unsafe_allow_html=True) 

    #- 5th Procedure*** : (  Data Cleaning/Wrangling )
    with st.expander("***5th Procedure*** : ( Data Cleaning/Wrangling )"):
        st.markdown(
                """
                - Those Problems Must Be Resolved To Clean Data And Producing Cleaned Dataset To \
                Determine High Accuracy While Modelling And Allow To Deploy This Model In user Environment
                    1. Some Names Of Variables Not Relavant And Not Easy To Understand
                    2. Some Data May Have Data Entry Errors 
                    3. Some Variables May Need Data Type Conversion 
                """
             )
        ftr_wrangling_path = os.path.join(os.getcwd(),
                                        "deployment","imgs","home_imgs","analysis_imgs",
                                        "DataWrangling-1.png"
                                        )
        ftr_wrangling_path1 = os.path.join(os.getcwd(),
                                        "deployment","imgs","home_imgs","analysis_imgs",
                                        "DataWrangling-2.png"
                                        )
        
        clean_img_py = gf.imgAsBase64(ftr_wrangling_path)
        clean_img1_py = gf.imgAsBase64(ftr_wrangling_path1)
        
        st.markdown(
                f"""
                ****Python Code Snippet-1****
                <img src='data:image/png;base64,{clean_img_py}' style="display:block;margin:auto;width:600px">
                """
            ,unsafe_allow_html=True)
        st.markdown(
                f"""
                ****Python Code Snippet-2****
                <img src='data:image/png;base64,{clean_img1_py}' style="display:block;margin:auto;width:600px">
                """
            ,unsafe_allow_html=True)
    #- 6th Procedure : (  Exploratory Data Analysis )
    with st.expander("***6th Procedure*** : ( Exploratory Data Analysis [EDA] )"):
        st.markdown(
                """
                - ***EDA*** Is Exploratory Data Analysis Is The Crucial Process For Performing Initial Investigations To Discover Patterns
                - ***EDA*** Check Assumptions With Help Of Summary Statistics And Graphical Representations 
                - ***EDA*** Can Be Leveraged To Check Outliers , Patterns And Trends In A Given Data
                - ***EDA*** Can Provide Meaningful Patterns 
                - ***EDA*** Provides In-Depth Insights To Solve Business Problems 
                - ***EDA*** Gives A Clue 'Evidence' To Impute Missing Values In A Data 
                """
             )
        tab1,tab2,tab3,tab4 = st.tabs(["📑 **Statistical Summary**","📈 **EDA_Univariate**","📉 **EDA_Bivariate**","📊 **EDA_Multivariate**"],)
        with tab1:
            st.markdown(f"""
            <div style="font-weight:bold;color:{head_color};text-align:center;margin:10px;">📑Statistical Summary</div>
            """,unsafe_allow_html=True)
            st.markdown(f"""
            <div style="padding:10px;">
                <p>
                    - Analyzing/visualizing The Dataset By Taking One Variable At Time<br/>
                    - Data Visualization Is Essential Such That We Decide What Charts Used To Plot Basic Charts<br>
                        - Trendy Python Libraries Are Used For Plotting/Visualizing Data<br/> 
                            <font style="color:{head_color};font-weight:bold;display:block;padding-left:20px">1. Matplotlib</font> 
                            <font style="color:{head_color};font-weight:bold;display:block;padding-left:20px">2. seaborn</font> 
                            <font style="color:{head_color};font-weight:bold;display:block;padding-left:20px">3. plotly</font>  
                </p>            
            <div>
            """,unsafe_allow_html=True)
            for i in range(1,4):
                img_path =  os.path.join(os.getcwd(),
                                        "deployment","imgs","home_imgs","analysis_imgs",
                                        f"statistical_summary_{i}.png"
                                        )
                img_as_base64 = gf.imgAsBase64(img_path=img_path)
                st.markdown(
                f"""
                ****Python Code Snippet-{i}****
                <img src='data:image/png;base64,{img_as_base64}' style="display:block;margin:auto;width:600px">
                """
            ,unsafe_allow_html=True)

        with tab2: 
            #-title Of Topic
            st.markdown(f"""
            <div style="font-weight:bold;color:{head_color};text-align:center;margin:10px;">📈EDA_Univariate</div>
            """,unsafe_allow_html=True) 
            st.markdown(f"""
            <div style="padding:10px;">
                <p>
                    - Univariate Analysis Is A Type Of Analysis On Which EDA Relies Can Be Done For Both Categorical And Numerical Variables <br/>
                            <font style="color:{head_color};font-weight:bold;padding-left:20px">Numerical Variables :</font> Can Be\
                            Visualized By Histogram Plot , Box Plot , Density Plot Or More <br/>
                            <font style="color:{head_color};font-weight:bold;padding-left:20px">Categorical Variables :</font> Can Be\
                            Visualized By count Plot , bar Plot , Pie Chart Or More 
                </p>            
            <div>
            """,unsafe_allow_html=True)
            ls = ["Categorical Features" , "Numerical Features"]
            for i in range(1,3):
                img_path =  os.path.join(os.getcwd(),
                                        "deployment","imgs","home_imgs","analysis_imgs",
                                        f"Univariate_analysis{i}.png"
                                        )
                img_as_base64 = gf.imgAsBase64(img_path=img_path)
                st.markdown(
                f"""
                ****Visual Chart- ( {ls[i-1]} )****
                <img src='data:image/png;base64,{img_as_base64}' style="display:block;margin:auto;width:600px">
                """
            ,unsafe_allow_html=True)
        with tab3:
            #-title Of Topic
            st.markdown(f"""
            <div style="font-weight:bold;color:{head_color};text-align:center;margin:10px;">📉EDA_Bivariate</div>
            """,unsafe_allow_html=True) 
            st.markdown(f"""
            <div style="padding:10px;">
                <p>
                    - Bivariate Analysis Is A Type Of Analysis On Which EDA Relies Can Be Done For Both Categorical And Numerical Variables.<br/>
                    - Bivariate Analysis Helps To Understand The Relationship Between Indpendent Ad Dependent Variables Present In The Data And How They're Related To Each Other.<br/>
                            <font style="color:{head_color};font-weight:bold;padding-left:20px;">Numerical Variables :</font> We Can Widely Us\
                            Pair Plot And Scatter Plot To Clear The Relationship <br/>
                            <font style="color:{head_color};font-weight:bold;padding-left:20px">Categorical Variables :</font><br>
                            <p style="padding-left:40px">1. If The Output Feature Is Continuous ,  bar plot Is Used Commonly.</p> 
                            <p style="padding-left:40px">2. If The Output Feature Is Categorical , stacked Bar plot Is Preformend Commonly.</p> 
                    <p style="font-style:{head_style}">- Bivariate Analysis Helps To Understand The Relationship Between Independent And Dependent Variables Present In The Data And How They're Related To Each Other</p>
                </p>            
            <div>
            """,unsafe_allow_html=True)
            img_path =  os.path.join(os.getcwd(),
                                        "deployment","imgs","home_imgs","analysis_imgs",
                                        f"pairplot.png"
                                        )
            img_as_base64_1 = gf.imgAsBase64(img_path=img_path)
            img_path =  os.path.join(os.getcwd(),
                                                    "deployment","imgs","home_imgs","analysis_imgs",
                                                    f"Bar-Plot-categorical.png"
                                                    )
            img_as_base64_2= gf.imgAsBase64(img_path=img_path)
            st.markdown(
                f"""
                ****Visual Chart-1 (Numerical Bivariate Analysis)****
                <img src='data:image/png;base64,{img_as_base64_1}' style="display:block;margin:auto;width:600px">
                """
            ,unsafe_allow_html=True)
            st.markdown(
                f"""
                ****Visual Chart-2 (Categorical Bivariate Analysis)****
                <img src='data:image/png;base64,{img_as_base64_2}' style="display:block;margin:auto;width:600px">
                """
            ,unsafe_allow_html=True)
        with tab4:
            #-title Of Topic
            st.markdown(f"""
            <div style="font-weight:bold;color:{head_color};text-align:center;margin:10px;">📊EDA_Multivariate</div>
            """,unsafe_allow_html=True)
            st.markdown(f"""
            <div style="padding:10px;">
                <p>
                    - Looks At More Than two Variables and Is One Of Most Useful Method To Determine The Relationships And Patterns In Data And How All Variables are Related With Each Other
                    <p style="font-style:{head_style};padding-left:20px"> A Heat Map Is Widely Used For Multivariate Analysis</p>
                    <p style="font-style:{head_style};padding-left:20px"> A Heat Map Gives The Correlations Between Variables Whether They've Positive Or Negative Correlation And Even No Correlation Found</p>
                </p>            
            <div>
            """,unsafe_allow_html=True)
            img_path =  os.path.join(os.getcwd(),
                                        "deployment","imgs","home_imgs","analysis_imgs",
                                        f"Correlation-matrix.png"
                                        )
            img_as_base64= gf.imgAsBase64(img_path=img_path)
            st.markdown(
                f"""
                ****Visual Chart (Numerical Multivariate Analysis)****
                <img src='data:image/png;base64,{img_as_base64}' style="display:block;margin:auto;width:600px">
                """
            ,unsafe_allow_html=True)
        #- 6th Procedure*** : (  Exploratory Data Analysis )
    #- 7th Procedure ("Data Transformation") 
    with st.expander("***7th Procedure*** : ( Data Transformation )"):
        st.markdown(
        """
            -  Data Transformation Is An Approach To Convert Numerical Feature Values \
            Such Those Converted Values Has Same Importance Of Orignal Values.
            - A Type Of Data Transformer Is ***Log Transformation*** Where \
            It Helps To Maintain Standard Deviation Scale Making It Similar To Other Variables 
            - It's Also Called As **Normalization** (Transforming Data Shape Onto Bill Curve)
        """
        ,unsafe_allow_html=True
        )
        img_path = os.path.join(os.getcwd(),"deployment","imgs","home_imgs","analysis_imgs",
                                        "Price_Distribution.png")
        img_as_base64 = gf.imgAsBase64(img_path)
        st.markdown(
            f"""
            ****Orginal Distribution Before Transformation****
            <img src='data:image/png;base64,{img_as_base64}' style="display:block;margin:auto;width:600px">
            """
            ,unsafe_allow_html=True)
        img_path = os.path.join(os.getcwd(),"deployment","imgs","home_imgs","analysis_imgs",
                                        "priceDistribution_transformed.png")
        img_as_base64 = gf.imgAsBase64(img_path)
        st.markdown(
            f"""
            ****Transformed Distribution After Normalization****
            <img src='data:image/png;base64,{img_as_base64}' style="display:block;margin:auto;width:600px">
            """
            ,unsafe_allow_html=True)
    #- 8th Procedure ("Data Imputation") 
    with st.expander("***8th Procedure*** : ( Data Imputation )"):
        st.markdown(
        """
            -  ***Missing Values*** Arise In Almost All Statistical Analysis And Therefore Many Ways Are Existed \
            To Impute Missing Values By Their Mean , Median , Most Frequent Or Even By Advanced Algorithms Like KNN \
            Or Regularizers
            - Before Imputing Missing Values , We Must Need Bussiness Knowledge Or Common Insights About The Data 
        """
        ,unsafe_allow_html=True
        )
        img_path = os.path.join(os.getcwd(),"deployment","imgs","home_imgs","analysis_imgs",
                                        "imputation_Categorical_ftrs.png")
        img_as_base64 = gf.imgAsBase64(img_path)
        st.markdown(
            f"""
            ****Imputation For Categorical Features****
            <img src='data:image/png;base64,{img_as_base64}' style="display:block;margin:auto;width:600px">
            """
            ,unsafe_allow_html=True)
        img_path = os.path.join(os.getcwd(),"deployment","imgs","home_imgs","analysis_imgs",
                                        "Imputation_ContinuousFtrs.png")
        img_as_base64 = gf.imgAsBase64(img_path)
        st.markdown(
            f"""
            ****Imputation For Numerical Features****
            <img src='data:image/png;base64,{img_as_base64}' style="display:block;margin:auto;width:600px">
            """
            ,unsafe_allow_html=True)

#-Machine Learning Info Section-# 
with st.container():
    #- Title Of Intro Of Machine Learning 
    gf.secTitleName(title_name="Info About Machine Learning 🧬 🤖")
    st.info("Machine Learning Uncoming Soon")

# -------------------------------------------------------
# Last snippet (Utilities)--> (Dependencies) (footer Sec)
# -------------------------------------------------------
gf.footerCreater()
####---- End Of What Home Page Contains---####
