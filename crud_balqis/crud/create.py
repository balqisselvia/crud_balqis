import mysql.connector

def create_record(id, nama, jenis_kel):
    mysb = mysql.connector.connect(
        host="localhost",
        user="root",
        password="",
        database="perpus"
    )

    mycursor = mysb.cursor()

    sql = "INSERT INTO pinjam (id, nama, jenis_kel) VALUES (%s, %s, %s)"
    val = (id, nama, jenis_kel)
    mycursor.execute(sql, val)

    mysb.commit()
    
    print(mycursor.rowcount, "record inserted.")

    mycursor.close()
    mysb.close()