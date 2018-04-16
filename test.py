import os
import requests
import csv
import argparse
from datetime import datetime
from datetime import timedelta
from bs4 import BeautifulSoup
import re

#Se crea el vector Resultante
vector_resultado=[]
cabecera=["Fecha","Evento","Hora","Categoria", "Precio", "Direccion", "Ubicacion", "Ciudad"]
vector_resultado.append(cabecera)

# Se crea el vector de pagínas a consultar para el ejercicio
pages_links =['https://www.nuevayork.com/eventos/que-hacer-en-nueva-york-en-abril-de-2018/',
'https://www.nuevayork.com/eventos/que-hacer-en-nueva-york-en-mayo-de-2018/',
'https://www.nuevayork.com/eventos/que-hacer-en-nueva-york-en-junio-de-2018/',
'https://www.nuevayork.com/eventos/que-hacer-en-nueva-york-en-julio-de-2018/',
'https://www.nuevayork.com/eventos/que-hacer-en-nueva-york-en-agosto-de-2018/',
'https://www.nuevayork.com/eventos/que-hacer-en-nueva-york-en-septiembre-de-2018/',
'https://www.nuevayork.com/eventos/que-hacer-en-nueva-york-en-octubre-de-2018/',
'https://www.nuevayork.com/eventos/que-hacer-en-nueva-york-en-noviembre-de-2018/',
'https://www.nuevayork.com/eventos/que-hacer-en-nueva-york-en-diciembre-de-2018/',
]

# Se recorre el vector de eventos por mes
for evento_mes in pages_links:
	# fetch the content from url
	page_response = requests.get(evento_mes, timeout=5)
	page_content = BeautifulSoup(page_response.content, "html.parser")
	#Se extrae los datos desde la pagina de consulta
	tablas=page_content.find_all(class_='vo-events-overview-event cf')

	# Recorre cada uno de los registros recuperados
	for i in tablas:
		elemento_lista=[]
		#Se almacena en las variables temporales
		fecha=i.find_all(class_='vo-events-overview-date')[0].text.strip()
		nombre_evento=i.find_all(class_='vo-events-overview-title')[0].text.strip()
		detalle_ev=i.find_all(class_='vo-events-overview-extended-date')[0].text.strip().split("|")
		detalle=""
		categoria=""
		precio=""
		if(len(detalle_ev)==3):
			detalle=detalle+detalle_ev[0]
			categoria=detalle_ev[1]
			precio=detalle_ev[2]
		if(len(detalle_ev)==2):
			detalle=detalle_ev[0]
			categoria=detalle_ev[1]
		if(len(detalle_ev)==1):
			detalle=detalle_ev[0]
		if(len(i.find_all(itemprop='streetAddress'))>0):
			direccion=i.find_all(itemprop='streetAddress')[0].text.strip()
			ubicacion=i.find_all(itemprop='addressLocality')[0].text.strip()
			ciudad=i.find_all(itemprop='addressRegion')[0].text.strip()
		# Se almacena los datos en el vector resultado
		elemento_lista=[fecha, nombre_evento, detalle, categoria, precio, direccion, ubicacion, ciudad]
		vector_resultado.append(elemento_lista)

# Se escribe el Archivo de salida
f = open("C:/Users/Usuario-03/py/resultado.csv", "w")
writer = csv.writer(f)
writer.writerows(vector_resultado)
f.close()
# ==============================================================================