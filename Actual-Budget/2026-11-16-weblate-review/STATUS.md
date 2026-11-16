# Actual Budget Swedish review

Date: 2026-11-16  
Component: `actual`  
Upstream: Hosted Weblate

Actual Budget documents Hosted Weblate's suggestion workflow as its only
translation contribution path. The live Swedish component had 3,017 strings;
1,589 were translated and 1,428 remained unfinished when this review began.

The raw English and Swedish exports are retained unchanged in `raw/`.
`actual-sv-api-batch-01.json` is a separately maintained suggestion batch.
Every proposal preserves placeholders and markup. Suggestions are pending the
project's required community voting; they are not accepted translations.

## Batch 1

The initial line-by-line pass covered all 41 units that were unfinished and
had no proposal. Two existing plural translations were retained: Swedish uses
the same visible noun form after a numeral in these contexts. The other 39
units now have Swedish suggestions. Six of those were submitted through the
Hosted Weblate REST API with HTTP `201`; a subsequent API readback confirms
`has_suggestion: true` for each. The first 33 low-risk UI and storage strings
were submitted through the same project suggestion workflow before the API
credential was located.

Remaining Swedish work is substantial: 1,402 unfinished units still have
existing suggestions and must be reviewed individually rather than bulk
accepted.

## Reviewed suggestions batch 1

Ten existing proposals were reviewed against their English source, terminology
and placeholders. Nine received a positive API vote and were accepted by
Weblate. Readback of all nine units shows state `20` with the reviewed Swedish
target and `has_suggestion: false`. The `All time` proposal was voted on but
remains subject to the component's voting workflow.

## Reviewed suggestions batch 2

Nine further UI, finance and server strings were reviewed and accepted through
the suggestion vote endpoint. Two weak suggestions were not endorsed:
`Lankesisk rupie` was replaced with `Srilankesisk rupie`, and `Trimma
intervall` with the clearer `Beskär intervall`. Both replacements are pending
community review.

## Reviewed suggestions batch 3

Twelve suggestions for storage actions and formula/query descriptions were
checked and accepted through the API. `Uzbekisk som` was not endorsed; a new
proposal, `Uzbekisk sum`, corrects the Swedish currency name and is pending
review.

## Reviewed suggestions batch 4

Seventeen formula-function descriptions were checked line by line and accepted
through the API. Technical literals such as `TRUE`, `FALSE` and `e` remain
unchanged, while the Swedish wording preserves the functions' return-value
semantics.

## Reviewed suggestions batch 5

Twenty additional formula-function descriptions were reviewed and accepted via
the API. The Swedish proposals preserve `TRUE`, `PI`, `#N/A` and the formula
terminology while keeping each predicate's meaning intact.

## Reviewed suggestions batch 6

Fifteen further formula-function descriptions were reviewed and accepted via
the API. `Returnerar TRUE om värdet är något fel.` was not endorsed; the
more idiomatic proposal `Returnerar TRUE om värdet är ett fel.` is pending
community review. API readback confirms state `20` and no remaining
suggestion for every accepted unit.

## Reviewed suggestions batch 7

Fourteen short import, scheduling, retirement and transaction UI strings were
reviewed line by line and accepted through the API. The accepted wording uses
the existing `schema` terminology and retains UI punctuation and `%` markers.

## Reviewed suggestions batch 8

Nine import, data-directory and transaction messages were reviewed and accepted
through the API. The review verified React-style tags, the
`{{githubIssueLink}}` placeholder, quoted identifiers and the `&rarr;` entity.

## Reviewed suggestions batch 9

Eleven data-directory, browser-compatibility, file-sharing, transaction and
retirement UI messages were reviewed and accepted through the API. Two
domain-dependent budget-scheduling proposals were deliberately deferred until
their feature context can be checked.

## Context-checked proposals batch 7

The two deferred terms were checked against the current Actual source and its
Tracking Budget documentation. API-submitted replacement proposals use
`uppföljningsbudgetering` for the documented mode and `schema som förfaller`
for a schedule due today. Both are pending community review; neither was
self-voted.

## Reviewed suggestions batch 10

Twenty synchronization, category-management, banking and reporting strings
were reviewed and accepted through the API. The accepted translations retain
`{{monthYearFormatted}}`, distinguish categories from category groups, and use
the established Swedish banking term `ingående saldo`.

## Reviewed suggestions batch 11

