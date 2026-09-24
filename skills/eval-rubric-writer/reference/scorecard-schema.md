# Scorecard and cases schema reference

This is the field-by-field schema the output of this skill must match, so
it drops directly into the agent-evals runner
(https://github.com/25andresbernal/agent-evals) with no editing required.

## Contents

- scorecard.yaml fields
- cases.yaml fields
- Built-in scorers and their config
- Validation rules to self-check before handing off output

## scorecard.yaml fields

| Field | Type | Required | Notes |
|---|---|---|---|
| `name` | string | yes | Human-readable name of the scorecard. |
| `pass_threshold` | float, 0 to 1 | yes | Weighted average across dimensions required for the suite to pass overall. |
| `dimensions` | list | yes | At least one dimension. |
| `dimensions[].name` | string | yes | A short, specific name. Not "quality" alone if there could be more than one quality-like dimension. |
| `dimensions[].scorer` | string | yes | One of `task_success`, `tool_correctness`, `cost`, `latency`, `llm_judge`, or a custom `module:function` path. |
| `dimensions[].weight` | float, 0 to 1 | yes | All dimension weights must sum to 1.0. |
| `dimensions[].threshold` | float, 0 to 1 | yes | Checked independently of the weighted average. A dimension scoring below its own threshold flags that dimension even if the overall weighted average passes. |
| `dimensions[].config` | object | scorer-dependent | See scorer table below. |

## cases.yaml fields

Each case is one entry in a top-level YAML list.

| Field | Type | Required | Notes |
|---|---|---|---|
| `id` | string | yes | Unique, kebab-case, describes the scenario, not a number. |
| `input` | string | yes | The message or request sent to the agent under test. |
| `tags` | list of strings | no | Free-form. Use consistent tags across a suite (`tier1`, `edge-case`, `regression`) so cases can be filtered. |
| `notes` | string | no | Why the case exists. Required in practice for any case seeded from a real failure report; state which report or incident. |
| `expected_output_contains` | list of strings | no | Every string must appear in the agent's output (used by `task_success` in `contains` mode). |
| `expected_output_exact` | string | no | The output must match exactly (used by `task_success` in `exact` mode). Use instead of, not alongside, `expected_output_contains`. |
| `expected_tool_calls` | list of objects | no | Each object has `name` and `args`. An empty list (`[]`) means the case expects no tool call at all, which is different from omitting the field. |
| `expected_tool_calls[].args` | object | no | Argument name to expected value. Use `null` for an argument whose value should not be checked (any value is acceptable), not for "this argument should be absent." |

## Built-in scorers and their config

- **`task_success`**: `config.mode` is `exact`, `contains`, or `custom`.
  `contains` checks every string in `expected_output_contains` appears in
  the output. `exact` checks `expected_output_exact` matches exactly.
- **`tool_correctness`**: checks the agent called the tools in
  `expected_tool_calls` with matching arguments. `config.strict: true`
  requires an exact argument match with no extra keys; the default,
  `false`, checks only the keys listed in the case.
- **`cost`**: `config.max_cost_usd` sets the budget; score decays linearly
  past it.
- **`latency`**: `config.max_latency_ms` sets the budget; score decays
  linearly past it.
- **`llm_judge`**: `config.rubric` is free text given to the judge model.
  Write it as instructions to the judge, stating what a 1.0 response and
  a 0.0 response each look like, and any specific behavior the agent must
  not exhibit (overpromising, wrong tone, fabricated details).

## Validation rules to self-check before handing off output

- [ ] Dimension weights sum to 1.0 (within floating-point rounding).
- [ ] Every dimension has both a `weight` and a `threshold`; a weight
      alone lets a strong dimension mask a specifically weak one.
- [ ] No `threshold` is set to exactly 1.0 unless the team truly wants zero
      tolerance; 1.0 thresholds fail on the first near-miss and tend to get
      disabled rather than fixed.
- [ ] Every case has at least one of `expected_output_contains`,
      `expected_output_exact`, or a non-empty `expected_tool_calls`. A case
      that asserts nothing does not test anything.
- [ ] `expected_tool_calls: []` is used deliberately, for cases that must
      not call a tool, not left as an accidental empty default.
- [ ] Every regression case (seeded from a real failure) has a `notes`
      field naming the source, so a future reader knows why the case
      exists.
