import streamlit as st

# Custom CSS to remove button borders and change text color to black
st.markdown("""
    <style>
    .stButton button {
        background-color: transparent;
        color: black;  /* Set text color to black */
        border: none;
        font-size: 1.2rem;
        text-align: left;
        padding: 0.5rem;
        transition: color 0.3s ease, background-color 0.3s ease;
        display: block;
        width: 100%;
    }
    .stButton button:hover {
        background-color: #4b4b4b;
        color: white;  /* Change text color to white on hover */
        cursor: pointer;
    }
    .stButton button:focus {
        outline: none;
    }
    .sidebar .sidebar-content h2 {
        color: #ff4b4b;
        padding-bottom: 10px;
    }
    </style>
""", unsafe_allow_html=True)

# Sidebar navigation
def nav_menu():
    st.sidebar.markdown("<h1>Nived Raj</h1>", unsafe_allow_html=True)
    st.sidebar.markdown("<h2>PROFILE</h2>", unsafe_allow_html=True)
    about_clicked = st.sidebar.button("About")
    education_clicked = st.sidebar.button("Education")
    skills_clicked = st.sidebar.button("Experience and Skills")
    contact_clicked = st.sidebar.button("Contact Me")
    
    st.sidebar.markdown("<h2>PROJECTS</h2>", unsafe_allow_html=True)
    youtube_clicked = st.sidebar.button("Real-Time YouTube Sentiment Analytics")
    anonymization_clicked = st.sidebar.button("Text Data Anonymization for Healthcare")
    movie_prediction_clicked = st.sidebar.button("Boxoffice Prediction")
    fraud_detection_clicked = st.sidebar.button("Credit Card Fraud Detection")
    spotify_prediction_clicked = st.sidebar.button("Spotify Song Genre Prediction")
    crypto_prediction_clicked = st.sidebar.button("Crypto Prediction")
    movie_recommendation_clicked = st.sidebar.button("Movie Recommendation System")
    glasgow_city_clicked = st.sidebar.button("Real-Time View of Glasgow City Centre")
    alcohol_analysis_clicked = st.sidebar.button("An Analysis of Alcohol-Related Callouts' Burden on Ambulance Waiting Times")
    syncorg_optimization_clicked = st.sidebar.button("Data Management & Workflow Optimization for SyncOrg")

    # Return the selected page
    if about_clicked:
        return "About"
    elif education_clicked:
        return "Education"
    elif skills_clicked:
        return "Skills"
    elif contact_clicked:
        return "Contact"
    elif youtube_clicked:
        return "YouTube"
    elif anonymization_clicked:
        return "Anonymization"
    elif movie_prediction_clicked:
        return "Movie"
    elif fraud_detection_clicked:
        return "Fraud"
    elif spotify_prediction_clicked:
        return "Spotify"
    elif crypto_prediction_clicked:
        return "Crypto"
    elif movie_recommendation_clicked:
        return "Movie Rec"
    elif glasgow_city_clicked:
        return "Glasgow"
    elif alcohol_analysis_clicked:
        return "Alcohol"
    elif syncorg_optimization_clicked:
        return "SyncOrg"
    else:
        return "About"  # Default page

# Display content based on the selected page
selected_page = nav_menu()

if selected_page == "About":
    st.title("Hey there! I’m Nived.")
    st.write("""
Iam a passionate **Data Scientist** who thrives on turning raw data into meaningful insights. For me, data isn’t just numbers on a screen—it’s a tool to shape decisions, drive innovation, and solve real-world problems. Whether I’m building **predictive models**, tackling **machine learning challenges**, or exploring **NLP**, I’m always looking for new ways to push the boundaries of what data can do.

My work spans across multiple domains. I’ve developed solutions for **healthcare data anonymization** to ensure privacy compliance, built **credit card fraud detection models**, and even created a **Real-Time YouTube Comment Sentiment Analysis web app** that provides instant insights into audience sentiment. Lately, I’ve been diving into **cloud deployment** with **AWS**, scaling projects to make them more efficient and accessible.

While I thrive in environments where **creativity meets logic**, life isn’t all about data! When I’m not immersed in my projects, you’ll find me out for a run, hitting the gym, or cooking up something new in the kitchen. I’m also a huge fan of **movies** and **video games**, which help me recharge after solving complex data problems.

In short, I’m always curious, always learning, and always ready for the next exciting challenge. Whether it’s predicting trends or breaking down complex problems, I’m eager to dive in and get to work.

Feel free to use the navigation on the left to check out my latest projects and learn more about me!

Nived Raj
""")


elif selected_page == "Education":
    st.title("Education")
    st.write("""
    I’ve always believed that strong foundations lead to greater heights, and my academic journey reflects that. Graduating with **Distinction** in my Master’s in Data Analytics and achieving **First Class** honors in my Computer Science Engineering degree, I’ve consistently pushed the boundaries of learning. From excelling in foundational subjects during my 10th grade (CGPA: 10) to mastering advanced data science concepts at the University of Strathclyde, my academic record speaks to my dedication and proficiency in the field.
    """)

    st.markdown("""

    - **Master’s in Data Analytics (Distinction)**  
      *University of Strathclyde* | September 2021 – September 2022  

    - **Bachelor of Technology in Computer Science and Engineering (First Class)**  
      *Kerala Technological University* | 2016 – 2020  
    *CGPA: 8.83*

    - **Higher Secondary Education in Computer Science (94%)**  
      *KTCT Higher Secondary School* | 2014 – 2016  

    - **10th Grade, Central Board of Secondary Education (CGPA: 10)**  
      *Sree Gokulam School* | 2013 – 2014  
    """)