Fifteen report, tag and account-management messages were reviewed and accepted
through the API. The batch preserves PluggyAI and SimpleFIN as product names,
and uses the same `kategorigrupp` terminology as the previous review.

## Reviewed suggestions batch 12

Seventeen payment, spending-limit, location and theme strings were reviewed and
accepted through the API. The accepted translations preserve the daily,
monthly and weekly placeholders and retain the financial distinction between a
soft and hard limit.

## Reviewed suggestions batch 13

Ten import, synchronization, account-linking and formula-result strings were
reviewed and accepted through the API. The batch preserves the `{{queryName}}`
placeholder and the established accounting terms for opening and closing
balances.

## Terminology

`TERMINOLOGY.md` records the project-specific Swedish decisions used in this
review, including accounting, scheduling, Tracking Budget and formula-query
terms. It is based on the reviewed component, the current source and Actual's
Tracking Budget documentation.

## Context-checked proposals batch 8

The current formula catalog and rule-editor source confirmed that `query` is a
formula-query concept rather than a general search. Six API proposals replace
the earlier `sökning` wording with `fråga`; they are pending community review
and were not self-voted.

## Reviewed suggestions batch 14

Seven category-control, empty-state and Sankey-report strings were reviewed and
accepted through the API. `Sankey` remains unchanged as the chart type name;
its UI compounds use standard Swedish hyphenation.

## Reviewed suggestions batch 15

Five formula-mode, sorting, currency and explanatory budget strings were
reviewed and accepted through the API. The review preserved the established
`Pengarnas ålder` name for the budget metric.

## Context-checked proposals batch 9

The transaction-edit confirmation and payee-merge source components were
checked before three API proposals were submitted. They improve the Swedish
wording for the target payee and for an account reconciliation becoming out of
balance. All three proposals are pending community review and were not
self-voted.

## Reviewed suggestions batch 16

Sixteen bank-synchronization, provider-configuration and error-recovery strings
were reviewed and accepted through the API. The review preserved provider
placeholders, Actual as a product name, and the distinction between normal and
hard page reloads.

## Reviewed suggestions batch 17

Nine template, chart, database-compatibility, encryption, currency and sorting
strings were reviewed and accepted through the API. The batch preserves the
`{{fileName}}` placeholder and uses Swedish alphabetical sorting endpoints.

## Reviewed suggestions batch 18

Eleven formula metadata and text-function strings were reviewed and accepted
through the API. The batch preserves `QUERY_EXTRACT_TIMEFRAME_START()` exactly
and uses Swedish technical terms for return types and strings.

## Reviewed suggestions batch 19

Eight bank-provider permissions and transaction-table strings were reviewed and
accepted through the API. The batch preserves the `{{ columnName }}`
placeholder and uses the accounting term `löpande saldo`.

## Reviewed suggestions batch 20

Three investment-planning strings were reviewed and accepted through the API:
portfolio allocation, portfolio performance and the name of a savings pot.

## Reviewed suggestions batch 21

Four budget-navigation and help strings were reviewed and accepted through the
API, including the month-picker guidance.

## Reviewed suggestions batch 22

The `Notifications` and `Offline` UI strings were reviewed and accepted through
the API. The plural notification and the financial `Ratcheting` explanation
were deferred for separate plural and terminology review.

## Reviewed suggestions batch 23

The encoding label and unchanged `ISO-8859-2` format name were reviewed and
accepted through the API. The auto-detection label was deferred for UI-context
review.

## Reviewed suggestions batch 24

Three savings-pot, report-widget and theme strings were reviewed and accepted
through the API.

## Reviewed suggestions batch 25

Two one-off withdrawal strings were reviewed and accepted through the API. The
review preserves all financial placeholders, arithmetic symbols and tax terms.

## Reviewed suggestions batch 26

The `Transactions` proposal was reviewed and received a positive API vote. It
remains pending the component's community voting workflow and is not accepted
translation state.

## Reviewed suggestions batch 27

Three one-off withdrawal labels and explanations were reviewed and accepted
through the API. The batch preserves requested, gross, tax and net placeholders
and the arithmetic symbols.

## Reviewed suggestions batch 28

The `Add key` UI action was reviewed and accepted through the API.

## Reviewed suggestions batch 29

The OpenID warning about closing sessions and revoking existing API keys was
reviewed and accepted through the API.

## Reviewed suggestions batch 30

