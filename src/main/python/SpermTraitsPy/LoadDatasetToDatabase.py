import psycopg2


def create_table():
    conn = psycopg2.connect(
        dbname="PGDATABASE",
        user="PGUSER",
        password="PGPASSWORD",
        host="PGHOST",
        port="PGPORT"
    )
    cur = conn.cursor()

    # Criação da sequência
    cur.execute("CREATE SEQUENCE data_classify_sequence START WITH 152;")

    # Criação da tabela
    cur.execute("""
        CREATE TABLE IF NOT EXISTS data_classify (
            numero BIGINT DEFAULT NEXTVAL('data_classify_sequence') NOT NULL,
            idade FLOAT NOT NULL,
            peso FLOAT NOT NULL,
            ec FLOAT NOT NULL,
            ce FLOAT NOT NULL,
            temp_retal FLOAT NOT NULL,
            temp_amb FLOAT NOT NULL,
            umidade FLOAT NOT NULL,
            mov_flanco FLOAT NOT NULL,
            hora BIGINT NOT NULL,
            turbilhao FLOAT NOT NULL,
            mot_moveis FLOAT NOT NULL,
            vigor FLOAT NOT NULL,
            volume FLOAT NOT NULL,
            zptz_106 FLOAT NOT NULL,
            zptz_totais FLOAT NOT NULL,
            def_mai FLOAT NOT NULL,
            def_mai_percent FLOAT NOT NULL,
            def_men FLOAT NOT NULL,
            def_men_percent FLOAT NOT NULL,
            normais FLOAT NOT NULL,
            normais_percent FLOAT NOT NULL,
            alvo FLOAT NOT NULL,
            CONSTRAINT pk_data_classify PRIMARY KEY (numero)
        );
    """)

    conn.commit()

    cur.close()
    conn.close()


def add_data_on_database():
    conn = psycopg2.connect(
        dbname="railway",
        user="postgres",
        password="CArBbfxiDbtRNuZVSCeMVQMEJZeMeCDk",
        host="viaduct.proxy.rlwy.net",
        port=16546
    )
    cur = conn.cursor()

    with open('/home/wesley/df.csv', 'r') as f:
        next(f)
        cur.copy_from(f, 'data_classify', sep=',')

    conn.commit()

    cur.close()
    conn.close()


create_table()

add_data_on_database()
