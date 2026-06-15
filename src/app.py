import streamlit as st
from openai import OpenAI
from dotenv import load_dotenv
import os

# API credentials are loaded from a local .env file.
# The real .env file must not be committed to GitHub.
load_dotenv()
client = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))
VECTOR_STORE_ID = os.getenv("VECTOR_STORE_ID")

SYSTEM_PROMPT = """Du bist ein M&A Due-Diligence-Assistent.
Beantworte Fragen ausschliesslich auf Basis der hochgeladenen VDR-Dokumente.
Nenne immer die Quelldatei bei jedem Datenpunkt.
Wenn eine Information nicht vorhanden ist, sage: Nicht im VDR vorhanden.
Antworte auf Deutsch, praezise und strukturiert."""

DD_FRAGEN = [
    "Was ist die Customer Concentration (Top 10 Kunden)?",
    "Wie hat sich der Umsatz in den letzten 3 Jahren entwickelt?",
    "Gibt es Change-of-Control-Klauseln in den Kundenvertraegen?",
    "Wie hoch ist die EBITDA-Marge?",
    "Welche offenen Rechtsstreitigkeiten gibt es?",
    "Wie viele Mitarbeiter hat das Unternehmen?",
    "Gibt es eine Finanzplanung fuer die naechsten Jahre?",
    "Welche wesentlichen Lieferantenvertraege existieren?",
]

st.set_page_config(page_title="VDR Assistent", layout="wide")
st.title("VDR Due Diligence Assistent")
st.caption("Fragen Sie den Datenraum - Antworten mit Quellenangabe")

if "messages" not in st.session_state:
    st.session_state.messages = []
if "quellen" not in st.session_state:
    st.session_state.quellen = []
if "auto_frage" not in st.session_state:
    st.session_state.auto_frage = None

col_chat, col_side = st.columns([2, 1])

with col_side:
    st.subheader("Standard-Fragen")
    for frage in DD_FRAGEN:
        if st.button(frage[:45] + "...", key=frage):
            st.session_state.auto_frage = frage

    st.divider()
    st.subheader("Quellen")
    if st.session_state.quellen:
        for q in st.session_state.quellen:
            st.info("📄 " + q)
    else:
        st.caption("Quellen erscheinen hier nach der ersten Anfrage.")

with col_chat:
    for msg in st.session_state.messages:
        with st.chat_message(msg["role"]):
            st.write(msg["content"])

    eingabe = st.chat_input("Frage an den VDR stellen...")

    aktive_frage = st.session_state.auto_frage or eingabe
    if st.session_state.auto_frage:
        st.session_state.auto_frage = None

    if aktive_frage:
        st.session_state.messages.append(
            {"role": "user", "content": aktive_frage}
        )
        with col_chat:
            with st.chat_message("user"):
                st.write(aktive_frage)

            with st.chat_message("assistant"):
                with st.spinner("Durchsuche VDR-Dokumente..."):
                    try:
                        response = client.responses.create(
                            model="gpt-4o",
                            input=aktive_frage,
                            tools=[{
                                "type": "file_search",
                                "vector_store_ids": [VECTOR_STORE_ID]
                            }],
                            instructions=SYSTEM_PROMPT
                        )

                        antwort = ""
                        quellen = []

                        for block in response.output:
                            if block.type == "message":
                                for content in block.content:
                                    if content.type == "output_text":
                                        antwort = content.text
                                        seen = set()
                                        for ann in content.annotations:
                                            ann_type = getattr(ann, "type", "")
                                            if ann_type == "file_citation":
                                                fn = getattr(ann, "filename", "")
                                                if not fn:
                                                    fn = getattr(ann, "file_id", "Unbekannte Datei")
                                                if fn not in seen:
                                                    seen.add(fn)
                                                    quellen.append(fn)

                        if not antwort:
                            antwort = "Keine Antwort erhalten. Bitte erneut versuchen."

                        st.write(antwort)
                        st.session_state.messages.append(
                            {"role": "assistant", "content": antwort}
                        )
                        st.session_state.quellen = quellen

                    except Exception as e:
                        st.error("Fehler: " + str(e))
