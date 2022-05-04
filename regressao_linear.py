# Bibliotecas
import pandas as pd
import numpy as np
from sklearn import metrics
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import MinMaxScaler
from sklearn.linear_model import LinearRegression

seed = 50
np.random.seed(seed)

# DataFrame utilizado:
df = pd.read_csv('Spotify Top 200 Global (2017-2021).csv')

# Transformação de Dados:
df.drop(['Artist', 'Track', 'Link', 'Week', 'Album_Name', 'Track_Number_on_Album', 'Artist_Genres'],
        axis=1, inplace=True)
# Perguntar alguma solução para o ,professor.
# def ms_to_min(x):
#     return x/60000
# df['Duration_MS'].apply(ms_to_min)

# Normalizando o DataFrame:
scaler = MinMaxScaler()
scaler.fit(df)

# Transformação de dados e criação de um novo DataFrame:

new_df = pd.DataFrame(scaler.transform(df), columns=df.columns)
print(new_df.head())

# Definindo variáveis Preditoras e variável de resposta:

X = df[['Rank', 'Streams', 'Duration_MS', 'Explicit']]
y = df['Artist_Followers']

# Dados de Treino e Teste:

X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.3, random_state=seed, shuffle=True)

# Criando modelo preditor e de aprendizado:

modelo = LinearRegression()
modelo.fit(X_train, y_train)
# Coeficientes:

coeficiente = pd.DataFrame(modelo.coef_, X.columns, columns=['Coeficiente'])
print(coeficiente)

predictions = modelo.predict(X_test)
print(predictions[1:10])

# Métricas de avaliação:

print('MAE:', metrics.mean_absolute_error(y_test, predictions))
print('MSE:', metrics.mean_squared_error(y_test, predictions))
print('RMSE:', np.sqrt(metrics.mean_squared_error(y_test, predictions)))

pd.DataFrame(predictions).to_csv('predictions.csv')