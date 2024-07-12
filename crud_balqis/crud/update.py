import mysql.connector

def update_record(id, nama, jenis_kel):
    try:
        mysb = mysql.connector.connect(
            host="localhost",
            user="root",
            password="",
            database="perpus"
        )

        mycursor = mysb.cursor()

        sql = "UPDATE pinjam SET id = %s, nama = %s, jenis_kel = %s WHERE id = %s"
        val = (id, nama, jenis_kel, id)
        print("Executing SQL:", sql % val)  # Debug statement
        mycursor.execute(sql, val)

        mysb.commit()
        
        print(mycursor.rowcount, "record(s) affected")

    except mysql.connector.Error as err:
        print("Error: {}".format(err))
    finally:
        mycursor.close()
        mysb.close()

# Example usage