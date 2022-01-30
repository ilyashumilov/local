import pandas as pd
import psycopg2
from psycopg2 import Error
from psycopg2.extensions import ISOLATION_LEVEL_AUTOCOMMIT

df = pd.read_csv('1.csv')
df = pd.DataFrame(df)
try:
    # Подключение к существующей базе данных
    connection = psycopg2.connect(user="django",
                                  # пароль, который указали при установке PostgreSQL
                                  # role="django",
                                  password="password",
                                  host="127.0.0.1",
                                  port="5432",
                                  database="c")
    connection.set_isolation_level(ISOLATION_LEVEL_AUTOCOMMIT)
    # Курсор для выполнения операций с базой данных
    cursor = connection.cursor()



    cargo = df['Cargo type'].dropna().reset_index()
    count = 0
    for i in cargo['Cargo type']:
        a = "'"+cargo.loc[count,'Cargo type']+"'"
        query = f'INSERT INTO inputs_materials (name) VALUES ({a});'
        print(query)
        count += 1
        cursor.execute(query)

    ports = df[['City','Country']].copy().reset_index()
    count = 0
    for i in ports['City']:
        a = "'"+str(ports.loc[count,'City'])+"'"
        b = "'"+str(ports.loc[count, 'Country'])+"'"

        query = f'INSERT INTO inputs_ports (port, country ) VALUES ({a},{b});'
        cursor.execute(query)

        count += 1

    empresas = df[['Customer-Supplier company', 'Companies Traders']].copy().dropna().reset_index()
    count = 0

    for i in empresas['Customer-Supplier company']:
        a = "'"+str(empresas.loc[count, 'Customer-Supplier company'])+"'"
        b = "'"+str(empresas.loc[count, 'Companies Traders'])+"'"
        query = f'INSERT INTO inputs_empresa (name, trader) VALUES ({a},{b});'
        cursor.execute(query)

        count += 1

except (Exception, Error) as error:
    print("Ошибка при работе с PostgreSQL", error)
finally:
    if connection:
        cursor.close()
        connection.close()
        print("Соединение с PostgreSQL закрыто")
