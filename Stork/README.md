# Stork Web UI translations

The Web UI uses Angular's built-in localization support. English is built at
`/`; each translated locale is built in its own directory, such as `/sv/`.
The Stork server recognizes those directories and serves their `index.html`
for client-side routes.

## Updating a catalog

Extract the current messages after adding or changing `$localize` messages:

```sh
npx ng extract-i18n --output-path src/locale --out-file messages.xlf
```

Create a translated copy named `messages.<locale>.xlf`, add it in the `i18n`
section of `angular.json`, and build all production locales with:

```sh
npx ng build --configuration production
```

Use stable custom message identifiers (`@@…`) for messages defined in
TypeScript. They keep translations valid when source files move.
