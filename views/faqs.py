import streamlit as st

# Page configuration options
page_title = "FAQs"
page_icon = "💬"
st.set_page_config(page_title=page_title, page_icon=page_icon, layout="wide", initial_sidebar_state="expanded")

st.title('FAQs')

expand_all = st.toggle("Expand all", value=False)

model_comparison = """
    <table>
        <thead>
            <tr>
                <th>Feature</th>
                <th>Stable Diffusion 2.1</th>
                <th>Stable Diffusion 3.5 Large</th>
            </tr>
        </thead>
        <tbody>
            <tr>
                <td><b>Image Quality</td>
                <td>High</td>
                <td>Superior (more realistic & detailed</td>
            </tr>
            <tr>
                <td><b>Prompt Understanding</td>
                <td>Good</td>
                <td>Excellent</td>
            </tr>
            <tr>
                <td><b>Model Size</td>
                <td>Smaller</td>
                <td>Larger</td>
            </tr>
                <tr>
                <td><b>Performance</td>
                <td>Faster, less resource-intensive</td>
                <td>Resource-intensive, higher quality</td>
            </tr>
                <tr>
                <td><b>Use Case</td>
                <td>Broad general-purpose applications</td>
                <td>Demanding, high-fidelity tasks</td>
            </tr>
                <tr>
                <td><b>Computational Needs</td>
                <td>Mid-range GPUs</td>
                <td>High-end GPUs or cloud platforms</td>
            </tr>
        </tbody>
    </table>
"""


faq_data = {
        'What this Application is about?': '<p>An innovative web app that transforms your text descriptions into breathtaking AI-generated images.</p>',

        'Which AI models are used to generate images?': '<p>This application supports the following models to generate high quality images: \
            <ul>\
                <li>stable-diffusion-2-1</li> \
                <li>stable-diffusion-3.5-large</li>\
                    </ul></p>',

        'What is the difference b/w these two models?': model_comparison,

        'Can I get the application source code?': '<p>Yes, Source code of this application is available at: <a href="https://github.com/mzeeshanaltaf/">GitHub</a></p>',

    }

# Display expandable boxes for each question-answer pair
for question, answer in faq_data.items():
    with st.expander(r"$\textbf{\textsf{" + question + r"}}$", expanded=expand_all):  # Use LaTeX for bold label
        st.markdown(f'<div style="text-align: justify;"> {answer} </div>', unsafe_allow_html=True)