# Import Flask de tao ung dung web
from flask import Flask, render_template

# Import load_dotenv de doc thong tin tu file .env
from dotenv import load_dotenv

# Import database
from models import db

# Import Blueprint nhan vien
from routes.nhanvien import nhanvien_bp

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
    f"mysql+pymysql://{os.getenv('DB_USER')}:"
    f"{os.getenv('DB_PASSWORD')}@"
    f"{os.getenv('DB_HOST')}:"
    f"{os.getenv('DB_PORT')}/"
    f"{os.getenv('DB_NAME')}"
)


# Tat tinh nang theo doi thay doi cua SQLAlchemy
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False


# Dang ky database voi Flask app
db.init_app(app)


# Dang ky Blueprint nhan vien
app.register_blueprint(nhanvien_bp)


# Route trang chu
@app.route("/")
def home():

    # Hien thi file index.html
    return render_template("index.html")


# Route kiem tra ket noi MySQL
@app.route("/test-db")
def test_db():

    try:

        # Gui lenh SQL "SELECT 1" toi MySQL
        db.session.execute(db.text("SELECT 1"))

        # Neu thanh cong
        return "Ket noi MySQL thanh cong!"

    except Exception as e:

        # Neu co loi
        return f"Loi ket noi MySQL: {e}"


# Tao cac bang trong database neu chua ton tai
with app.app_context():
    db.create_all()


# Kiem tra file co duoc chay truc tiep hay khong
if __name__ == "__main__":

    # Khoi dong Flask
    app.run(debug=True)