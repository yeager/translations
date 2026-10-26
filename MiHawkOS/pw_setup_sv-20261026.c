/* SPDX-License-Identifier: GPL-3.0-or-later */
/* The guided setup's steps, languages, text and record (pw_setup.h). */
#include "pw_setup.h"

#include <errno.h>
#include <math.h>
#include <stdio.h>
#include <string.h>
#include <unistd.h>

PwSetupStep pw_setup_start(const PwSetupFacts *facts)
{
    if (!facts->data) return PW_SETUP_NONE;
    if (facts->returning) return facts->prefix ? PW_SETUP_DONE : PW_SETUP_PREPARING;
    if (facts->asked || !facts->done) return PW_SETUP_WELCOME;
    if (!facts->runtime) return PW_SETUP_METHOD;
    if (!facts->prefix) return PW_SETUP_PREPARING;
    return PW_SETUP_NONE;
}

PwSetupStep pw_setup_next(PwSetupStep step, const PwSetupFacts *facts)
{
    switch (step) {
    case PW_SETUP_WELCOME: return PW_SETUP_LANGUAGE;
    case PW_SETUP_LANGUAGE: return PW_SETUP_METHOD;
    case PW_SETUP_METHOD: return facts->runtime ? pw_setup_next(PW_SETUP_INSTALLING, facts) : PW_SETUP_USB;
    case PW_SETUP_USB: return PW_SETUP_INSTALLING;
    case PW_SETUP_INSTALLING: return facts->prefix ? PW_SETUP_DONE : PW_SETUP_PREPARING;
    case PW_SETUP_PREPARING: return PW_SETUP_DONE;
    default: return PW_SETUP_NONE;
    }
}

PwSetupStep pw_setup_back(PwSetupStep step)
{
    switch (step) {
    case PW_SETUP_LANGUAGE: return PW_SETUP_WELCOME;
    case PW_SETUP_METHOD: return PW_SETUP_LANGUAGE;
    case PW_SETUP_USB: return PW_SETUP_METHOD;
    case PW_SETUP_PREPARING: return PW_SETUP_METHOD;
    default: return PW_SETUP_NONE;
    }
}

/* English (US). */
static const char *const text_en[PW_TEXT_COUNT] = {
    [PW_TEXT_WELCOME_TITLE] = "Welcome to MihawkOS",
    [PW_TEXT_WELCOME_BODY] = "Let’s get your PS5 ready for Windows games. It takes about ten minutes.",
    [PW_TEXT_GET_STARTED] = "Get started",
    [PW_TEXT_SKIP_SETUP] = "Skip setup",
    [PW_TEXT_LANGUAGE_TITLE] = "Choose your language",
    [PW_TEXT_LANGUAGE_BODY] = "Your Windows games use it too, with its keyboard layout. The Mihawk OS desktop stays in English.",
    [PW_TEXT_METHOD_TITLE] = "Choose how to install",
    [PW_TEXT_METHOD_BODY] = "MihawkOS needs its Windows runtime, about 1.2 GB.",
    [PW_TEXT_METHOD_USB] = "USB drive",
    [PW_TEXT_METHOD_USB_BODY] = "Copy the files to a USB drive on any computer.",
    [PW_TEXT_METHOD_INTERNET] = "Internet",
    [PW_TEXT_METHOD_INTERNET_BODY] = "Download straight to your PS5.",
    [PW_TEXT_COMING_SOON] = "Coming soon",
    [PW_TEXT_METHOD_INSTALLED] = "The Windows runtime is already installed.",
    [PW_TEXT_CONTINUE] = "Continue",
    [PW_TEXT_QR_CAPTION] = "Scan for step-by-step instructions on your phone.",
    [PW_TEXT_USB_TITLE] = "Prepare a USB drive",
    [PW_TEXT_USB_STEP1] = "On a computer, format a USB drive as exFAT with an MBR partition table. This erases the drive.",
    [PW_TEXT_USB_STEP2] = "Download MihawkOS and copy its mihawkos folder to the top of the drive.",
    [PW_TEXT_USB_STEP3] = "Plug the drive into a USB port on your PS5.",
    [PW_TEXT_USB_STEP4] = "Choose Check drive.",
    [PW_TEXT_CHECK_DRIVE] = "Check drive",
    [PW_TEXT_FOUND] = "The drive holds {1} to install.",
    [PW_TEXT_INSTALL] = "Install",
    [PW_TEXT_RETRY] = "Try again",
    [PW_TEXT_ERR_NO_STICK] = "No USB drive found. Plug it in, wait a few seconds, then try again. If it is already in, "
        "format it as exFAT with MBR: the PS5 does not read GPT or NTFS drives.",
    [PW_TEXT_ERR_NO_FOLDER] = "The drive has no mihawkos folder at its top. Copy the folder to the drive, then try again.",
    [PW_TEXT_ERR_PARTIAL] = "The mihawkos folder is incomplete: it has {1} of {2} pieces. Copy the whole folder again, "
        "then try again.",
    [PW_TEXT_ERR_NO_SPACE] = "Your PS5 needs {1} free and has {2}. Delete something, then try again.",
    [PW_TEXT_ERR_READ] = "The USB drive could not be read. Check that it is still plugged in, then try again. What is "
        "already installed is kept.",
    [PW_TEXT_ERR_DAMAGED] = "A file on the drive is damaged or from another version. Copy the mihawkos folder again, "
        "then try again.",
    [PW_TEXT_ERR_FULL] = "Your PS5’s storage is full. Delete something, then try again. What is already installed "
        "is kept.",
    [PW_TEXT_ERR_WRITE] = "Your PS5’s storage refused a write. Try again; if it happens again, restart the PS5.",
    [PW_TEXT_ERR_CANCELLED] = "The install stopped. What is already installed is kept.",
    [PW_TEXT_ERR_BUILD] = "This copy of MihawkOS cannot install a Windows runtime. Reinstall MihawkOS.",
    [PW_TEXT_INSTALLING_TITLE] = "Installing the Windows runtime",
    [PW_TEXT_INSTALLING_BODY] = "Keep the drive plugged in. This takes about a minute.",
    [PW_TEXT_INSTALLING_CHECKING] = "Checking what is already installed…",
    [PW_TEXT_INSTALLING_STATS] = "{1} of {2} MB · {3} MB/s",
    [PW_TEXT_INSTALLED] = "Installed.",
    [PW_TEXT_STOP] = "Stop",
    [PW_TEXT_PREPARE_TITLE] = "Preparing Mihawk OS",
    [PW_TEXT_PREPARE_BODY] = "The first start builds your Windows drive. It takes a few minutes, and the screen may stay "
        "still for a while. It ends by itself and comes back here.",
    [PW_TEXT_PREPARE_NOTE] = "During this first start the controller does not work in games, so MihawkOS ends it as "
        "soon as the drive is ready.",
    [PW_TEXT_PREPARE_START] = "Start",
    [PW_TEXT_PREPARE_FAILED] = "The first start did not finish. Try again: it carries on where it stopped.",
    [PW_TEXT_BUILD_TITLE] = "Building your Windows drive",
    [PW_TEXT_BUILD_BODY] = "This takes about a minute. When the drive is ready, MihawkOS comes back to the setup by "
        "itself.",
    [PW_TEXT_BUILD_SETTINGS] = "Setting up Windows",
    [PW_TEXT_BUILD_DOTNET] = "Installing .NET support",
    [PW_TEXT_BUILD_FINISHING] = "Finishing up",
    [PW_TEXT_DONE_TITLE] = "You’re all set",
    [PW_TEXT_DONE_BODY] = "Mihawk OS is ready. You can run this setup again from Settings, in the library.",
    [PW_TEXT_ENTER] = "Enter Mihawk OS",
    [PW_TEXT_HINT_SELECT] = "Select",
    [PW_TEXT_HINT_BACK] = "Back",
    [PW_TEXT_HINT_MOVE] = "Move",
    [PW_TEXT_STEP_OF] = "Step {1} of {2}",
    [PW_TEXT_GIGABYTES] = "{1} GB",
    [PW_TEXT_DECIMAL] = ".",
};

