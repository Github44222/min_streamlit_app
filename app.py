import streamlit as st
import boto3
from boto3.dynamodb.conditions import Attr

AWS_REGION = "us-east-1"
dynamodb = boto3.resource("dynamodb", region_name=AWS_REGION)
table = dynamodb.Table("Spara")

def SpararData(innehåll, titel, vecka_num, dag, tid_stampel):
    table.put_item(
        Item={
            'innehåll': innehåll,
            'titel': titel,
            'vecka_num': vecka_num,
            'dag': dag,
            'tid_stampel': tid_stampel
        }
    )

def SpararSeletions(vecka_num, dag, tid_stampel):
    try:
        response = table.scan(
            FilterExpression=Attr('vecka_num').eq(vecka_num) &
            Attr('dag').eq(dag) &
            Attr('tid_stampel').eq(tid_stampel)
        )
        return response['Items']
    except Exception as e:
        st.error(f"Error scanning table: {e}")
        return []

st.title("Min Dagbok.")
titel = st.text_input("Lägg in en titel")
innehåll = st.text_area("Dokumentera i dagboksinlägget här")
spara = st.button("Spara inlägg.")

st.title("Välj vecka, dag och tid.")

vecka_num = st.selectbox('Vecka', ['41', '42', '43', '44', '45', '46', '47', '48'])
dag = st.selectbox('Dag', ['måndag', 'tisdag', 'onsdag', 'torsdag', 'fredag'])
tid_stampel = st.selectbox('Tid', ['9:00-11:00', '11:00-14:00'])

items = SpararSeletions(vecka_num, dag, tid_stampel)

if spara:
    if not titel or not innehåll:
        st.error("Lägg in en titel och skriv något.")
    else:
        SpararData(innehåll, titel, vecka_num, dag, tid_stampel)
        st.success("Ditt inlägg har nu sparats.")

if not items:
    st.info("Inga sparade dokument hittades för denna vecka.")
    
else:
    for item in items:
        st.write(f"**Titel:** {item['titel']}")
        st.write("------------------------------")
        st.write(f"**Innehåll:** {item['innehåll']}")
        st.write("------------------------------")
        st.write(f"**Vecka:** {item['vecka_num']}")
        st.write("------------------------------")
        st.write(f"**Dag:** {item['dag']}")
        st.write("------------------------------")
        st.write(f"**Tid:** {item['tid_stampel']}")
        st.write("------------------------------")
