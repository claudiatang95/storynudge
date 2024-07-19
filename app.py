import streamlit as st
import requests
import json


st.title("Welcome!")
st.write("This quiz lasts a couple of minutes, is completely anonymous but will allow us to make the blogging service more accurate.")

gender = st.selectbox(
    "What's your gender?",
    ("Male", "Female", "Other"))

st.selectbox(
    "In which region of Italy do you live?",
    ("North East", "North West", "Center","South","Islands"))

age = st.selectbox(
    "How old are you?",
    ("Less than 18","Between 18 and 34","Between 35 and 45","Between 46 and 65","More than 65")
)

profession = st.selectbox(
    "What type of profession do you have?",
    ("Employee"," Self-employed","Retired","Other")
)

goal = st.multiselect(
    "What's your major financial goal(s)?",
    ["saving for retirement","saving for a house","saving for children's education","other"]
)

if "other" in goal:
    goal_other = st.text_input("Please indicate your goal")
    goal.remove("other")
else:
    goal_other = ""

goal_str = ",".join(goal)
if len(goal_other)>0:
    goal_str = goal_str + "," + goal_other


button = st.button("submit")

if button:
    st.subheader("Please read the following message and make your choice")
    # propmt_userinfo = "Write me a story based on following information: Gender: male, age group: 45-65, type of profession: employee, major financial goal: saving for retirement"
    propmt_userinfo = f'Write me a story based on following information: Gender: {gender},age group: {age},type of profession: {profession},major financial goal: {goal_str}'
    print(propmt_userinfo)


# request API
endpoint_url = ''  # url of model on Azure
api_key = ''      

headers = {
    "Content-Type": "application/json",
    "Authorization": f"Bearer {api_key}",
    'azureml-model-deployment': 'Phi-3-mini-4k-instruct-ouddk'
}

propmt_background = "You are an online financial literacy blog editor. Your website focuses on personal finance, education on topics such as how to balance savings and investments.Your goal is to nudge people to seek further information on investment.\
Now your task is to write stories on people's personal financial situations, identify their potential problems and which appropriate investment can address the problems and help them meet their financial goals. You should imitate the following story.\
Example story:\
Luigi is 61 years old and his life still revolves around work – a window and door company that he built from scratch with hard work and enormous sacrifices. A job that has always taken up a lot of his time, even when, after becoming a widower, he had to manage two teenage children on his own.\
For a few years now, he has had a new partner who lives with him. He has no health problems and still feels young. He has never activated insurance coverage, although he has set up a pension fund, even though the contributions he has made are not sufficient to guarantee him a pension that meets his expectations.\
In the past two years, he has become a grandfather to two grandchildren. Luigi is beginning to feel the passage of time and would like to have more time to spend with the little ones or even travel a bit. But he doesn't know where to start. So, he goes to speak with a financial advisor.\
The advisor talks about the risk of longevity, showing Luigi some somewhat harsh but objective statistics on the incidence of age-related diseases and the costs associated with them. In the end, Luigi is convinced of the importance of increasing his contributions to his pension fund and also of subscribing to an investment product called income, which is capable of generating supplementary income, allowing him to peacefully enjoy his well-deserved relaxation with his new partner and family.\
Now write a personalized story with 200 words based on the information provided by the user. Remember the user lives in Italy and so the investment you suggest should be available in Italy. "



if button:
    input_data = {
        "messages":[
            {
            "role":"user",
            "content":propmt_background
            },
            {
             "role":"user",
             "content": propmt_userinfo
            }
        ],
            "max_tokens":500
}
    input_json = str.encode(json.dumps(input_data))
    response = requests.post(endpoint_url, headers=headers, data=input_json)
    if response.status_code == 200:
    # Parse and print the response
      result = response.json()
      text = result['choices'][0]['message']['content']
      st.write(text)
      st.selectbox("Do you want to know more information about the investment?",["Yes","No",""], index=2)
    else:
       print(f"Request failed with status code {response.status_code}")
       print(response.text)
       st.write("Oops, something is wrong, please retry")