/* Svenska (Sverige). */
static const char *const text_sv[PW_TEXT_COUNT] = {
    [PW_TEXT_WELCOME_TITLE] = "Välkommen till MihawkOS",
    [PW_TEXT_WELCOME_BODY] = "Vi gör din PS5 redo för Windows-spel. Det tar ungefär tio minuter.",
    [PW_TEXT_GET_STARTED] = "Kom i gång",
    [PW_TEXT_SKIP_SETUP] = "Hoppa över konfigurationen",
    [PW_TEXT_LANGUAGE_TITLE] = "Välj språk",
    [PW_TEXT_LANGUAGE_BODY] = "Dina Windows-spel använder också språket och dess tangentbordslayout. Mihawk OS-skrivbordet är på engelska.",
    [PW_TEXT_METHOD_TITLE] = "Välj hur du vill installera",
    [PW_TEXT_METHOD_BODY] = "MihawkOS behöver sin Windows-miljö, ungefär 1,2 GB.",
    [PW_TEXT_METHOD_USB] = "USB-enhet",
    [PW_TEXT_METHOD_USB_BODY] = "Kopiera filerna till en USB-enhet på valfri dator.",
    [PW_TEXT_METHOD_INTERNET] = "Internet",
    [PW_TEXT_METHOD_INTERNET_BODY] = "Hämta filerna direkt till PS5:an.",
    [PW_TEXT_COMING_SOON] = "Kommer snart",
    [PW_TEXT_METHOD_INSTALLED] = "Windows-miljön är redan installerad.",
    [PW_TEXT_CONTINUE] = "Fortsätt",
    [PW_TEXT_QR_CAPTION] = "Skanna för stegvisa instruktioner på telefonen.",
    [PW_TEXT_USB_TITLE] = "Förbered en USB-enhet",
    [PW_TEXT_USB_STEP1] = "Formatera en USB-enhet på en dator som exFAT med MBR-partitionstabell. Då raderas enheten.",
    [PW_TEXT_USB_STEP2] = "Hämta MihawkOS och kopiera mappen mihawkos till enhetens rot.",
    [PW_TEXT_USB_STEP3] = "Anslut enheten till en USB-port på PS5:an.",
    [PW_TEXT_USB_STEP4] = "Välj Kontrollera enhet.",
    [PW_TEXT_CHECK_DRIVE] = "Kontrollera enhet",
    [PW_TEXT_FOUND] = "Enheten innehåller {1} som kan installeras.",
    [PW_TEXT_INSTALL] = "Installera",
    [PW_TEXT_RETRY] = "Försök igen",
    [PW_TEXT_ERR_NO_STICK] = "Ingen USB-enhet hittades. Anslut den, vänta några sekunder och försök sedan igen. Om den redan är ansluten, formatera den som exFAT med MBR: PS5:an kan inte läsa GPT- eller NTFS-enheter.",
    [PW_TEXT_ERR_NO_FOLDER] = "Enheten saknar mappen mihawkos i roten. Kopiera mappen till enheten och försök sedan igen.",
    [PW_TEXT_ERR_PARTIAL] = "Mappen mihawkos är ofullständig: den innehåller {1} av {2} delar. Kopiera hela mappen igen och försök sedan igen.",
    [PW_TEXT_ERR_NO_SPACE] = "PS5:an behöver {1} ledigt utrymme och har {2}. Ta bort något och försök sedan igen.",
    [PW_TEXT_ERR_READ] = "Det gick inte att läsa USB-enheten. Kontrollera att den fortfarande är ansluten och försök igen. Det som redan är installerat behålls.",
    [PW_TEXT_ERR_DAMAGED] = "En fil på enheten är skadad eller kommer från en annan version. Kopiera mappen mihawkos igen och försök sedan igen.",
    [PW_TEXT_ERR_FULL] = "PS5:ans lagring är full. Ta bort något och försök sedan igen. Det som redan är installerat behålls.",
    [PW_TEXT_ERR_WRITE] = "PS5:ans lagring kunde inte skriva data. Försök igen. Starta om PS5:an om det händer igen.",
    [PW_TEXT_ERR_CANCELLED] = "Installationen stoppades. Det som redan är installerat behålls.",
    [PW_TEXT_ERR_BUILD] = "Den här kopian av MihawkOS kan inte installera en Windows-miljö. Installera om MihawkOS.",
    [PW_TEXT_INSTALLING_TITLE] = "Installerar Windows-miljön",
    [PW_TEXT_INSTALLING_BODY] = "Låt enheten vara ansluten. Det tar ungefär en minut.",
    [PW_TEXT_INSTALLING_CHECKING] = "Kontrollerar det som redan är installerat…",
    [PW_TEXT_INSTALLING_STATS] = "{1} av {2} MB · {3} MB/s",
    [PW_TEXT_INSTALLED] = "Installerat.",
    [PW_TEXT_STOP] = "Stoppa",
    [PW_TEXT_PREPARE_TITLE] = "Förbereder Mihawk OS",
    [PW_TEXT_PREPARE_BODY] = "Första starten bygger din Windows-enhet. Det tar några minuter och skärmen kan stå still en stund. Programmet avslutas automatiskt och återgår hit.",
    [PW_TEXT_PREPARE_NOTE] = "Handkontrollen fungerar inte i spel under den första starten, så MihawkOS avslutar den när enheten är klar.",
    [PW_TEXT_PREPARE_START] = "Starta",
    [PW_TEXT_PREPARE_FAILED] = "Första starten slutfördes inte. Försök igen; den fortsätter där den slutade.",
    [PW_TEXT_BUILD_TITLE] = "Bygger din Windows-enhet",
    [PW_TEXT_BUILD_BODY] = "Det tar ungefär en minut. När enheten är klar återgår MihawkOS automatiskt till konfigurationen.",
    [PW_TEXT_BUILD_SETTINGS] = "Konfigurerar Windows",
    [PW_TEXT_BUILD_DOTNET] = "Installerar .NET-stöd",
    [PW_TEXT_BUILD_FINISHING] = "Slutför",
    [PW_TEXT_DONE_TITLE] = "Allt är klart",
    [PW_TEXT_DONE_BODY] = "Mihawk OS är redo. Du kan köra konfigurationen igen från Inställningar i biblioteket.",
    [PW_TEXT_ENTER] = "Öppna Mihawk OS",
    [PW_TEXT_HINT_SELECT] = "Välj",
    [PW_TEXT_HINT_BACK] = "Tillbaka",
    [PW_TEXT_HINT_MOVE] = "Flytta",
    [PW_TEXT_STEP_OF] = "Steg {1} av {2}",
    [PW_TEXT_GIGABYTES] = "{1} GB",
    [PW_TEXT_DECIMAL] = ",",
};

static const char *const text_fr[PW_TEXT_COUNT] = {
    [PW_TEXT_WELCOME_TITLE] = "Bienvenue sur MihawkOS",
    [PW_TEXT_WELCOME_BODY] = "Préparons votre PS5 pour les jeux Windows. Comptez une dizaine de minutes.",
    [PW_TEXT_GET_STARTED] = "Commencer",
    [PW_TEXT_SKIP_SETUP] = "Passer la configuration",
    [PW_TEXT_LANGUAGE_TITLE] = "Choisissez votre langue",
    [PW_TEXT_LANGUAGE_BODY] = "Vos jeux Windows l’utilisent aussi, avec sa disposition de clavier. Le bureau de "
        "Mihawk OS reste en anglais.",
    [PW_TEXT_METHOD_TITLE] = "Choisissez comment installer",
    [PW_TEXT_METHOD_BODY] = "MihawkOS a besoin de son environnement Windows, environ 1,2 Go.",
    [PW_TEXT_METHOD_USB] = "Clé USB",
    [PW_TEXT_METHOD_USB_BODY] = "Copiez les fichiers sur une clé USB depuis n’importe quel ordinateur.",
    [PW_TEXT_METHOD_INTERNET] = "Internet",
    [PW_TEXT_METHOD_INTERNET_BODY] = "Téléchargez directement sur votre PS5.",
    [PW_TEXT_COMING_SOON] = "Bientôt disponible",
    [PW_TEXT_METHOD_INSTALLED] = "L’environnement Windows est déjà installé.",
    [PW_TEXT_CONTINUE] = "Continuer",
    [PW_TEXT_QR_CAPTION] = "Scannez pour suivre les instructions pas à pas sur votre téléphone.",
    [PW_TEXT_USB_TITLE] = "Préparez une clé USB",
    [PW_TEXT_USB_STEP1] = "Sur un ordinateur, formatez une clé USB en exFAT avec une table de partition MBR. "
        "Cela efface la clé.",
    [PW_TEXT_USB_STEP2] = "Téléchargez MihawkOS et copiez son dossier mihawkos à la racine de la clé.",
    [PW_TEXT_USB_STEP3] = "Branchez la clé sur un port USB de votre PS5.",
    [PW_TEXT_USB_STEP4] = "Choisissez Vérifier la clé.",
    [PW_TEXT_CHECK_DRIVE] = "Vérifier la clé",
    [PW_TEXT_FOUND] = "La clé contient {1} à installer.",
    [PW_TEXT_INSTALL] = "Installer",
    [PW_TEXT_RETRY] = "Réessayer",
    [PW_TEXT_ERR_NO_STICK] = "Aucune clé USB trouvée. Branchez-la, attendez quelques secondes, puis "
        "réessayez. Si elle est déjà branchée, formatez-la en exFAT avec MBR : la PS5 ne lit pas "
        "les clés GPT ou NTFS.",
    [PW_TEXT_ERR_NO_FOLDER] = "La clé n’a pas de dossier mihawkos à sa racine. Copiez le dossier sur la "
        "clé, puis réessayez.",
    [PW_TEXT_ERR_PARTIAL] = "Le dossier mihawkos est incomplet : il contient {1} morceaux sur {2}. Copiez de nouveau le "
        "dossier entier, puis réessayez.",
    [PW_TEXT_ERR_NO_SPACE] = "Votre PS5 a besoin de {1} libres et n’en a que {2}. Supprimez quelque chose, puis "
        "réessayez.",
    [PW_TEXT_ERR_READ] = "Impossible de lire la clé USB. Vérifiez qu’elle est toujours branchée, "
        "puis réessayez. Ce qui est déjà installé est conservé.",
    [PW_TEXT_ERR_DAMAGED] = "Un fichier de la clé est endommagé ou d’une autre version. Copiez de nouveau "
        "le dossier mihawkos, puis réessayez.",
    [PW_TEXT_ERR_FULL] = "Le stockage de votre PS5 est plein. Supprimez quelque chose, puis réessayez. Ce qui est "
        "déjà installé est conservé.",
    [PW_TEXT_ERR_WRITE] = "Le stockage de votre PS5 a refusé une écriture. Réessayez ; si cela se "
        "reproduit, redémarrez la PS5.",
    [PW_TEXT_ERR_CANCELLED] = "Installation arrêtée. Ce qui est déjà installé est "
        "conservé.",
    [PW_TEXT_ERR_BUILD] = "Cette copie de MihawkOS ne peut pas installer d’environnement Windows. Réinstallez "
        "MihawkOS.",
    [PW_TEXT_INSTALLING_TITLE] = "Installation de l’environnement Windows",
    [PW_TEXT_INSTALLING_BODY] = "Laissez la clé branchée. Cela prend environ une minute.",
    [PW_TEXT_INSTALLING_CHECKING] = "Vérification de ce qui est déjà installé…",
    [PW_TEXT_INSTALLING_STATS] = "{1} sur {2} Mo · {3} Mo/s",
    [PW_TEXT_INSTALLED] = "Installé.",
    [PW_TEXT_STOP] = "Arrêter",
    [PW_TEXT_PREPARE_TITLE] = "Préparation de Mihawk OS",
    [PW_TEXT_PREPARE_BODY] = "Le premier démarrage crée votre disque Windows. Cela prend quelques minutes, et "
        "l’écran peut rester immobile un moment. Il se termine tout seul et revient ici.",
    [PW_TEXT_PREPARE_NOTE] = "Pendant ce premier démarrage, la manette ne fonctionne pas dans les jeux : MihawkOS "
        "le termine donc dès que le disque est prêt.",
    [PW_TEXT_PREPARE_START] = "Démarrer",
    [PW_TEXT_PREPARE_FAILED] = "Le premier démarrage ne s’est pas terminé. Réessayez : il reprend "
        "là où il s’est arrêté.",
    [PW_TEXT_BUILD_TITLE] = "Création de votre disque Windows",
    [PW_TEXT_BUILD_BODY] = "Cela prend environ une minute. Une fois le disque prêt, MihawkOS revient tout seul à la "
        "configuration.",
    [PW_TEXT_BUILD_SETTINGS] = "Configuration de Windows",
    [PW_TEXT_BUILD_DOTNET] = "Installation de la prise en charge de .NET",
    [PW_TEXT_BUILD_FINISHING] = "Finalisation",
    [PW_TEXT_DONE_TITLE] = "Tout est prêt",
    [PW_TEXT_DONE_BODY] = "Mihawk OS est prêt. Vous pouvez relancer cette configuration depuis Settings, dans la "
        "bibliothèque.",
    [PW_TEXT_ENTER] = "Entrer dans Mihawk OS",
    [PW_TEXT_HINT_SELECT] = "Choisir",
    [PW_TEXT_HINT_BACK] = "Retour",
    [PW_TEXT_HINT_MOVE] = "Déplacer",
    [PW_TEXT_STEP_OF] = "Étape {1} sur {2}",
    [PW_TEXT_GIGABYTES] = "{1} Go",
    [PW_TEXT_DECIMAL] = ",",
};

