#import necessary modules

import streamlit as st
from pathlib import Path
import google.generativeai as genai
from api_key import api_key

# configure genai with api_key
genai.configure(api_key=api_key)

#setup the model
generation_config = {
    "temperature": 0.4,
    "top_p": 1,
    "top_k": 32,
    "max_output_tokens": 4096
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

system_prompt = """
As a highly skilled medical practitioner specializing in image analysis, you are tasked with medical images from a hospital.
Your expertize is crucial in indentifying any anomalies, diseases or health issues that may be present in the images.

Your responsibilities include

1. Detailed Analysis: Thoroughly analyze each image, focusing on identifying any abnormal findings.
2. Findings Report: Document all observed anomalies or signs of disease. 
3. Recommendations and Next Steps: Based on your analysis, suggest potential next steps
4. Treatment Suggestions: If appropriate, recommend possible treatment options or interventions

Important Points:
1. Scope of response: Only respond if the image pertains to human health issues.
2. Clarity of Image: In cases where the image quality impedes clear analysis, respond 'Please upload good quality image'
3. Disclaimer: Accompany your analysis with the disclaimer: "Consult a doctor before making decisions"


Please provide the output response with these 4 headings Detailed Analysis, Findings Report, Recommendations and Next Steps,Treatment Suggestions

"""

#setting up our model
model = genai.GenerativeModel(
    model_name = "gemini-2.0-flash-exp",
    generation_config=generation_config,
    safety_settings=safety_settings
)



# set the page config
st.set_page_config(page_title="VitalImage Analysis", page_icon=":robot:")

# set title
st.title("Vital Image Analytics")

# set the subtitle
st.subheader("An application that can help users to identify medical images")

uploaded_file = st.file_uploader("Upload the medical image for analysis", type = ["png", "jpg", "jpeg"])

submit_btn = st.button("Generate the analysis")

if submit_btn:
    image_data = uploaded_file.getvalue()

    #making our image ready
    image_parts = [
        {
            "mime_type": "image/jpeg",
            "data": image_data
        }
    ]

    #making our prompt ready
    prompt_parts = [
        image_parts[0],
        system_prompt
    ]

    response = model.generate_content(prompt_parts)
    st.write(response.text)