import os
import django

# Configura la ruta para tu proyecto Django
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'monitor_project.settings')

# Configura Django
django.setup()

from monitor.models import Sucursal
#from monitor import Sucursal 

MODULES = [
    {"sucursal": "Alto Hospicio", "ip": "10.101.13.94", "active": True, "region": "Tarapacá"},
    {"sucursal": "Iquique", "ip": "10.101.12.25", "active": True, "region": "Tarapacá"},
    {"sucursal": "Calama", "ip": "10.101.22.121", "active": True, "region": "Antofagasta"},
    {"sucursal": "Antofagasta", "ip": "10.101.23.21", "active": False, "region": "Antofagasta"},
    {"sucursal": "Chañaral", "ip": "10.101.31.25", "active": True, "region": "Atacama"},
    {"sucursal": "Copiapo", "ip": "10.101.32.25", "active": True, "region": "Atacama"},
    {"sucursal": "Vallenar", "ip": "10.101.33.25", "active": False, "region": "Atacama"},
    {"sucursal": "Coquimbo", "ip": "10.101.42.25", "active": True, "region": "Coquimbo"},
    {"sucursal": "Illapel", "ip": "10.101.44.25", "active": True, "region": "Coquimbo"},
    {"sucursal": "La Serena", "ip": "10.101.41.25", "active": True, "region": "Coquimbo"},
    {"sucursal": "Vicuña", "ip": "10.101.40.223", "active": False, "region": "Coquimbo"},
    {"sucursal": "Los Vilos", "ip": "10.101.47.25", "active": True, "region": "Coquimbo"},
    {"sucursal": "Ovalle", "ip": "10.101.43.25", "active": True, "region": "Coquimbo"},
    {"sucursal": "Salamanca", "ip": "10.101.48.25", "active": True, "region": "Coquimbo"},
    {"sucursal": "Angol", "ip": "10.101.91.25", "active": False, "region": "Araucanía"},
    {"sucursal": "Lautaro", "ip": "10.101.99.62", "active": True, "region": "Araucanía"},
    {"sucursal": "Loncoche", "ip": "10.101.99.94", "active": True, "region": "Araucanía"},
    {"sucursal": "Temuco", "ip": "10.101.93.25", "active": True, "region": "Araucanía"},
    {"sucursal": "Victoria", "ip": "10.101.92.25", "active": False, "region": "Araucanía"},
    {"sucursal": "Villarica", "ip": "10.101.94.25", "active": True, "region": "Araucanía"},
    {"sucursal": "ConCon", "ip": "10.101.50.190", "active": True, "region": "Valparaíso"},
    {"sucursal": "La Ligua", "ip": "10.101.50.150", "active": True, "region": "Valparaíso"},
    {"sucursal": "Los Andes", "ip": "10.101.59.94", "active": True, "region": "Valparaíso"},
    {"sucursal": "Quillota", "ip": "10.101.52.25", "active": True, "region": "Valparaíso"},
    {"sucursal": "Quilpue", "ip": "10.101.57.25", "active": True, "region": "Valparaíso"},
    {"sucursal": "Quintero", "ip": "10.101.59.126", "active": True, "region": "Valparaíso"},
    {"sucursal": "San Antonio", "ip": "10.101.55.25", "active": True, "region": "Valparaíso"},
    {"sucursal": "San Felipe", "ip": "10.101.51.25", "active": True, "region": "Valparaíso"},
    {"sucursal": "Valparaiso", "ip": "10.101.54.25", "active": True, "region": "Valparaíso"},
    {"sucursal": "Villa Alemana", "ip": "10.101.56.25", "active": True, "region": "Valparaíso"},
    {"sucursal": "Viña del Mar", "ip": "10.101.53.25", "active": True, "region": "Valparaíso"},
    {"sucursal": "Pichilemu", "ip": "10.101.65.25", "active": True, "region": "O'Higgins"},
    {"sucursal": "Rancagua", "ip": "10.101.61.25", "active": True, "region": "O'Higgins"},
    {"sucursal": "Rengo", "ip": "10.101.66.25", "active": True, "region": "O'Higgins"},
    {"sucursal": "San Fernando", "ip": "10.101.63.25", "active": True, "region": "O'Higgins"},
    {"sucursal": "San Vicente", "ip": "10.101.62.25", "active": True, "region": "O'Higgins"},
    {"sucursal": "Santa Cruz", "ip": "10.101.64.25", "active": True, "region": "O'Higgins"},
    {"sucursal": "Cauquenes", "ip": "10.101.75.25", "active": True, "region": "Maule"},
    {"sucursal": "Constitucion", "ip": "10.101.73.25", "active": True, "region": "Maule"},
    {"sucursal": "Curico", "ip": "10.101.71.25", "active": True, "region": "Maule"},
    {"sucursal": "Linares", "ip": "10.101.74.25", "active": True, "region": "Maule"},
    {"sucursal": "Parral", "ip": "10.101.77.25", "active": True, "region": "Maule"},
    {"sucursal": "San Javier", "ip": "10.101.76.25", "active": True, "region": "Maule"},
    {"sucursal": "Talca", "ip": "10.101.72.16", "active": True, "region": "Maule"},
    {"sucursal": "Concepcion", "ip": "10.101.83.25", "active": True, "region": "Biobío"},
    {"sucursal": "Coronel", "ip": "10.101.84.25", "active": True, "region": "Biobío"},
    {"sucursal": "Curanilahue", "ip": "10.101.89.25", "active": True, "region": "Biobío"},
    {"sucursal": "Los Angeles", "ip": "10.101.86.25", "active": True, "region": "Biobío"},
    {"sucursal": "Lota", "ip": "10.101.85.25", "active": True, "region": "Biobío"},
    {"sucursal": "Talcahuano", "ip": "10.101.82.25", "active": True, "region": "Biobío"},
    {"sucursal": "Ancud", "ip": "10.101.106.30", "active": True, "region": "Los Lagos"},
    {"sucursal": "Calbuco", "ip": "10.101.106.158", "active": True, "region": "Los Lagos"},
    {"sucursal": "Castro", "ip": "10.101.104.25", "active": True, "region": "Los Lagos"},
    {"sucursal": "Osorno", "ip": "10.101.102.25", "active": True, "region": "Los Lagos"},
    {"sucursal": "Puerto Montt", "ip": "10.101.103.25", "active": True, "region": "Los Lagos"},
    {"sucursal": "Quellon", "ip": "10.101.107.110", "active": True, "region": "Los Lagos"},
    {"sucursal": "Coyhaique", "ip": "10.101.111.25", "active": True, "region": "Aysén"},
    {"sucursal": "Puerto Aysen", "ip": "10.101.112.25", "active": True, "region": "Aysén"},
    {"sucursal": "Puerto Natales", "ip": "10.101.205.179", "active": True, "region": "Magallanes"},
    {"sucursal": "Punta Arenas", "ip": "10.101.122.25", "active": True, "region": "Magallanes"},
    {"sucursal": "Alameda", "ip": "10.101.181.26", "active": True, "region": "Metropolitana"},
    {"sucursal": "Buin", "ip": "10.101.143.25", "active": True, "region": "Metropolitana"},
    {"sucursal": "Colina", "ip": "10.101.145.25", "active": True, "region": "Metropolitana"},
    {"sucursal": "Estación", "ip": "10.101.135.25", "active": True, "region": "Metropolitana"},
    {"sucursal": "Independencia", "ip": "10.101.132.25", "active": True, "region": "Metropolitana"},
    {"sucursal": "La Florida", "ip": "10.101.140.25", "active": True, "region": "Metropolitana"},
    {"sucursal": "Lampa", "ip": "10.101.148.25", "active": True, "region": "Metropolitana"},
    {"sucursal": "Las Condes", "ip": "10.101.131.25", "active": True, "region": "Metropolitana"},
    {"sucursal": "Maipu", "ip": "10.101.138.25", "active": True, "region": "Metropolitana"},
    {"sucursal": "Melipilla", "ip": "10.101.142.25", "active": True, "region": "Metropolitana"},
    {"sucursal": "Ñuñoa", "ip": "10.101.136.25", "active": True, "region": "Metropolitana"},
    {"sucursal": "Providencia", "ip": "10.101.133.25", "active": True, "region": "Metropolitana"},
    {"sucursal": "Puente Alto", "ip": "10.101.141.25", "active": True, "region": "Metropolitana"},
    {"sucursal": "San Bernardo", "ip": "10.101.139.25", "active": True, "region": "Metropolitana"},
    {"sucursal": "San Miguel", "ip": "10.101.137.25", "active": True, "region": "Metropolitana"},
    {"sucursal": "Santiago", "ip": "10.101.134.25", "active": True, "region": "Metropolitana"},
    {"sucursal": "Santo Domingo", "ip": "10.101.161.25", "active": True, "region": "Valparaíso"},
    {"sucursal": "Talagante", "ip": "10.101.146.25", "active": True, "region": "Metropolitana"},
    {"sucursal": "La Union", "ip": "10.101.109.25", "active": True, "region": "Los Ríos"},
    {"sucursal": "Valdivia", "ip": "10.101.101.25", "active": True, "region": "Los Ríos"},
    {"sucursal": "Arica", "ip": "10.101.11.25", "active": True, "region": "Arica y Parinacota"},
    {"sucursal": "Chillan", "ip": "10.101.81.25", "active": True, "region": "Ñuble"},
    {"sucursal": "San Carlos", "ip": "10.101.88.25", "active": True, "region": "Ñuble"}
    
]


for module in MODULES:
    Sucursal.objects.create(
        sucursal=module['sucursal'],
        ip=module['ip'],
        active=module['active'],
        region=module['region']
    )

# Realizar el ping después de crear cada objeto Sucursal
    response = os.system(f"ping -c 1 {module['ip']}")
    
    if response == 0:
        print(f"La IP {module['ip']} respondió al ping.")
    else:
        print(f"La IP {module['ip']} no respondió al ping.")