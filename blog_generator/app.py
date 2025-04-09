import streamlit as st
import google.generativeai as genai
from openai import OpenAI
from apikey import google_gemini_api_key,openai_api_key

client = OpenAI(api_key=openai_api_key)

genai.configure(api_key=google_gemini_api_key)

generation_config = {
    "temperature":0.9,
    "top_p":1,
    "top_k":1,
    "max_output_tokens":2048
}

safety_settings = [
    {
        "category": "HARM_CATEGORY_HARASSMENT",
        "threshold": "BLOCK_MEDIUM_AND_ABOVE"
    },
    {
        "category": "HARM_CATEGORY_HATE_SPEECH",
        "threshold": "BLOCK_MEDIUM_AND_ABOVE"
    },
    {
        "category": "HARM_CATEGORY_SEXUALLY_EXPLICIT",
        "threshold": "BLOCK_MEDIUM_AND_ABOVE"
    },
    {
        "category": "HARM_CATEGORY_DANGEROUS_CONTENT",
        "threshold": "BLOCK_MEDIUM_AND_ABOVE"
    }
]

#setting up our model
model = genai.GenerativeModel(
    model_name = "gemini-2.0-flash-exp",
    generation_config=generation_config,
    safety_settings=safety_settings
)


st.set_page_config(layout="wide")

#title of our app
st.title("BlogCraft: Your AI writing companion")

#create a subheader
st.subheader("Now you can craft perfect blogs with the help of AI- BlogCraft is your new AI Blog Companion")

#sidebar for user input
with st.sidebar:
    st.title("Input your blog details")
    st.subheader("Enter details of the blog you generate")

    #Blog Title
    blog_title = st.text_input("Blog Title")

    #keywords input
    keywords = st.text_area("Keywords (comma separated)")

    #Number of words
    num_words = st.slider("Number of Words", min_value=250, max_value=1000, step=100)

    #Number of images
    num_images = st.number_input("Number of Images", min_value=1, max_value=5,step=1)

    prompt_parts = [
        f"Generate a comprehensive, engaging blog post relevant to the given title \"{blog_title}\" and keywords \"{keywords}\" with number of words \"{num_words}\""
    ]



    #Submit button
    submit_button = st.button("Generate Blog")


if submit_button:

    images = []
    for i in range(num_images):
        image_response = client.images.generate(
            model="dall-e-3",
            prompt=f"Generate a Blog Post Image on the title {blog_title}",
            size="1024x1024",
            quality="standard",
            n=1
        )

        images.append(image_response.data[0].url)


    response = model.generate_content(prompt_parts)

    for i in range(num_images):
        st.image(images[i], caption="Generated Image")

    st.title("Your Blog Post")

    st.write(response.text)