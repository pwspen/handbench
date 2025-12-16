How well can models see the number of fingers on a hand?

<table width="100%">
<colgroup>
    <col width="70%">
    <col width="30%">
</colgroup>
  <thead>
    <tr><th>Model</th><th>Accuracy</th></tr>
  </thead>
  <tbody>
    <tr><td>google/gemini-3-pro-preview</td><td>14/17</td></tr>
    <tr><td>qwen/qwen3-vl-235b-a22b-instruct</td><td>5/17</td></tr>
    <tr><td>anthropic/claude-opus-4.5</td><td>4/17</td></tr>
    <tr><td>openai/gpt-5.2</td><td>2/17</td></tr>
    <tr><td>x-ai/grok-4-fast</td><td>0/17</td></tr>
  </tbody>
</table>

I saved a few pictures of hands with numbers of fingers other than five to find out. Most images are real hands, some are AI, some are edited. No matter what, the human baseline for this is certainly 100%, but most models score less than 30%! Gemini is a notable outlier.

Now that we're in the benchmaxxing era, where all labs are RLing their models on all sorts of verifiable domains, silly little benchmarks like this will come in handy to test generalization, because they probe areas that there was almost certainly no direct model incentive to learn during training - i.e., models *probably* are not trained on large datasets of hands with different numbers of fingers, with the number of fingers labelled in text.

See the small dataset [here](./tables/answers.md), or the per-model answers in the respective files in [/tables](./tables/).