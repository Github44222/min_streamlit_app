import streamlit as st

# 1
st.title("Min Dagbok.")
st.text_area("Dokumentera i dagboksinlägget här.:")
if st.button("Spara alla inlägg."):

    if "st.title":
        st.success("Ditt inlägg har nu sparats.")
    else:
        st.error("Ditt inlägg har inte sparats än, skriv något.")


st.subheader("Tidigare Inlägg.")
st.write("Inga tidigare inlägg finns tillgängliga.")


# 2
st.title("Humör för dagen.")
st.selectbox('Humör',['Glad', 'Ledsen', 'Arg'])
st.text_area('Förklara varför du känner dig så idag')
if 'st.title':
    st.success("Ditt inlägg har sparats.")
else:
    st.error("Ditt inlägg har inte sparats, skriv något.")


# 3
st.title('Olika taggar inom området.')
st.multiselect('Taggar',['Skola', 'IT', 'Nätverk', 'Datorer', 'Hårdvara','Inlägg'])
st.text_area('Förklara ytterligare varför dessa taggar tillhör inom ditt område.')
if "st.title":
    st.success("Ditt inlägg har sparats.")
else:
    st.error("Ditt inlägg har inte sparats, skriv något.")


# 4
st.title("Välj vecka, dag och tid.")
st.selectbox('week_num',['41','42','43','44','45','46','47','48'])
st.selectbox('day_num',['måndag','tisdag','onsdag','torsdag','fredag'])
st.selectbox('time_num',['9:00-11:00','11:00-14:00'])
st.text_area('Förklara med korta ord vad du gjorde varje vecka, inom dagen, vid dessa tider.')
if 'st.title':
    st.success("Ditt inlägg har sparats.")
else:
    st.error("Ditt inlägg har inte sparats, skriv något.")
