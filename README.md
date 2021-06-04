# Aplicativo de Previsão de Aluguéis

O treinamento do modelo foi realizado no Colab Research e pode ser visualizado em https://github.com/henriquevedoveli/previsao-alugueis/blob/master/houses_to_rent.ipynb

Os dados foram retirados do site [Brazilian Houses to Rent](https://www.kaggle.com/rubenssjr/brasilian-houses-to-rent), foram tratados e foi realizado a análise exploratória dos dados. As features escolhidas para realizar a regressão foram: _Número de Quartos_, _Número de Banheiros_, _Valor do Condomínio_, _Valor do IPTU_, _Valor do Seguro Contra Incêndio_ e a _Cidade onde está o imóvel_

O modelo regressor treinado foi um modelo Lasso Regressor. 

Para realizar o deploy do modelo foi utilizado a biblioteca [streamlit](https://streamlit.io/) para a construção do site e para hospedar o site foi utilizado o [herokuapp](https://devcenter.heroku.com/categories/reference)


* link: https://regressor-aluguel.herokuapp.com/
