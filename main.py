import pandas as pd
import streamlit as st
import home,attendence_list,faces
from streamlit_option_menu import option_menu

with st.sidebar:
    selection = option_menu(
        menu_title="Navigation Pane", 
        options=['Home', 'Attendence List', 'Faces Detected'],
        icons=["house","database","bar-chart-line"],
        menu_icon="cast",
        default_index=0)


if selection == 'Home':
    home.app()

elif selection == 'Attendence List':
    st.title('Attendence List')
    attendence_list.app()
     
elif selection == 'Faces Detected':
    st.title('Faces Detected')
    faces.app()



