
class Config:
    NAME = "Inventario"
    URL = "https://inventario.dim.uchile.cl",
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    SECRET_KEY = ");bN<LE#1@]pJkym)@0etysLHBCl=/@e+2JK:<>6Its#dI<fp"
    pass


class DevelopmentConfig(Config):
    DEBUG = True
    HOST = "0.0.0.0"
    PORT = 8005
    LIFETIME = 100000
    SQLALCHEMY_DATABASE_URI = "mysql://ccollado:avriL015897@10.0.0.196/inventario?charset=utf8mb4"


class ProductionConfig(Config):
    DEBUG = False
    HOST = "127.0.0.1"
    PORT = 80
    LIFETIME = 120
    SQLALCHEMY_DATABASE_URI = ""


config = {
    "production": ProductionConfig,
    "development": DevelopmentConfig
}
