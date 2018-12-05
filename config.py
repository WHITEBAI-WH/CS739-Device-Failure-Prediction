# Server Specific Configurations
server = {
    'port': '8080',
    'host': '0.0.0.0'
}

# Pecan Application Configurations
app = {
    'root': 'cs739devicefailureprediction.controllers.root.RootController',
    'modules': ['cs739devicefailureprediction'],
    'static_root': '%(confdir)s/public',
    'template_path': '%(confdir)s/cs739devicefailureprediction/templates',
    'debug': False,
    'errors': {
        404: '/error/404',
        '__force_dict__': True
    }
}

logging = {
    'root': {'level': 'INFO', 'handlers': ['console']},
    'loggers': {
        'cs739devicefailureprediction': {'level': 'DEBUG', 'handlers': ['console'], 'propagate': False},
        'pecan': {'level': 'DEBUG', 'handlers': ['console'], 'propagate': False},
        'py.warnings': {'handlers': ['console']},
        '__force_dict__': True
    },
    'handlers': {
        'console': {
            'level': 'DEBUG',
            'class': 'logging.StreamHandler',
            'formatter': 'color'
        }
    },
    'formatters': {
        'simple': {
            'format': ('%(asctime)s %(levelname)-5.5s [%(name)s]'
                       '[%(threadName)s] %(message)s')
        },
        'color': {
            '()': 'pecan.log.ColorFormatter',
            'format': ('%(asctime)s [%(padded_color_levelname)s] [%(name)s]'
                       '[%(threadName)s] %(message)s'),
            '__force_dict__': True
        }
    }
}

# Custom Configurations must be in Python dictionary format::
#
# foo = {'bar':'baz'}
#
# All configurations are accessible at::
# pecan.conf

custom_config = {
    'mongo_config': {
        'host': 'localhost',
        'port': 27017,
        'global_db_username': 'test-user',
        'global_db_password': 'test-password',
    },
    'es_config': {
        'node1': {
            'host': 'localhost',
            'port': 9200,
        },
    },
    'cipher_secret': b'-lQIXhsB87t-6WGXte9brqGZa0WpNsYtgwbx0xEPQcU='
}