elif selected_page == "Skills":
    st.title("Experience and Skills")
    st.write("### Skills")
    st.write("From machine learning to cloud deployment, these are the core tools I rely on to deliver impactful data-driven solutions.")
    # Custom CSS for card styling
    st.markdown("""
        <style>
        .skill-card {
            background-color: #f0f0f5;
            border: 1px solid #e1e1eb;
            padding: 20px;
            margin: 10px;
            border-radius: 8px;
            box-shadow: 2px 2px 10px rgba(0, 0, 0, 0.1);
            text-align: center;
        }
        .skill-title {
            font-size: 1.2em;
            font-weight: bold;
            margin-bottom: 10px;
            color: #4b4b4b;
        }
        </style>
    """, unsafe_allow_html=True)

    # Function to create a skill card
    def skill_card(title, content):
        st.markdown(f"""
        <div class="skill-card">
            <div class="skill-title">{title}</div>
            <div>{content}</div>
        </div>
        """, unsafe_allow_html=True)

    # Skill categories with content
    skills = {
        "Programming Languages": "Python (NumPy, Pandas, Scikit-learn, Matplotlib, Seaborn), SQL (MySQL), R (Tidyverse), C++, HTML/CSS",
        "Data Science & Machine Learning": "Supervised & Unsupervised Learning, Feature Engineering, Model Deployment, Hyperparameter Tuning, Cross-Validation, Imbalanced Data Techniques (SMOTE, Undersampling), XGBoost, LightGBM, Random Forest, Logistic Regression, KNN, LSTM, Time Series Analysis",
        "Data Analytics & Visualization": "Tableau, Power BI (Dashboard Design, ETL, Data Modeling, Power Query, DAX), Altair, Excel (Advanced Formulas, Pivot Tables, VBA)",
        "Cloud & DevOps": "AWS (EC2, S3), Streamlit, Git, GitHub",
        "Natural Language Processing (NLP)": "spaCy, NLTK, Bigrams, Sentiment Analysis, Named Entity Recognition (NER), Custom Dictionaries, Word Clouds",
        "Databases": "SQL (MySQL), NoSQL (MongoDB basics)",
        "Artificial Intelligence & Deep Learning": "Neural Networks, LSTM, Time Series Forecasting, Sentiment Analysis",
        "Mathematics & Statistics": "Probability, Statistics, Hypothesis Testing, Optimization for Analytics",
        "Soft Skills": "Stakeholder Communication, Cross-functional Collaboration, Team Leadership, Presentations, Mentoring & Training"
    }

    # Display skills as cards in multiple columns
    cols = st.columns(2)
    i = 0
    for title, content in skills.items():
        with cols[i % 2]:
            skill_card(title, content)
        i += 1

    st.write(" ")
    st.write(" ")
    st.write(" ")
    st.write("---")
    st.write("### Professional Experience")
    st.write("""

    **Data Science & Machine Learning Intern** | Sep 2020 – Dec 2020  
    **Zesty Beanz Technologies**, Trivandrum, India  
    - Completed a 4-month internship focused on the full data science lifecycle, honing skills in **data preprocessing**, **feature engineering**, and **model evaluation**.  
    - Participated in hands-on machine learning workshops, mastering both **foundational** and **advanced techniques**, which culminated in self-directed projects that demonstrated real-world problem-solving abilities.  
    - Developed a deep understanding of **supervised learning** and **data-driven insights** under the mentorship of experienced industry professionals, laying a strong foundation for future data science work.  

    **Junior Data Analyst (Part-Time)** | Oct 2019 – May 2020  
    **HiTech Spare Parts Centre**, Trivandrum, India  
    - Utilized **Power BI** for end-to-end **ETL processes**, data modeling, and building **interactive dashboards** to track key business metrics such as spare part sales, stock, and inventory levels.  
    - Conducted **inventory trend analysis** using Excel, providing crucial insights to support and optimize daily operations.  
    - Spearheaded training sessions on Excel and Power BI, empowering the team to leverage data for improved decision-making and operational efficiency.  

    **Computer Science Tutor** | Mar 2020 – Jul 2020  
    **Campuzon**, Trivandrum, India  
    - Taught **Python, SQL**, and core computer science concepts to over 100 undergraduate students, delivering hands-on, practical lessons.  
    - Led workshops and personalized support sessions, adapting teaching methods to diverse learning styles and ensuring a deeper understanding of programming fundamentals.  
    - Demonstrated leadership by managing a team of tutors, ensuring consistent teaching quality, and enhancing the department's ability to support student learning outcomes.  
    - Played a pivotal role in creating an engaging and collaborative learning environment, boosting student confidence in mastering programming languages and problem-solving techniques.
    """)



elif selected_page == "Contact":
    # Introduction line
    st.title("Contact Me")
    st.write("Feel free to reach out to me through any of the following platforms:")

    # Contact details
    st.write("""
    - **Phone**: +44 7824819279 
    - **Email**: nived2033@gmail.com 
    - **LinkedIn**: [linkedin.com/in/nivedraj](https://www.linkedin.com/in/nived-raj-2033da)
    """)

    