The warning about revoking a named integration key was reviewed and accepted
through the API. The `{{name}}` placeholder and data-retention consequence are
preserved.

## Reviewed suggestions batch 31

The budget-storage warning was reviewed and accepted through the API. The
`{{id}}` placeholder and the assurance that no data was deleted are preserved.

## Reviewed suggestions batch 32

The API-key creation error message was reviewed and accepted through the API.

## Reviewed suggestions batch 33

The `Done` API-key modal button was checked in the current source and accepted
through the API as `Klar`.

## Reviewed suggestions batch 34

The API-key loading error message was reviewed and accepted through the API.

## Reviewed suggestions batch 35

Ten API-key, retry and tag-management UI strings were checked in the current
source and accepted through the API. The batch preserves the `{{id}}`, `{{tag}}`
and `{{name}}` placeholders.

## Reviewed suggestions batch 36

Seven tag and infopanel UI strings were checked in the current source and
accepted through the API. The `{{ dashboardName }}` and `{{minimumVersion}}`
placeholders are preserved. A plural and two of the reviewer's own proposals
were intentionally left for separate handling.

## Reviewed suggestions batch 37

Eight API-key and browser-storage UI strings were checked in the current source
and accepted through the API. The `{{id}}` placeholder and the product terms
`OpenID`, `API` and `CLI` are preserved.

## Reviewed suggestions batch 38

Thirteen update, budget-average and investment UI strings were accepted through
the API. The `{{displayMonth}}`, `{{months}}`, `{{share}}` and `{{mean}}`
placeholders are preserved. Two financial-planning explanations remain pending
because their terminology and punctuation need separate contextual review.

## Reviewed suggestions batch 39

Twelve investment, banking and export UI strings were checked in current source
and accepted through the API. The `{{name}}`, `{{reason}}` and `<5>` markup
are preserved. The source label `Auto` and two financial-planning strings were
left for more specific terminology review.

## Reviewed suggestions batch 40

Thirteen encoding, tag, release-note and notification strings were accepted
through the API. Format names, `{{group}}`, `{{max}}`, `{{title}}`,
`{{changeCount}}` and `<0>` markup are preserved. Two alternatives were sent
as unvoted proposals: `Fäll ut {{group}}` and `Nydesignat sidofält`.

## Reviewed suggestions batch 41

Fourteen automatic-sync and bank-connection UI strings were accepted through
the API. The Actual and GoCardless product names are retained; the explanatory
text was checked as account-sync UI context.

## Reviewed suggestions batch 42

Eleven release, account-group and synchronisation UI strings were accepted
through the API. The lengthy market-simulation explanations were deferred for
separate financial terminology review.

## Reviewed suggestions batch 43

Twelve account-group, release and local-folder UI strings were accepted through
the API. The `{{version}}` placeholder and the Actual product name are
preserved. The account-identifier formula documentation remains for separate
technical terminology review.

## Reviewed suggestions batch 44

Four onboarding strings were accepted through the API, with `{{appName}}` and
`<1>`/`<4>` markup preserved. A complete, unvoted alternative replaces the
English loanword in the tracking-budget explanation with `uppföljningsbudget`.
The tour and investment-pot wording remains pending because it needs separate
UI terminology review.

## Reviewed suggestions batch 45

Fifteen simulation settings and result UI strings were accepted through the API.
The `{{age}}`, `{{number}}`, `{{total}}`, `{{from}}` and `{{to}}` placeholders
are preserved. Ratcheting terminology, its explanatory copy and two proposals
using an em dash contrary to the source punctuation were left pending.

## Reviewed suggestions batch 46

Seventeen simulation and tax UI strings were accepted through the API. The
`{{age}}`, `{{number}}`, `{{total}}`, `{{from}}` and `{{to}}` placeholders are
preserved. The source-specific ratcheting and progressive-tax wording remains
pending for terminology review.

## Reviewed suggestions batch 47

Seven concise tax and simulation-result UI labels were accepted through the API.
The surrounding tax-rate explanations remain pending for financial terminology
review.

## Reviewed suggestions batch 48

Twelve concise simulation-setting and result UI strings were accepted through
the API. The `{{age}}` placeholder is preserved. The age-access, spending-rule
and capital-preservation explanations remain pending for specific financial UI
context review.

## Reviewed suggestions batch 49

Fourteen values, transaction-range, export, budget and server-sync strings were
accepted through the API. The `<1>` markup is preserved. A more idiomatic,
unvoted alternative, `Transaktioner genom tiderna`, was submitted for the
all-time transaction filter.

