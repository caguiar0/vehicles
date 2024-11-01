import pandas as pd
import plotly.express as px
import streamlit as st

st.set_page_config(page_title='Meu app com Streamlit')
st.title('Histograma e Grafico de anúncios de vendas de carros')
st.write('Escolha qual deseja executar:') 

car_data = pd.read_csv('vehicles.csv') # lendo os dados
hist_button = st.button('Criar histograma') # criar um botão
plot_express_button = st.button('Criar gráfico de dispersão') # criar um botão    

if hist_button: # se o botão for clicado
         # escrever uma mensagem
    st.write('Criando um histograma para o conjunto de dados de anúncios de vendas de carros')
         
         # criar um histograma
    fig = px.histogram(car_data, x="odometer")
     
         # exibir um gráfico Plotly interativo
    st.plotly_chart(fig, use_container_width=True)

     
if plot_express_button: # se o botão for clicado
         # escrever uma mensagem
    st.write('Criando um grafico de dispersão para o conjunto de dados de anúncios de vendas de carros')
         
         # criar um grafico de dispersão
    fig = px.scatter(car_data, x="odometer", y="price")
     
         # exibir um gráfico Plotly interativo
    st.plotly_chart(fig, use_container_width=True)