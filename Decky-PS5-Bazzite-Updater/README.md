# PS5 Bazzite Updater (Decky plugin)

A [Decky Loader](https://github.com/SteamDeckHomebrew/decky-loader) plugin for [PS5 Bazzite Deck](https://github.com/VivaLaVent/ps5-bazzite-deck) by VivaLaVent.

It saves you from checking GitHub by hand: it tells you when a new PS5 Bazzite Deck version is out, shows its release notes, and can install it and power off the console for you.

> **Unofficial.** This plugin is not made by or affiliated with VivaLaVent or the PS5 Linux projects. It installs kernels: use it at your own risk.

## Features

- Shows your installed version (`/etc/ps5-bazzite-deck-version`).
- Checks [the project's releases](https://github.com/VivaLaVent/ps5-bazzite-deck/releases) when Steam starts and every 6 hours. A Steam notification appears once per new version.
- Two cards: the latest **Stable** release, plus the latest **Pre-release** when it's newer than the stable one. Test builds like `vrr-test20` are ignored.
- **Release notes** opens the full notes in a popup, with a link to GitHub.
- **Install and power off**, after a confirmation:
  1. Downloads that version's update bundle (`ps5-bazzite-deck-<version>-update.tar.xz`).
  2. Checks its SHA256 against the published `.sha256` file.
  3. Runs the bundle's own `update.sh`, the same script as the project's manual update (it backs up the current kernel and modules first).
  4. Powers off after 10 seconds (you can cancel), **only** if `update.sh` ends with `DONE`. If anything fails, nothing is powered off and the log is shown.

After it powers off, turn the PS5 on and start Linux with the loader as usual. A new kernel needs that cold start.

## Requirements

- A PS5 running **PS5 Bazzite Deck v1.0.3 or newer**: the in-place update bundles start there.
- **Decky Loader** installed.
- A network connection.

## Install

The plugin isn't in the Decky store, so install it from Decky's developer options.

### 1. Turn on Developer mode in Decky

1. Press the **`...`** button (Quick Access Menu) and open the **Decky** tab (the plug icon).
2. Select the **gear icon** (Decky settings).
3. Under **General**, switch **Developer mode** on.

A new **Developer** section appears in Decky's settings.

### 2. Install the plugin

**Option A: from URL (easiest)**

1. Decky settings → **Developer** → **Install Plugin from URL**.
2. Enter:
   ```
   https://github.com/cmartinespinosa/decky-ps5-bazzite-updater/releases/latest/download/decky-ps5-bazzite-updater.zip
   ```
3. Select **Install** and confirm.

**Option B: from a ZIP file**

1. Download `decky-ps5-bazzite-updater.zip` from the [latest release](https://github.com/cmartinespinosa/decky-ps5-bazzite-updater/releases/latest) onto the PS5 (for example in Desktop Mode, into `~/Downloads`).
2. Decky settings → **Developer** → **Install Plugin from ZIP File** → **Browse** → pick the ZIP → **Install**.

**PS5 Updates** then shows up in the Decky plugin list. You can switch Developer mode off again afterwards.

### Why it runs as root

Installing a kernel needs root, so the plugin has Decky's `root` flag. Decky shows this when you install it. The plugin only runs `curl`, `tar`, the downloaded bundle's `update.sh` (after the SHA256 check), and `systemctl poweroff`.

## Undo an update

`update.sh` prints an undo command and keeps a backup in `/var/lib/ps5-update-backup/<date>/`. See the [PS5 Bazzite Deck releases](https://github.com/VivaLaVent/ps5-bazzite-deck/releases) for details.

## Build from source

Needs Node.js 18+.

```bash
npx -y pnpm@9 install
npx -y pnpm@9 run build
```

The plugin is `plugin.json`, `package.json`, `main.py`, `LICENSE` and `dist/index.js`. Copy them to `~/homebrew/plugins/PS5 Updates/` on the PS5 (as root), then run `sudo systemctl restart plugin_loader`.

## Status

Tested on a base PS5 with PS5 Bazzite Deck v1.5.1: the plugin loads and reads the releases from GitHub. The full install-and-power-off flow runs the project's own update script, but hasn't been tried end to end through the plugin yet. Please open an issue if it fails for you.

## Translations

The plugin follows the language exposed by Decky's browser UI. English source
texts are the built-in fallback and Swedish is included. To add another
language, add its ISO language code and translations to `catalogs` in
`src/i18n.ts`; no component changes or external translation service are
required.

## Credits

- [VivaLaVent/ps5-bazzite-deck](https://github.com/VivaLaVent/ps5-bazzite-deck) for the distro and its update bundles.
- [Steam Deck Homebrew](https://github.com/SteamDeckHomebrew) for Decky Loader and the plugin template.

## License

BSD-3-Clause, see [LICENSE](LICENSE).
