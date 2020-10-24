import streamlit as st 
import numpy as np 
import pandas as pd 

# Adiciona titulo e breve descrição
st.title('Violências domésticas, sexual e outras')
st.write('Percentual de casos de diversas formas de viôlencia')
st.write('Fonte: http://sage.saude.gov.br/')

# Leitura de arquivos usando Pandas
vio_etnia = pd.read_csv('dados/violencia_etnia.csv')
vio_faixa = pd.read_csv('dados/violencia_faixa.csv')
vio_genero = pd.read_csv('dados/violencia_genero.csv')

# Apresenta os dados por gênero
st.subheader('Percentual de casos de violência por gênero')
st.line_chart(vio_genero.loc[:, ['Masculino', 'Feminino']])

# Apresenta os dados por faixa etária
st.subheader('Percentual de casos de violência por faixa etária')
st.line_chart(vio_faixa.loc[:, ['0-09 Anos', '10-19 Anos', '20-59 Anos', '60e+']])

# Apresenta os dados por etnia
st.subheader('Percentual de casos de violência por etnia')
st.line_chart(vio_etnia.loc[:, ['Branca', 'Amarela', 'Ignorada', 'Indígena', 'Parda', 'Preta']])