## Reviewed suggestions batch 50

Sixteen warning, Akahu banking, budget-automation and transaction-schedule
strings were accepted through the API. The `SharedArrayBuffer` and Akahu names
and `<2>` markup are preserved. Three unvoted alternatives were submitted:
`Genomsnittliga utgifter` for the two spending-average labels and
`Uppföljningsbudget` for the tracking-budget label.

## Reviewed suggestions batch 51

Fifteen authentication, Enable Banking and long-term goal strings were accepted
through the API. The `.pem` format, `Enable Banking`, `{{amount}}` and `<2>`
markup are preserved. One unvoted alternative improves the automation forecast
wording to `det högsta belopp`.

## Reviewed suggestions batch 52

Eight automation-export and pool-management UI strings were accepted through
the API. The `{{groupName}}` placeholder is preserved. Early-spending wording
and the longer end-of-month-cleanup explanation remain pending because their
financial feature terminology needs contextual review.

## Reviewed suggestions batch 53

Nineteen data-status, widget, filter, synchronisation, schedule and category UI
strings were accepted through the API. The filter placeholders and markup are
preserved. The CSS label retains the source em dash, as does the source.

## Reviewed suggestions batch 54

Five automation, currency, rule, transfer and formula-row strings were accepted
through the API. The three transfer placeholders are preserved. An unvoted
alternative improves the widget-save failure message to `Det gick inte att
spara`. Query terminology, currency names, schedule wording and all-time
filter wording remain under distinct review rather than being auto-accepted.

## Suggestion-vote update

On 2026-11-16, nine archived reviewer proposals each had an existing positive
vote. Following explicit authorization, each received the reviewer's positive
vote through the API. Weblate returned `voted` for all nine; none was reported
as accepted by that vote call, so they remain pending project acceptance.

Following explicit authorization, nine competing proposals were also given a
negative vote where an archived reviewer proposal was concretely better:
`Fäll ut`, `Nydesignat`, `uppföljningsbudget`, `Transaktioner genom tiderna`,
`Genomsnittliga utgifter`, `det högsta belopp` and `Det gick inte att spara`.
Weblate returned `voted` for each negative-vote call.

Three further archived reviewer proposals with existing positive votes received
the reviewer's positive vote, while the three less precise alternatives received
a negative vote. An additional better alternative, `Maskerat skript`, was
submitted and the competing `Dolt skript` proposal received a negative vote.

Nine additional terminology proposals with existing positive votes also
received the reviewer's positive vote. Less accurate competing terms received a
negative vote: `All Historik`, `Genom tiderna`, `Trimma intervall`, the less
specific currency names, `Sökningsdefinitioner`, `något fel`, `Sökningens
namn`, `tracking-budgetering` and `förfallet schema`. This preserves the
project's reviewed terms `Hela perioden`, `Beskär intervall`,
`Frågedefinitioner`, `uppföljningsbudgetering` and `schema som förfaller`.

## Reviewed suggestions batch 55

Sixteen filter, transaction-status, infopanel and custom-theme UI strings were
accepted through the API. The `CSS` term is preserved.

## Reviewed suggestions batch 56

Twenty transaction, time-setting, currency, account and infopanel error strings
were accepted through the API. The repeated messages were reviewed as a shared
UI family to ensure consistent wording.

## Reviewed suggestions batch 57

Nine infopanel, split-status, budget-analysis and money-age UI strings were
accepted through the API. The `{{count}}` and `{{days}}` placeholders are
preserved. `Maskerat skript` was submitted as an unvoted alternative to the
less accurate `Dolt skript`.

## Reviewed suggestions batch 58

The fixed-decimal formula description was accepted through the API. Two plural
suggestions were intentionally excluded: the suggestion-vote helper only
supports singular targets and the plural forms require a separate safe upload
path.

## Reviewed suggestions batch 59

Seventeen automation-template, time-unit and Enable Banking setup strings were
accepted through the API. The `{{source}}` placeholder, HTML quote entities,
`Enable Banking` and `ID` terms are preserved.

## Reviewed suggestions batch 60

Thirteen formula, calculator and chart UI strings were accepted through the API.
The `{{amount}}` placeholder is preserved, along with the function and format
terminology.

## Reviewed suggestions batch 61