static const char *const text_es[PW_TEXT_COUNT] = {
    [PW_TEXT_WELCOME_TITLE] = "Bienvenido a MihawkOS",
    [PW_TEXT_WELCOME_BODY] = "Vamos a preparar tu PS5 para los juegos de Windows. Tardarás unos diez minutos.",
    [PW_TEXT_GET_STARTED] = "Empezar",
    [PW_TEXT_SKIP_SETUP] = "Omitir la configuración",
    [PW_TEXT_LANGUAGE_TITLE] = "Elige tu idioma",
    [PW_TEXT_LANGUAGE_BODY] = "Tus juegos de Windows también lo usarán, con su distribución de teclado. El escritorio de "
        "Mihawk OS sigue en inglés.",
    [PW_TEXT_METHOD_TITLE] = "Elige cómo instalar",
    [PW_TEXT_METHOD_BODY] = "MihawkOS necesita su entorno de Windows, de unos 1,2 GB.",
    [PW_TEXT_METHOD_USB] = "Unidad USB",
    [PW_TEXT_METHOD_USB_BODY] = "Copia los archivos en una unidad USB desde cualquier ordenador.",
    [PW_TEXT_METHOD_INTERNET] = "Internet",
    [PW_TEXT_METHOD_INTERNET_BODY] = "Descárgalo directamente en tu PS5.",
    [PW_TEXT_COMING_SOON] = "Próximamente",
    [PW_TEXT_METHOD_INSTALLED] = "El entorno de Windows ya está instalado.",
    [PW_TEXT_CONTINUE] = "Continuar",
    [PW_TEXT_QR_CAPTION] = "Escanea el código para ver las instrucciones paso a paso en tu móvil.",
    [PW_TEXT_USB_TITLE] = "Prepara una unidad USB",
    [PW_TEXT_USB_STEP1] = "En un ordenador, formatea una unidad USB como exFAT con una tabla de particiones MBR. Esto borra "
        "la unidad.",
    [PW_TEXT_USB_STEP2] = "Descarga MihawkOS y copia su carpeta mihawkos en la raíz de la unidad.",
    [PW_TEXT_USB_STEP3] = "Conecta la unidad a un puerto USB de tu PS5.",
    [PW_TEXT_USB_STEP4] = "Elige Comprobar unidad.",
    [PW_TEXT_CHECK_DRIVE] = "Comprobar unidad",
    [PW_TEXT_FOUND] = "La unidad contiene {1} para instalar.",
    [PW_TEXT_INSTALL] = "Instalar",
    [PW_TEXT_RETRY] = "Reintentar",
    [PW_TEXT_ERR_NO_STICK] = "No se encuentra ninguna unidad USB. Conéctala, espera unos segundos y vuelve a intentarlo. "
        "Si ya está conectada, formatéala como exFAT con MBR: la PS5 no lee unidades GPT ni NTFS.",
    [PW_TEXT_ERR_NO_FOLDER] = "La unidad no tiene una carpeta mihawkos en su raíz. Copia la carpeta en la unidad y vuelve "
        "a intentarlo.",
    [PW_TEXT_ERR_PARTIAL] = "La carpeta mihawkos está incompleta: tiene {1} de {2} partes. Copia de nuevo la carpeta entera "
        "y vuelve a intentarlo.",
    [PW_TEXT_ERR_NO_SPACE] = "Tu PS5 necesita {1} libres y tiene {2}. Borra algo y vuelve a intentarlo.",
    [PW_TEXT_ERR_READ] = "No se puede leer la unidad USB. Comprueba que sigue conectada y vuelve a intentarlo. Lo que ya "
        "está instalado se conserva.",
    [PW_TEXT_ERR_DAMAGED] = "Un archivo de la unidad está dañado o es de otra versión. Copia de nuevo la carpeta mihawkos "
        "y vuelve a intentarlo.",
    [PW_TEXT_ERR_FULL] = "El almacenamiento de tu PS5 está lleno. Borra algo y vuelve a intentarlo. Lo que ya está instalado "
        "se conserva.",
    [PW_TEXT_ERR_WRITE] = "El almacenamiento de tu PS5 ha rechazado una escritura. Vuelve a intentarlo; si pasa de nuevo, "
        "reinicia la PS5.",
    [PW_TEXT_ERR_CANCELLED] = "La instalación se ha detenido. Lo que ya está instalado se conserva.",
    [PW_TEXT_ERR_BUILD] = "Esta copia de MihawkOS no puede instalar un entorno de Windows. Vuelve a instalar MihawkOS.",
    [PW_TEXT_INSTALLING_TITLE] = "Instalando el entorno de Windows",
    [PW_TEXT_INSTALLING_BODY] = "Deja la unidad conectada. Tarda alrededor de un minuto.",
    [PW_TEXT_INSTALLING_CHECKING] = "Comprobando lo que ya está instalado…",
    [PW_TEXT_INSTALLING_STATS] = "{1} de {2} MB · {3} MB/s",
    [PW_TEXT_INSTALLED] = "Instalado.",
    [PW_TEXT_STOP] = "Detener",
    [PW_TEXT_PREPARE_TITLE] = "Preparando Mihawk OS",
    [PW_TEXT_PREPARE_BODY] = "El primer inicio crea tu disco de Windows. Tarda unos minutos y la pantalla puede quedarse "
        "quieta un rato. Termina solo y vuelve aquí.",
    [PW_TEXT_PREPARE_NOTE] = "Durante este primer inicio el mando no funciona en los juegos, así que MihawkOS lo termina "
        "en cuanto el disco está listo.",
    [PW_TEXT_PREPARE_START] = "Iniciar",
    [PW_TEXT_PREPARE_FAILED] = "El primer inicio no ha terminado. Vuelve a intentarlo: continúa donde se quedó.",
    [PW_TEXT_BUILD_TITLE] = "Creando tu disco de Windows",
    [PW_TEXT_BUILD_BODY] = "Tarda alrededor de un minuto. Cuando el disco esté listo, MihawkOS vuelve solo a la "
        "configuración.",
    [PW_TEXT_BUILD_SETTINGS] = "Configurando Windows",
    [PW_TEXT_BUILD_DOTNET] = "Instalando la compatibilidad con .NET",
    [PW_TEXT_BUILD_FINISHING] = "Terminando",
    [PW_TEXT_DONE_TITLE] = "Todo listo",
    [PW_TEXT_DONE_BODY] = "Mihawk OS está listo. Puedes repetir esta configuración desde Settings, en la biblioteca.",
    [PW_TEXT_ENTER] = "Entrar en Mihawk OS",
    [PW_TEXT_HINT_SELECT] = "Elegir",
    [PW_TEXT_HINT_BACK] = "Atrás",
    [PW_TEXT_HINT_MOVE] = "Mover",
    [PW_TEXT_STEP_OF] = "Paso {1} de {2}",
    [PW_TEXT_GIGABYTES] = "{1} GB",
    [PW_TEXT_DECIMAL] = ",",
};

