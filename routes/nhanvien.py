# Import cac thu vien can thiet
from flask import Blueprint, render_template, request, redirect, url_for

# Import database va model NhanVien
from models import db, NhanVien


# Tao Blueprint cho chuc nang nhan vien
nhanvien_bp = Blueprint("nhanvien", __name__)


# Hien thi danh sach nhan vien
@nhanvien_bp.route("/nhanvien")
def danh_sach_nhan_vien():

     # Lay ma nhan vien tu o tim kiem
    tu_khoa = request.args.get("ma_nv", "")

    # Neu co nhap ma nhan vien
    if tu_khoa:
        danh_sach = NhanVien.query.filter(
            NhanVien.ma_nv.like(f"%{tu_khoa}%")
        ).all()

    # Neu khong nhap thi hien thi tat ca
    else:
        danh_sach = NhanVien.query.all()

    return render_template(
        "nhanvien/list.html",
        danh_sach=danh_sach,
        tu_khoa=tu_khoa
    )


# Hien thi form va xu ly them nhan vien
@nhanvien_bp.route("/nhanvien/them", methods=["GET", "POST"])
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
        return redirect(url_for("nhanvien.danh_sach_nhan_vien"))

    # Neu truy cap bang GET thi hien thi form
    return render_template("nhanvien/them.html")


# Sua thong tin nhan vien
@nhanvien_bp.route("/nhanvien/sua/<int:id>", methods=["GET", "POST"])
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
        return redirect(url_for("nhanvien.danh_sach_nhan_vien"))

    # Hien thi form sua
    return render_template(
        "nhanvien/sua.html",
        nhan_vien=nhan_vien
    )


# Xoa nhan vien
@nhanvien_bp.route("/nhanvien/xoa/<int:id>", methods=["POST"])
def xoa_nhan_vien(id):

    # Tim nhan vien theo ID
    nhan_vien = NhanVien.query.get_or_404(id)

    # Xoa nhan vien
    db.session.delete(nhan_vien)

    # Luu thay doi vao MySQL
    db.session.commit()

    # Quay lai danh sach
    return redirect(url_for("nhanvien.danh_sach_nhan_vien"))