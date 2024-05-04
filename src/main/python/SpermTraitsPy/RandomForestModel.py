import pandas as pd
import numpy as np
import json
import psycopg2
from sklearn.ensemble import RandomForestClassifier as rf
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score, f1_score, precision_score, recall_score
import warnings


warnings.filterwarnings('ignore')


def classify(data_instance):
    df = get_data()
    X = df.drop(['alvo', 'numero'], axis=1)
    y = df['alvo']

    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.35, random_state=42)

    model = rf(n_estimators=100, random_state=42)
    model.fit(X_train, y_train)
    y_pred = model.predict(X_test)
    acc = accuracy_score(y_test, y_pred)
    f1 = f1_score(y_test, y_pred, average='macro')
    precision = precision_score(y_test, y_pred, zero_division=1, average='macro')
    recall = recall_score(y_test, y_pred, zero_division=1, average='macro')

    data = np.array([[
        data_instance.idade, data_instance.peso, data_instance.ec, data_instance.ce,
        data_instance.temp_retal, data_instance.temp_amb, data_instance.umidade,
        data_instance.mov_flanco, data_instance.hora, data_instance.turbilhao,
        data_instance.mot_moveis, data_instance.vigor, data_instance.volume, data_instance.zptz_106,
        data_instance.zptz_totais, data_instance.def_mai, data_instance.def_men, data_instance.def_mai_percent,
        data_instance.def_men_percent, data_instance.normais, data_instance.normais_percent
    ]]).reshape(1, -1)

    prediction = model.predict(data)

    alvo = prediction[0]
    hora = data_instance.hora
    add_data(alvo, hora)

    if prediction[0] == 0.0:
        print(f"Animal totalmente apto à reprodução, com a precisão de {acc * 100:.2f}%")
        return 'Animal totalmente apto à reprodução', acc
    elif prediction[0] == 1.0:
        print(f"Animal apto à reprodução, porém, com restrições, com a precisão de {acc * 100:.2f}%")
        return 'Animal apto à reprodução, porém com restrições', acc
    elif prediction[0] == 3.0:
        print(f"Animal não apto à reprodução, com a precisão de {acc * 100:.2f}%")
        return 'Animal não apto à reprodução', acc
    else:
        print("Prediction not recognized")
        return 'Prediction not recognized', acc


class Data:
    def __init__(self, idade, peso, ec, ce, temp_retal, temp_amb, umidade, mov_flanco, hora, turbilhao,
                 mot_moveis, vigor, volume, zptz_106, zptz_totais, def_mai, def_mai_percent, def_men, def_men_percent,
                 normais, normais_percent):

        self.idade = float(idade)
        self.peso = float(peso)
        self.ec = float(ec)
        self.ce = float(ce)
        self.temp_retal = float(temp_retal)
        self.temp_amb = float(temp_amb)
        self.umidade = float(umidade)
        self.mov_flanco = float(mov_flanco)
        self.hora = self.convert_hora_to_int(hora)
        self.turbilhao = float(turbilhao)
        self.mot_moveis = float(mot_moveis)
        self.vigor = float(vigor)
        self.volume = float(volume)
        self.zptz_106 = float(zptz_106)
        self.zptz_totais = float(zptz_totais)
        self.def_mai = float(def_mai)
        self.def_mai_percent = float(def_mai_percent)
        self.def_men = float(def_men)
        self.def_men_percent = float(def_men_percent)
        self.normais = float(normais)
        self.normais_percent = float(normais_percent)

    @staticmethod
    def convert_hora_to_int(hora):
        if hora != 0:
            hora_int = pd.to_datetime(hora, format='%H:%M').hour * 60 + pd.to_datetime(hora, format='%H:%M').minute
            return hora_int
        else:
            return 0

    @staticmethod
    def json_to_data_object(data):
        return Data(data["idade"],
                    data["peso"],
                    data["ec"],
                    data["ce"],
                    data["temp_retal"],
                    data["temp_amb"],
                    data["umidade"],
                    data["mov_flanco"],
                    data["hora"],
                    data["turbilhao"],
                    data["mot_moveis"],
                    data["vigor"],
                    data["volume"],
                    data["zptz_106"],
                    data["zptz_totais"],
                    data["def_mai"],
                    data["def_mai_percent"],
                    data["def_men"],
                    data["def_men_percent"],
                    data["normais"],
                    data["normais_percent"])


def get_data():
    conn = psycopg2.connect(
        dbname="classify",
        user="postgres",
        password="123456",
        host="localhost"
    )

    data = pd.read_sql("SELECT * FROM DATA_CLASSIFY;", conn)
    conn.close()
    return data


def add_data(alvo, hora):
    conn = psycopg2.connect(
        dbname="classify",
        user="postgres",
        password="123456",
        host="localhost"
    )
    cursor = conn.cursor()

    data = Connect.get_data_to_classify()

    data.update({"alvo": alvo})
    data.update({"hora": hora})
    data.pop("id")

    values = tuple(data.values())

    sql = '''INSERT INTO data_classify (idade, peso, ec, ce, temp_retal, temp_amb, umidade, mov_flanco, hora, turbilhao,
                      mot_moveis, vigor, volume, zptz_106, zptz_totais, def_mai, def_mai_percent, def_men, def_men_percent,
                      normais, normais_percent, alvo)
                 VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s);'''

    cursor.execute(sql, values)

    conn.commit()
    cursor.close()
    conn.close()


class Connect:
    def __init__(self):
        pass

    @staticmethod
    def get_data_to_classify():
        conn = psycopg2.connect(
            dbname="classify",
            user="postgres",
            password="123456",
            host="localhost"
        )

        cursor = conn.cursor()

        cursor.execute('''SELECT * FROM DATA_VIEW ORDER BY id DESC LIMIT 1;''')

        column_names = [desc[0] for desc in cursor.description]

        result = cursor.fetchall()

        rows_as_dicts = [dict(zip(column_names, row)) for row in result]

        json_result = json.dumps(rows_as_dicts)
        json_result = json.loads(json_result)

        conn.commit()
        conn.close()
        return json_result[0]


classify(Data.json_to_data_object(Connect.get_data_to_classify()))