static const char *const text_de[PW_TEXT_COUNT] = {
    [PW_TEXT_WELCOME_TITLE] = "Willkommen bei MihawkOS",
    [PW_TEXT_WELCOME_BODY] = "Machen wir deine PS5 bereit für Windows-Spiele. Das dauert etwa zehn Minuten.",
    [PW_TEXT_GET_STARTED] = "Los geht’s",
    [PW_TEXT_SKIP_SETUP] = "Einrichtung überspringen",
    [PW_TEXT_LANGUAGE_TITLE] = "Wähle deine Sprache",
    [PW_TEXT_LANGUAGE_BODY] = "Deine Windows-Spiele verwenden sie auch, samt Tastaturlayout. Der Desktop von Mihawk OS "
        "bleibt auf Englisch.",
    [PW_TEXT_METHOD_TITLE] = "Wähle die Installationsart",
    [PW_TEXT_METHOD_BODY] = "MihawkOS braucht seine Windows-Laufzeitumgebung, etwa 1,2 GB.",
    [PW_TEXT_METHOD_USB] = "USB-Laufwerk",
    [PW_TEXT_METHOD_USB_BODY] = "Kopiere die Dateien an einem beliebigen Computer auf ein USB-Laufwerk.",
    [PW_TEXT_METHOD_INTERNET] = "Internet",
    [PW_TEXT_METHOD_INTERNET_BODY] = "Direkt auf deine PS5 herunterladen.",
    [PW_TEXT_COMING_SOON] = "Demnächst",
    [PW_TEXT_METHOD_INSTALLED] = "Die Windows-Laufzeitumgebung ist bereits installiert.",
    [PW_TEXT_CONTINUE] = "Weiter",
    [PW_TEXT_QR_CAPTION] = "Scanne den Code für eine Schritt-für-Schritt-Anleitung auf deinem Handy.",
    [PW_TEXT_USB_TITLE] = "USB-Laufwerk vorbereiten",
    [PW_TEXT_USB_STEP1] = "Formatiere an einem Computer ein USB-Laufwerk als exFAT mit MBR-Partitionstabelle. Dabei wird "
        "das Laufwerk gelöscht.",
    [PW_TEXT_USB_STEP2] = "Lade MihawkOS herunter und kopiere den Ordner mihawkos in die oberste Ebene des Laufwerks.",
    [PW_TEXT_USB_STEP3] = "Stecke das Laufwerk in einen USB-Anschluss deiner PS5.",
    [PW_TEXT_USB_STEP4] = "Wähle Laufwerk prüfen.",
    [PW_TEXT_CHECK_DRIVE] = "Laufwerk prüfen",
    [PW_TEXT_FOUND] = "Das Laufwerk enthält {1} zum Installieren.",
    [PW_TEXT_INSTALL] = "Installieren",
    [PW_TEXT_RETRY] = "Erneut versuchen",
    [PW_TEXT_ERR_NO_STICK] = "Kein USB-Laufwerk gefunden. Stecke es ein, warte ein paar Sekunden und versuche es erneut. "
        "Steckt es schon, formatiere es als exFAT mit MBR: Die PS5 liest keine GPT- oder NTFS-Laufwerke.",
    [PW_TEXT_ERR_NO_FOLDER] = "Auf der obersten Ebene des Laufwerks liegt kein Ordner mihawkos. Kopiere den Ordner auf "
        "das Laufwerk und versuche es erneut.",
    [PW_TEXT_ERR_PARTIAL] = "Der Ordner mihawkos ist unvollständig: Er enthält {1} von {2} Teilen. Kopiere den ganzen Ordner "
        "noch einmal und versuche es erneut.",
    [PW_TEXT_ERR_NO_SPACE] = "Deine PS5 braucht {1} freien Speicher und hat {2}. Lösche etwas und versuche es erneut.",
    [PW_TEXT_ERR_READ] = "Das USB-Laufwerk konnte nicht gelesen werden. Prüfe, ob es noch steckt, und versuche es erneut. "
        "Bereits Installiertes bleibt erhalten.",
    [PW_TEXT_ERR_DAMAGED] = "Eine Datei auf dem Laufwerk ist beschädigt oder stammt aus einer anderen Version. Kopiere "
        "den Ordner mihawkos noch einmal und versuche es erneut.",
    [PW_TEXT_ERR_FULL] = "Der Speicher deiner PS5 ist voll. Lösche etwas und versuche es erneut. Bereits Installiertes "
        "bleibt erhalten.",
    [PW_TEXT_ERR_WRITE] = "Der Speicher deiner PS5 hat einen Schreibvorgang abgelehnt. Versuche es erneut; passiert es "
        "wieder, starte die PS5 neu.",
    [PW_TEXT_ERR_CANCELLED] = "Die Installation wurde gestoppt. Bereits Installiertes bleibt erhalten.",
    [PW_TEXT_ERR_BUILD] = "Diese Kopie von MihawkOS kann keine Windows-Laufzeitumgebung installieren. Installiere MihawkOS "
        "neu.",
    [PW_TEXT_INSTALLING_TITLE] = "Windows-Laufzeitumgebung wird installiert",
    [PW_TEXT_INSTALLING_BODY] = "Lass das Laufwerk eingesteckt. Das dauert etwa eine Minute.",
    [PW_TEXT_INSTALLING_CHECKING] = "Bereits Installiertes wird geprüft…",
    [PW_TEXT_INSTALLING_STATS] = "{1} von {2} MB · {3} MB/s",
    [PW_TEXT_INSTALLED] = "Installiert.",
    [PW_TEXT_STOP] = "Stoppen",
    [PW_TEXT_PREPARE_TITLE] = "Mihawk OS wird vorbereitet",
    [PW_TEXT_PREPARE_BODY] = "Der erste Start legt dein Windows-Laufwerk an. Das dauert ein paar Minuten, und der Bildschirm "
        "kann eine Weile stillstehen. Er endet von selbst und kehrt hierher zurück.",
    [PW_TEXT_PREPARE_NOTE] = "Beim ersten Start funktioniert der Controller in Spielen nicht. Deshalb beendet MihawkOS "
        "ihn, sobald das Laufwerk bereit ist.",
    [PW_TEXT_PREPARE_START] = "Starten",
    [PW_TEXT_PREPARE_FAILED] = "Der erste Start wurde nicht abgeschlossen. Versuche es erneut: Er macht dort weiter, wo "
        "er aufgehört hat.",
    [PW_TEXT_BUILD_TITLE] = "Dein Windows-Laufwerk wird angelegt",
    [PW_TEXT_BUILD_BODY] = "Das dauert etwa eine Minute. Sobald das Laufwerk bereit ist, kehrt MihawkOS von selbst "
        "zur Einrichtung zurück.",
    [PW_TEXT_BUILD_SETTINGS] = "Windows wird eingerichtet",
    [PW_TEXT_BUILD_DOTNET] = ".NET-Unterstützung wird installiert",
    [PW_TEXT_BUILD_FINISHING] = "Wird abgeschlossen",
    [PW_TEXT_DONE_TITLE] = "Alles bereit",
    [PW_TEXT_DONE_BODY] = "Mihawk OS ist bereit. Diese Einrichtung kannst du in der Bibliothek unter Settings wiederholen.",
    [PW_TEXT_ENTER] = "Zu Mihawk OS",
    [PW_TEXT_HINT_SELECT] = "Auswählen",
    [PW_TEXT_HINT_BACK] = "Zurück",
    [PW_TEXT_HINT_MOVE] = "Bewegen",
    [PW_TEXT_STEP_OF] = "Schritt {1} von {2}",
    [PW_TEXT_GIGABYTES] = "{1} GB",
    [PW_TEXT_DECIMAL] = ",",
};

static const char *const text_it[PW_TEXT_COUNT] = {
    [PW_TEXT_WELCOME_TITLE] = "Benvenuto in MihawkOS",
    [PW_TEXT_WELCOME_BODY] = "Prepariamo la tua PS5 per i giochi Windows. Ci vogliono circa dieci minuti.",
    [PW_TEXT_GET_STARTED] = "Inizia",
    [PW_TEXT_SKIP_SETUP] = "Salta la configurazione",
    [PW_TEXT_LANGUAGE_TITLE] = "Scegli la lingua",
    [PW_TEXT_LANGUAGE_BODY] = "Anche i tuoi giochi Windows la useranno, con il suo layout di tastiera. Il desktop di Mihawk "
        "OS resta in inglese.",
    [PW_TEXT_METHOD_TITLE] = "Scegli come installare",
    [PW_TEXT_METHOD_BODY] = "MihawkOS ha bisogno del suo ambiente Windows, circa 1,2 GB.",
    [PW_TEXT_METHOD_USB] = "Unità USB",
    [PW_TEXT_METHOD_USB_BODY] = "Copia i file su un’unità USB da qualsiasi computer.",
    [PW_TEXT_METHOD_INTERNET] = "Internet",
    [PW_TEXT_METHOD_INTERNET_BODY] = "Scarica direttamente sulla tua PS5.",
    [PW_TEXT_COMING_SOON] = "Prossimamente",
    [PW_TEXT_METHOD_INSTALLED] = "L’ambiente Windows è già installato.",
    [PW_TEXT_CONTINUE] = "Continua",
    [PW_TEXT_QR_CAPTION] = "Inquadra il codice per le istruzioni passo passo sul telefono.",
    [PW_TEXT_USB_TITLE] = "Prepara un’unità USB",
    [PW_TEXT_USB_STEP1] = "Su un computer, formatta un’unità USB in exFAT con tabella delle partizioni MBR. L’unità verrà "
        "cancellata.",
    [PW_TEXT_USB_STEP2] = "Scarica MihawkOS e copia la sua cartella mihawkos nella radice dell’unità.",
    [PW_TEXT_USB_STEP3] = "Collega l’unità a una porta USB della PS5.",
    [PW_TEXT_USB_STEP4] = "Scegli Controlla unità.",
    [PW_TEXT_CHECK_DRIVE] = "Controlla unità",
    [PW_TEXT_FOUND] = "L’unità contiene {1} da installare.",
    [PW_TEXT_INSTALL] = "Installa",
    [PW_TEXT_RETRY] = "Riprova",
    [PW_TEXT_ERR_NO_STICK] = "Nessuna unità USB trovata. Collegala, attendi qualche secondo e riprova. Se è già collegata, "
        "formattala in exFAT con MBR: la PS5 non legge le unità GPT o NTFS.",
    [PW_TEXT_ERR_NO_FOLDER] = "L’unità non ha una cartella mihawkos nella radice. Copia la cartella sull’unità e riprova.",
    [PW_TEXT_ERR_PARTIAL] = "La cartella mihawkos è incompleta: contiene {1} parti su {2}. Copia di nuovo l’intera cartella "
        "e riprova.",
    [PW_TEXT_ERR_NO_SPACE] = "La PS5 ha bisogno di {1} liberi e ne ha {2}. Elimina qualcosa e riprova.",
    [PW_TEXT_ERR_READ] = "Impossibile leggere l’unità USB. Verifica che sia ancora collegata e riprova. Ciò che è già installato "
        "viene conservato.",
    [PW_TEXT_ERR_DAMAGED] = "Un file sull’unità è danneggiato o di un’altra versione. Copia di nuovo la cartella mihawkos "
        "e riprova.",
    [PW_TEXT_ERR_FULL] = "La memoria della PS5 è piena. Elimina qualcosa e riprova. Ciò che è già installato viene conservato.",
    [PW_TEXT_ERR_WRITE] = "La memoria della PS5 ha rifiutato una scrittura. Riprova; se succede di nuovo, riavvia la PS5.",
    [PW_TEXT_ERR_CANCELLED] = "Installazione interrotta. Ciò che è già installato viene conservato.",
    [PW_TEXT_ERR_BUILD] = "Questa copia di MihawkOS non può installare un ambiente Windows. Reinstalla MihawkOS.",
    [PW_TEXT_INSTALLING_TITLE] = "Installazione dell’ambiente Windows",
    [PW_TEXT_INSTALLING_BODY] = "Lascia l’unità collegata. Ci vuole circa un minuto.",
    [PW_TEXT_INSTALLING_CHECKING] = "Controllo di ciò che è già installato…",
    [PW_TEXT_INSTALLING_STATS] = "{1} di {2} MB · {3} MB/s",
    [PW_TEXT_INSTALLED] = "Installato.",
    [PW_TEXT_STOP] = "Interrompi",
    [PW_TEXT_PREPARE_TITLE] = "Preparazione di Mihawk OS",
    [PW_TEXT_PREPARE_BODY] = "Il primo avvio crea il tuo disco Windows. Ci vogliono alcuni minuti e lo schermo può restare "
        "fermo per un po’. Termina da solo e torna qui.",
    [PW_TEXT_PREPARE_NOTE] = "Durante questo primo avvio il controller non funziona nei giochi, quindi MihawkOS lo termina "
        "appena il disco è pronto.",
    [PW_TEXT_PREPARE_START] = "Avvia",
    [PW_TEXT_PREPARE_FAILED] = "Il primo avvio non è terminato. Riprova: riprende da dove si era fermato.",
    [PW_TEXT_BUILD_TITLE] = "Creazione del tuo disco Windows",
    [PW_TEXT_BUILD_BODY] = "Ci vuole circa un minuto. Quando il disco è pronto, MihawkOS torna da solo alla "
        "configurazione.",
    [PW_TEXT_BUILD_SETTINGS] = "Configurazione di Windows",
    [PW_TEXT_BUILD_DOTNET] = "Installazione del supporto .NET",
    [PW_TEXT_BUILD_FINISHING] = "Completamento",
    [PW_TEXT_DONE_TITLE] = "Tutto pronto",
    [PW_TEXT_DONE_BODY] = "Mihawk OS è pronto. Puoi ripetere questa configurazione da Settings, nella libreria.",
    [PW_TEXT_ENTER] = "Entra in Mihawk OS",
    [PW_TEXT_HINT_SELECT] = "Scegli",
    [PW_TEXT_HINT_BACK] = "Indietro",
    [PW_TEXT_HINT_MOVE] = "Sposta",
    [PW_TEXT_STEP_OF] = "Passo {1} di {2}",
    [PW_TEXT_GIGABYTES] = "{1} GB",
    [PW_TEXT_DECIMAL] = ",",
};

