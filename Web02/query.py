from models.service import Service
import mlab

mlab.connect()

id_to_find = "5b7824d25f029f42645b8d1b"

# hera = Service.objects(id = id_to_find) ## -> []
# hera = Service.objects.get(id = id_to_find) ## -> Service obj
service = Service.objects.with_id(id_to_find) ## -> Service obj

if service is not None: 
    # service.delete()
    # print('Deleted')
    print(service.to_mongo())
    service.update(set__yob = 2005, set__name = 'Linh kute')
    service.reload()
    print(service.to_mongo())
else:
    print('Not found')