Sixteen connection, onboarding, date-navigation and transaction-state strings
were accepted through the API. Four better unvoted alternatives were submitted
for a server-link sentence, guided onboarding, tagline punctuation and the
reconciled-state label. The less accurate competing proposals received a
negative vote as explicitly authorized.

## Reviewed suggestions batch 62

Thirteen Monte Carlo and simulation-plan labels were accepted through the API.
The `{{age}}` and `{{number}}` placeholders are preserved. The age-limit label
and rule terminology remain pending for more specific simulation context.

## Reviewed suggestions batch 63

Eleven contribution, schedule, currency, tag, transfer-view, account-group and
release-note strings were accepted through the API. Investment-range and other
ambiguous feature labels remain pending contextual review.

## Reviewed suggestions batch 64

Six existing suggestions used an em dash even though their English source uses
a hyphen or ordinary sentence punctuation. Better Swedish alternatives were
submitted without an em dash, preserving every placeholder. Following explicit
authorization, the six less suitable alternatives received a negative vote.
The new alternatives remain pending project acceptance.

## Reviewed suggestions batch 65

The overspent-category plural pair was reviewed against the established term
`Kategorier över budget`. A precise plural-safe alternative was submitted with
both Swedish forms and the less natural adjective construction received a
negative vote. The parallel uncategorized-transaction pair was left unchanged:
its existing suggestion is idiomatic and technically valid.

## Reviewed suggestions batch 66

Thirteen import, planning, error, status and calculation strings were reviewed
and accepted through the API. Placeholders and markup are preserved. The import
progress label `Setting up...` remains pending because `Ställer in...` does not
fit that operation's context.

## Reviewed suggestions batch 67

Twenty formula, simulation, authentication and settings strings were reviewed
and accepted through the API. Formula decimal points and identifiers remain
unchanged, while Swedish UI typography is used in explanatory prose.

## Reviewed suggestions batch 68

Twenty-seven security and settings strings were reviewed and accepted through
the API. The user confirmed `Totalsträckskryptering` as the correct Swedish
security term. The prior negative vote was corrected to a positive vote, which
accepted the term; Weblate removed the competing `End-to-end-kryptering`
proposal automatically.

## Reviewed suggestions batch 69

Twenty-six forecast, transaction and account strings were reviewed and accepted
through the API. Four clearer alternatives were submitted for the remaining UI
labels: `Automatiskt`, `Måluppfyllelse`, a formal SimpleFIN maintenance message
and `Ta bort kontobegränsning`. They remain pending project acceptance.

## Reviewed suggestions batch 70

Twenty-three forecast, goal and scheduled-transaction strings were reviewed and
accepted through the API. The weekday selector label received the more natural
`Varje` alternative instead of the incomplete `En gång var`; it remains pending
project acceptance.

## Reviewed suggestions batch 71

Nine withdrawal strings were accepted through the API. Eleven earlier
browser-storage proposals received a positive review vote but were not accepted
by Weblate and remain pending. The standalone Monte Carlo table heading
received `Engångsuttag`, matching the established nearby noun; the fragment
`Engångs` was downvoted and the better term remains pending project acceptance.

## Reviewed suggestions batch 72

Eighteen previously archived tag-management proposals with existing positive
votes were reviewed again and received a positive review vote through the API.
Weblate returned `voted` for every proposal and all eighteen units remain
untranslated, so they are pending project acceptance rather than accepted.

## Reviewed suggestions batch 73

Seventeen account-group, investment and filtering strings were reviewed and
accepted through the API. Better Swedish alternatives were submitted for the
Discord community label and the two expand controls; they remain pending
project acceptance.

## Reviewed suggestions batch 74

Seventeen local-storage, account-group and data-folder strings were reviewed
and accepted through the API. The correctly inflected notifications plural pair
was submitted through the plural-safe vote path and is verified separately.

## Reviewed suggestions batch 75

Eighteen import, income and transaction strings were reviewed and accepted
through the API. Better label alternatives were submitted for an income-stream
name and minimum spending; they remain pending project acceptance.

## Reviewed suggestions batch 76

Eleven update, encoding, currency and settings strings were reviewed and
accepted through the API. The tag-count plural pair was handled through the
plural-safe path. `Automatisk identifiering` and `Taggurval` were submitted as
clearer alternatives for the remaining controls and await project acceptance.

## Reviewed suggestions batch 77

Three troubleshooting and experimental-feature messages were reviewed and
accepted through the API. The other-schedules plural pair was accepted through
the plural-safe path.

