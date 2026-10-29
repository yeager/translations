type Values = Record<string, string | number>;

const catalogs: Record<string, Record<string, string>> = {
  sv: {
    "Backend error": "Bakändsfel",
    "PS5 Updates": "PS5-uppdateringar",
    "{{tag}} available{{prerelease}}": "{{tag}} är tillgänglig{{prerelease}}",
    " (pre-release)": " (förhandsversion)",
    "Update failed: {{error}}": "Uppdateringen misslyckades: {{error}}",
    "{{tag}} installed. Powering off in {{seconds}} s":
      "{{tag}} har installerats. Stänger av om {{seconds}} s",
    "Update to {{tag}}?": "Uppdatera till {{tag}}?",
    "Installs the new kernel (with a backup) and powers off the PS5. Then turn it on and start Linux with the loader.":
      "Installerar den nya kärnan med en säkerhetskopia och stänger av PS5:an. Starta sedan PS5:an och Linux med startprogrammet.",
    " This is a pre-release (test build).":
      " Detta är en förhandsversion (testbygge).",
    Continue: "Fortsätt",
    Cancel: "Avbryt",
    Close: "Stäng",
    "Open on GitHub": "Öppna på GitHub",
    "Update and power off": "Uppdatera och stäng av",
    "just now": "just nu",
    "{{hours}} h ago": "för {{hours}} tim sedan",
    "{{days}} days ago": "för {{days}} dagar sedan",
    "Pre-release": "Förhandsversion",
    Stable: "Stabil",
    "Up to date": "Aktuell",
    "Release notes": "Versionsinformation",
    "Install and power off": "Installera och stäng av",
    "Updating to {{tag}}": "Uppdaterar till {{tag}}",
    Update: "Uppdatera",
    "The PS5 stays on.": "PS5:an förblir påslagen.",
    "Cancel power off ({{seconds}} s)": "Avbryt avstängning ({{seconds}} s)",
    Back: "Tillbaka",
    "Installed:": "Installerad:",
    "Checking…": "Kontrollerar …",
    "Check now": "Kontrollera nu",
    "Checked at {{time}}": "Kontrollerad {{time}}",
  },
};

function locale() {
  const language =
    typeof navigator === "undefined"
      ? "en"
      : (navigator.languages?.[0] ?? navigator.language ?? "en");
  return language.toLowerCase().split("-")[0];
}

export function t(source: string, values: Values = {}) {
  const target = catalogs[locale()]?.[source] ?? source;
  return target.replace(/\{\{(\w+)\}\}/g, (_, key) =>
    String(values[key] ?? `{{${key}}}`),
  );
}

export const supportedLocales = Object.freeze(Object.keys(catalogs));
