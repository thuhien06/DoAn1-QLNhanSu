# Import Flask de tao ung dung web
from flask import Flask, render_template, request, redirect, url_for

# Import load_dotenv de doc thong tin tu file .env
from dotenv import load_dotenv

from models import db, NhanVien

# Import os de lay gia tri bien moi truong
import os

# Doc cac bien cau hinh trong file .env
load_dotenv()


# Tao ung dung Flask
app = Flask(__name__)


# Cau hinh ket noi toi MySQL
# Cau truc:
# mysql+pymysql://user:password@host:port/database
app.config["SQLALCHEMY_DATABASE_URI"] = (
    f"mysql+pymysql://{os.getenv('DB_USER')}:"       # Ten tai khoan MySQL
    f"{os.getenv('DB_PASSWORD')}@"                   # Mat khau MySQL
    f"{os.getenv('DB_HOST')}:"                       # Dia chi may chu MySQL
    f"{os.getenv('DB_PORT')}/"                       # Cong MySQL
    f"{os.getenv('DB_NAME')}"                        # Ten database
)


# Tat tinh nang theo doi thay doi cua SQLAlchemy
# Giup giam canh bao va tiet kiem tai nguyen
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False

# Dang ky database voi Flask app
db.init_app(app)


# Tao route cho trang chu
# Khi truy cap http://127.0.0.1:5000/
# Flask se chay ham home()
@app.route("/")
def home():
    # Hien thi file index.html trong thu muc templates
    return render_template("index.html")


# Tao route de kiem tra ket noi MySQL
# Truy cap: http://127.0.0.1:5000/test-db
@app.route("/test-db")
def test_db():
    try:
        # Gui lenh SQL "SELECT 1" toi MySQL
        # Neu chay duoc thi ket noi database thanh cong
        db.session.execute(db.text("SELECT 1"))

        # Tra ve thong bao neu ket noi thanh cong
        return "Ket noi MySQL thanh cong!"

    except Exception as e:
        # Neu ket noi that bai thi hien thi loi
        return f"Loi ket noi MySQL: {e}"

# Hien thi danh sach nhan vien
@app.route("/nhanvien")
def danh_sach_nhan_vien():

    # Lay tat ca nhan vien trong database
    danh_sach = NhanVien.query.all()

    # Truyen danh sach nhan vien sang file list.html
    return render_template(
        "nhanvien/list.html",
        danh_sach=danh_sach
    )


# Hien thi form va xu ly them nhan vien
@app.route("/nhanvien/them", methods=["GET", "POST"])
def them_nhan_vien():

    # Neu nguoi dung bam nut Them nhan vien
    if request.method == "POST":

        # Lay du lieu tu form
        ma_nv = request.form["ma_nv"]
        ho_ten = request.form["ho_ten"]
        ngay_sinh = request.form["ngay_sinh"]
        gioi_tinh = request.form["gioi_tinh"]
        so_dien_thoai = request.form["so_dien_thoai"]
        email = request.form["email"]
        dia_chi = request.form["dia_chi"]
        ngay_vao_lam = request.form["ngay_vao_lam"]
        phong_ban = request.form["phong_ban"]
        chuc_vu = request.form["chuc_vu"]

        # Tao doi tuong nhan vien moi
        nhan_vien = NhanVien(
            ma_nv=ma_nv,
            ho_ten=ho_ten,
            ngay_sinh=ngay_sinh,
            gioi_tinh=gioi_tinh,
            so_dien_thoai=so_dien_thoai,
            email=email,
            dia_chi=dia_chi,
            ngay_vao_lam=ngay_vao_lam,
            phong_ban=phong_ban,
            chuc_vu=chuc_vu
        )

        # Them nhan vien vao database
        db.session.add(nhan_vien)

        # Luu thay doi vao MySQL
        db.session.commit()

        # Them xong thi quay ve danh sach nhan vien
        return redirect(url_for("danh_sach_nhan_vien"))

    # Neu truy cap bang GET thi hien thi form
    return render_template("nhanvien/them.html")

# Sua thong tin nhan vien
@app.route("/nhanvien/sua/<int:id>", methods=["GET", "POST"])
def sua_nhan_vien(id):

    # Tim nhan vien theo ID
    nhan_vien = NhanVien.query.get_or_404(id)

    # Neu nguoi dung bam nut Luu
    if request.method == "POST":

        # Cap nhat thong tin
        nhan_vien.ma_nv = request.form["ma_nv"]
        nhan_vien.ho_ten = request.form["ho_ten"]
        nhan_vien.ngay_sinh = request.form["ngay_sinh"]
        nhan_vien.gioi_tinh = request.form["gioi_tinh"]
        nhan_vien.so_dien_thoai = request.form["so_dien_thoai"]
        nhan_vien.email = request.form["email"]
        nhan_vien.dia_chi = request.form["dia_chi"]
        nhan_vien.ngay_vao_lam = request.form["ngay_vao_lam"]
        nhan_vien.phong_ban = request.form["phong_ban"]
        nhan_vien.chuc_vu = request.form["chuc_vu"]

        # Luu thay doi vao MySQL
        db.session.commit()

        # Quay lai danh sach
        return redirect(url_for("danh_sach_nhan_vien"))

    # Hien thi form sua
    return render_template(
        "nhanvien/sua.html",
        nhan_vien=nhan_vien
    )

# Tao cac bang trong database neu chua ton tai
with app.app_context():
    db.create_all()

# Kiem tra xem file nay co duoc chay truc tiep hay khong
if __name__ == "__main__":

    # Khoi dong Flask
    # debug=True giup tu dong reload khi sua code
    # va hien thi loi chi tiet khi co loi
    app.run(debug=True)# Import Flask de tao ung dung web