elif selected_page == "YouTube":
    # Custom CSS for tag-style words
    # Custom CSS for inline tag-style words
    st.markdown("""
        <style>
        .tag {
            display: inline-block;
            padding: 5px 10px;
            margin: 5px;
            background-color: #f0f0f5;
            border-radius: 6px;
            border: 1px solid #ccc;
            font-size: 14px;
            color: #333;
            font-weight: bold;
        }
        .tag-container {
            display: flex;
            flex-wrap: wrap;
            gap: 8px;
        }
        </style>
    """, unsafe_allow_html=True)

    # Project Description
    st.write("""
    # Real-Time YouTube Comment Sentiment Analytics Dashboard

    This interactive dashboard is designed for marketing, advertising, and development teams to gain real-time insights into audience reactions on YouTube. Whether it’s a new movie trailer or a game reveal, this tool delivers actionable data to help teams understand how audiences engage, what excites them, and where the key moments lie.

    ### Tools & Technologies
    """)

    # Display tags inline
    st.markdown("""
    <div class="tag-container">
        <div class="tag">Python</div>
        <div class="tag">Dash</div>
        <div class="tag">AWS (EC2)</div>
        <div class="tag">YouTube API</div>
        <div class="tag">Interactive Dashboard</div>
        <div class="tag">Friendly UI</div>
        <div class="tag">NLP</div>
        <div class="tag">NLTK</div>
        <div class="tag">Topic Extraction</div>
        <div class="tag">Sentiment Analysis</div>
        <div class="tag">Live API Integration</div>
        <div class="tag">Custom Algorithm</div>
        <div class="tag">Emoji Sentiment Extraction</div>
    </div>
    """, unsafe_allow_html=True)

    # Continue with Project Description
    st.write("""
    ### Project Overview
    The dashboard provides an intuitive interface for analyzing YouTube comments on videos, especially **trailers and reviews**. It allows users to search for a video by keyword and retrieve real-time comments. From there, the dashboard breaks down **audience sentiment**, **key discussion points**, and the most **engaging moments** of the video. This makes it especially useful for media and advertising teams who want to understand what resonates most with their target audience.

    ### Key Features

    #### 1. Interactive Time-Bucket Popularity Chart
    A unique feature that analyzes the most discussed 10-second intervals of a video. Each bar in the chart represents a time segment, and by clicking on it, users can dive into the most liked comments during that interval. This reveals what parts of the video generated the most discussion—whether it’s a dramatic reveal or a controversial moment.
    """)

    st.image("images/yt timebucket.png", caption="Popular Times segments of the video chart example", use_column_width=True)

    st.write("""
    #### 2. Custom Sentiment Analysis
    The backbone of the dashboard is a custom-built sentiment analyzer that avoids spams, off topic comments - and calcualtes sentiment scores per comment. It is then used to caclulate the overall sentiment score - giving weight to comments per likes which gives comments most people agree on, more say in the final sentment score. Using this, the positive to negative proportion is calculated - and the scores are shown in a doughnut chart - which also assign a verdict like **“High Hype”** or **“Mostly Negative”** to the video.  I also integrated **emoji sentiment extraction** becuase emojies these days carry a lot of important sentiment that users express, adding another layer of depth to understand nuanced audience reactions.
    """)

    st.image("images/yt sentiment.png", caption="Sentiment Scores and Verdict Example", use_column_width=True)

    st.write("""
    #### 3. Interactive Word Clouds
    These **NLP-based word clouds** break down the most common phrases used in comments with **positive**, **negative**, and **overall** sentiments. This allows users to quickly see recurring themes in the audience’s feedback. The result is a visual representation of the conversation happening around a video.

    #### 4. Bigram Topic Extraction
    Using advanced NLP techniques, I extracted the top 20 topics from the comments. Each topic is plotted in an interactive chart. When users click on a topic, they can view the most liked and replied comments discussing that theme. This provides deeper insight into what specific parts of the video audience members are reacting to the most.
    """)
    st.image("images/yt topics.png", caption="Popular Topics Chart Example", use_column_width=True)

    st.write("""
    ### Impact
    The dashboard gives marketing teams a clear view of how their content is performing and what audiences are buzzing about. By analyzing audience engagement in real time, companies can fine-tune their messaging, pinpoint popular segments, and gain insights into both positive and negative feedback.

    What’s more, the dashboard is not limited to YouTube. Its design is adaptable for other platforms like **Twitter** and **Instagram**, as well as industries beyond entertainment, including **product reviews**, **news events**, and **consumer feedback**.

    This project highlights my ability to blend **data science**, **NLP**, and **cloud computing** to build a scalable tool that transforms raw comments into meaningful insights. Stay tuned for more updates and screenshots!
    """)



elif selected_page == "Anonymization":
    # Custom CSS for tag-style words
    st.markdown("""
        <style>
        .tag {
            display: inline-block;
            padding: 5px 10px;
            margin: 5px;
            background-color: #f0f0f5;
            border-radius: 6px;
            border: 1px solid #ccc;
            font-size: 14px;
            color: #333;
            font-weight: bold;
        }
        .tag-container {
            display: flex;
            flex-wrap: wrap;
            gap: 8px;
        }
        </style>
    """, unsafe_allow_html=True)

    # Project Description
    st.write("""
    # Text Data Anonymization & Analysis for Healthcare Services in Scotland

    This project, conducted in partnership with the **Argyll & Bute Health and Social Care Partnership (NHS)**, focused on developing a highly secure and GDPR-compliant solution to anonymize unstructured Electronic Health Records (EHR) data. By ensuring **100% removal of Personally Identifiable Information (PII)**, the tool enabled safe data sharing for research without compromising the utility of the data.

    ### Tools & Technologies
    """)

    # Tools & Technologies Tags
    st.markdown("""
    <div class="tag-container">
        <div class="tag">Python</div>
        <div class="tag">spaCy</div>
        <div class="tag">Named-Entity Recognition (NER)</div>
        <div class="tag">Natural Language Processing (NLP)</div>
        <div class="tag">Application Development</div>
        <div class="tag">Text Analytics</div>
        <div class="tag">Regex</div>
        <div class="tag">Custom Algorithm</div>
        <div class="tag">GDPR Compliance</div>
        <div class="tag">Data Anonymization</div>
        <div class="tag">Executable Workflow</div>
    </div>
    """, unsafe_allow_html=True)

    # Continue with Project Description

    

    st.write("""
    ### Project Overview
    In response to the need for secure, anonymized health records that comply with **GDPR regulations**, this project developed a robust tool to anonymize data without compromising its utility for research. The solution anonymized data for over **10,000 individuals**, ensuring secure data sharing within the healthcare sector while providing flexibility for broader applications in other industries.
    """)
    st.markdown("""
    <iframe src="https://1drv.ms/p/c/b1cefbb29bc4dda5/IQQ7jcn1gTJOTrP2Ig5UYBypARWDeSgpVqDo8jWyVG06240?em=2&amp;wdAr=1.7777777777777777" width="800px" height="450px" frameborder="0">This is an embedded <a target="_blank" href="https://office.com">Microsoft Office</a> presentation, powered by <a target="_blank" href="https://office.com/webapps">Office</a>.</iframe>
    """, unsafe_allow_html=True)

    st.write("""
    ### Key Features

    #### 1. Hybrid Anonymization System
    This project introduced a **two-layer anonymization system** using **spaCy’s Named Entity Recognition (NER)** combined with a **custom dictionary-based filter**. This approach allowed the tool to tag and remove sensitive data like names, addresses, and other PII from unstructured text, while still maintaining context and ensuring the data remained useful for research purposes.

    #### 2. Complete PII Removal with Perfect Recall
    The algorithm achieved a **perfect recall (1.0)**, ensuring no personal data was left exposed. The **transparency** of the tool was a significant factor in its compliance with GDPR standards, making sure every step of the anonymization process was trackable and verifiable.

    #### 3. Secure Workflow for Low-Clearance Users
    A standout feature of the tool was its **secure workflow**. The tool was designed to be used by personnel with **lower security clearance**, such as IT engineers, without exposing them to sensitive information. The anonymization process was fully encapsulated, ensuring that intermediate results and final outputs could **never be traced back to any individual**. This design allowed safe operation and handling of the tool without risking PII exposure, even in environments where users did not have high-level data access.

    #### 4. Flexible, Adaptable Design
    The **layered architecture** of the tool makes it easily adaptable for use across various industries beyond healthcare. The flexibility in its design allows for the anonymization of different types of unstructured data, making it applicable in fields such as finance, legal, and social services.

    ### Impact
    The tool anonymized the records of over **10,000 individuals**, facilitating secure and compliant data sharing for healthcare research. This project not only achieved **distinction** but was also praised for its innovative design and potential applications in other sectors. It demonstrated how cutting-edge data anonymization techniques can be deployed in real-world settings to handle sensitive data responsibly and effectively.
    """)


