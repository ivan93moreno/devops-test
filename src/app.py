# -*- coding: utf-8 -*-

from flask import Flask
from src.domain.drivers.redis_management import RedisManagement
from configuration import ConfigurationManager

# For import *
__all__ = ['create_app']


def create_app(settings_path, app_name='Is3 Frontend'):
    configuration_manager = ConfigurationManager(settings_path)
    app = Flask(app_name)
    configure_blueprints(app)
    redis_configuration = configuration_manager.get_redis_configuration()
    configure_conectors(app, redis_configuration)
    return app

def configure_blueprints(app):
    """Configure blueprints in views."""
    from src.views.monitoring import mod_monitoring
    app.register_blueprint(mod_monitoring, url_prefix='/')

def configure_conectors(app, redis_configuration):
    app.config['redis_connector'] = RedisManagement(redis_configuration)