## Reviewed suggestions batch 78

Eight retirement-model labels were reviewed and accepted through the API. Four
clearer alternatives were submitted for the age label, two run-status labels
and the Spending tab, avoiding an em dash where the source has a hyphen. They
remain pending project acceptance.

## Reviewed suggestions batch 79

Twenty-one withdrawal, simulation and query-preset strings were reviewed and
accepted through the API. `Årliga utgifter` and the two date-range labels with
`under` were submitted as clearer alternatives and await project acceptance.

## Reviewed suggestions batch 80

Twenty-five contribution and financial-formula strings were reviewed and
accepted through the API. `Namn på insättning` was submitted as the clearer
table heading for the remaining contribution-name field and awaits acceptance.

## Reviewed suggestions batch 81

Six date-range, group and import strings were reviewed and accepted through
the API. The imported-transactions plural pair was accepted through the
plural-safe path.

## Reviewed suggestions batch 82

Seventeen transaction-status, budget-file, synchronization, table-layout and
investment-mix strings were reviewed and accepted through the API. Product and
format identifiers such as Pluggy.ai, ID and the lowercase `global` value are
preserved intentionally.

## Reviewed suggestions batch 83

Twenty-three simulation, fee and tax settings strings were reviewed and
accepted through the API. Better alternatives were submitted for the expand-all
control and the per-pot tax-model label. The ambiguous `First earnings` label
remains pending a separate contextual review.

## Reviewed suggestions batch 84

Fourteen investment, account and statistical-summary strings were reviewed and
accepted through the API. `Behåll pottarnas målfördelning` was submitted as a
more idiomatic target-mix control label and awaits project acceptance. A
transient Weblate 503 during this batch was retried only for the unconfirmed
units; all fourteen accepted targets were then read back successfully.

## Reviewed suggestions batch 85

Six Monte Carlo and onboarding labels were reviewed and accepted through the
API. Six clearer alternatives were submitted for the typical-failure status,
guided-tour controls and investment-pot guidance. The alternatives use
`rundtur` rather than the anglicized `tur`, preserve `{{appName}}`, and replace
an earlier em dash with a Swedish colon because the source has no em dash; they
await project acceptance.

## Reviewed suggestions batch 86

Nine account-introduction strings were reviewed and accepted through the API.
Four earlier server-setup, guided-onboarding, reconciliation and slogan
proposals received a positive review vote but remain pending project
acceptance. The review preserves the React markup, `URL`, Actual and the
QIF/OFX/QFX format identifiers, and uses the existing Swedish financial
terminology consistently.

## Reviewed suggestions batch 87

Nine Monte Carlo investment-allocation and capital-preservation labels were
reviewed and accepted through the API. The fee explanation retains the source
em dash, while the financial percentages and the Swedish space-before-percent
convention are preserved. `Ålder då potten blir tillgänglig` was submitted as a
clearer alternative to the fragmentary accessibility-age label and awaits
project acceptance.

## Reviewed suggestions batch 88

Nine Monte Carlo withdrawal-rule and simulation strings were reviewed and
accepted through the API. Two fee and tax descriptions received alternatives
that replace em dashes with Swedish full-stop and colon constructions because
their source strings use hyphens, not em dashes. Those alternatives await
project acceptance; the ambiguous `First earnings` label remains deferred.

## Reviewed suggestions batch 89

Three Monte Carlo withdrawal summaries were reviewed and accepted through the
API. Three alternatives for fixed costs, an unlucky run and a live balance were
submitted without em dashes because their source strings use hyphens, not em
dashes. The tax-bands explanation remains deferred for separate Swedish tax
terminology review.

## Reviewed suggestions batch 90

Two budget-introduction and Monte Carlo model explanations, plus a schedule
preview plural pair, were reviewed and accepted through the API. The tracking
budget summary received a positive review vote and remains pending. Alternatives
were submitted for the two onboarding descriptions to use the established
`uppföljningsbudgetering` terminology and for the guided-tour help text to use
`rundtur`; those alternatives await project acceptance.

## Reviewed suggestions batch 91

Five boundary and guardrail status explanations were context-reviewed. Clearer
alternatives were submitted with complete Swedish noun phrases for planned
amounts, `skyddsregler` instead of the literal `skyddsräcken`, and no em dash
where the source uses a hyphen. They await project acceptance.

## Reviewed suggestions batch 92