elif selected_page == "Movie":
    # Custom CSS for tag-style words
    # Custom CSS for tag-style words
    st.markdown("""
        <style>
        .tag {
            display: inline-block;
            padding: 5px 10px;
            margin: 5px;
            background-color: #f0f0f5;
            border-radius: 6px;
            border: 1px solid #ccc;
            font-size: 14px;
            color: #333;
            font-weight: bold;
        }
        .tag-container {
            display: flex;
            flex-wrap: wrap;
            gap: 8px;
        }
        </style>
    """, unsafe_allow_html=True)

    # Project Description
    st.write("""
    # Boxoffice Revenue Prediction Interactive Web App

    """)

    st.markdown("""
    **Check out the Live App!** 👉 [Box Office Prediction Web App](https://boxofficeprediction.streamlit.app/)
    """)

    st.write("""
    This interactive web app allows users to predict the box office revenue of a movie based on various factors such as the director, cast, genre, and runtime. It also accounts for **inflation adjustments** and **trend analysis** to predict the gross revenue in **2024**, offering a realistic forecast based on historical data and future projections.

    ### Tools & Technologies
    """)

    


    # Tools & Technologies Tags
    st.markdown("""
    <div class="tag-container">
        <div class="tag">Python</div>
        <div class="tag">Streamlit</div>
        <div class="tag">AWS (EC2)</div>
        <div class="tag">XGBoost</div>
        <div class="tag">LightGBM</div>
        <div class="tag">KNN</div>
        <div class="tag">Cosine Similarity</div>
        <div class="tag">Feature Engineering</div>
        <div class="tag">Data Augmentation</div>
        <div class="tag">Sprse Matrix</div>
        <div class="tag">Trend Analysis</div>
    </div>
    """, unsafe_allow_html=True)

    # Continue with Project Description
    st.write("""
    ### Project Overview
    The web app offers a **user-friendly interface** where users can input various movie-related features (such as **director**, **actors**, **genre**, **certificate**, and **runtime**) and receive a prediction of the movie’s potential revenue. The model adjusts for **inflation** and uses **trend analysis** to project the **gross revenue in 2024**, making the predictions both realistic and forward-looking.

    ### Key Features

    #### 1. Creative Feature Engineering
    Handling **categorical features** such as directors and actors required advanced **feature engineering** and **data augmentation**. The model deals with **sparse matrices**, creating meaningful relationships between features like director-actor pairings and genre combinations, enriching the dataset to provide accurate predictions.

    #### 2. Algorithm Experiments and Custom KNN Approach
    Initially, I experimented with popular algorithms like **XGBoost** and **LightGBM**, but ultimately implemented a **custom KNN-based approach** using **cosine similarity**. This method compares new movies against similar ones, estimating expected revenue by analyzing factors like cast, genre, and runtime. The combination of traditional algorithms and custom modeling allowed for greater flexibility and accuracy in the predictions.

    #### 3. Inflation Adjustment and 2024 Trend Prediction
    The model adjusts the **historical gross revenue** figures to match the expected **2024 value**. By applying **inflation rates** and conducting **trend analysis** based on box office patterns, the predictions account for future changes in movie revenue dynamics. This ensures that users get a **realistic prediction** of how much a movie could gross in 2024, reflecting both past trends and projected future growth.

    #### 4. User-Friendly Deployment on Streamlit
    The entire model is deployed using **Streamlit**, providing a clean, interactive interface for users to input movie features and get real-time predictions. Hosted on **AWS EC2**, the app is scalable, ensuring fast and reliable performance.

    ### Impact
    This web app provides a fun and interactive way to explore the factors that contribute to a movie’s success at the box office. It accounts for both **inflation adjustments** and **2024 trend projections**, offering realistic and forward-looking predictions. The project highlights creative problem-solving through **feature engineering**, **custom algorithms**, and the ability to deploy a user-friendly **machine learning model**.
    """)



