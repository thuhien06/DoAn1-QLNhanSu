# Import SQLAlchemy
from flask_sqlalchemy import SQLAlchemy


# Tao doi tuong database
db = SQLAlchemy()


# Model NhanVien dai dien cho bang nhanvien
class NhanVien(db.Model):

    # Ten bang trong MySQL
    __tablename__ = "nhanvien"

    # Khoa chinh
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)

    # Ma nhan vien
    ma_nv = db.Column(db.String(20), unique=True, nullable=False)

    # Ho va ten
    ho_ten = db.Column(db.String(100), nullable=False)

    # Ngay sinh
    ngay_sinh = db.Column(db.Date)

    # Gioi tinh
    gioi_tinh = db.Column(db.String(10))

    # So dien thoai
    so_dien_thoai = db.Column(db.String(15))

    # Email
    email = db.Column(db.String(100))

    # Dia chi
    dia_chi = db.Column(db.String(255))

    # Ngay vao lam
    ngay_vao_lam = db.Column(db.Date)

    # Phong ban
    phong_ban = db.Column(db.String(100))

    # Chuc vu
    chuc_vu = db.Column(db.String(100))