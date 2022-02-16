from unittest import result
from flask import Flask, render_template
from flask import request, redirect, url_for
from mysql import connector

app = Flask(__name__)


db = connector.connect(
    host    = 'localhost',
    user    = 'root',
    passwd  = '',
    database= 'db_sample_api_0539'
)


@app.route('/')
def halaman_awal():
    cursor = db.cursor()
    cursor.execute('select * from tbl_students_0539')
    result = cursor.fetchall()
    cursor.close()
    return render_template('index.html', hasil = result)

@app.route('/tambah/')
def tambah_data():
    return render_template('tambah.html')

@app.route('/proses_tambah/', methods=['POST'])
def proses_tambah():
    id =request.form['id']
    nim = request.form['nim']
    nama = request.form['nama']
    jk = request.form['jk']
    jurusan = request.form['jurusan']
    alamat = request.form['alamat']
    cur = db.cursor()
    cur.execute('INSERT INTO tbl_students_0539 (nim, nama, jk, jurusan, alamat) VALUES ( %s, %s, %s, %s, %s)', (nim, nama, jk, jurusan, alamat))
    db.commit()
    
    return redirect(url_for('halaman_awal'))
    
@app.route('/ubah/<angka>', methods=['GET'])
def ubah_data(id):
    cur = db.cursor()
    cur.execute('select * from tbl_students_0539 where id=%s', (id,))
    res = cur.fetchall()
    cur.close()
    return render_template('ubah.html', hasil=res)

@app.route('/proses_ubah/', methods=['POST'])
def proses_ubah():
    id = request.form['id']
    nim = request.form['nim']
    nama = request.form['nama']
    jk = request.form['jk']
    jurusan = request.form['jurusan']
    alamat = request.form['alamat']
    cur = db.cursor()
    sql = "UPDATE tbl_students_0539 SET nim=%s, nama=%s, jk=%s, jurusan=%s, alamat=%s WHERE id=%s"
    value = (id, nim, nama, jk, jurusan, alamat)
    cur.execute(sql, value)
    db.commit()
    return redirect(url_for('halaman_awal'))

@app.route('/hapus/<angka>', methods=['GET'])
def hapus_data(id):
    cur = db.cursor()
    cur.execute('DELETE from tbl_students_0539 where id=%s', (id,))
    db.commit()
    return redirect(url_for('halaman_awal'))

if __name__ == '__main__':
    app.run()