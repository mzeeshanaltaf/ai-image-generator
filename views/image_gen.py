import streamlit as st
from PIL import Image
import io
import torch
from diffusers import  StableDiffusion3Pipeline, StableDiffusionPipeline, DPMSolverMultistepScheduler
from util import *

# Page Configuration
page_title = "Text to Image Generator"
page_icon = "🖼️"
st.set_page_config(page_title=page_title, page_icon=page_icon, layout="wide")

# Title and description of application
st.title(f"{page_title} {page_icon}")
st.write(":blue[***Turn Words into Stunning Visuals Instantly!***]")
st.write("""An innovative web app that transforms your text descriptions into 
         breathtaking AI-generated images. Unleash your creativity and see your imagination come to life!""")

# Model Selection
st.subheader('Model Selection', divider='gray', help='View FAQs page to know the difference between these models')
options = ["stable-diffusion-2-1", "stable-diffusion-3.5-large"]
selection = st.pills("Model", options, selection_mode="single", default='stable-diffusion-2-1', label_visibility='collapsed')
model = f"stabilityai/{selection}"

# User prompt
st.subheader('Prompt', divider='gray', help='Either select from pre-defined prompt or enter your own prompt')
prompt_predefined = st.selectbox('Select from Pre-Defined Prompts:', pre_defined_prompts, index=None)
st.write('***OR***') 
prompt_user = st.text_area('Enter Your Own Prompt:', 
                       placeholder="Enter a detailed description of the image you want to create (e.g., 'A serene sunset over a mountain lake with pine trees')", 
                       label_visibility='visible', disabled=not (not prompt_predefined))
prompt = prompt_predefined if prompt_predefined else prompt_user

submit = st.button('Submit', type='primary', disabled=not prompt)

# Generate Image if button is clicked
if submit:
    with st.spinner('Generating Image ...'):
        
        if selection == 'stable-diffusion-2-1':
            pipe = StableDiffusionPipeline.from_pretrained(model, torch_dtype=torch.bfloat16)
            pipe.scheduler = DPMSolverMultistepScheduler.from_config(pipe.scheduler.config)


        elif selection == 'stable-diffusion-3.5-large':
            pipe = StableDiffusion3Pipeline.from_pretrained(model, torch_dtype=torch.bfloat16)
       
        pipe.enable_attention_slicing()
        pipe = pipe.to("cuda")
        result = pipe(prompt, num_inference_steps=100, guidance_scale=3.5, height=512, width=512)
        st.toast('Image Generated Successfully!', icon='🖼️')
        
        # Display the image in Streamlit
        st.subheader('Generated Image:', divider='gray')
        st.image(result.images[0], caption="An AI Generated Image", use_container_width=True)
