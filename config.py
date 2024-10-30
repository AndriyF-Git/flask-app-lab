import os

# Базова конфігурація
class Config:
    SECRET_KEY = os.environ.get('SECRET_KEY') or 'a_very_secret_key'
    DEBUG = False
    TESTING = False
    DATABASE_URI = os.environ.get('DATABASE_URI') or 'sqlite:///default.db'
    SESSION_COOKIE_SECURE = True
    # Інші загальні налаштування

# Конфігурація для розробки
class DevelopmentConfig(Config):
    DEBUG = True
    DATABASE_URI = os.environ.get('DEV_DATABASE_URI') or 'sqlite:///development.db'
    SESSION_COOKIE_SECURE = False
    # Інші специфічні налаштування для розробки

# Конфігурація для тестування
class TestingConfig(Config):
    TESTING = True
    DEBUG = True
    DATABASE_URI = os.environ.get('TEST_DATABASE_URI') or 'sqlite:///test.db'
    SESSION_COOKIE_SECURE = False
    # Специфічні налаштування для тестування, наприклад, використання фейкових баз даних

# Конфігурація для продакшена
class ProductionConfig(Config):
    DATABASE_URI = os.environ.get('PROD_DATABASE_URI') or 'sqlite:///production.db'
    SESSION_COOKIE_SECURE = True
    # Інші специфічні налаштування для продакшена

# Маппінг конфігурацій за середовищем
config = {
    'development': DevelopmentConfig,
    'testing': TestingConfig,
    'production': ProductionConfig,
    'default': DevelopmentConfig
}
