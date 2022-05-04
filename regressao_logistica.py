# Importa bibliotecas
from matplotlib import pyplot as plt
from sklearn.linear_model import LogisticRegression
from sklearn.model_selection import train_test_split
from sklearn.metrics import confusion_matrix, classification_report
from sklearn.metrics import roc_curve
import pandas as pd

df = pd.read_csv('Spotify Top 200 Global (2017-2021).csv')

# Exclusão de variáveis não necessárias:

df.drop(['Artist', 'Track', 'Link', 'Week', 'Album_Name', 'Track_Number_on_Album', 'Artist_Genres'],
        axis=1, inplace=True)

# Definindo variáveis Preditoras e variável de resposta:

X = df[['Rank', 'Streams', 'Duration_MS', 'Explicit']]
y = df['Artist_Followers']

X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.3, random_state=42)

logit = LogisticRegression()

# Treina o Modelo:
logit.fit(X_train, y_train)

y_pred = logit.predict(X_test)

# Acuracia
logit.score(X_test, y_test)

# Matriz de Confusao
print(confusion_matrix(y_test, y_pred))

# Outras Metricas
print(classification_report(y_test, y_pred))

# computa probabilidades
y_pred_prob = logit.predict_proba(X_test)[:, 1]

# Gera fpr, tpr e thresholds
fpr, tpr, thresholds = roc_curve(y_test, y_pred_prob)

# Curva ROC
plt.plot([0, 1], [0, 1], 'k--')
plt.plot(fpr, tpr)
plt.xlabel('False Positive Rate')
plt.ylabel('True Positive Rate')
plt.title('ROC Curve')
plt.show()