# HA-termer verifierade i granskningen 2026-11-25

## Matter: Occupied setback

Core exponerar `ThermostatOccupiedSetback` som ett temperaturvärde. Matter-specifikationen beskriver det som en temperaturavvikelse som tillåts från termostatens börvärde. Därför används `Tillåten temperaturavvikelse vid närvaro`; `Temperatursänkning` skulle felaktigt ange en riktning.

Källa: [Matter Application Cluster Specification R1.1](https://csa-iot.org/wp-content/uploads/2023/05/matter-1-1-application-cluster-specification.pdf), avsnitt om `OccupiedSetback`.

## Yardian: water hammer

Yardian låter bevattningszoner överlappa under en inställbar tid för att minska tryckslag när ventiler stänger. `Tryckslag` används för fenomenet; sensorns namn översätts som `Överlappningstid för att minska tryckslag`.

Källa: [Yardian Water Hammer Reduction](https://www.yardian.com/blogs/guides/water-hammer-reduction/).

## HDFury: Issue hotplug

Home Assistant beskriver knappen som ett kommando till anslutna TX- och RX-enheter. Etiketten `Skicka hotplug-signal` anger knappens handling; `hotplug` behålls som protokollterm.

Källa: [Home Assistant HDFury](https://www.home-assistant.io/integrations/hdfury/).
