# Sparade ändringar – 2026-11-19 (granskning 7021–7260)

Samtliga nio poster matchade aktuell Lokalise-källa och lästes tillbaka efter sparning.

## `component::mcp_server::options::step::init::data_description::read_only`

**Engelska:** Only expose tools that are marked as not changing anything.

**Befintlig svenska:** Exponera bara reglage som inte ändrar något.

**Sparad svenska:** Exponera bara verktyg som är markerade som att de inte ändrar något.

**Motivering:** Förbättrar svensk terminologi eller formulering utan betydelseförändring.

## `component::vicare::services::set_circulation_schedule::fields::monday::description`

**Engelska:** Circulation slots for this day. Each slot has a from and to time on a 10-minute grid (use 00:00 or 24:00 as end time for the end of the day) and a circulation mode supported by the device. Days not passed keep their current schedule.

**Befintlig svenska:** Cirkulationsintervall för denna dag. Varje intervall har en start- och sluttid i ett tiominutersrutnät, använd 00:00 eller 24:00 som sluttid för dagens slut och ett cirkulationsläge som stöds av enheten. Dagar som inte skickas behåller sitt nuvarande schema.

**Sparad svenska:** Cirkulationsintervall för den här dagen. Varje intervall har en start- och sluttid i steg om 10 minuter (använd 00:00 eller 24:00 som sluttid vid dagens slut) och ett cirkulationsläge som stöds av enheten. Dagar som inte anges behåller sitt nuvarande schema.

**Motivering:** Förbättrar svensk terminologi eller formulering utan betydelseförändring.

## `component::vicare::exceptions::api_error::message`

**Engelska:** Unable to communicate with the ViCare API

**Befintlig svenska:** Det gick inte att kommunicera med ViCare API.

**Sparad svenska:** Det gick inte att kommunicera med ViCare-API:t.

**Motivering:** Förbättrar svensk terminologi eller formulering utan betydelseförändring.

## `component::http::issues::ssl_profile_outdated::fix_flow::step::init::menu_options::ignore`

**Engelska:** Keep the current profile

**Befintlig svenska:** Behåll den aktuella profilen och ignorera reparationen

**Sparad svenska:** Behåll den aktuella profilen

**Motivering:** Förbättrar svensk terminologi eller formulering utan betydelseförändring.

## `component::http::issues::ssl_profile_outdated::fix_flow::step::init::menu_options::confirm_intermediate_v6`

**Engelska:** Upgrade to Intermediate v6 (recommended)

**Befintlig svenska:** Uppgradera till Intermediate v6, behåller TLS 1.2 (rekommenderas)

**Sparad svenska:** Uppgradera till Intermediate v6 (rekommenderas)

**Motivering:** Förbättrar svensk terminologi eller formulering utan betydelseförändring.

## `component::http::issues::ssl_profile_outdated::fix_flow::step::init::description`

**Engelska:** Your Home Assistant's HTTPS encryption settings are outdated. They use `{profile}`, which is based on Mozilla's TLS recommendations from 2016 (version 4) and still allows older encryption methods that are no longer considered secure. Your SSL certificate is not affected and does not need to change.

This only affects devices and apps that connect to Home Assistant over HTTPS, such as browsers, the Home Assistant apps, wall tablets, devices that call webhooks, and speakers that play text-to-speech or media from Home Assistant. Connections Home Assistant makes to your devices and services are not affected.

We recommend upgrading to **Intermediate v6**, based on the current recommendations (version 6). It accepts TLS 1.2 and TLS 1.3, but only with current encryption methods, so it works with almost all devices and apps.

Choose **Modern v6** only if you know that everything connecting to Home Assistant supports TLS 1.3. Current browsers do, but some smart home devices, older speakers, and phones or tablets older than Android 10 do not.

Oldest supported clients:

| Profile | Chrome | Firefox | Safari | iOS | Android | Edge |
| --- | --- | --- | --- | --- | --- | --- |
| Intermediate v6 | 49 | 31 | 9 | 9 | 4.4 | 15 |
| Modern v6 | 70 | 63 | 12.1 | 12.2 | 10 | 75 |

If you can no longer reach Home Assistant after the restart, it switches back to `{profile}` automatically after 5 minutes. You can close this dialog to decide later, or change the profile at any time under **Settings** > **System** > **Network** > **HTTP server** > **SSL/TLS**.

