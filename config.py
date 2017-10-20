class BaseConfig:
    SQLALCHEMY_DATABASE_URI = 'mysql+pymysql://root:1@localhost:3306/db_test'
    SECRET_KEY = 'test'
    SQLALCHEMY_COMMIT_ON_TEARDOWN=True
    SQLALCHEMY_TRACK_MODIFICATIONS = True

    @staticmethod
    def init_app(app):
        pass



config={
'default':BaseConfig
}