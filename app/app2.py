import streamlit as st
import pandas as pd


@st.cache
def loadData(path, nRows):
    data = pd.read_csv(path)
    data = data.head(nRows)
    return data


def app():
    st.title('Sobre')

    st.write('''Definir o preço ou encontrar a casa com o preço ideal pode ser uma tarefa muito difícil. 
                Diversos fatores podem influenciar no momento de precificar o valor do aluguel de um imóvel, como a cidade do imóvel, 
                tamanho, número de quartos, entre outras razões. Portanto é possível prever um valor para o aluguel de um imóvel 
                utilizando características do mesmo, podendo assim tornar a precificação mais fácil.''')

    data = loadData('https://raw.githubusercontent.com/henriquevedoveli/previsao-alugueis/master/dados/houses_to_rent_v2.csv' , 25)
    st.dataframe(data)

    st.write('''Para conseguir realizar a previsão dos preços de aluguéis foi utilizado como base de dados um dataset com 
                informações para cinco grandes cidades brasileiras. Em um jupyter notebook foi realizado o tratamento desses
                dados, a análise exploratória dos mesmos e o treinamento do modelo preditivo.''')

    st.write('''Para a construção do modelo foi escolhido as seguintes features: número de quartos, número de banheiros, 
    valor do condomínio, valor do IPTU, valor do seguro contra incêndio e a cidade do imóvel. Essas features foram 
    escolhidas durante a análise exploratória dos dados, já que são as que tem a correlação mais forte com o preço total
    sem ter correlação com outras features, apesar da cidade não ter correlação forte com o preço total achei importante
    utilizar como parâmetro para regressão, já que a cidade é algo importante na hora que alguém vai escolher onde morar,
    na construção do aplicativo foi colocado andares como parâmetro de regressão, porém ele não modifica o preço, já que 
    na análise exploratória não se mostrou relevante, porém achei que seria relevante na hora de construir uma aplicação.''')

    st.write('### Matriz de Confussão para os dados')

    st.image('/img/matrizconfussao.png')

    st.write('''O modelo escolhido foi o que obteve melhor acurácia, no caso foi o regressor Lasso, após o treinamento do 
                modelo foi realizado a validação do modelo, onde foi realizado um gráfico do Valor Real x Valor Previsto, além
                do gráfico de Resíduos.''')

    st.write('### Gráfico de Validação do Modelo')

    st.image('/img/realxprevisto.png')

    st.write('''
    Dados Utilizados: [Brazilian Hoises to Rent](https://www.kaggle.com/rubenssjr/brasilian-houses-to-rent)
    
    Notebook de Treinamento : [https://github.com/henriquevedoveli/previsao-alugueis/blob/master/houses_to_rent.ipynb](https://github.com/henriquevedoveli/previsao-alugueis/blob/master/houses_to_rent.ipynb)
    ''')

    st.write('### Contato')
    col1, col2 = st.beta_columns(2)

    col1.markdown('''
    * Email: [henriquevedoveli@gmail.com](mailto:henriquevedoveli@gmail.com) 

    * Linkedin: [https://www.linkedin.com/in/henrique-vedoveli/](https://www.linkedin.com/in/henrique-vedoveli/)

    ''', unsafe_allow_html=False)

    col2.write(
        '''
        * Site: [https://sites.google.com/view/henriquevedoveli](https://sites.google.com/view/henriquevedoveli/home)
    
        * Github: [https://github.com/henriquevedoveli](https://github.com/henriquevedoveli)
        '''
    )