**Befintlig svenska:** HTTP-servern använder SSL-profilen `{profile}`, som följer Mozillas föråldrade TLS-riktlinjer: den accepterar TLS 1.2 och senare, men tillåter fortfarande äldre krypteringar som CBC-sviter, RSA-nyckelutbyte eller DHE.

Vi rekommenderar **Modern v6**, som endast accepterar TLS 1.3. Webbläsare, mobilappar och operativsystem har haft stöd för TLS 1.3 sedan omkring 2018 till 2019, så de flesta uppsättningar påverkas inte. Välj i stället **Intermediate v6** om enheter som slutade få uppdateringar före dess, till exempel äldre smarta TV-apparater, kameror eller hubbar, ansluter direkt till Home Assistant. Den accepterar TLS 1.2 och senare med aktuella krypteringar.

Äldsta klienter som kan ansluta:

| Profil | Chrome | Firefox | Safari | iOS | Android | Edge |
| --- | --- | --- | --- | --- | --- | --- |
| Modern v6 | 70 | 63 | 12.1 | 12.2 | 10 | 75 |
| Intermediate v6 | 49 | 31 | 9 | 9 | 4.4 | 15 |

Klienter som är beroende av de äldre krypteringarna, till exempel Windows 7 och 8.1 med Internet Explorer eller annan TLS på systemnivå och ett RSA-certifikat, kan bara fortsätta ansluta med `{profile}`.

Båda uppgraderingarna tillämpas på prov och återställs automatiskt om du inte bekräftar den nya konfigurationen inom fem minuter. Du kan stänga dialogrutan och bestämma senare eller när som helst ändra profilen under **Inställningar** > **System** > **Nätverk** > **HTTP-server** > **SSL/TLS**.

**Sparad svenska:** Home Assistants inställningar för HTTPS-kryptering är föråldrade. De använder `{profile}`, som bygger på Mozillas TLS-rekommendationer från 2016 (version 4) och fortfarande tillåter äldre krypteringsmetoder som inte längre anses säkra. Ditt SSL-certifikat påverkas inte och behöver inte ändras.

Det här påverkar bara enheter och appar som ansluter till Home Assistant via HTTPS, till exempel webbläsare, Home Assistant-apparna, väggmonterade surfplattor, enheter som anropar webhooks och högtalare som spelar upp tal eller media från Home Assistant. Anslutningar som Home Assistant gör till dina enheter och tjänster påverkas inte.

Vi rekommenderar att du uppgraderar till **Intermediate v6**, som bygger på de aktuella rekommendationerna (version 6). Den accepterar TLS 1.2 och TLS 1.3, men bara med aktuella krypteringsmetoder, och fungerar därför med nästan alla enheter och appar.

Välj **Modern v6** bara om du vet att allt som ansluter till Home Assistant stöder TLS 1.3. Aktuella webbläsare gör det, men vissa smarta hemenheter, äldre högtalare och telefoner eller surfplattor med äldre versioner än Android 10 gör det inte.

Äldsta klienter som stöds:

| Profil | Chrome | Firefox | Safari | iOS | Android | Edge |
| --- | --- | --- | --- | --- | --- | --- |
| Intermediate v6 | 49 | 31 | 9 | 9 | 4.4 | 15 |
| Modern v6 | 70 | 63 | 12.1 | 12.2 | 10 | 75 |

Om du inte längre kan nå Home Assistant efter omstarten återgår systemet automatiskt till `{profile}` efter 5 minuter. Du kan stänga dialogrutan och bestämma senare eller när som helst ändra profilen under **Inställningar** > **System** > **Nätverk** > **HTTP-server** > **SSL/TLS**.

**Motivering:** Förbättrar svensk terminologi eller formulering utan betydelseförändring.

## `component::http::issues::ssl_profile_outdated::fix_flow::step::confirm_modern_v6::description`

**Engelska:** Home Assistant will restart and use the **Modern v6** profile. Devices and apps without TLS 1.3 support will no longer be able to connect, for example some smart home devices, older speakers, or phones and tablets older than Android 10.

After the restart, confirm the new configuration within 5 minutes once Home Assistant opens in your browser. If you don't confirm, for example because you can no longer connect, Home Assistant restores the `{profile}` profile automatically.

