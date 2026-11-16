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