elif selected_page == "Fraud":
    # Custom CSS for tag-style words
    st.markdown("""
        <style>
        .tag {
            display: inline-block;
            padding: 5px 10px;
            margin: 5px;
            background-color: #f0f0f5;
            border-radius: 6px;
            border: 1px solid #ccc;
            font-size: 14px;
            color: #333;
            font-weight: bold;
        }
        .tag-container {
            display: flex;
            flex-wrap: wrap;
            gap: 8px;
        }
        </style>
    """, unsafe_allow_html=True)

    # Project Description
    st.write("""
    # Credit Card Fraud Detection

    This project focused on predicting fraudulent credit card transactions using an **imbalanced dataset**, where only **1.8%** of the transactions were flagged as fraud. By employing advanced machine learning techniques, the project successfully tackled the challenges of class imbalance, optimizing model performance to improve fraud detection for real-world financial systems.

    ### Tools & Technologies
    """)

    # Tools & Technologies Tags
    st.markdown("""
    <div class="tag-container">
        <div class="tag">Python</div>
        <div class="tag">XGBoost</div>
        <div class="tag">LightGBM</div>
        <div class="tag">Logistic Regression</div>
        <div class="tag">Random Forest</div>
        <div class="tag">SMOTE</div>
        <div class="tag">SMOTE-Tomek</div>
        <div class="tag">iForest</div>
        <div class="tag">GridSearchCV</div>
        <div class="tag">RandomizedSearchCV</div>
        <div class="tag">Isolation Forest</div>
        <div class="tag">Class Imbalance Techniques</div>
        <div class="tag">Outlier Detection</div>
        <div class="tag">PCA</div>
    </div>
    """, unsafe_allow_html=True)

    # Continue with Project Description
    st.write("""
    ### Project Overview
    The goal of this project was to build a model capable of accurately predicting **fraudulent transactions** from a highly **imbalanced dataset**, where fraud accounted for only **1.8%** of the transactions. The features were **anonymized** and reduced using **PCA**, adding an additional challenge to feature interpretation and model development.

    ### Key Features

    #### 1. Advanced Class Imbalance Handling
    Addressing class imbalance was a major challenge, given the highly skewed nature of the dataset. I applied **SMOTE** (Synthetic Minority Over-sampling Technique) and **SMOTE-Tomek** to oversample the minority class (fraud cases) and remove overlapping majority class data points. Additionally, **undersampling** was implemented to reduce the imbalance further, helping models learn more effectively. The combination of these techniques ensured a **balanced dataset**, leading to improved performance in fraud detection.

    #### 2. Model Optimization with GridSearchCV and RandomizedSearchCV
    The models were tuned extensively using **GridSearchCV** and **RandomizedSearchCV** to identify the best hyperparameters. I experimented with a variety of machine learning models, including **XGBoost**, **LightGBM**, **Logistic Regression**, and **Random Forest**, optimizing them for **recall** and **AUC-ROC**. Special attention was paid to model performance on the minority (fraud) class, ensuring that the models were not biased toward the majority class (non-fraud).

    #### 3. Isolation Forest for Outlier Detection
    To improve the quality of the training data, I implemented **Isolation Forest** (iForest), a powerful outlier detection method. The iForest technique identified and removed outliers, preventing them from skewing the model’s learning process. By removing noisy and irrelevant data points, the models were able to better generalize and detect true fraud cases.

    #### 4. Custom Similarity-Based Fraud Detection
    A custom **fraud proximity projection technique** was developed to further enhance detection. This method involved projecting fraud data points into a multidimensional space and assigning probabilities to new transactions based on their proximity to known fraud cases. The closer a new transaction was to past fraud transactions, the higher the probability of it being fraudulent. This novel approach boosted the accuracy of the predictions and helped detect previously unseen fraud patterns.

    ### Results
    The model achieved a **Kaggle score of 0.81**, demonstrating strong performance in detecting fraudulent transactions. This score represents a significant improvement over baseline models and highlights the effectiveness of the techniques applied, particularly in handling the highly imbalanced nature of the dataset.

    ### Impact
    Through this project, I gained **hands-on experience** with advanced **fraud detection techniques** and **class imbalance handling**, both of which are highly applicable in real-world financial systems. The project showcased my ability to work with **outlier detection**, **imbalanced datasets**, and various **machine learning algorithms**, providing valuable insights into how fraud detection models can be optimized and deployed at scale.
    """)