Three concise labels and progress text were reviewed and accepted through the
API. Three related guardrail explanations received matching `skyddsregler`
alternatives with complete planned-amount phrases and no em dashes where the
source uses hyphens; they await project acceptance. Ratcheting messages remain
deferred for terminology review.

## Reviewed suggestions batch 93

Four contribution, income and spending status strings received positive review
votes and remain pending project acceptance. Three alternatives were submitted
for surplus-cash explanations and status: they preserve `{{surplusPotName}}`,
`{{pot}}` and the previously omitted `{{amount}}` placeholder, and avoid em
dashes where the sources use hyphens. They also await project acceptance.

## Reviewed suggestions batch 94

Seventeen settings, navigation, retirement and browser-storage strings were
reviewed through the API. The batch preserves product names, placeholders and
the established `Fäll ut`, `Taggurval` and `Engångsuttag` controls. Acceptance
state was read back after the API votes: the withdrawal-order explanation was
accepted, while the other sixteen proposals remain pending project acceptance.

## Reviewed suggestions batch 95

Twenty-three browser-storage and tag-management labels were reviewed through
the API. The batch preserves `OPFS`, `{{color}}` and `{{name}}`, and uses the
existing `tagg` terminology consistently. All twenty-three received positive
review votes and remain pending project acceptance after readback.

## Reviewed suggestions batch 96

One retirement string was accepted through the API. Three browser-storage and
goal strings received positive review votes and remain pending. Four alternatives
were submitted for unspent income, an extra withdrawal and browser-recovery
messages. They retain all placeholders and markup, avoid em dashes where the
sources use hyphens, use `utgifter` for financial spending in explanatory prose,
and await project acceptance.

## Reviewed suggestions batch 97

Seven sidebar, currency, recovery, synchronization and browser-storage
instructions were reviewed through the API: six were accepted and the
browser-storage instruction remains pending. An alternative withdrawal-order
explanation replaces the opaque `åtkomstålder` compound with a complete Swedish
phrase and awaits project acceptance.

## Reviewed suggestions batch 98

Two Swedish plural pairs for weekly budgeting and rule counts were reviewed
through the plural-safe API path. A clearer alternative for the minimum-spending
floor status uses the established `minimiutgifter` term and awaits project
acceptance.

## Queue snapshot

After batch 98, Weblate reports 463 Swedish units that are still untranslated
and have at least one suggestion. They are queued for contextual review; this
count is a live snapshot, not a claim that all proposed translations are
correct or accepted.

## Reviewed suggestions batch 99

Ten history, interval, currency, formula, query and server-status labels were
reviewed through the API. The batch preserves `TRUE`, OpenID and query syntax,
and uses `Fråga` consistently for Actual's formula/query feature. Two targets
were accepted; the other eight received positive review votes and remain
pending project acceptance.

## Reviewed suggestions batch 100

Fifteen investment-projection, chart, budget-analysis and location-management
labels were reviewed through the API. The established financial terms
`insättning`, `avkastning`, `slutsaldo` and `överspendering` are used
consistently. All fifteen targets were accepted and read back successfully.

## Reviewed suggestions batch 101

Three formula-query descriptions were reviewed using the established `Fråga`
terminology. Seven units unexpectedly contained Dutch targets in the Swedish
component. Swedish replacements were submitted, but Weblate returned HTTP 403
when a review vote was attempted because the affected, already-approved units
are locked. The formula-query proposals received positive review votes but
remain pending project acceptance.

## Reviewed suggestions batch 102

Thirteen budget-automation labels and three plural pairs were reviewed through
the API. The review preserves markup, `{{amount}}`, `{{count}}` and the quoted
schedule name, and applies Swedish singular/plural forms for month references.
All thirteen singular targets and one plural pair were accepted; two plural
pairs are pending server-side validation.

## Reviewed suggestions batch 103

Eleven automation-template and target-setting labels were reviewed through the
API. The batch preserves `{{weight}}`, follows Swedish numeric percent spacing,
and uses consistent `automatisering`, `målbelopp` and category terminology. All
eleven targets were accepted and read back successfully.

## Reviewed suggestions batch 104

Five pool and early-spending controls were reviewed through the API. The
ambiguous `scopes` plural remains deferred for contextual terminology review.
All five targets were accepted and read back successfully.

## Reviewed suggestions batch 105

Four early-spending target controls were reviewed through the API, preserving
the numeric markup and month placeholders.

