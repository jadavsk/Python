dw_string = "host='10.0.0.13' dbname='dw' user='dwuser' 

password='dwpass'" dw_pgconn = psycopg2.connect(dw_string) 
dw_conn_wrapper = pygrametl.ConnectionWrapper(connection=dw_pgconn)