elif selected_page == "Spotify":
    # Custom CSS for tag-style words
    st.markdown("""
        <style>
        .tag {
            display: inline-block;
            padding: 5px 10px;
            margin: 5px;
            background-color: #f0f0f5;
            border-radius: 6px;
            border: 1px solid #ccc;
            font-size: 14px;
            color: #333;
            font-weight: bold;
        }
        .tag-container {
            display: flex;
            flex-wrap: wrap;
            gap: 8px;
        }
        </style>
    """, unsafe_allow_html=True)

    


    # Project Description
    st.write("""
    # Spotify Song Genre Prediction (Kaggle Competition – 2nd Place)
    """)

    st.markdown("""
    **Check out the Kaggle Competetion!** 👉 [Spotify Genre Prediction Leaderboard](https://www.kaggle.com/competitions/cs9856-spotify-classification-problem-2022/overview)
    """)

    st.write("""
    This project involved building a **genre prediction model** for Spotify songs using features such as the artist, release year, and various song attributes like energy, duration, and popularity. Competing in a **Kaggle competition**, I achieved **2nd place**, showcasing my ability to work with real-world data, optimize model performance, and deliver high accuracy in a competitive environment.

    ### Tools & Technologies
    """)

    # Tools & Technologies Tags
    st.markdown("""
    <div class="tag-container">
        <div class="tag">Python</div>
        <div class="tag">Scikit-Learn</div>
        <div class="tag">LinearSVC</div>
        <div class="tag">Logistic Regression</div>
        <div class="tag">Random Forest</div>
        <div class="tag">GridSearchCV</div>
        <div class="tag">Cross-Validation</div>
        <div class="tag">Feature Selection</div>
    </div>
    """, unsafe_allow_html=True)

    # Continue with Project Description
    st.write("""
    ### Project Overview
    The goal of this project was to accurately predict the **genre** of Spotify songs based on a variety of features, such as artist, song attributes, and popularity metrics. By employing multiple machine learning models and fine-tuning them, I managed to achieve a **Kaggle score of 0.68421**, placing **2nd** in the competition.
    """)

    st.image("images/Leaderboard Kaggle.png", caption="Kaggle Leaderboard", use_column_width=True)

    st.write("""
    ### Key Features

    #### 1. Algorithm Tuning with Linear SVC
    After testing several machine learning algorithms, including **Logistic Regression** and **Random Forest**, I found that **Linear SVC (Support Vector Classification)** outperformed more complex models in terms of accuracy. By carefully tuning the **hyperparameters** using **GridSearchCV**, I optimized the Linear SVC model to achieve the best possible accuracy on the dataset. This demonstrated that sometimes simpler models can outperform more intricate algorithms, especially on high-dimensional data like song attributes.

    #### 2. Cross-Validation & Feature Selection for Consistent Results
    To prevent overfitting and ensure that the model generalizes well, I implemented **cross-validation** techniques across multiple folds. This not only helped in evaluating the robustness of the model but also in fine-tuning its performance. Additionally, **feature selection** was applied to eliminate irrelevant or redundant features, leading to more efficient training and consistent results across the test set.

    #### 3. Model Comparison and Selection
    While experimenting with models, I found that **Linear SVC** consistently delivered the highest accuracy compared to **Logistic Regression** and **Random Forest**. By striking a balance between model complexity and performance, the Linear SVC model outperformed more complex algorithms like Random Forest, highlighting the importance of algorithm selection based on the dataset at hand.

    ### Results
    The final model achieved a **Kaggle score of 0.68421** with **Linear SVC**, securing **2nd place** in the competition. This score demonstrated the effectiveness of the model in classifying songs by genre and highlighted my ability to tune and optimize machine learning models to handle high-dimensional data.

    ### Impact
    This project emphasized the importance of **model tuning**, **feature engineering**, and **cross-validation** in achieving top-tier results. Placing **2nd** in a competitive Kaggle leaderboard further showcased my ability to apply machine learning techniques in a real-world context, optimizing performance and demonstrating mastery in model selection and evaluation.
    """)


elif selected_page == "Crypto":
    # Custom CSS for tag-style words
    st.markdown("""
        <style>
        .tag {
            display: inline-block;
            padding: 5px 10px;
            margin: 5px;
            background-color: #f0f0f5;
            border-radius: 6px;
            border: 1px solid #ccc;
            font-size: 14px;
            color: #333;
            font-weight: bold;
        }
        .tag-container {
            display: flex;
            flex-wrap: wrap;
            gap: 8px;
        }
        </style>
    """, unsafe_allow_html=True)

    # Project Description
    st.write("""
    # Cryptocurrency Price Prediction | Academic Competetion Project

    As the **team leader** of a group of five, I led the development of a model to predict cryptocurrency price movements based on both **financial data** and **sentiment analysis** from social media mentions. The project explored **traditional machine learning** and **deep learning** approaches to forecast price direction in the highly volatile cryptocurrency market.

    ### Tools & Technologies
    """)

    # Tools & Technologies Tags
    st.markdown("""
    <div class="tag-container">
        <div class="tag">Python</div>
        <div class="tag">Random Forest</div>
        <div class="tag">LSTM</div>
        <div class="tag">NLP</div>
        <div class="tag">Sentiment Analysis</div>
        <div class="tag">Financial Time Series</div>
        <div class="tag">Social Media Data</div>
    </div>
    """, unsafe_allow_html=True)

    


    # Continue with Project Description
    st.write("""
    ### Project Overview
    The goal of this project was to predict the **upward or downward movement** of cryptocurrency prices, specifically **Bitcoin**, using a combination of **financial time series data** and **social media sentiment analysis**. The project involved applying both traditional machine learning methods like **Random Forest** and advanced **deep learning** techniques like **LSTM** (Long Short-Term Memory), providing valuable insights into the challenges of forecasting highly volatile assets like cryptocurrencies.
    """)

    st.markdown("""
    <iframe src="https://1drv.ms/p/c/b1cefbb29bc4dda5/IQRG3RkutIScSZHVFF4cIIZcAXyQvwGYdNUAvBtNh1B0H4M?em=2&amp;wdAr=1.7777777777777777" width="800px" height="450px" frameborder="0">This is an embedded <a target="_blank" href="https://office.com">Microsoft Office</a> presentation, powered by <a target="_blank" href="https://office.com/webapps">Office</a>.</iframe>
    """, unsafe_allow_html=True)


    st.write("""
    ### Key Features

    #### 1. Movement Prediction with Random Forest
    We used a **Random Forest classifier** to predict whether the price of Bitcoin would go **up** or **down** based on engineered features. These features included the **percentage change** from the previous days, **trading volume**, and other financial metrics. The model was designed to identify patterns in the data that could indicate future price movements, providing a reliable baseline prediction method.

    #### 2. Sentiment Integration for Enhanced Accuracy
    Recognizing the impact of market sentiment on cryptocurrency prices, we incorporated **sentiment analysis** into our model. We analyzed **social media mentions** related to Bitcoin, extracting sentiment scores that reflected the overall mood of the market. By integrating these sentiment features into the model, we achieved a slight improvement in accuracy, demonstrating the influence of public opinion on short-term price movements.

    #### 3. Experimenting with LSTM for Time Series Prediction
    Given the time series nature of financial data, we also explored a **deep learning approach** using an **LSTM model**. This method used the **previous 100 days of historical data** to predict future prices. While the LSTM model showed promise, the inherent **volatility** of the cryptocurrency market limited its predictive accuracy. The experiment provided valuable insights into the challenges of applying deep learning to financial markets.

    #### 4. Leading the Team and Presentation Design
    As the team leader, I was responsible for **coordinating efforts** across the team and ensuring the timely completion of tasks. I also designed and delivered the **PowerPoint presentation**, which received the **highest grade** in the class. The clarity of the design and the structure of the presentation were specifically praised, demonstrating my ability to effectively communicate complex technical concepts.

    ### Impact
    This project not only strengthened my leadership and collaboration skills, but also gave me hands-on experience with **financial time series data**, **machine learning**, and **sentiment analysis**. The integration of **social media data** into a financial model was a key learning experience, highlighting the real-world impact of public sentiment on market movements. The project also provided valuable insights into the limitations and potential of **deep learning models** in the context of volatile markets like cryptocurrency.
    """)


