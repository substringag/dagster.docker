=Getting started=

== Step 1: Image erstellen ==
`$ ./build_image.sh`

== Step 2: Container erstellen & starten ==
`$ docker-compose up`

Falls der Container bereits erstellt wurde kann man den bestehenden Container einfach wieder starten.
`$ docker-compose start`

== Step 3: IP adresse erkennen ==
`$ docker inspect dagstertest`

== Step 4: Web-Interface öffnen ==
https://172.20.0.2:3000 (hier die richtige IP einsetzen)