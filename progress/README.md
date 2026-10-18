# Progress site data

These two files feed the public progress site ("Building with Claude" dashboard):
https://claude.ai/artifact/EYMT3aQDYaopkYHMyDDzoK

- `weeks.json`: one row per week. The Friday review fills in that week's row: `status` ("done"), `gate_result` ("passed" / "partly" / "missed"), `quiz_pct`, `tutor_pass_pct`, `tutor_rating` (average for the week), `agent_hours`, `my_hours`, the five rubric scores (1–5), and `link` (the week's public review or post, if any). It then sets the next week's `status` to "current".
- `shipped.json`: one row per thing shipped: `date`, `week`, `kind` (Build, Essay, Post, Report, Workshop), `title` (unique), `metric` (its headline result), `url` (https only), `public` (true once anyone can see it).

Only public facts go here: the site can be shared, so no private notes, founder names without permission, or credentials.
