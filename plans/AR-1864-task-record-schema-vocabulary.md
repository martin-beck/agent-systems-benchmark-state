# AR-1864 plan: task-record schema vocabulary

1. Inspect the current task-record schema and its consumers to identify the exact execution,
   retry, and standard metadata vocabulary mismatch.
2. Update only the schema vocabulary and generated documentation, retaining strict unknown-field
   rejection and existing bounds.
3. Add positive and hostile schema fixtures/tests for every changed vocabulary path.
4. Run focused schema/generated-view validation, obtain independent review, and publish through a
   signed-DCO pull request.