elif selected_page == "Movie Rec":
    # Custom CSS for tag-style words
    st.markdown("""
        <style>
        .tag {
            display: inline-block;
            padding: 5px 10px;
            margin: 5px;
            background-color: #f0f0f5;
            border-radius: 6px;
            border: 1px solid #ccc;
            font-size: 14px;
            color: #333;
            font-weight: bold;
        }
        .tag-container {
            display: flex;
            flex-wrap: wrap;
            gap: 8px;
        }
        </style>
    """, unsafe_allow_html=True)

    # Project Description
    st.write("""
    # Recommender System Study on MovieLens Dataset

    In the age of streaming services, **recommender systems** have become essential for delivering personalized content. This project explored different types of recommendation engines, focusing on building and optimizing a **hybrid recommender system** using the **MovieLens dataset**. The system combined **content-based filtering** and **collaborative filtering**, ultimately scaling it with **Apache Spark** to handle large-scale data efficiently.

    ### Project Overview

    The project began by examining various **recommender system** approaches, including **content-based** and **collaborative filtering** models. After testing individual algorithms, I developed a **hybrid recommender system** that integrated **Content-Based KNN** and **Restricted Boltzmann Machines (RBM)** to deliver more accurate and personalized recommendations.

    ### Key Features

    #### 1. Hybrid Recommender System: Combining RBM & Content-Based KNN
    - **Content-Based KNN**: Utilized **Cosine Similarity** to measure the similarity between movies based on user preferences. This method allowed the system to recommend movies that share features with the ones a user has liked.
    
    - **Restricted Boltzmann Machines (RBM)**: Implemented **RBM** for collaborative filtering, enabling the system to predict user preferences based on patterns in user ratings and interactions.

    #### 2. Hybrid Approach
    The combination of **Content-Based KNN** and **RBM** harnessed the strengths of both methods—content-based filtering’s focus on movie attributes and collaborative filtering’s ability to learn from user behavior—resulting in more accurate recommendations.

    #### 3. Scaling with Apache Spark
    To handle larger datasets, I scaled the hybrid model using **Apache Spark**, which enabled the system to efficiently process and analyze the **20 million MovieLens dataset**. This ensured that recommendations were generated quickly, even with a massive amount of data.

    ### Evaluation Metrics and Results

    The hybrid system was evaluated using several metrics:
    - **Mean Absolute Error (MAE)** and **Root Mean Square Error (RMSE)** to assess prediction accuracy.
    - **Hit Rate** and **Cumulative Hit Rate** to determine how often the correct movie appeared in the top recommendations.
    - **Diversity** and **Coverage** to ensure varied and comprehensive recommendations.

    By combining **Content-Based KNN** and **RBM**, the system outperformed individual models, providing more accurate, diverse, and personalized recommendations. Additionally, **Apache Spark** improved scalability, allowing the model to process large datasets without compromising performance.

    ### Tools & Technologies
    """)

    # Tools & Technologies Tags
    st.markdown("""
    <div class="tag-container">
        <div class="tag">Python</div>
        <div class="tag">Apache Spark</div>
        <div class="tag">Content-based KNN</div>
        <div class="tag">Restricted Boltzmann Machine (RBM)</div>
        <div class="tag">Cosine Similarity</div>
        <div class="tag">Collaborative Filtering</div>
        <div class="tag">MovieLens Dataset</div>
        <div class="tag">Hybrid Models</div>
        <div class="tag">Evaluation Metrics</div>
    </div>
    """, unsafe_allow_html=True)

    # Continue with Project Description
    st.write("""
    ### Conclusion
    This project showcased the advantages of **hybrid recommender systems** in enhancing recommendation accuracy by combining multiple approaches. Scaling the model using **Apache Spark** demonstrated how big data processing can be leveraged to improve performance, making the system suitable for real-time, large-scale applications in the movie recommendation domain.
    """)


elif selected_page == "Glasgow":
    # Custom CSS for tag-style words
    st.markdown("""
        <style>
        .tag {
            display: inline-block;
            padding: 5px 10px;
            margin: 5px;
            background-color: #f0f0f5;
            border-radius: 6px;
            border: 1px solid #ccc;
            font-size: 14px;
            color: #333;
            font-weight: bold;
        }
        .tag-container {
            display: flex;
            flex-wrap: wrap;
            gap: 8px;
        }
        </style>
    """, unsafe_allow_html=True)

    # Project Description
    st.write("""
    # Real-Time View of Glasgow City Centre Busy-ness Using Data

    This project, developed in collaboration with **Glasgow City Council**, aimed to provide a real-time view of the city's busyness by utilizing data visualization techniques. I led a team of 4 in creating a **Real-Time Dashboard** that delivered actionable insights into the flow of people and activities across the city.

    ### Key Contributions

    - **Team Leadership**: I successfully led a **team of 4**, managing the project from planning to execution, ensuring all team members collaborated effectively to meet the client’s needs.
    
    - **Real-Time Dashboard Development**: We built a real-time dashboard using **Tableau** and **Python** to visualize city busyness data, allowing city officials to track and analyze busy areas in real time.

    - **Data Source Optimization**: I suggested improvements for existing data collection methods and proposed new data sources, providing **cost estimates** and timelines for implementation, helping the council optimize their data infrastructure.

    ### Tools & Technologies
    """)

    # Tools & Technologies Tags
    st.markdown("""
    <div class="tag-container">
        <div class="tag">Tableau</div>
        <div class="tag">Python</div>
        <div class="tag">Real-Time Data</div>
        <div class="tag">Geographical Data Visualization</div>
        <div class="tag">Data Source Optimization</div>
    </div>
    """, unsafe_allow_html=True)

    # Learning Outcomes
    st.write("""
    ### Learning Outcomes
    Through this project, I gained valuable experience in:
    - **Visualizing geographical data** effectively, using tools like Tableau to represent real-time data in a meaningful way.
    - **Working with real-time data**, ensuring that the dashboard accurately reflected the city’s busyness as events unfolded.
    - **Client collaboration** and how to optimize data sources for real-time analytics.
    """)


