import os
import streamlit as st
import psycopg2
from psycopg2.extras import RealDictCursor

def get_db_connection():
    return psycopg2.connect(
        os.getenv("DATABASE_URL", "postgresql://user:password@localhost:5432/evals_db"),
        cursor_factory=RealDictCursor
    )

def init_db():
    conn = get_db_connection()
    cur = conn.cursor()
    cur.execute("""
        CREATE TABLE IF NOT EXISTS human_labels (
            id SERIAL PRIMARY KEY,
            sample_id VARCHAR(64) NOT NULL,
            labeler_id VARCHAR(64) NOT NULL,
            criterion VARCHAR(64) NOT NULL,
            score INT NOT NULL,
            notes TEXT,
            created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
        );
    """)
    conn.commit()
    cur.close()
    conn.close()

def render_labeling_app():
    st.title("Project 4: Human-in-the-Loop Calibration Suite")
    st.markdown("Label evaluation outputs to build your gold standard baseline.")
    
    labeler_id = st.text_input("Labeler ID", value="engineer_alpha")
    sample_id = st.selectbox("Select Evaluation Sample ID", ["sample_001", "sample_002", "sample_003"])
    
    st.markdown("---")
    st.subheader("Sample Context")
    st.info("**Query:** How do I configure database connection pooling in Postgres?")
    st.text_area("Generated Output", "Use pgBouncer to handle high connection spikes...", height=150, disabled=True)
    
    st.subheader("Scoring Rubric")
    scores = {}
    for criterion in ["relevance", "factual_accuracy", "clarity"]:
        scores[criterion] = st.slider(f"{criterion.capitalize()} (1-3)", 1, 3, 2)
        
    notes = st.text_area("Disagreement / Edge Case Notes")
    
    if st.button("Commit Label"):
        conn = get_db_connection()
        cur = conn.cursor()
        for criterion, score in scores.items():
            cur.execute(
                "INSERT INTO human_labels (sample_id, labeler_id, criterion, score, notes) VALUES (%s, %s, %s, %s, %s)",
                (sample_id, labeler_id, criterion, score, notes)
            )
        conn.commit()
        cur.close()
        conn.close()
        st.success("Label committed successfully to PostgreSQL.")

if __name__ == "__main__":
    init_db()
    render_labeling_app()
