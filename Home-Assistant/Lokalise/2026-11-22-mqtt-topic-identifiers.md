# MQTT: återställda ämnesidentifierare

`component::mqtt::issues::topic_template_deprecation::description` rättades
via Lokalise API den 22 november 2026. De maskinella alternativen
`topic_template` och `topic`, samt platshållarna `{topic}` och
`{topic_template}`, hade förlorat kodmarkering och `topic` hade felaktigt
översatts till ”ämne”. Samtliga återställdes som kod och värdet lästes tillbaka
efter sparning.