elif selected_page == "Alcohol":
    # Custom CSS for tag-style words
    st.markdown("""
        <style>
        .tag {
            display: inline-block;
            padding: 5px 10px;
            margin: 5px;
            background-color: #f0f0f5;
            border-radius: 6px;
            border: 1px solid #ccc;
            font-size: 14px;
            color: #333;
            font-weight: bold;
        }
        .tag-container {
            display: flex;
            flex-wrap: wrap;
            gap: 8px;
        }
        </style>
    """, unsafe_allow_html=True)

    # Project Description
    st.write("""
    # An Analysis of Alcohol-Related Callouts' Burden on Ambulance Waiting Times

    In collaboration with **Ernst & Young** and the **NHS**, I conducted an analysis of the impact that alcohol-related callouts have on the **Scottish Ambulance Service**. The project aimed to identify bottlenecks in ambulance waiting times caused by these incidents and offer actionable recommendations to alleviate the burden.

    ### Key Contributions

    - **Data Analysis**: Analyzed the **Scottish Ambulance Service data**, focusing on the impact of alcohol-related callouts and how they affect **ambulance waiting times**.
    
    - **Time-Based Insights**: Presented the **temporal distribution** of these callouts, showing how **time of day** and **day of the week** affect the frequency and strain on ambulance services. This provided a clearer picture of peak times and allowed for targeted recommendations.

    - **Sober Centre Recommendations**: Proposed the introduction of **sober centers** to handle alcohol-related cases, estimating the potential improvement in ambulance waiting times. This included **cost estimates** for setting up these centers and recommendations for **staff allocation**.

    - **Geographical Analysis**: Identified areas in **Glasgow** with the highest rate of alcohol-related callouts, recommending optimal locations for the sober centers. The analysis highlighted key zones where these centers would have the most impact on reducing ambulance waiting times.

    ### Tools & Technologies
    """)

    # Tools & Technologies Tags
    st.markdown("""
    <div class="tag-container">
        <div class="tag">Python</div>
        <div class="tag">Tableau</div>
        <div class="tag">Geographical Data Analysis</div>
        <div class="tag">Cost Analysis</div>
        <div class="tag">Scottish Ambulance Service Data</div>
    </div>
    """, unsafe_allow_html=True)

    # Continue with Project Description
    st.write("""
    ### Impact
    The analysis revealed key patterns in alcohol-related callouts, highlighting their significant impact on **ambulance response times**. By proposing **sober centers** and identifying the best locations for them, the project offered **realistic solutions** to improve emergency response efficiency in Glasgow. The insights provided can inform **policy decisions** aimed at improving public health services.
    """)


elif selected_page == "SyncOrg":
    # Custom CSS for tag-style words
    st.markdown("""
        <style>
        .tag {
            display: inline-block;
            padding: 5px 10px;
            margin: 5px;
            background-color: #f0f0f5;
            border-radius: 6px;
            border: 1px solid #ccc;
            font-size: 14px;
            color: #333;
            font-weight: bold;
        }
        .tag-container {
            display: flex;
            flex-wrap: wrap;
            gap: 8px;
        }
        </style>
    """, unsafe_allow_html=True)

    # Project Description
    st.write("""
    # Data Management & Workflow Optimization for SyncOrg

    This project involved designing an efficient **data management framework** for **SyncOrg**, a company that gathered customer data from various sources and in different formats. My role was to analyze current workflows, recommend improvements, and propose a centralized system to manage customer data effectively.

    ### Key Contributions

    - **CRM Software Analysis**: Conducted a thorough analysis of various **Customer Relationship Management (CRM)** tools available on the market, evaluating them based on SyncOrg's specific requirements. Recommended the best CRM solution that could integrate with their existing processes and systems.

    - **Framework Proposal**: Designed a comprehensive data management framework where customer data would be:
    1. **Gathered** from multiple sources,
    2. **Validated** to ensure data quality,
    3. **Converted** into a desirable format, and
    4. **Stored** in a **centralized database**, with automation built in to handle the process seamlessly.

    - **Workflow Optimization**: Suggested workflow optimizations that would reduce manual data handling and ensure that data from different departments flowed smoothly into a **single system**.

    ### Tools & Technologies
    """)

    # Tools & Technologies Tags
    st.markdown("""
    <div class="tag-container">
        <div class="tag">Python</div>
        <div class="tag">Data Management</div>
        <div class="tag">CRM Analysis</div>
        <div class="tag">Workflow Optimization</div>
        <div class="tag">Automation</div>
    </div>
    """, unsafe_allow_html=True)

    # Continue with Project Description
    st.write("""
    ### Impact
    The proposed framework streamlined SyncOrg’s **customer data management** process, reducing redundancy and manual effort while improving data quality and accessibility. The recommendation for a new CRM system helped the company move towards a more **centralized** and **efficient data management system**, enhancing overall customer relationship management and workflow efficiency.
    """)

