import Foundation
import SwiftUI

/// The application-facing localization boundary.  Keep UI text as stable English
/// keys and put translations in `Resources/<language>.lproj/Localizable.strings`.
/// Adding a language therefore needs no code change.
enum L10n {
    static func string(_ key: String, comment: String = "") -> String {
        NSLocalizedString(key, tableName: nil, bundle: .module, value: key, comment: comment)
    }
}

/// A localized equivalent of `Text("…")` for Swift Package resources.
/// SwiftUI's literal initializer looks in the main bundle, whereas this app's
/// package resources are in `Bundle.module`.
struct L10nText: View {
    private let key: String

    init(_ key: String) {
        self.key = key
    }

    var body: some View {
        Text(verbatim: L10n.string(key))
    }
}

/// A localized label with an SF Symbol.  Use it for controls backed by the
/// package resource bundle instead of `Label("…", systemImage: …)`.
struct L10nLabel: View {
    private let key: String
    private let systemImage: String

    init(_ key: String, systemImage: String) {
        self.key = key
        self.systemImage = systemImage
    }

    var body: some View {
        Label {
            L10nText(key)
        } icon: {
            Image(systemName: systemImage)
        }
    }
}
