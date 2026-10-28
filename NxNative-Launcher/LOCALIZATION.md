# Localizing NxNative Launcher

The graphical application is a Swift package, so its localized resources live
with the `NXNativeGUI` target rather than in the main application bundle.

## Add a language

1. Create `Sources/Resources/<language>.lproj/Localizable.strings`, for
   example `de.lproj/Localizable.strings`.
2. Copy the English keys from the Swedish catalog. Keep the text on the left
   unchanged and translate only the value on the right.
3. Use `L10n.string("Key")` for a string property and `L10nText("Key")` for
   visible SwiftUI text. `L10nLabel("Key", systemImage: "…")` is the
   equivalent for SF Symbol labels.
4. Run the checks below. On macOS, set the app language in the system language
   settings and relaunch the app to verify the result in context.

## Checks

```sh
cd gui
swift build
plutil -lint Sources/Resources/sv.lproj/Localizable.strings
python3 ../scripts/check_localization.py
```

`L10n` looks up strings in `Bundle.module`, which is required for resources
processed by Swift Package Manager. Missing translations deliberately fall
back to their English key, so adding a language is safe while it is being
completed.
