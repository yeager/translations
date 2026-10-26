# Ymir SDL3 translations

The unmerged [PR #959](https://github.com/ymir-emu/Ymir/pull/959) proposed GNU gettext support. It was closed without merging on 2026-10-25; the maintainer wants the core team to discuss an internationalization solution first. The files here are an archive of the proposal, not a description of current upstream functionality.

In that proposal, `sv.po` is the Swedish catalog and builds to
`locale/sv/LC_MESSAGES/ymir-sdl3.mo` next to the executable.

Within the proposed implementation, when a source string changes, regenerate the template from the sources listed
in `apps/ymir-sdl3/CMakeLists.txt` and merge it into each catalog:

```sh
cmake --build <build-directory> --target ymir-sdl3-pot
msgmerge --update sv.po ymir-sdl3.pot
msgfmt --check --check-format --output-file=/dev/null sv.po
```

Use `_()` for a translatable string. Keep ImGui ID suffixes such as `##vdp1`
outside the translated text and use `ImGui::PushID()` when two visible strings
need separate widget identifiers.
