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