## Reviewed suggestions batch 106

Five early-spending and target controls were reviewed through the API.

## Reviewed suggestions batch 107

Seven balance-forecast, running-total and time-range labels were reviewed and
accepted through the API.

## Reviewed suggestions batches 108-111

Sixteen balance-cap, goal, tag-filter, chart and forecast labels were reviewed
through the API. The batches retain established terminology including
`slutsaldo`, `pott` and `taggar`; all sixteen targets were accepted and read
back successfully.

## Reviewed suggestions batch 112

Six tags and monthly-cap labels were reviewed through the API. The weekly-cap
explanation preserves all three template variables. Four short UI labels were
accepted and read back successfully; the two longer suggestions received
positive review votes and await project acceptance.

## Reviewed suggestions batch 113

Seven average-spending, automation and tracking-budget labels, plus one plural
pair, were reviewed through the API. The batch keeps template markup and
`{{rangeLabel}}` intact, uses `utgifter` for spending in the financial UI, and
uses the established `uppföljningsbudget` term. Three singular targets and the
plural pair were accepted and read back successfully; four detailed labels
received positive review votes and await project acceptance.

## Reviewed suggestions batch 114

Five formula-field descriptions and one plural budget-average label were
reviewed and accepted through the API. Formula functions, variable names,
comparisons and the `TRUE`/`FALSE` tokens were retained exactly; only
human-readable output strings and prose were translated.

## Reviewed suggestions batch 115

Six additional formula-field descriptions for categories, payment recipients
and transaction data were reviewed. Code-level identifiers, formula functions
and the `YYYY-MM-DD` format token are unchanged. Three translations were
accepted and read back with the required paragraph breaks; three revised
alternatives received positive review votes and await project acceptance.

## Reviewed suggestions batch 116

Twenty-two form-builder field labels were reviewed through the API. Formula
identifiers such as `QUERY_EXTRACT_CATEGORIES()` and
`QUERY_EXTRACT_TIMEFRAME_END()` remain unchanged. Twenty labels were accepted
and read back successfully; two labels have positive review votes pending
project acceptance.

## Reviewed suggestions batch 117

Nineteen formula-builder labels for numeric, logical and query operations were
reviewed through the API. `budgeted`, `spent`, `balance_start`, `balance_end`
and `goal` remain code values. Fourteen targets were accepted and read back;
five terminology improvements, including Actual's established `fråga`, have
positive review votes pending project acceptance.

## Reviewed suggestions batch 118

Nineteen formula, query and synchronisation labels were reviewed through the
API. Template markup, `QUERY`, `QUERY_COUNT`, `BUDGET_QUERY` and all formula
identifiers were retained. Twelve targets were accepted and read back; seven
contextual terminology and Swedish-punctuation improvements received positive
review votes pending project acceptance.

## Reviewed suggestions batch 119

Six budget-template status messages and two plural template labels were
reviewed and accepted through the API. The `$t(...)` calls, JSON argument
structure, `{{sourceCount}}` and `{{sinkCount}}` placeholders were preserved
and read back successfully.

## Reviewed suggestions batch 120

Ten archive-import validation and recovery messages were reviewed and accepted
through the API. Quoted `{{entryName}}`, `{{maxSizeMB}}`, URLs and references
to Actual were preserved and read back successfully.

## Reviewed suggestions batch 121

Eight server-onboarding and reconciliation labels were reviewed through the
API. Markup around the setup and guided-tour links was preserved. Four targets
were accepted and read back; four already well-contextualized targets received
positive review votes and await project acceptance.

## Reviewed suggestions batch 122

Ten remaining formula-builder fields and one plural template-status label were
reviewed and accepted through the API. The `TRUE`, `FALSE` and `#N/A` formula
tokens, as well as the plural `{{count}}` placeholder, were retained and read
back successfully.

## Reviewed suggestions batch 123

Five investment-plan tax, spending and inflation descriptions were reviewed.
All template markup and numeric placeholders are preserved. Two targets were
accepted and read back; three Swedish punctuation improvements received
positive review votes and await project acceptance. The improvements use full
stops because the corresponding source strings use hyphens, not em dashes.

## Reviewed suggestions batch 124

Three investment-allocation explanations were reviewed. Markup, percentages,
and the established `pott`, `fördelning`, `avkastning` and `volatilitet`
terminology are retained. All three Swedish punctuation and phrasing
improvements received positive review votes and await project acceptance.
