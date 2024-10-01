import paho.mqtt.client as paho
import time
import streamlit as st
import json

act1 = "OFF"

def on_publish(client, userdata, result):
    print("el dato ha sido publicado \n")
    pass

def on_message(client, userdata, message):
    global message_received
    time.sleep(2)
    message_received = str(message.payload.decode("utf-8"))
    st.write(message_received)

broker = "broker.mqttdashboard.com"
port = 1883
client1 = paho.Client("GIT-HUB")
client1.on_message = on_message

st.title("MQTT Control")

if st.button('ON'):
    act1 = "ON"
    client1 = paho.Client("CLIENTE_CAMILA")
    client1.on_publish = on_publish
    client1.connect(broker, port)
    message = json.dumps({"Act1": act1})
    ret = client1.publish("topico2", message)
else:
    st.write('')

if st.button('OFF'):
    act1 = "OFF"
    client1 = paho.Client("CLIENTE_CAMILA")
    client1.on_publish = on_publish
    client1.connect(broker, port)
    message = json.dumps({"Act1": act1})
    ret = client1.publish("topico1", message)
else:
    st.write('')

values = st.slider('Selecciona el rango de valores', 0.0, 100.0)
st.write('Values:', values)

if values < 40:
    bar_color = "lightblue"
elif 40 <= values <= 70:
    bar_color = "darkblue"
else:
    bar_color = "black"

st.markdown(
    f"""
    <div style="background-color: {bar_color}; height: 30px; width: {values}%; border-radius: 5px;"></div>
    """,
    unsafe_allow_html=True
)

if st.button('Enviar valor analógico'):
    client1 = paho.Client("GIT-HUB")
    client1.on_publish = on_publish
    client1.connect(broker, port)
    message = json.dumps({"Analog": float(values)})
    ret = client1.publish("cmqtt_a", message)
else:
    st.write('')