Afterwards, check that devices that connect to Home Assistant using HTTPS still work, for example speakers playing media from Home Assistant or devices calling webhooks. If something can no longer connect, switch back under **Settings** > **System** > **Network** > **HTTP server** > **SSL/TLS**.

**Befintlig svenska:** Home Assistant startar om med profilen **Modern v6** och ber dig bekräfta den nya konfigurationen. Klienter utan stöd för TLS 1.3 kan inte längre ansluta. Om du inte bekräftar inom fem minuter återställs profilen `{profile}` automatiskt.

**Sparad svenska:** Home Assistant startar om och använder profilen **Modern v6**. Enheter och appar utan stöd för TLS 1.3 kan inte längre ansluta, till exempel vissa smarta hemenheter, äldre högtalare samt telefoner och surfplattor med äldre versioner än Android 10.

Bekräfta den nya konfigurationen inom 5 minuter efter omstarten när Home Assistant öppnas i webbläsaren. Om du inte bekräftar, till exempel för att du inte längre kan ansluta, återställer Home Assistant automatiskt profilen `{profile}`.

Kontrollera därefter att enheter som ansluter till Home Assistant via HTTPS fortfarande fungerar, till exempel högtalare som spelar upp media från Home Assistant eller enheter som anropar webhooks. Om något inte längre kan ansluta kan du byta tillbaka under **Inställningar** > **System** > **Nätverk** > **HTTP-server** > **SSL/TLS**.

**Motivering:** Förbättrar svensk terminologi eller formulering utan betydelseförändring.

## `component::http::issues::ssl_profile_outdated::fix_flow::step::confirm_intermediate_v6::description`

**Engelska:** Home Assistant will restart and use the **Intermediate v6** profile. Clients that rely on the older encryption methods will no longer be able to connect, for example Internet Explorer or other apps using the built-in encryption of Windows 7 or 8.1 if your certificate uses an RSA key.

After the restart, confirm the new configuration within 5 minutes once Home Assistant opens in your browser. If you don't confirm, for example because you can no longer connect, Home Assistant restores the `{profile}` profile automatically.

Afterwards, check that devices that connect to Home Assistant using HTTPS still work, for example speakers playing media from Home Assistant or devices calling webhooks. If something can no longer connect, switch back under **Settings** > **System** > **Network** > **HTTP server** > **SSL/TLS**.

**Befintlig svenska:** Home Assistant startar om med profilen **Intermediate v6** och ber dig bekräfta den nya konfigurationen. Klienter som är beroende av de äldre krypteringarna i `{profile}`, till exempel Windows 7 och 8.1 med Internet Explorer eller annan TLS på systemnivå och ett RSA-certifikat, kan inte längre ansluta. Om du inte bekräftar inom fem minuter återställs profilen `{profile}` automatiskt.

**Sparad svenska:** Home Assistant startar om och använder profilen **Intermediate v6**. Klienter som är beroende av äldre krypteringsmetoder kan inte längre ansluta, till exempel Internet Explorer eller andra appar som använder den inbyggda krypteringen i Windows 7 eller 8.1 om ditt certifikat använder en RSA-nyckel.

Bekräfta den nya konfigurationen inom 5 minuter efter omstarten när Home Assistant öppnas i webbläsaren. Om du inte bekräftar, till exempel för att du inte längre kan ansluta, återställer Home Assistant automatiskt profilen `{profile}`.

Kontrollera därefter att enheter som ansluter till Home Assistant via HTTPS fortfarande fungerar, till exempel högtalare som spelar upp media från Home Assistant eller enheter som anropar webhooks. Om något inte längre kan ansluta kan du byta tillbaka under **Inställningar** > **System** > **Nätverk** > **HTTP-server** > **SSL/TLS**.

**Motivering:** Förbättrar svensk terminologi eller formulering utan betydelseförändring.

## `component::http::issues::ssl_profile_outdated::fix_flow::abort::pending_config`

**Engelska:** Another HTTP configuration change is waiting to be applied or confirmed. Confirm or revert it first, then try again.

**Befintlig svenska:** En ny HTTP-konfiguration väntar redan på att tillämpas eller bekräftas. Bekräfta eller återställ den först.

**Sparad svenska:** En annan ändring av HTTP-konfigurationen väntar på att tillämpas eller bekräftas. Bekräfta eller återställ den först och försök sedan igen.

**Motivering:** Förbättrar svensk terminologi eller formulering utan betydelseförändring.