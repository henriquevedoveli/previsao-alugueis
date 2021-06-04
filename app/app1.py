import streamlit as st  # version 0.82.0
import joblib
import pandas as pd

emoji = 'https://emojipedia-us.s3.dualstack.us-west-1.amazonaws.com/thumbs/120/google/274/house-with-garden_1f3e1.png'

def pred(model, data):
    return model.predict(data)

def app():
    model = joblib.load('model.sav')
    st.markdown("<br>", unsafe_allow_html=True)
    st.image(emoji, width=80)
    st.write(
    '''
    # Aplicativo de Previsão de Aluguéis

    O Aplicativo realiza a regressão com os dados passados e realiza a previsão de qual vai ser o preço do aluguel do imóvel
    com base em um modelo treinado anteriormente.

    '''
    )
    st.write('---')
    st.sidebar.write('---')
    st.sidebar.header('Parâmetros para Regressão')

    # obtencao dos dados
    city = st.sidebar.selectbox('Cidade', ['São Paulo', 'Belo Horizonte', 'Campinas', 'Porto Alegre', 'Rio de Janeiro'])
    rooms = st.sidebar.selectbox('Número de Quartos', [1, 2, 3, 4, 5, 6, 7, 8, 9, 10])
    bathrooms = st.sidebar.selectbox('Número de Banheiros', [1, 2, 3, 4, 5, 6, 7, 8])
    floor = st.sidebar.selectbox('Número de Andares', [1, 2, 3, 4])
    hoa = st.sidebar.slider('Valor do Condomínio', min_value=200, max_value=15000)
    propertyTax = st.sidebar.slider('Valor do IPTU', min_value=50, max_value=400)
    fireInsurance = st.sidebar.slider('Valor do Seguro Contra Incêndio', min_value=5, max_value=400)

    if city == 'São Paulo':
        cityMapped = 1
    elif city == 'Porto Alegre':
        cityMapped = 2
    elif city == 'Rio de Janeiro':
        cityMapped = 3
    elif city == 'Campinas':
        cityMapped = 4
    else:
        cityMapped = 5

    data = [[rooms, bathrooms, hoa, propertyTax, fireInsurance, cityMapped]]

    df = pd.DataFrame([city, rooms, bathrooms, floor, hoa, propertyTax, fireInsurance],
                      ['Cidade', 'Número de Quartos', 'Número de Banheiros', 'Número de Andares', 'Valor do Condomínio',
                       'IPTU', 'Seguro Contra Incendio'],
                      ['Valores'])

    col1, col2, col3 = st.beta_columns([1, 6, 1])

    col2.header('Valores Utilizados')
    col2.write(df)

    if col2.button('Realizar a Regressão'):
        result = pred(model, data)

    with col1:
        col1.write(' ')

    with col3:
        st.write("")

    try:
        st.write('''## O valor previsto do aluguel é R$ %s
        ''' % result[0].round(2))

    except:
        pass

