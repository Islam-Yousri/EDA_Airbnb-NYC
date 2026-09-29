import os 
import io
import base64 
import pandas as pd
from  PIL import Image
import streamlit as st 

#---Definations Of Functions---# 
    #- This Function Is Used To Configure CSS Style For All Elements In This Website :
#---Defination Of Function (CSS Style)---# 
def cssStyle():
     st.markdown(
    """
        <style> 
            /*Global Properties*/
            *{
                font-family: "Times New Roman", Times, serif;
            }
            /*Start Of information Card*/
            .imformation-cd {
                width:80%;
                height: 300px;
                overflow-y: auto;
                overflow-x: hidden;
                background: linear-gradient(#135deg, #ffffff, #f7fbfc);
                border-left: 6px solid #2BBBD7;
                border-radius: 15px;
                padding: 25px 30px;
                margin: 20px auto;
                box-shadow: 0 8px 25px rgba(0, 0, 0, 0.08);
            }
            .imformation-cd-title {
                font-size: 20px;
                font-weight: 700;
                font-style:italic;
                color: #2BBBD7;
                margin-bottom: 15px;
            }

            .imformation-cd-content {
                font-size: 16px;
                padding-left:20px;
                line-height: 1.7;
                color: #333333;
            }
            .imformation-cd-subtitle{
                font-size: 16px;
                font-weight: 600;
                text-align:center;
                color: #247BA0;
                line-height: 1.6;
                letter-spacing: 0.3px;
                padding-left:15px;
                margin-top: 5px;
                margin-bottom: 15px;
                border-radius:3px;
                background: linear-gradient(
                    90deg,
                    #DFF1F1,
                    #C5C1C1,
                    #BFC6C4,
                    #A8BBA3,
                    #E8E2D8
                );
            }
            .imformation-cd-content strong , .insights-view strong {
                color: #FF5A5F;
                font-weight: 600;
                padding-left:15px;
            }
            .imformation-cd-content a {
                display: inline-block;
                padding: 5px 10px;
                border-radius: 8px;

                color: #2BBBD7;
                background-color: rgba(43, 187, 215, 0.08);

                border: 1px solid rgba(43, 187, 215, 0.35);

                text-decoration: none;
                font-size: 15px;
                font-weight: 600;
                transition: all 0.25s ease;
            }

            .imformation-cd-content a:hover {
                color: white;
                background-color: #2BBBD7;
                border-color: #2BBBD7;

                transform: translateY(-2px);
                box-shadow: 0 5px 12px rgba(43, 187, 215, 0.25);
            }  
        /*End Of information Card*/
            .feature-card {
                position: relative;
                width: 100%;
                min-height: 130px;
                padding-left: 22px;
                margin-bottom: 20px;
                border-radius: 16px;
                border: 1px solid rgba(43, 187, 215, 0.25);
                background: linear-gradient(
                    135deg,
                    rgba(255,255,255,0.95),
                    rgba(240,249,255,0.95)
                );
                box-shadow: 0 6px 20px rgba(0,0,0,0.08);
                overflow: hidden;
                transition:
                    transform 0.35s ease,
                    box-shadow 0.35s ease,
                    border-color 0.35s ease;
                cursor: pointer;
            }

            /* Card hover */
            .feature-card:hover {
                transform: translateY(-7px);
                border-color: #2BBBD7;
                box-shadow:
                    0 12px 30px rgba(43,187,215,0.20);
            }
            /* Feature name */
            .feature-title {
                font-size: 16px;
                font-weight: 700;
                color: #247BA0;
                margin-bottom: 8px;
                transition: color 0.3s ease;
            }
            .feature-card:hover .feature-title {
                color: #FF6B6B;
            }
            /* Description */
            .feature-description {
                font-size: 14px;
                line-height: 1.6;
                color: #64748B;
                opacity: 0;
                transform: translateY(10px);
                transition:
                    opacity 0.35s ease,
                    transform 0.35s ease;
            }
            /* Show description on hover */
            .feature-card:hover .feature-description {
                opacity: 1;
                transform: translateY(0);
            }
            /* Small decorative element */
            .feature-card::before {
                content: "";
                position: absolute;
                width: 5px;
                height: 100%;
                left: 0;
                top: 0;
                background: linear-gradient(
                    180deg,
                    #2BBBD7,
                    #6C63FF
                );
                border-radius: 16px 0 0 16px;
            }
            .predictor-header {
                display: flex;
                align-items: center;
                gap: 12px;

                margin-top: 25px;
                margin-bottom: 20px;
                padding: 10px 0;

                border-bottom: 2px solid rgba(43, 187, 215, 0.25);
            }

            .predictor-icon {
                font-size: 25px;
                color: #2BBBD7;

                filter: drop-shadow(0 0 6px rgba(43, 187, 215, 0.35));
            }

            .predictor-title {
                font-size: 18px;
                font-weight: 750;
                letter-spacing: 0.5px;

                background: linear-gradient(
                    90deg,
                    #247BA0,
                    #2BBBD7,
                    #6C63FF
                );

                -webkit-background-clip: text;
                -webkit-text-fill-color: transparent;
                background-clip: text;
            }
            .libraries-container {
                padding: 24px;
                margin: 20px 0;

                border-radius: 18px;

                background: linear-gradient(
                    135deg,
                    rgba(255,255,255,0.95),
                    rgba(240,249,255,0.95)
                );

                border: 1px solid rgba(43,187,215,0.25);

                box-shadow:
                    0 8px 25px rgba(0,0,0,0.08);

                transition: all 0.35s ease;
            }

            .libraries-container:hover {
                transform: translateY(-5px);

                border-color: #2BBBD7;

                box-shadow:
                    0 12px 30px rgba(43,187,215,0.18);
            }

            .libraries-title {
                font-size: 23px;
                font-weight: 750;

                margin-bottom: 18px;

                background: linear-gradient(
                    90deg,
                    #247BA0,
                    #2BBBD7,
                    #6C63FF
                );

                -webkit-background-clip: text;
                -webkit-text-fill-color: transparent;
                background-clip: text;
            }

            .library-item {
                display: inline-block;

                padding: 8px 14px;
                margin: 5px;

                border-radius: 10px;

                background: rgba(43,187,215,0.08);

                border: 1px solid rgba(43,187,215,0.20);

                color: #247BA0;

                font-size: 14px;
                font-weight: 600;

                transition: all 0.25s ease;
            }

            .library-item:hover {
                transform: translateY(-3px);

                background: rgba(43,187,215,0.15);

                border-color: #2BBBD7;

                box-shadow: 0 4px 12px rgba(43,187,215,0.15);
            }
            /*sidebar subtitle*/
            .sidebar-subtitle {
                font-size: 16px;
                font-weight: 650;
                color: #DE3E3E;

                letter-spacing: 0.5px;
                line-height: 1.5;

                margin-top: 8px;
                margin-bottom: 12px;

                text-shadow: 0 0 8px rgba(222, 62, 62, 0.20);
            }
            .sidebar-subtitle strong{
                color:#39B1D1;
            }
            .chart-description {
                margin: 15px 0 25px 0;
                padding: 16px 20px;

                border-radius: 14px;

                background: linear-gradient(
                    135deg,
                    rgba(43, 187, 215, 0.12),
                    rgba(108, 99, 255, 0.10),
                    rgba(255, 107, 107, 0.08)
                );

                border-left: 5px solid #2BBBD7;
                border-top: 1px solid rgba(43, 187, 215, 0.20);

                box-shadow:
                    0 6px 18px rgba(43, 187, 215, 0.10);

                transition: all 0.3s ease;
            }

            .chart-description:hover {
                transform: translateY(-3px);

                box-shadow:
                    0 10px 25px rgba(43, 187, 215, 0.18);

                border-left-color: #FF6B6B;
            }

            .chart-description-title {
                font-size: 17px;
                font-weight: 750;

                margin-bottom: 6px;

                background: linear-gradient(
                    90deg,
                    #247BA0,
                    #2BBBD7,
                    #6C63FF
                );

                -webkit-background-clip: text;
                -webkit-text-fill-color: transparent;
                background-clip: text;
            }

            .chart-description-text {
                font-size: 14px;
                font-weight: 500;

                color: #475569;

                line-height: 1.7;
                letter-spacing: 0.2px;

                margin: 0;
            }

            .chart-description-highlight {
                color: #DE3E3E;
                font-weight: 700;
            }
            .extracted-features {
                padding: 22px;
                margin: 20px 0;
                border-radius: 18px;
                background: linear-gradient(
                    135deg,
                    rgba(43,187,215,0.08),
                    rgba(108,99,255,0.08)
                );
                border: 1px solid rgba(43,187,215,0.25);
                box-shadow: 0 8px 25px rgba(0,0,0,0.07);
            }

            .extracted-title {
                font-size: 21px;
                font-weight: 750;
                color: #247BA0;
                margin-bottom: 18px;
            }

            .feature-list {
                display: flex;
                flex-wrap: wrap;
                gap: 10px;
            }

            .feature-chip {
                padding: 9px 15px;
                border-radius: 10px;
                background: rgba(43,187,215,0.10);
                border: 1px solid rgba(43,187,215,0.25);
                color: #247BA0;
                font-size: 14px;
                font-weight: 650;
                transition: all 0.3s ease;
            }

            .feature-chip:hover {
                transform: translateY(-3px);
                background: rgba(108,99,255,0.12);
                border-color: #6C63FF;
                color: #6C63FF;
                box-shadow: 0 5px 15px rgba(108,99,255,0.15);
            }
            .insights-view{
                height: 500px;
                overflow-y: auto;
                overflow-x: hidden;
                padding: 20px 25px;
                border-radius: 15px;
                border: 1px solid rgba(100,100,100,0.25);
                background: rgba(255,255,255,0.75);
                box-shadow: 0 4px 15px rgba(0,0,0,0.08);
                font-size: 16px;
                line-height: 1.7;
            }
            .insights-view .insights-title {
                font-family: "Times New Roman", serif;
                font-size: 22px;
                font-weight: 700;
                color: #247BA0;
                text-align: left;
                letter-spacing: 0.5px;
                line-height: 1.3;
                margin: 0 0 18px 0;
                padding: 0 0 10px 0;
                border-bottom: 2px solid #2BBBD7;
            }
            .insights-view .insight-text {
                font-family: "Times New Roman", serif;
                font-size: 16px;
                font-weight: 500;
                color: #334E5C;
                line-height: 1.7;
                letter-spacing: 0.2px;
                text-align: justify;
                margin: 0 0 14px 0;
                padding: 10px 14px;
                border-left: 3px solid #2BBBD7;
                background: rgba(43, 187, 215, 0.05);
                border-radius: 6px;
            }
            /* Download button */
            div[data-testid="stDownloadButton"] button {
                background: linear-gradient(
                135deg,
                #247BA0,
                #2BBBD7
                );

                margin-top:20px; 
                margin-left:20px;
                color: white;

                border: none;
                border-radius: 12px;

                padding: 12px 24px;

                font-size: 16px;
                font-weight: 600;

                font-family: "Times New Roman", serif;

                cursor: pointer;

                transition: all 0.3s ease;

                box-shadow:
                    0 5px 15px rgba(36, 123, 160, 0.25);
            }      

            /* Hover */
            div[data-testid="stDownloadButton"] button:hover {
                transform: translateY(-3px);

                box-shadow:
                    0 8px 22px rgba(36, 123, 160, 0.40);

                background: linear-gradient(
                    135deg,
                    #2BBBD7,
                    #247BA0
                );
            }

            /* Click */
            div[data-testid="stDownloadButton"] button:active {
                transform: translateY(0px);
            }
        </style>
    """      
     ,
     unsafe_allow_html=True)