static const char *const text_ru[PW_TEXT_COUNT] = {
    [PW_TEXT_WELCOME_TITLE] = "Добро пожаловать в MihawkOS",
    [PW_TEXT_WELCOME_BODY] = "Подготовим вашу PS5 к играм для Windows. Это займёт около десяти минут.",
    [PW_TEXT_GET_STARTED] = "Начать",
    [PW_TEXT_SKIP_SETUP] = "Пропустить настройку",
    [PW_TEXT_LANGUAGE_TITLE] = "Выберите язык",
    [PW_TEXT_LANGUAGE_BODY] = "Ваши игры для Windows тоже будут его использовать вместе с раскладкой клавиатуры. Рабочий "
        "стол Mihawk OS останется на английском.",
    [PW_TEXT_METHOD_TITLE] = "Выберите способ установки",
    [PW_TEXT_METHOD_BODY] = "MihawkOS нужна своя среда Windows, около 1,2 ГБ.",
    [PW_TEXT_METHOD_USB] = "USB-накопитель",
    [PW_TEXT_METHOD_USB_BODY] = "Скопируйте файлы на USB-накопитель на любом компьютере.",
    [PW_TEXT_METHOD_INTERNET] = "Интернет",
    [PW_TEXT_METHOD_INTERNET_BODY] = "Загрузка прямо на вашу PS5.",
    [PW_TEXT_COMING_SOON] = "Скоро",
    [PW_TEXT_METHOD_INSTALLED] = "Среда Windows уже установлена.",
    [PW_TEXT_CONTINUE] = "Продолжить",
    [PW_TEXT_QR_CAPTION] = "Отсканируйте код, чтобы открыть пошаговую инструкцию на телефоне.",
    [PW_TEXT_USB_TITLE] = "Подготовьте USB-накопитель",
    [PW_TEXT_USB_STEP1] = "На компьютере отформатируйте USB-накопитель в exFAT с таблицей разделов MBR. Все данные на нём "
        "будут удалены.",
    [PW_TEXT_USB_STEP2] = "Загрузите MihawkOS и скопируйте его папку mihawkos в корень накопителя.",
    [PW_TEXT_USB_STEP3] = "Подключите накопитель к USB-порту PS5.",
    [PW_TEXT_USB_STEP4] = "Выберите «Проверить накопитель».",
    [PW_TEXT_CHECK_DRIVE] = "Проверить накопитель",
    [PW_TEXT_FOUND] = "На накопителе {1} для установки.",
    [PW_TEXT_INSTALL] = "Установить",
    [PW_TEXT_RETRY] = "Повторить",
    [PW_TEXT_ERR_NO_STICK] = "USB-накопитель не найден. Подключите его, подождите несколько секунд и повторите попытку. "
        "Если он уже подключён, отформатируйте его в exFAT с MBR: PS5 не читает накопители GPT и NTFS.",
    [PW_TEXT_ERR_NO_FOLDER] = "В корне накопителя нет папки mihawkos. Скопируйте папку на накопитель и повторите попытку.",
    [PW_TEXT_ERR_PARTIAL] = "Папка mihawkos неполная, частей: {1} из {2}. Скопируйте всю папку заново и повторите попытку.",
    [PW_TEXT_ERR_NO_SPACE] = "PS5 нужно {1} свободного места, а доступно {2}. Удалите что-нибудь и повторите попытку.",
    [PW_TEXT_ERR_READ] = "Не удалось прочитать USB-накопитель. Убедитесь, что он подключён, и повторите попытку. Уже установленное "
        "сохранится.",
    [PW_TEXT_ERR_DAMAGED] = "Файл на накопителе повреждён или от другой версии. Скопируйте папку mihawkos заново и повторите "
        "попытку.",
    [PW_TEXT_ERR_FULL] = "Хранилище PS5 заполнено. Удалите что-нибудь и повторите попытку. Уже установленное сохранится.",
    [PW_TEXT_ERR_WRITE] = "Хранилище PS5 отказало в записи. Повторите попытку; если это повторится, перезапустите PS5.",
    [PW_TEXT_ERR_CANCELLED] = "Установка остановлена. Уже установленное сохранится.",
    [PW_TEXT_ERR_BUILD] = "Эта копия MihawkOS не может установить среду Windows. Переустановите MihawkOS.",
    [PW_TEXT_INSTALLING_TITLE] = "Установка среды Windows",
    [PW_TEXT_INSTALLING_BODY] = "Не отключайте накопитель. Это займёт около минуты.",
    [PW_TEXT_INSTALLING_CHECKING] = "Проверка уже установленного…",
    [PW_TEXT_INSTALLING_STATS] = "{1} из {2} МБ · {3} МБ/с",
    [PW_TEXT_INSTALLED] = "Установлено.",
    [PW_TEXT_STOP] = "Остановить",
    [PW_TEXT_PREPARE_TITLE] = "Подготовка Mihawk OS",
    [PW_TEXT_PREPARE_BODY] = "При первом запуске создаётся ваш диск Windows. Это займёт несколько минут, и экран может "
        "какое-то время не меняться. Запуск завершится сам и вернётся сюда.",
    [PW_TEXT_PREPARE_NOTE] = "Во время первого запуска контроллер не работает в играх, поэтому MihawkOS завершает его, "
        "как только диск готов.",
    [PW_TEXT_PREPARE_START] = "Запустить",
    [PW_TEXT_PREPARE_FAILED] = "Первый запуск не завершился. Повторите попытку: он продолжится с того места, где остановился.",
    [PW_TEXT_BUILD_TITLE] = "Создание вашего диска Windows",
    [PW_TEXT_BUILD_BODY] = "Это займёт около минуты. Когда диск будет готов, MihawkOS сам вернётся к настройке.",
    [PW_TEXT_BUILD_SETTINGS] = "Настройка Windows",
    [PW_TEXT_BUILD_DOTNET] = "Установка поддержки .NET",
    [PW_TEXT_BUILD_FINISHING] = "Завершение",
    [PW_TEXT_DONE_TITLE] = "Всё готово",
    [PW_TEXT_DONE_BODY] = "Mihawk OS готова. Повторить эту настройку можно в разделе Settings в библиотеке.",
    [PW_TEXT_ENTER] = "Войти в Mihawk OS",
    [PW_TEXT_HINT_SELECT] = "Выбрать",
    [PW_TEXT_HINT_BACK] = "Назад",
    [PW_TEXT_HINT_MOVE] = "Перейти",
    [PW_TEXT_STEP_OF] = "Шаг {1} из {2}",
    [PW_TEXT_GIGABYTES] = "{1} ГБ",
    [PW_TEXT_DECIMAL] = ",",
};

