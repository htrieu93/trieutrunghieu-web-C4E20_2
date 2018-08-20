from models.service import Service
import mlab

mlab.connect()

Get all documents from colletion
all_service = Service.objects()

first_service = all_service[0]




