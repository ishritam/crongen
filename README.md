# Crongen

Crongen is an AI app to generate crontab rules from raw sentences built using OpenAI and Streamlit.
![crongen](https://user-images.githubusercontent.com/40149802/119294593-75962580-bc72-11eb-980b-6f39f9e52d3c.gif)


## Project structure:
------------

    .
    ├── app.py                      > Main file which contains all the functionality to run the APP
    ├── Procfile                    > Enviornment Procfile for Heroku app deployement 
    ├── README.md                   > The top-level README for developers using this project.
    ├── requirements.txt            > All the requirements which is needed to run this project.
    ├── setup.sh                    > Setup file to run streamlit app on Heroku environment. 

        


--------
## Testing:

  - This can run on Windows / Linux(Ubuntu 20.04) system.
  - It is advised to create a virtual enviornment if you have existing conflicts with python & other libraries/packages installtions.

## Quickstart:

  - Make sure that you have Python 3.6 - Python 3.8 installed.
  - Install all necessary dependencies for this project from requirements.txt
    - Run `pip install -r requirements.txt` for installing dependencies. 
 - Run app.py file in for turn on the APP.
    - Run `streamlit run app.py`
  - A new tab will open in your default browser with port 8501.

## Insights:
* WebApp: https://crongen-gpt3.herokuapp.com/
* Blog: https://shritam.medium.com/how-to-create-an-ai-app-to-generate-crontabs-using-openai-and-streamlit-23aacbf20a9c