static const char *const text_zh[PW_TEXT_COUNT] = {
    [PW_TEXT_WELCOME_TITLE] = "欢迎使用 MihawkOS",
    [PW_TEXT_WELCOME_BODY] = "让我们为 Windows 游戏准备好你的 PS5。大约需要十分钟。",
    [PW_TEXT_GET_STARTED] = "开始",
    [PW_TEXT_SKIP_SETUP] = "跳过设置",
    [PW_TEXT_LANGUAGE_TITLE] = "选择语言",
    [PW_TEXT_LANGUAGE_BODY] = "你的 Windows 游戏也会使用该语言及其键盘布局。Mihawk OS 桌面仍为英文。",
    [PW_TEXT_METHOD_TITLE] = "选择安装方式",
    [PW_TEXT_METHOD_BODY] = "MihawkOS 需要安装其 Windows 运行环境，约 1.2 GB。",
    [PW_TEXT_METHOD_USB] = "U 盘",
    [PW_TEXT_METHOD_USB_BODY] = "在任意电脑上将文件复制到 U 盘。",
    [PW_TEXT_METHOD_INTERNET] = "互联网",
    [PW_TEXT_METHOD_INTERNET_BODY] = "直接下载到你的 PS5。",
    [PW_TEXT_COMING_SOON] = "即将推出",
    [PW_TEXT_METHOD_INSTALLED] = "Windows 运行环境已安装。",
    [PW_TEXT_CONTINUE] = "继续",
    [PW_TEXT_QR_CAPTION] = "扫码即可在手机上查看分步说明。",
    [PW_TEXT_USB_TITLE] = "准备 U 盘",
    [PW_TEXT_USB_STEP1] = "在电脑上将 U 盘格式化为 exFAT，分区表选择 MBR。这会清除 U 盘上的所有数据。",
    [PW_TEXT_USB_STEP2] = "下载 MihawkOS，并将其中的 mihawkos 文件夹复制到 U 盘根目录。",
    [PW_TEXT_USB_STEP3] = "将 U 盘插入 PS5 的 USB 接口。",
    [PW_TEXT_USB_STEP4] = "选择“检查 U 盘”。",
    [PW_TEXT_CHECK_DRIVE] = "检查 U 盘",
    [PW_TEXT_FOUND] = "U 盘中有 {1} 待安装。",
    [PW_TEXT_INSTALL] = "安装",
    [PW_TEXT_RETRY] = "重试",
    [PW_TEXT_ERR_NO_STICK] = "未找到 U 盘。请插入 U 盘，等待几秒后重试。如果已经插入，请将其格式化为 exFAT（MBR）：PS5 无法读取 GPT 或 NTFS 格式的磁盘。",
    [PW_TEXT_ERR_NO_FOLDER] = "U 盘根目录中没有 mihawkos 文件夹。请将该文件夹复制到 U 盘后重试。",
    [PW_TEXT_ERR_PARTIAL] = "mihawkos 文件夹不完整：只有 {1}/{2} 个部分。请重新复制整个文件夹后重试。",
    [PW_TEXT_ERR_NO_SPACE] = "PS5 需要 {1} 可用空间，当前只有 {2}。请删除一些内容后重试。",
    [PW_TEXT_ERR_READ] = "无法读取 U 盘。请确认它仍已插入，然后重试。已安装的内容会保留。",
    [PW_TEXT_ERR_DAMAGED] = "U 盘上的某个文件已损坏或来自其他版本。请重新复制 mihawkos 文件夹后重试。",
    [PW_TEXT_ERR_FULL] = "PS5 存储空间已满。请删除一些内容后重试。已安装的内容会保留。",
    [PW_TEXT_ERR_WRITE] = "PS5 存储拒绝了一次写入。请重试；如果再次发生，请重启 PS5。",
    [PW_TEXT_ERR_CANCELLED] = "安装已停止。已安装的内容会保留。",
    [PW_TEXT_ERR_BUILD] = "此 MihawkOS 副本无法安装 Windows 运行环境。请重新安装 MihawkOS。",
    [PW_TEXT_INSTALLING_TITLE] = "正在安装 Windows 运行环境",
    [PW_TEXT_INSTALLING_BODY] = "请勿拔出 U 盘。大约需要一分钟。",
    [PW_TEXT_INSTALLING_CHECKING] = "正在检查已安装的内容…",
    [PW_TEXT_INSTALLING_STATS] = "{1} / {2} MB · {3} MB/s",
    [PW_TEXT_INSTALLED] = "已安装。",
    [PW_TEXT_STOP] = "停止",
    [PW_TEXT_PREPARE_TITLE] = "正在准备 Mihawk OS",
    [PW_TEXT_PREPARE_BODY] = "首次启动会创建你的 Windows 磁盘。这需要几分钟，期间画面可能会静止一段时间。完成后会自动结束并返回这里。",
    [PW_TEXT_PREPARE_NOTE] = "首次启动期间，手柄在游戏中无法使用，因此磁盘准备就绪后 MihawkOS 会立即结束本次启动。",
    [PW_TEXT_PREPARE_START] = "启动",
    [PW_TEXT_PREPARE_FAILED] = "首次启动未完成。请重试：它会从中断的地方继续。",
    [PW_TEXT_BUILD_TITLE] = "正在创建你的 Windows 磁盘",
    [PW_TEXT_BUILD_BODY] = "大约需要一分钟。磁盘准备就绪后，MihawkOS 会自动返回设置。",
    [PW_TEXT_BUILD_SETTINGS] = "正在设置 Windows",
    [PW_TEXT_BUILD_DOTNET] = "正在安装 .NET 支持",
    [PW_TEXT_BUILD_FINISHING] = "即将完成",
    [PW_TEXT_DONE_TITLE] = "一切就绪",
    [PW_TEXT_DONE_BODY] = "Mihawk OS 已准备就绪。如需再次运行此设置，请在资料库中打开 Settings。",
    [PW_TEXT_ENTER] = "进入 Mihawk OS",
    [PW_TEXT_HINT_SELECT] = "选择",
    [PW_TEXT_HINT_BACK] = "返回",
    [PW_TEXT_HINT_MOVE] = "移动",
    [PW_TEXT_STEP_OF] = "第 {1} 步，共 {2} 步",
    [PW_TEXT_GIGABYTES] = "{1} GB",
    [PW_TEXT_DECIMAL] = ".",
};

static const char *const text_ja[PW_TEXT_COUNT] = {
    [PW_TEXT_WELCOME_TITLE] = "MihawkOS へようこそ",
    [PW_TEXT_WELCOME_BODY] = "PS5 で Windows のゲームを遊ぶ準備をしましょう。所要時間は約 10 分です。",
    [PW_TEXT_GET_STARTED] = "はじめる",
    [PW_TEXT_SKIP_SETUP] = "セットアップをスキップ",
    [PW_TEXT_LANGUAGE_TITLE] = "言語を選択",
    [PW_TEXT_LANGUAGE_BODY] = "Windows のゲームでもこの言語とそのキーボード配列が使われます。Mihawk OS のデスクトップは英語のままです。",
    [PW_TEXT_METHOD_TITLE] = "インストール方法を選択",
    [PW_TEXT_METHOD_BODY] = "MihawkOS には Windows 実行環境（約 1.2 GB）が必要です。",
    [PW_TEXT_METHOD_USB] = "USB ドライブ",
    [PW_TEXT_METHOD_USB_BODY] = "お好きなパソコンで USB ドライブにファイルをコピーします。",
    [PW_TEXT_METHOD_INTERNET] = "インターネット",
    [PW_TEXT_METHOD_INTERNET_BODY] = "PS5 に直接ダウンロードします。",
    [PW_TEXT_COMING_SOON] = "近日対応",
    [PW_TEXT_METHOD_INSTALLED] = "Windows 実行環境はインストール済みです。",
    [PW_TEXT_CONTINUE] = "続ける",
    [PW_TEXT_QR_CAPTION] = "スマートフォンでスキャンすると、詳しい手順を確認できます。",
    [PW_TEXT_USB_TITLE] = "USB ドライブを準備する",
    [PW_TEXT_USB_STEP1] = "パソコンで USB ドライブを exFAT（パーティションテーブルは MBR）でフォーマットします。ドライブの内容は消去されます。",
    [PW_TEXT_USB_STEP2] = "MihawkOS をダウンロードし、mihawkos フォルダーをドライブの最上位にコピーします。",
    [PW_TEXT_USB_STEP3] = "ドライブを PS5 の USB ポートに接続します。",
    [PW_TEXT_USB_STEP4] = "「ドライブを確認」を選びます。",
    [PW_TEXT_CHECK_DRIVE] = "ドライブを確認",
    [PW_TEXT_FOUND] = "ドライブにインストールできる {1} があります。",
    [PW_TEXT_INSTALL] = "インストール",
    [PW_TEXT_RETRY] = "再試行",
    [PW_TEXT_ERR_NO_STICK] = "USB ドライブが見つかりません。接続して数秒待ってから、もう一度お試しください。接続済みの場合は exFAT（MBR）でフォーマットしてください。PS5 は GPT や NTFS "
        "のドライブを読み取れません。",
    [PW_TEXT_ERR_NO_FOLDER] = "ドライブの最上位に mihawkos フォルダーがありません。フォルダーをドライブにコピーしてから、もう一度お試しください。",
    [PW_TEXT_ERR_PARTIAL] = "mihawkos フォルダーが不完全です（{2} 個中 {1} 個）。フォルダー全体をコピーし直してから、もう一度お試しください。",
    [PW_TEXT_ERR_NO_SPACE] = "PS5 に {1} の空き容量が必要ですが、{2} しかありません。不要なデータを削除してから、もう一度お試しください。",
    [PW_TEXT_ERR_READ] = "USB ドライブを読み取れません。接続されているか確認してから、もう一度お試しください。インストール済みの内容は保持されます。",
    [PW_TEXT_ERR_DAMAGED] = "ドライブ上のファイルが壊れているか、別のバージョンのものです。mihawkos フォルダーをコピーし直してから、もう一度お試しください。",
    [PW_TEXT_ERR_FULL] = "PS5 のストレージがいっぱいです。不要なデータを削除してから、もう一度お試しください。インストール済みの内容は保持されます。",
    [PW_TEXT_ERR_WRITE] = "PS5 のストレージへの書き込みが拒否されました。もう一度お試しください。繰り返し起こる場合は PS5 を再起動してください。",
    [PW_TEXT_ERR_CANCELLED] = "インストールを停止しました。インストール済みの内容は保持されます。",
    [PW_TEXT_ERR_BUILD] = "この MihawkOS では Windows 実行環境をインストールできません。MihawkOS を入れ直してください。",
    [PW_TEXT_INSTALLING_TITLE] = "Windows 実行環境をインストール中",
    [PW_TEXT_INSTALLING_BODY] = "ドライブは接続したままにしてください。約 1 分かかります。",
    [PW_TEXT_INSTALLING_CHECKING] = "インストール済みの内容を確認しています…",
    [PW_TEXT_INSTALLING_STATS] = "{1} / {2} MB · {3} MB/s",
    [PW_TEXT_INSTALLED] = "インストールしました。",
    [PW_TEXT_STOP] = "停止",
    [PW_TEXT_PREPARE_TITLE] = "Mihawk OS を準備しています",
    [PW_TEXT_PREPARE_BODY] = "初回の起動で Windows ドライブを作成します。数分かかり、しばらく画面が止まって見えることがあります。完了すると自動で終了し、この画面に戻ります。",
    [PW_TEXT_PREPARE_NOTE] = "初回の起動中はゲームでコントローラーが使えないため、ドライブの準備ができしだい MihawkOS が起動を終了します。",
    [PW_TEXT_PREPARE_START] = "起動",
    [PW_TEXT_PREPARE_FAILED] = "初回の起動が完了しませんでした。もう一度お試しください。中断したところから再開します。",
    [PW_TEXT_BUILD_TITLE] = "Windows ドライブを作成しています",
    [PW_TEXT_BUILD_BODY] = "約 1 分かかります。準備ができると、MihawkOS が自動でセットアップに戻ります。",
    [PW_TEXT_BUILD_SETTINGS] = "Windows を設定しています",
    [PW_TEXT_BUILD_DOTNET] = ".NET サポートをインストールしています",
    [PW_TEXT_BUILD_FINISHING] = "仕上げています",
    [PW_TEXT_DONE_TITLE] = "準備完了",
    [PW_TEXT_DONE_BODY] = "Mihawk OS の準備ができました。このセットアップは、ライブラリの Settings からもう一度実行できます。",
    [PW_TEXT_ENTER] = "Mihawk OS に入る",
    [PW_TEXT_HINT_SELECT] = "決定",
    [PW_TEXT_HINT_BACK] = "戻る",
    [PW_TEXT_HINT_MOVE] = "移動",
    [PW_TEXT_STEP_OF] = "ステップ {1}/{2}",
    [PW_TEXT_GIGABYTES] = "{1} GB",
    [PW_TEXT_DECIMAL] = ".",
};