#- 1st Function To Configure The Page 
    #- This Function Is Used To Configure The Page :
        #- parameters : str:page_title , str:page_icon , str:layout ;

def pageConfig(page_title,page_icon,layout):
    st.set_page_config(
        page_title=page_title,
        page_icon=page_icon,
        layout=layout
    )  

#- 2nd Function To Make Top Buttons bar 
    #- This Function Is Used To Make Buttons Bar On The Top Of The Page
      #- parameters : 
        #- list:button_names --> contains the names of Top buttons

def showTopButtons(button_names):
    cols = st.columns(len(button_names))
    for btn_name in button_names:
        with cols[button_names.index(btn_name)]:
            if st.button(btn_name):
                st.session_state.page_name = btn_name  

#- 3rd Function To Change Background Color Of The Page
    #- This Function Is Used To Change The Background Color Of The Page
      #- parameters : 
        #- str:color --> contains the color code of the background
def animatedLine():
     st.markdown(f"""
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
#- 4th Function To Change Background Color Of The Page
    #- This Function Is Used To Change The Background Color Of The Page
      #- parameters : 
        #- str:color --> contains the color code of the background
def changeBackgroundColor(color):
    if color == "#E3F2FD":
        st.markdown(
            f"""
            <style>
                .stApp {{
                    background-color: {color};
                }}
                [data-testid="stHeader"] {{
                background-color: {color};
                }}
            </style>
            """,
            unsafe_allow_html=True
        )
    if color == "#E7F5EB":
        st.markdown(
            f"""
            <style>
                .stApp {{
                    background-color: {color};
                }}
                [data-testid="stHeader"] {{
                    background-color: {color};
                }}
            </style>
            """,
            unsafe_allow_html=True
        )
    if color == "#FFFFFF":
                st.markdown(
            f"""
            <style>
                .stApp {{
                    background-color: {color};
                }}
                [data-testid="stHeader"] {{
                    background-color: {color};
                }}
            </style>
            """,
            unsafe_allow_html=True
        )

#- 5th Function To Create the top title header Of The Page 
    #- This Function Is Used To Create The Top Title header Of The Page
      #- parameters : 
        #- str:color --> contains the color code of Text 
def createTopTitleHeader(title,color,bg_color=''):
    # Centered H3 header with custom color
    st.markdown(
        
        f"""
            <style>
            .animated-title {{
                font-size: 25px;
                font-weight: 700;
                text-align: center;
                margin: 20px 0;
                font-family: "Times New Roman", Times, serif;
                font-size:25px;
                background-color:{bg_color};
                animation: colorChange 5s infinite;
            }}

            @keyframes colorChange {{
                0%   {{ color: {color}; }}
                25%  {{ color: #00B8FF; }}
                50%  {{ color: #2979FF; }}
                75%  {{ color: #651FFF; }}
                100% {{ color: #D500F9; }}
            }}
            </style>

            <div class="animated-title">
                {title}
            </div>
            """,
        unsafe_allow_html=True
    )

#- 6th Function To Set up the icon Of Sidebar  
    #- This Function Is Used For Inserting icon shown in menu bar
      #- parameters : 
        #- str: icon_path : The Path Of Icon 
def sidebarLogoConfig(icon_path):
     st.logo(icon_path,size="large")

#- 7th Function To show Image In Our Platform 
    #- This Function Is Used For Displaying An Image By Converting It 
    #   Onto Suitable Format Where Platform Can Read     
      #- parameters : 
        #- str: img_path --> Represent The Path Of Passed image 
      
      #- Return --> image In base64 (Byte File Of Passed Image) 
def imgAsBase64(img_path):
         # Load image
    image = Image.open(img_path)
    # Convert image to Base64 (Byte File)
    buffer = io.BytesIO()
    image.save(buffer, format="PNG")
    img_base64 = base64.b64encode(buffer.getvalue()).decode() 
    return img_base64

#- 8th Function To show Information Card  
    #- This Function Is Used For Displaying Card Holding Some Of Information  
      #- parameters : 
        #- str: title_card --> Represent The Title Of info Snippet 
        #- str: text_card  --> Represents The Text Will Be Shown
def showInfoCard(title_card:str,text_card:str):
    st.markdown(
        f"""
        <div class='imformation-cd '>
            <div class='imformation-cd-title'>
                {title_card}    
            </div>
            <div class='imformation-cd-content'>
                {text_card}
            </div>
        </div>
        """
    ,unsafe_allow_html=True
     )

#- 9th Function To show Section Titke 
    #- This Function Is Used For Displaying Section Title
      #- parameters : 
        #- str: sec_title  --> Represent The Title Name Of Section 
def secTitleName(title_name:str):
     st.markdown(
    f"""
        <div class="predictor-header">
        <span class="predictor-icon">◈</span>
        <span class="predictor-title">{title_name}</span>
        </div>
    """
    ,unsafe_allow_html=True )
#- 10th Function To show Information Card  
    #- This Function Is Used For Displaying Card Holding Some Of Information  
      #- parameters : 
        #- str: feature_name  --> Represent The Name Of Feature 
        #- str: feature_desc  --> Represents The Description Of Feature
def ftrCardCreater(feature_name:str , feature_desc:str):
    st.markdown(f"""
    <div class="feature-card">
        <div class="feature-title">
            {feature_name}
        </div>
        <div class="feature-description">
            {feature_desc}
        </div>
    </div>
    """, unsafe_allow_html=True)
#- 11th Function To show Footer Sections   
    #- This Function Is Used For Displaying Footer Sections Expresses Card 
        #- This Card Is Consists Of Libraries Used In This APP And They Are Clickable Links    
def footerCreater():
    st.markdown("""
    <div class="libraries-container">
        <div class="libraries-title">
            ⚙️ Libraries Used
        </div>
        <span class="library-item"><a href='https://python.readthedocs.io/fr/latest/library/os.html' style='text-decoration: none;'>🖥️ os          </a></span>
        <span class="library-item"><a href='https://docs.python.org/3/library/io.html' style='text-decoration: none;'>🔄 io          </a></span>
        <span class="library-item"><a href='https://docs.python.org/3/library/base64.html' style='text-decoration: none;'>🔐 base64      </a></span>
        <span class="library-item"><a href='https://pillow.readthedocs.io/en/stable/' style='text-decoration: none;'>🖼️ PIL         </a></span>
                <span class="library-item"><a href='https://pypi.org/project/datasist/' style='text-decoration: none;'>🧪 datasist    </a></span>
        <span class="library-item"><a href='https://pypi.org/project/num2words/' style='text-decoration: none;'>1️⃣➜📝 num2words</a></span>
        <span class="library-item"><a href='https://plotly.com/python-api-reference/' style='text-decoration: none;'>📊 Plotly      </a></span>
        <span class="library-item"><a href='https://pandas.pydata.org/docs/' style='text-decoration: none;'>🐼 Pandas      </a></span>
        <span class="library-item"><a href='https://numpy.org/' style='text-decoration: none;'>🔢 NumPy       </a></span>
        <span class="library-item"><a href='https://matplotlib.org/stable/index.html' style='text-decoration: none;'>📊 Matplotlib  </a></span>
        <span class="library-item"><a href='https://pypi.org/project/seaborn/' style='text-decoration: none;'>📈 Seaborn     </a></span>
        <span class="library-item"><a href='https://www.geeksforgeeks.org/python/a-beginners-guide-to-streamlit/' style='text-decoration: none;'>🌐 Streamlit   </a></span>
        <!--<span class="library-item"><a href='https://scikit-learn.org/stable/index.html' style='text-decoration: none;'>🤖 Scikit-Learn</a></span>-->
    </div>
    """,unsafe_allow_html=True)
#- 12th Function To show Dataset   
    #- This Function Is Used For Reading Dataset 
@st.cache_data
def load_dataset(file):
    return pd.read_csv(file)
#- 13th Function   
    #- This Function Is Used For Displaying Subtitles 
def subtitleView(subtitle_name): 
     st.markdown(f"<font class='sidebar-subtitle'>\
                         <strong style='padding-right:5px'>⬤</strong> {subtitle_name}</font><br/>"
                         ,unsafe_allow_html=True)
#- 14th Function   
    #- This Function Is Used For Displaying Chart Description 
def chartDesc(chart_title , desc_chart): 
     st.markdown(f"""
    <div class="chart-description">
        <div class="chart-description-title">
            {chart_title}
        </div>
        <p class="chart-description-text">
            {desc_chart}
        </p>
    </div>
    """, unsafe_allow_html=True) 
#- 15th Function   
    #- This Function Is Used For Displaying Names Of Extracted Features 
def extractFtrName(feature_names:list):
    if feature_names:
        ls_html=''
        for ftr_name in feature_names:
             ls_html+=f'<span class="feature-chip">{ftr_name}</span>'
        st.markdown(
        f"""
        <div class="extracted-features">
            <div class="extracted-title">
                ✦ Extracted Features
            </div>
            <div class="feature-list">
                {ls_html}
            </div>
        </div>
        """ 
        ,unsafe_allow_html=True)
#- 16th Function   
    #- This Function Is Used For Displaying insights in insights page 
def insightsShow(text_title , card_text):
       st.markdown(f"""
        <div class='insights-view'>
            <div class='insights-title'>{text_title}</div>
            <div class='insights-text'>{card_text}</div>
        </div>
    """,unsafe_allow_html=True)
#- 17th Function   
    #- This Function Is Used For Downlaoding A File Holding Set Of Information  
    #-params
        #   file_path : str
        #         Path to the file.
    
        #     button_text : str
        #         Text displayed on the button.
    
        #     icon : str
        #         Icon displayed before the text.
    
        #     file_name : str
        #         Name used when downloading the file.

        #     mime_type : str
        #         MIME type of the file.

def download_file_button(
    file_path,
    button_text="Download File",
    icon="⬇️",
    file_name=None,
    mime_type="application/octet-stream"
):
    if file_name is None:
        file_name = file_path.split("/")[-1]
    # Read file
    with open(file_path, "rb") as file:
        file_data = file.read()
    # Create hidden Streamlit download button
    st.download_button(
        label=f"{icon} {button_text}",
        data=file_data,
        file_name=file_name,
        mime=mime_type,
        key=f"download_{file_name}",
        use_container_width=False
    )
    