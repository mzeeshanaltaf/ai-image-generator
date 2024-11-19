# Import libraries
import streamlit as st

# --- PAGE SETUP ---
main_page = st.Page(
    "views/image_gen.py",
    title="AI Image Generator",
    icon=":material/image:",
    default=True,
)

faq_page = st.Page(
    "views/faqs.py",
    title="FAQs",
    icon=":material/help:",
)


contact_us = st.Page(
    "views/contact.py",
    title="Contact Us",
    icon=":material/contact_page:",
)

pg = st.navigation({
    "Home": [main_page],
    "FAQs": [faq_page],
    "Contact Us": [contact_us],
                    })

pg.run()