static const char *const text_pt[PW_TEXT_COUNT] = {
    [PW_TEXT_WELCOME_TITLE] = "Boas-vindas ao MihawkOS",
    [PW_TEXT_WELCOME_BODY] = "Vamos preparar seu PS5 para jogos do Windows. Leva cerca de dez minutos.",
    [PW_TEXT_GET_STARTED] = "Começar",
    [PW_TEXT_SKIP_SETUP] = "Pular configuração",
    [PW_TEXT_LANGUAGE_TITLE] = "Escolha seu idioma",
    [PW_TEXT_LANGUAGE_BODY] = "Seus jogos do Windows também vão usá-lo, com o layout de teclado dele. A área de trabalho "
        "do Mihawk OS continua em inglês.",
    [PW_TEXT_METHOD_TITLE] = "Escolha como instalar",
    [PW_TEXT_METHOD_BODY] = "O MihawkOS precisa do ambiente Windows dele, com cerca de 1,2 GB.",
    [PW_TEXT_METHOD_USB] = "Pen drive",
    [PW_TEXT_METHOD_USB_BODY] = "Copie os arquivos para um pen drive em qualquer computador.",
    [PW_TEXT_METHOD_INTERNET] = "Internet",
    [PW_TEXT_METHOD_INTERNET_BODY] = "Baixe direto no seu PS5.",
    [PW_TEXT_COMING_SOON] = "Em breve",
    [PW_TEXT_METHOD_INSTALLED] = "O ambiente Windows já está instalado.",
    [PW_TEXT_CONTINUE] = "Continuar",
    [PW_TEXT_QR_CAPTION] = "Escaneie para ver as instruções passo a passo no celular.",
    [PW_TEXT_USB_TITLE] = "Prepare um pen drive",
    [PW_TEXT_USB_STEP1] = "Em um computador, formate um pen drive em exFAT com tabela de partição MBR. Isso apaga o pen "
        "drive.",
    [PW_TEXT_USB_STEP2] = "Baixe o MihawkOS e copie a pasta mihawkos dele para a raiz do pen drive.",
    [PW_TEXT_USB_STEP3] = "Conecte o pen drive a uma porta USB do seu PS5.",
    [PW_TEXT_USB_STEP4] = "Escolha Verificar pen drive.",
    [PW_TEXT_CHECK_DRIVE] = "Verificar pen drive",
    [PW_TEXT_FOUND] = "O pen drive tem {1} para instalar.",
    [PW_TEXT_INSTALL] = "Instalar",
    [PW_TEXT_RETRY] = "Tentar de novo",
    [PW_TEXT_ERR_NO_STICK] = "Nenhum pen drive encontrado. Conecte-o, espere alguns segundos e tente de novo. Se ele já "
        "estiver conectado, formate-o em exFAT com MBR: o PS5 não lê unidades GPT nem NTFS.",
    [PW_TEXT_ERR_NO_FOLDER] = "O pen drive não tem uma pasta mihawkos na raiz. Copie a pasta para o pen drive e tente de "
        "novo.",
    [PW_TEXT_ERR_PARTIAL] = "A pasta mihawkos está incompleta: tem {1} de {2} partes. Copie a pasta inteira de novo e tente "
        "outra vez.",
    [PW_TEXT_ERR_NO_SPACE] = "Seu PS5 precisa de {1} livres e tem {2}. Apague algo e tente de novo.",
    [PW_TEXT_ERR_READ] = "Não foi possível ler o pen drive. Verifique se ele ainda está conectado e tente de novo. O que "
        "já foi instalado é mantido.",
    [PW_TEXT_ERR_DAMAGED] = "Um arquivo do pen drive está danificado ou é de outra versão. Copie a pasta mihawkos de novo "
        "e tente outra vez.",
    [PW_TEXT_ERR_FULL] = "O armazenamento do seu PS5 está cheio. Apague algo e tente de novo. O que já foi instalado é "
        "mantido.",
    [PW_TEXT_ERR_WRITE] = "O armazenamento do seu PS5 recusou uma gravação. Tente de novo; se acontecer outra vez, reinicie "
        "o PS5.",
    [PW_TEXT_ERR_CANCELLED] = "A instalação parou. O que já foi instalado é mantido.",
    [PW_TEXT_ERR_BUILD] = "Esta cópia do MihawkOS não pode instalar um ambiente Windows. Reinstale o MihawkOS.",
    [PW_TEXT_INSTALLING_TITLE] = "Instalando o ambiente Windows",
    [PW_TEXT_INSTALLING_BODY] = "Deixe o pen drive conectado. Leva cerca de um minuto.",
    [PW_TEXT_INSTALLING_CHECKING] = "Verificando o que já está instalado…",
    [PW_TEXT_INSTALLING_STATS] = "{1} de {2} MB · {3} MB/s",
    [PW_TEXT_INSTALLED] = "Instalado.",
    [PW_TEXT_STOP] = "Parar",
    [PW_TEXT_PREPARE_TITLE] = "Preparando o Mihawk OS",
    [PW_TEXT_PREPARE_BODY] = "A primeira inicialização cria seu disco do Windows. Leva alguns minutos, e a tela pode ficar "
        "parada por um tempo. Ela termina sozinha e volta para cá.",
    [PW_TEXT_PREPARE_NOTE] = "Durante esta primeira inicialização o controle não funciona nos jogos, por isso o MihawkOS "
        "a encerra assim que o disco fica pronto.",
    [PW_TEXT_PREPARE_START] = "Iniciar",
    [PW_TEXT_PREPARE_FAILED] = "A primeira inicialização não terminou. Tente de novo: ela continua de onde parou.",
    [PW_TEXT_BUILD_TITLE] = "Criando seu disco do Windows",
    [PW_TEXT_BUILD_BODY] = "Leva cerca de um minuto. Quando o disco estiver pronto, o MihawkOS volta sozinho para a "
        "configuração.",
    [PW_TEXT_BUILD_SETTINGS] = "Configurando o Windows",
    [PW_TEXT_BUILD_DOTNET] = "Instalando o suporte a .NET",
    [PW_TEXT_BUILD_FINISHING] = "Finalizando",
    [PW_TEXT_DONE_TITLE] = "Tudo pronto",
    [PW_TEXT_DONE_BODY] = "O Mihawk OS está pronto. Você pode refazer esta configuração em Settings, na biblioteca.",
    [PW_TEXT_ENTER] = "Entrar no Mihawk OS",
    [PW_TEXT_HINT_SELECT] = "Selecionar",
    [PW_TEXT_HINT_BACK] = "Voltar",
    [PW_TEXT_HINT_MOVE] = "Mover",
    [PW_TEXT_STEP_OF] = "Etapa {1} de {2}",
    [PW_TEXT_GIGABYTES] = "{1} GB",
    [PW_TEXT_DECIMAL] = ",",
};

/* The languages, in the owner's order (2026-10-18). Chinese and Japanese draw with their own faces (the setup's
 * Noto Sans SC and JP, baked with only these strings' characters: ps5/tools/generate_assets.py); the others with the
 * launcher's. Each flag is in ps5/assets/flags. */
