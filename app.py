import openai
import streamlit as st

# Page config
st.set_page_config(page_title="Crongen - Shritam")

st.title("Crongen")
st.header("**An AI app to generate crontab rules**")

# OpenAI API key (store it securely, e.g., as an environment variable)
openai.api_key = "YOUR_OPENAI_API_KEY"

# Define GPT-3 function
def gpt3(prompt, engine='davinci', response_length=0,
         temperature=0, top_p=0, frequency_penalty=0, presence_penalty=0,
         start_text='', restart_text='', stop_seq=[]):
    response = openai.Completion.create(
        prompt=prompt + start_text,
        engine=engine,
        max_tokens=response_length,
        temperature=temperature,
        top_p=top_p,
        frequency_penalty=frequency_penalty,
        presence_penalty=presence_penalty,
        stop=stop_seq,
    )
    answer = response.choices[0]['text']
    new_prompt = prompt + start_text + answer + restart_text
    return answer, new_prompt


prompt="""English: each day
GPT: 0 0 * * *
English: every day
GPT: 0 0 * * *
English: daily
GPT: 0 0 * * *
English: every day at 3 AM
GPT: 0 3 * * *
English: 5am
GPT: 0 5 * * *
English: daily at 5am
GPT: 0 5 * * *
English: every friday at 5am
GPT: 0 5 * * 5
English: daily at 17:30
GPT: 30 17 * * *
English: every week
GPT: 0 0 * * 0
English: weekly
GPT: 0 0 * * 0
English: every minute
GPT: * * * * *
English: every 5 minutes
GPT: */5 * * * *
English: every 30 minutes
GPT: */30 * * * *
English: every month
GPT: 0 0 1 * *
English: monthly
GPT: 0 0 1 * *
English: every Monday
GPT: 0 0 * * 1
English: every Wednesday
GPT: 0 0 * * 3
English: every Friday
GPT: 0 0 * * 5
English: every hour
GPT: 0 * * * *
English: every 6 hours
GPT: 0 */6 * * *
English: hourly
GPT: 0 * * * *
English: every year
GPT: 0 0 1 1 *
English: yearly
GPT: 0 0 1 1 *
English: annually
GPT: 0 0 1 1 *
English: every day at 9am
GPT: 0 9 * * *
English: every day at 5pm
GPT: 0 17 * * *
English: every day at 5:45pm
GPT: 45 17 * * *
English: every day at 17:00
GPT: 0 17 * * *
English: every day at 17:25
GPT: 25 17 * * *
English: 5:15am every Tuesday
GPT: 15 5 * * 2
English: 7pm every Thursday
GPT: 0 19 * * 4
English: every May
GPT: 0 0 1 5 *
English: every December
GPT: 0 0 1 12 *
English: midnight
GPT: 0 0 * * *
English: midnight on tuesdays
GPT: 0 0 * * 2
English: every 5 minutes on Tuesdays
GPT: */5 * * * 2
English: noon
GPT: 0 12 * * *
English: every 25th
GPT: 0 0 25 * *
English: every 3rd of January
GPT: 0 0 3 1 *
English: every day at 9AM from 24 to 28
GPT: 0 9 24-28 * *
English: At 09:00 AM, between day 24 and 28 of the month, only in May
GPT: 0 9 24-28 5 *
English: 5:30 PM between 12 and 28 of this month
GPT: 30 17 12-28 * *
English: Everyday between 19 to 23 at 9 AM only in June
GPT: 0 9 19-23 6 *
English: at 17:30 on the 30th of May
GPT: 30 17 30 5 *
English: on Sunday at 9:30 PM
GPT: 0 21 * * 0
English: on every Sunday at 9:30 PM
GPT: 0 21 * * 0
English: """

# Streamlit form
try:
    form_1 = st.form(key='my-form1')
    command = form_1.text_input("Enter Command:")
    submit = form_1.form_submit_button('Submit')

    if submit:
        st.info("Generating crontab rule...")  # Feedback to the user
        prompt += command  # Insert the input textarea's text
        answer, prompt = gpt3(prompt, response_length=64,
                              temperature=0.58,
                              start_text='\nGPT:',
                              restart_text='\n\nEnglish:',
                              stop_seq=['\n\nEnglish:', '\n'])
        st.header(f"**Result:**")
        st.write(f"**{answer}**")
        command = ""  # Clear input after submission
except Exception as e:
    st.error(f'Something Went Wrong! 😁 {e}')

# Footer
footer = """
<style>
a:link , a:visited{
color: blue;
background-color: transparent;
text-decoration: underline;
}

a:hover,  a:active {
color: red;
background-color: transparent;
text-decoration: underline;
}

.footer {
position: fixed;
left: 0;
bottom: 0;
width: 100%;
background-color: white;
color: black;
text-align: center;
}
</style>
<div class="footer">
<p>Developed with ❤ </p>
</div>
"""
st.markdown(footer, unsafe_allow_html=True)

# Remove Streamlit hamburger menu
hide_streamlit_style = """
<style>
#MainMenu {visibility: hidden;}
footer {visibility: hidden;}
</style>
"""
st.markdown(hide_streamlit_style, unsafe_allow_html=True)
