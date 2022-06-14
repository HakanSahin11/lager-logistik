Forked Kopi af det der er lavet indtil videre i projektets hovedgruppe.

# Lager og logistik system
Vi har brug for at system som kan tage stregkode fra udstyr og gemme det i en simpel database. Data kommer i første omgang fra en csv fra inventar systemet.

# Todo
- [ ] Definere Hardware - software grænseflader
- [ ] Definere API endpoints. Hvad skal systemet snakke sammen med og hvordan
- [ ] Mangler at færdiggøre dokumentation
- [ ] Definere opsætning af CI/CD miljø
- [ ] Hvordan skal den hostes?
- [ ] Fastlæggelse af Python udvikling miljø
- [ ] Fastlægge modeller (db felter) som er nødvendige
- [ ] Hvordan styrer man Python virtuelt miljø i forhold til container (eks. Docker) udvikling<br />Læs evt.: [Should I use virtualenv or Docker containers with Python?](https://coderbook.com/@marcus/should-i-use-virtualenv-or-docker-containers-with-python/)
- [ ] Fastlæggelse af braches
- [ ] Fastlægge udseende på stregkode
- [ ] Få stregkoden ud på Dymo

# Python udviklingsmiljø
* Python 3.9
* Pylance - intellisense
* Pylint
* Django 4.0.4
* Virtuelt miljø -> Docker miljø -> Kubernetes miljø

# Struktur
```
├── dokumentation
│   ├── Inspiration
│   ├── Stregkode
│   └── Orig mindmap
├── backend
│   └── __pycache__
├── frontend
│   ├── migrations
│   │   └── __pycache__
│   ├── __pycache__
│   └── static
│       ├── data
│       ├── img
│       ├── javascript
│       └── css
├── db.sqlite3
├── Dockerfile              // command line to assemble an image
├── Dockerfile-compose-dev  // define and start multi-container applikation - Development
├── Dockerfile-compose-prod // define and start multi-container applikation - Production
├── LICENCE                 // MIT licence
├── README.md               // This file
└── requirements.txt        // Python libraries
```

# Ordforklaring
* API (står for Application Programming Interface) en fælles grænseflade som to (eller flere) systemer kan bruger til at udveksle data. Det giver stor frihed til at benytte forskellige teknologier med fælles tilgang (interface) for andre programmer.
* REST er en software arkitektur
* REST api bruger JSON formattet til at udveksling af data. Er som udgangspunkt stateless dvs. kald til api kan foregå uafhængigt af hinanden
* RESTful. En applikation, der implementerer en RESTful API, definerer et eller flere URL-slutpunkter med et domæne, port, sti og / eller forespørgselsstreng - for eksempel https: // mitdomæne / bruger / 123? Format = json. Eksempler: ... en PUT-anmodning til / bruger / 123 opdaterer bruger 123 med kroppens data. en GET-anmodning til / bruger / 123 returnerer detaljerne om bruger 123.
* JSON er et akronym for JavaScript objekt notation. JSON er et format til strukturering af data, der sendes frem og tilbage via en API. JSON er et alternativ til XML. REST API'er reagerer mere almindeligt med JSON - et åbent standardformat, der bruger menneskelig læsbar tekst til at transmittere dataobjekter bestående af attributværdipar.

# Inspiration og tutorials
* Django REST framework - Quickstart<br />
https://www.django-rest-framework.org/tutorial/quickstart/
* Django Rest Framework – An Introduction<br />
https://realpython.com/django-rest-framework-quick-start/
* How to create a REST API with Django REST framework<br />
https://blog.logrocket.com/django-rest-framework-create-api/
* Python® Notes for Professionals book<br />https://books.goalkicker.com/PythonBook/
