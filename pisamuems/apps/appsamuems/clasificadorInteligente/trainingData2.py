training_data = {  # Datos para entrenar al clasificador

    #"Ciencia": [
    #    'https://es.wikipedia.org/wiki/Ciencia',  # Entrenamos al clasificador con paginas web.
    #    'https://es.wikipedia.org/wiki/Qu%C3%ADmica'
    #],
    #"Enfermedad": [
    #    'https://es.wikipedia.org/wiki/Enfermedad',
    #],
    #"Tecnologia": [
    #    'https://es.wikipedia.org/wiki/Tecnolog%C3%ADa',
    #],
    "Alergia": [
        'https://www.mayoclinic.org/es-es/diseases-conditions/allergies/symptoms-causes/syc-20351497',
        'https://medlineplus.gov/spanish/allergy.html',
        'https://cuidateplus.marca.com/enfermedades/alergias/alergia.html',
        'http://pacientes.seicap.es/es/-qu%C3%A9-es-la-alergia-_23832',
        #'https://es.wikipedia.org/wiki/Alergia',
        #'https://www.sanitas.es/sanitas/seguros/es/particulares/biblioteca-de-salud/prevencion-salud/que-es-alergia.html',
        #'https://www.sanitas.es/sanitas/seguros/es/particulares/biblioteca-de-salud/prevencion-salud/alergias-piel.html',
        #'https://alergia.leti.com/es/que-es-la-alergia_945',
        #'https://www.mayoclinic.org/es-es/diseases-conditions/allergies/symptoms-causes/syc-20351497',
        #'https://kidshealth.org/es/kids/allergies-esp.html'
    ],
    "Apendicitis": [
        'https://www.mayoclinic.org/es-es/diseases-conditions/appendicitis/symptoms-causes/syc-20369543',
        'https://cuidateplus.marca.com/enfermedades/digestivas/apendicitis.html',
        'https://medlineplus.gov/spanish/appendicitis.html',
        'https://medlineplus.gov/spanish/ency/article/000256.htm',
        #'https://www.radiologyinfo.org/sp/info.cfm?pg=appendicitis',
        #'https://kidshealth.org/es/parents/appendicitis-esp.html',
        #'https://www.portalfarma.com/Ciudadanos/saludpublica/consejosdesalud/Paginas/apendicitis.aspx',
        #'https://www.hospitalaleman.org.ar/prevencion/apendicitis-como-detectarla-a-tiempo/',
        #'https://www.healthychildren.org/Spanish/health-issues/conditions/abdominal/Paginas/Appendicitis-in-Teens.aspx',
        #'https://www.elconfidencial.com/alma-corazon-vida/2017-05-05/apendicitis-sintomas-dolor-tripa_1341368/'
    ],
    "Bronquiolitis": [
        'https://kidshealth.org/es/parents/bronchiolitis-esp.html',
        'https://www.mayoclinic.org/es-es/diseases-conditions/bronchiolitis/symptoms-causes/syc-20351565',
        'https://www.msdmanuals.com/es-co/professional/pediatr%C3%ADa/trastornos-respiratorios-en-ni%C3%B1os-peque%C3%B1os/bronquiolitis',
        'https://medlineplus.gov/spanish/ency/article/000975.htm',
        #'https://www.healthychildren.org/Spanish/health-issues/conditions/chest-lungs/Paginas/Bronchiolitis.aspx',
        #'https://www.stanfordchildrens.org/es/topic/default?id=bronquiolitis-90-P06022',
        #'http://www.familiaysalud.es/sintomas-y-enfermedades/sistema-respiratorio/bronquios-y-pulmones/llega-la-bronquiolitis-que-debemos',
        #'https://es.wikipedia.org/wiki/Bronquiolitis',
        #'https://es.familydoctor.org/condicion/bronquiolitis/',
        #'https://www.webconsultas.com/bebes-y-ninos/afecciones-tipicas-infantiles/bronquiolitis-aguda-que-es-y-causas'
    ],
    "Crisis asmática": [
        'https://kidshealth.org/es/parents/flare-up-esp.html',
        'https://kidshealth.org/es/teens/asthma-flare-up-esp.html',
        'https://www.connecticutchildrens.org/health-library/es/teens/flare-up-esp/',
        'https://www.mayoclinic.org/es-es/diseases-conditions/asthma-attack/symptoms-causes/syc-20354268',
        #'https://www.brennerchildrens.org/KidsHealth/Kids/Asthma-Center/Asthma-En-Espanol/Que-es-una-crisis-asmatica.htm',
        #'https://cuidateplus.marca.com/enfermedades/respiratorias/asma.html',
        #'https://www.analesdepediatria.org/es-tratamiento-crisis-asmatica-pediatria-articulo-13110615',
        #'https://accessmedicina.mhmedical.com/content.aspx?bookid=1846&sectionid=130559219',
        #'https://www.pfizerpro.es/news/asma-como-actuar-ante-una-crisis-de-asma',
        #'https://www.madrid.es/ficheros/SAMUR/data/310_01.htm'
    ],
    "Diabetes": [
        'https://cuidateplus.marca.com/enfermedades/digestivas/diabetes.html',
        'https://medlineplus.gov/spanish/diabetes.html',
        'https://www.niddk.nih.gov/health-information/informacion-de-la-salud/diabetes/informacion-general/que-es',
        'https://www.mayoclinic.org/es-es/diseases-conditions/diabetes/symptoms-causes/syc-20371444',
        #'https://www.fundaciondiabetes.org/infantil/176/que-es-la-diabetes-ninos',
        #'http://www.diabetes.org/es/informacion-basica-de-la-diabetes/',
        #'https://www.cdc.gov/diabetes/spanish/basics/diabetes.html',
        #'https://fundaciondelcorazon.com/prevencion/riesgo-cardiovascular/diabetes.html',
        #'http://www.msal.gob.ar/ent/index.php/informacion-para-ciudadanos/diabetes',
        #'https://www.sanitas.es/sanitas/seguros/es/particulares/biblioteca-de-salud/dieta-alimentacion/diabetes/que-es-diabetes.html'
    ],
    "Dolor abdominal": [
        'https://medlineplus.gov/spanish/ency/article/003120.htm',
        'https://medlineplus.gov/spanish/abdominalpain.html',
        'https://www.msdmanuals.com/es-co/hogar/trastornos-gastrointestinales/s%C3%ADntomas-de-los-trastornos-digestivos/dolor-abdominal-agudo',
        'https://empendium.com/manualmibe/chapter/B34.I.1.3.',
        #'https://www.cigna.com/individuals-families/health-wellness/hw-en-espanol/temas-de-salud/causas-del-dolor-abdominal-tv7118',
        #'https://www.mayoclinic.org/es-es/symptoms/abdominal-pain/basics/causes/sym-20050728',
        #'https://gi.org/patients/recursos-en-espanol/dolor-abdominal/',
        #'https://www.merckmanuals.com/es-us/hogar/trastornos-gastrointestinales/s%C3%ADntomas-de-los-trastornos-digestivos/dolor-abdominal-cr%C3%B3nico-y-recurrente',
        #'https://kidshealth.org/es/kids/abdominal-pain-esp.html',
        #'https://www.sabervivirtv.com/medicina-general/causas-dolor-estomago_737'
    ],
    #"Enfermedad cardiovascular": [
    #    'https://medlineplus.gov/spanish/ency/patientinstructions/000759.htm',
    #    'https://www.who.int/cardiovascular_diseases/about_cvd/es/',
    #    'http://www.msal.gob.ar/ent/index.php/informacion-para-ciudadanos/enfermedad-cardiovascular',
    #    'https://cuidateplus.marca.com/enfermedades/enfermedades-vasculares-y-del-corazon/factores-de-riesgo-cardiovascular.html',
    #    'https://www.mayoclinic.org/es-es/diseases-conditions/heart-disease/symptoms-causes/syc-20353118',
    #    'https://fundaciondelcorazon.com/informacion-para-pacientes/enfermedades-cardiovasculares.html',
    #    'https://www.cancer.gov/espanol/publicaciones/diccionario/def/enfermedad-cardiovascular',
    #    'https://www.paho.org/hq/index.php?option=com_topics&view=article&id=218&Itemid=40876&lang=es',
    #    'https://es.wikipedia.org/wiki/Enfermedades_cardiovasculares',
    #    'https://www.revespcardiol.org/es-promocion-salud-cardiovascular-global-estrategias-articulo-S0300893214001742'
    #],
    #"Enfermedad diarreica aguda": [
    #    'https://www.who.int/es/news-room/fact-sheets/detail/diarrhoeal-disease',
    #    'https://www.minsalud.gov.co/salud/publica/Paginas/enfermedades-diarreicas-agudas.aspx',
    #    'https://www.gob.mx/salud/articulos/enfermedades-diarreicas-agudas-edas',
    #    'https://consultorsalud.com/enfermedad-diarreica-aguda-eda-guia-de-practica-clinica-gpc/',
    #    'https://www.scielosp.org/article/rpsp/2005.v17n1/6-14/',
    #    'http://scielo.isciii.es/scielo.php?script=sci_arttext&pid=S1130-01082005000400009',
    #    'https://www.intramed.net/contenidover.asp?contenidoid=61686',
    #    'http://www.elhospitalblog.com/enfermedad-diarreica-aguda-en-ninos/',
    #    'https://www.ecured.cu/Enfermedad_Diarreica_Aguda',
    #    'https://www.emermedica.com.co/infografias-emermedica/enfermedad-diarreica-aguda/'
    #],
    #"Enfermedad pulmonar obstructiva": [
    #    'https://www.mayoclinic.org/es-es/diseases-conditions/copd/symptoms-causes/syc-20353679',
    #    'https://medlineplus.gov/spanish/ency/article/000091.htm',
    #    'https://cuidateplus.marca.com/enfermedades/respiratorias/epoc.html',
    #    'https://www.who.int/es/news-room/fact-sheets/detail/chronic-obstructive-pulmonary-disease-(copd)',
    #    'https://www.msdmanuals.com/es-co/professional/trastornos-pulmonares/enfermedad-pulmonar-obstructiva-cr%C3%B3nica-y-trastornos-relacionados/enfermedad-pulmonar-obstructiva-cr%C3%B3nica-epoc',
    #    'https://www.lung.org/espanol/epoc.html',
    #    'https://www.nhlbi.nih.gov/health-topics/espanol/epoc',
    #    'https://www.riojasalud.es/ciudadanos/catalogo-multimedia/neumologia/enfermedad-pulmonar-obstructiva-cronica-epoc',
    #    'https://www.tucuentasmucho.com/informacion/que-es-epoc/',
    #    'https://www.clinicbarcelona.org/asistencia/enfermedades/enfermedad-pulmonar-obstructiva-cronica-epoc'
    #],
    "Fractura": [
        'https://medlineplus.gov/spanish/fractures.html',
        'https://medlineplus.gov/spanish/ency/article/000001.htm',
        'https://cuidateplus.marca.com/ejercicio-fisico/diccionario/fractura.html',
        'https://www.efisioterapia.net/articulos/generalidades-las-fracturas',
        #'http://www.ahuce.org/Osteogenesis_imperfecta/Diagnostico_y_Manifestaciones_de_la_Osteogenesis/Que_es_una_fractura_osea.aspx',
        #'https://kidshealth.org/es/kids/broken-bones-esp.html',
        #'https://www.mayoclinic.org/es-es/first-aid/first-aid-fractures/basics/art-20056641',
        #'https://www.healthychildren.org/Spanish/health-issues/injuries-emergencies/sports-injuries/Paginas/Stress-Fractures.aspx',
        #'https://www.uv.es/sfpenlinia/cas/45_fracturas.html',
        #'https://www.msdmanuals.com/es-co/hogar/traumatismos-y-envenenamientos/fracturas,-luxaciones-y-esguinces/fracturas-de-la-mano'
    ],
    #"Hemorragia digestiva": [
    #    'https://medlineplus.gov/spanish/ency/article/003133.htm',
    #    'https://medlineplus.gov/spanish/gastrointestinalbleeding.html',
    #    'https://www.msdmanuals.com/es-co/hogar/trastornos-gastrointestinales/s%C3%ADntomas-de-los-trastornos-digestivos/hemorragia-digestiva',
    #    'https://www.mayoclinic.org/es-es/diseases-conditions/gastrointestinal-bleeding/symptoms-causes/syc-20372729',
    #   'https://www.cun.es/enfermedades-tratamientos/enfermedades/hemorragia-digestiva',
    #    'https://www.niddk.nih.gov/health-information/informacion-de-la-salud/enfermedades-digestivas/hemorragia-tracto-digestivo',
    #    'http://www.librodopeto.com/5-enfermedades-digestivas/51-hemorragia-digestiva-alta-y-baja/',
    #    'https://es.wikipedia.org/wiki/Hemorragia_gastrointestinal',
    #    'https://www.merckmanuals.com/es-pr/professional/trastornos-gastrointestinales/hemorragia-digestiva/rese%C3%B1a-sobre-hemorragia-digestiva',
    #    'https://www.elsevier.es/es-revista-medicina-integral-63-articulo-la-hemorragia-digestiva-aguda-10021655'
    #],
    "Infarto de miocardio": [
        'https://cuidateplus.marca.com/enfermedades/enfermedades-vasculares-y-del-corazon/infarto-miocardio.html',
        'http://cardioalianza.org/las-enfermedades-cardiovasculares/infarto-de-miocardio/',
        'https://medlineplus.gov/spanish/ency/article/000195.htm',
        'https://es.wikipedia.org/wiki/Infarto_agudo_de_miocardio',
        #'https://www.infosalus.com/enfermedades/cardiologia/infarto-miocardio/que-es-infarto-miocardio-23.html',
        #'https://www.cun.es/enfermedades-tratamientos/enfermedades/infarto-miocardio',
        #'https://www.msdmanuals.com/es-co/professional/trastornos-cardiovasculares/enfermedad-coronaria/infarto-agudo-de-miocardio-im',
        #'https://www.salud.mapfre.es/enfermedades/cardiovasculares/infarto-agudo-de-miocardio/',
        #'https://www.redclinica.cl/plantilla/especialidades/cardiologia/enfe_card/infarto-al-miocardio.aspx',
        #'https://www.hmhospitales.com/usuario-hm/apuntes-de-salud/infarto-agudo-de-miocardio'
    ],
    #"Lipotimia": [
    #    'https://cuidateplus.marca.com/enfermedades/enfermedades-vasculares-y-del-corazon/lipotimia.html',
    #    'https://www.fesemi.org/informacion-pacientes/conozca-mejor-su-enfermedad/sincope-y-lipotimia',
    #    'https://es.wikipedia.org/wiki/Lipotimia',
    #    'https://www.webconsultas.com/salud-al-dia/lipotimia/lipotimia-5831',
    #    'https://www.webconsultas.com/categoria/salud-al-dia/lipotimia',
    #    'http://www.damsu.uncuyo.edu.ar/lipotimiaprimeros-auxilios',
    #    'http://www.teknon.es/es/especialidades/rius-gelabert-teresa/sincope-lipotimia',
    #    'http://www3.gobiernodecanarias.org/medusa/mediateca/publicaciones/?attachment_id=49',
    #    'https://www.ecured.cu/Lipotimia',
    #    'https://www.cun.es/diccionario-medico/terminos/lipotimia'
    #],
    "Neumonia": [
        'https://www.mayoclinic.org/es-es/diseases-conditions/pneumonia/symptoms-causes/syc-20354204',
        'https://medlineplus.gov/spanish/ency/article/000145.htm',
        'https://medlineplus.gov/spanish/pneumonia.html',
        'https://cuidateplus.marca.com/enfermedades/respiratorias/neumonia.html',
        #'https://kidshealth.org/es/teens/pneumonia-esp.html',
        #'https://www.who.int/es/news-room/fact-sheets/detail/pneumonia',
        #'https://www.sanitas.es/sanitas/seguros/es/particulares/biblioteca-de-salud/prevencion-salud/neumonia.html',
        #'https://www.msdmanuals.com/es-co/hogar/trastornos-del-pulm%C3%B3n-y-las-v%C3%ADas-respiratorias/neumon%C3%ADa/introducci%C3%B3n-a-la-neumon%C3%ADa',
        #'https://www.cun.es/enfermedades-tratamientos/enfermedades/neumonia',
        #'https://www.healthychildren.org/Spanish/health-issues/conditions/chest-lungs/Paginas/Pneumonia.aspx'
    ],
    "Politraumatismo": [
        'https://www.elsevier.es/es-revista-medicina-integral-63-articulo-politraumatismo-craneoencefalico-toracicoabdominal-medular-13020961',
        'https://www.cun.es/diccionario-medico/terminos/politraumatismo',
        'https://www.intramed.net/contenidover.asp?contenidoid=35629',
        'https://www.ecured.cu/Politraumatismo',
        #'http://scielo.sld.cu/scielo.php?script=sci_arttext&pid=S1029-30192014000500010',
        #'https://www.sciencedirect.com/science/article/abs/pii/S1286935X12618978',
        #'https://www.sciencedirect.com/science/article/abs/pii/S1286935X02722557',
        #'http://scielo.sld.cu/scielo.php?script=sci_arttext&pid=S0138-65572017000200008',
        #'http://scielo.isciii.es/scielo.php?script=sci_arttext&pid=S0212-16112005000500014',
        #'http://skorpiomenlamedicina.blogspot.com/2012/02/politraumatismo.html'
    ]
}
