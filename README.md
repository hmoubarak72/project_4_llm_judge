# Project 4: LLM-as-Judge with Human Calibration

Built an LLM-as-judge evaluation pipeline calibrated against human labels at high agreement; quantified position, length, and self-preference bias, gating production releases in CI.

## Architecture
- **Judge Model:** Claude API via DeepEval / G-Eval
- **Labeling Interface:** Streamlit
- **Persistence:** PostgreSQL
- **Validation Metrics:** Weighted Cohen's Kappa, Spearman Correlation

## Quick Start
1. Set up your `.env` file with `DATABASE_URL` and `ANTHROPIC_API_KEY`.
2. Run the labeling app: `streamlit run app.py`
3. Run tests in CI: `pytest test_evals.py`
