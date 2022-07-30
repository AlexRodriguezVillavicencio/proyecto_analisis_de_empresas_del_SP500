def load_db(df,con,name):
    try:
        df.to_sql(name=name,con=con, index=False)
    except:
        print("la tabla ya existe")