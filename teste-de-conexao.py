import cx_Oracle
import config

# Caminho onde está o plugin da biblioteca Oracle
cx_Oracle.init_oracle_client(lib_dir=r"C:\instantclient_21_3")

conexao = None
try:
    conexao = cx_Oracle.connect(
        config.username,
        config.password,
        config.dsn,
        encoding = config.encoding)
    print('Conexão com o BD Oracle estabelecida!\n')

    # Mostra a versão do BD Oracle
    print("Versão do BD: ", conexao.version)

    # Criação de um cursor
    cursor = conexao.cursor()
    
    # Consulta SQL (Obs: não coloque ; na consulta)
    sql = """
        SELECT DISTINCT C.ID, C.Name
        FROM glbHealthProvider C
        WHERE C.ID <> 2
        ORDER BY C.ID
    """

    cursor.execute(sql) # executa a consulta

    resultado = cursor.fetchone() # busca o resultado da consulta

    if resultado == None:
        print("\nNenhum Resultado")
        exit
    else:
        while resultado:   
            print("\n", resultado[0], resultado[1])
            resultado = cursor.fetchone()

except cx_Oracle.Error as error:
    print(error)
finally:
    # Libera a conexão
    if conexao:
        cursor.close()
conexao.close()
