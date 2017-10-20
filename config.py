class BaseConfig:
    SQLALCHEMY_DATABASE_URI = 'mysql+pymysql://root:1@localhost:3306/test'
    SECRET_KEY = 'test'



config={
'default':BaseConfig
}