static const PwSetupLanguage languages[] = {
    {"en-US", "English (US)", "us", "en_US.UTF-8", NULL, text_en},
    {"sv-SE", "Svenska", "se", "sv_SE.UTF-8", NULL, text_sv},
    {"fr-FR", "Français", "fr", "fr_FR.UTF-8", NULL, text_fr},
    {"es-ES", "Español", "es", "es_ES.UTF-8", NULL, text_es},
    {"de-DE", "Deutsch", "de", "de_DE.UTF-8", NULL, text_de},
    {"it-IT", "Italiano", "it", "it_IT.UTF-8", NULL, text_it},
    {"ru-RU", "Русский", "ru", "ru_RU.UTF-8", NULL, text_ru},
    {"zh-CN", "简体中文", "cn", "zh_CN.UTF-8", "noto-sans-sc", text_zh},
    {"ja-JP", "日本語", "jp", "ja_JP.UTF-8", "noto-sans-jp", text_ja},
    {"pt-BR", "Português (Brasil)", "br", "pt_BR.UTF-8", NULL, text_pt},
};

const PwSetupLanguage *pw_setup_languages(size_t *count)
{
    *count = sizeof(languages) / sizeof(languages[0]);
    return languages;
}

const PwSetupLanguage *pw_setup_language(const char *tag)
{
    for (size_t i = 0; tag && i < sizeof(languages) / sizeof(languages[0]); ++i)
        if (languages[i].text && !strcmp(languages[i].tag, tag)) return &languages[i];
    return NULL;
}

const PwSetupLanguage *pw_setup_default_language(void)
{
    return &languages[0];
}

const char *pw_setup_text(const PwSetupLanguage *language, PwSetupText key)
{
    if ((unsigned)key >= PW_TEXT_COUNT) return "";
    if (!language || !language->text) language = pw_setup_default_language();
    return language->text[key];
}

size_t pw_setup_fill(char *out, size_t size, const char *text, const char *const *args, size_t count)
{
    size_t used = 0;
    if (!size) return 0;
    for (const char *p = text; *p; ++p) {
        const char *piece = p;
        size_t length = 1;
        if (p[0] == '{' && p[1] >= '1' && p[1] <= '9' && p[2] == '}' && (size_t)(p[1] - '1') < count) {
            piece = args[p[1] - '1'];
            length = strlen(piece);
            p += 2;
        }
        if (length > size - 1 - used) length = size - 1 - used;
        memcpy(out + used, piece, length);
        used += length;
    }
    out[used] = 0;
    return used;
}

size_t pw_setup_gigabytes(const PwSetupLanguage *language, unsigned long long bytes, char *out, size_t size)
{
    const unsigned long long hundredths = (bytes + 5000000ull) / 10000000ull;
    char number[48];
    snprintf(number, sizeof(number), "%llu%s%02llu", hundredths / 100, pw_setup_text(language, PW_TEXT_DECIMAL),
             hundredths % 100);
    const char *args[] = {number};
    return pw_setup_fill(out, size, pw_setup_text(language, PW_TEXT_GIGABYTES), args, 1);
}

int pw_setup_record_load(PwSetupRecord *out, const char *path)
{
    char text[512];
    memset(out, 0, sizeof(*out));
    FILE *file = fopen(path, "r");
    if (!file) return errno;
    const size_t size = fread(text, 1, sizeof(text), file);
    const int error = ferror(file) ? EIO : 0;
    fclose(file);
    if (error) return error;
    const char *end = text + size;
    for (const char *line = text; line < end;) {
        const char *stop = memchr(line, '\n', (size_t)(end - line));
        if (!stop) stop = end;
        size_t length = (size_t)(stop - line);
        if (length && line[length - 1] == '\r') --length;
        if (length > 9 && !memcmp(line, "language=", 9) && length - 9 < sizeof(out->language)) {
            memcpy(out->language, line + 9, length - 9);
            out->language[length - 9] = 0;
        } else if (length == 6 && !memcmp(line, "done=1", 6)) {
            out->done = 1;
        }
        line = stop + 1;
    }
    return 0;
}

int pw_setup_record_save(const PwSetupRecord *record, const char *path)
{
    char temporary[1024];
    if (snprintf(temporary, sizeof(temporary), "%s.tmp", path) >= (int)sizeof(temporary)) return ENAMETOOLONG;
    FILE *file = fopen(temporary, "w");
    if (!file) return errno;
    int error = 0;
    if ((record->language[0] && fprintf(file, "language=%s\n", record->language) < 0) ||
        (record->done && fputs("done=1\n", file) < 0))
        error = EIO;
    if (fflush(file) || fsync(fileno(file))) error = errno;
    if (fclose(file) && !error) error = errno;
    if (!error && rename(temporary, path)) error = errno;
    if (error) unlink(temporary);
    return error;
}

int pw_setup_prefix_made(char *stamp)
{
    size_t length = strlen(stamp);
    while (length && strchr("\r\n ", stamp[length - 1])) stamp[--length] = 0;
    return length >= 6 && !strcmp(stamp + length - 6, " wow64");
}

PwSetupBuild pw_setup_build_next(PwSetupBuild stage, const char *command_line)
{
    if (!command_line || stage >= PW_SETUP_BUILD_FINISHING) return stage;
    const int mono = strstr(command_line, "mono") != NULL;
    if (stage == PW_SETUP_BUILD_SETTINGS) return mono ? PW_SETUP_BUILD_DOTNET : stage;
    return mono ? stage : PW_SETUP_BUILD_FINISHING;
}

/* The cover's marks: anti-aliased by each pixel's distance to the shape, over the square they own. */
enum { MARK_X0 = PW_SETUP_COVER_MARK_X - 32, MARK_X1 = PW_SETUP_COVER_MARK_X + 32,
       MARK_Y0 = PW_SETUP_COVER_ROW_Y - 32, MARK_Y1 = PW_SETUP_COVER_ROW_Y + 2 * PW_SETUP_COVER_ROW_STEP + 32 };

static void cover_blend(unsigned *pixel, unsigned color, float coverage)
{
    if (coverage <= 0.0f) return;
    const unsigned alpha = coverage >= 1.0f ? 255u : (unsigned)(coverage * 255.0f + 0.5f), keep = 255u - alpha;
    unsigned out = 0xff000000u;
    for (int shift = 0; shift < 24; shift += 8)
        out |= ((((*pixel >> shift) & 0xffu) * keep + ((color >> shift) & 0xffu) * alpha + 127u) / 255u) << shift;
    *pixel = out;
}

/* shape: 0 a disc of radius r, 1 a ring of radius r and half-width w, 2 the segment (x0, y0)-(x1, y1) of half-width w. */
static void cover_shape(unsigned *frame, int shape, float x0, float y0, float x1, float y1, float r, float w,
                        unsigned color, float strength)
{
    const float reach = (shape == 2 ? 0.0f : r) + w + 1.0f;
    const int left = (int)fminf(x0, x1) - (int)reach, right = (int)fmaxf(x0, x1) + (int)reach + 1;
    const int top = (int)fminf(y0, y1) - (int)reach, bottom = (int)fmaxf(y0, y1) + (int)reach + 1;
    for (int y = top < MARK_Y0 ? MARK_Y0 : top; y < bottom && y < MARK_Y1; ++y)
        for (int x = left < MARK_X0 ? MARK_X0 : left; x < right && x < MARK_X1; ++x) {
            const float px = (float)x + 0.5f, py = (float)y + 0.5f;
            float distance;
            if (shape == 2) {
                const float dx = x1 - x0, dy = y1 - y0;
                float t = ((px - x0) * dx + (py - y0) * dy) / (dx * dx + dy * dy);
                t = t < 0.0f ? 0.0f : t > 1.0f ? 1.0f : t;
                distance = hypotf(px - x0 - t * dx, py - y0 - t * dy) - w;
            } else {
                const float d = hypotf(px - x0, py - y0);
                distance = shape == 0 ? d - r : fabsf(d - r) - w;
            }
            cover_blend(&frame[(size_t)y * PW_SETUP_COVER_WIDTH + (size_t)x], color, (0.5f - distance) * strength);
        }
}

void pw_setup_cover_draw(unsigned *frame, const unsigned *picture, PwSetupBuild stage, unsigned tick)
{
    /* The tour's Gloss colours (examples/ps5proton/setup_tour.hpp's renders): success, primary, and a muted grey. */
    const unsigned green = 0xff32a56du, blue = 0xff2f8cf0u, grey = 0xff96a0acu, white = 0xffffffffu;
    for (int y = MARK_Y0; y < MARK_Y1; ++y)
        memcpy(frame + (size_t)y * PW_SETUP_COVER_WIDTH + MARK_X0, picture + (size_t)y * PW_SETUP_COVER_WIDTH + MARK_X0,
               (MARK_X1 - MARK_X0) * sizeof(unsigned));
    for (int row = 0; row < 3; ++row) {
        const float x = PW_SETUP_COVER_MARK_X, y = (float)(PW_SETUP_COVER_ROW_Y + row * PW_SETUP_COVER_ROW_STEP);
        if (row < (int)stage) {
            cover_shape(frame, 0, x, y, x, y, 22.0f, 0.0f, green, 1.0f);
            cover_shape(frame, 2, x - 10.0f, y + 1.0f, x - 3.0f, y + 8.0f, 0.0f, 2.6f, white, 1.0f);
            cover_shape(frame, 2, x - 3.0f, y + 8.0f, x + 10.0f, y - 7.0f, 0.0f, 2.6f, white, 1.0f);
        } else if (row == (int)stage) {
            for (unsigned dot = 0; dot < 8; ++dot) {
                const float angle = (float)dot * 0.785398163f - 1.570796327f;
                const unsigned behind = (tick + 8u - dot) % 8u;
                const float dx = x + 15.0f * cosf(angle), dy = y + 15.0f * sinf(angle);
                cover_shape(frame, 0, dx, dy, dx, dy, 3.6f, 0.0f, blue,
                            behind < 6u ? 1.0f - (float)behind * 0.15f : 0.15f);
            }
        } else {
            cover_shape(frame, 1, x, y, x, y, 20.0f, 1.5f, grey, 1.0f);
        }
    }
}
