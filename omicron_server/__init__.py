from flask import Flask, request, jsonify
from rq import Queue
from redis import Redis
import logging.config
from .components.inventory import *
from .components.scanner import *
from .components.record_database import *
from .components.full_scan import *
from .components.search_vulnerability import *

app = Flask(__name__)
q = Queue(connection=Redis(), default_timeout=3600)

log_path = "omicron_server/logs/"
if not os.path.exists(log_path):
    os.mkdir(log_path)
setting_path = "omicron_server/settings/"
if not os.path.exists(setting_path):
    os.mkdir(setting_path)

# create the logging file handler
logging.config.fileConfig("omicron_server/settings/log.conf")
log = logging.getLogger("SpotterApp")


from . import views