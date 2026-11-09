# Zammad development: svensk API-granskning och import, 9 november 2026

Zammad är ett ärendehanteringssystem för kundsupport. Den aktuella svenska
development-komponenten granskades lokalt med fokus på dess AI-/MCP-funktioner,
kunskapsbas, aviseringar, sökning, kalender och supportärenden.

Den initiala lokala exporten från 2 november innehöll 88 redigeringsmarkerade
och 8 tomma poster. En kontextgranskad deltafil med 96 poster skapades. Den
kontrollerades med `msgfmt`, l10n-lint, svlang, Hunspell-sv och Gitleaks.
Hunspell-sv:s kvarvarande träffar är verifierade produkt- eller facktermer,
bland annat *MCP*, *HMAC*, *Elasticsearch*, *Zammad* och HTTP-rubriknamn.

Weblate API-importen accepterade 20 poster och avvisade 76 som `not_found`.
Ingen ersättning tvingades igenom: API:t visade därefter revision
`bbab371003dcc835182ac295b935c2b42a323221`, 5 325 av 5 325 översatta
poster och inga fuzzy- eller tomma poster. De 76 avvisade posterna hörde till
en äldre lokal källrevision och finns inte i den aktuella serverkatalogen.

Filen `zammad-zammad-development-sv-reviewed-20261109.po` är arkiverad som
evidens för de granskade förslagen. Endast de 20 accepterade posterna är
verifierat inskickade till Zammad Weblate. Kontot har inte behörighet att
godkänna poster, så accepterade ändringar ligger som översättningar för
projektets granskning.
