import streamlit as st
import pandas as pd

st.set_page_config(page_title="Motor de Tubos y Derivación", layout="centered")

# LOGO
c1, c2, c3 = st.columns([1, 2, 1])
with c2:
    st.image("logo.png", width=220)

st.markdown("## Motor de Tubos y Derivación")
st.caption("Define tubo y lugar de proceso según Hospital + Examen")
st.divider()

HOSPITALES = ["Villarrica", "Loncoche", "Temuco"]
EXAMENES = [
    "GLUCOSA SANGRE",
    "GAMAGLUTAMIL TRANSFERASA (GGT) SANGRE",
    "TROPONINA T SANGRE",
    "PROGESTERONA SANGRE",
    "HORMONA LUTEINIZANTE (LH) SANGRE",
]

RULES = {
    "Villarrica": {
        "GLUCOSA SANGRE": {"tubo": "tubo amarillo gel 1", "proceso": "PROCESA LOCAL"},
        "GAMAGLUTAMIL TRANSFERASA (GGT) SANGRE": {"tubo": "tubo amarillo gel 1", "proceso": "PROCESA LOCAL"},
        "TROPONINA T SANGRE": {"tubo": "tubo amarillo gel 1", "proceso": "PROCESA LOCAL"},
        "PROGESTERONA SANGRE": {"tubo": "tubo amarillo gel 2", "proceso": "DERIVA A TEMUCO"},
        "HORMONA LUTEINIZANTE (LH) SANGRE": {"tubo": "tubo amarillo gel 1", "proceso": "PROCESA LOCAL"},
    },
    "Loncoche": {
        "GLUCOSA SANGRE": {"tubo": "tubo amarillo gel 1", "proceso": "PROCESA LOCAL"},
        "GAMAGLUTAMIL TRANSFERASA (GGT) SANGRE": {"tubo": "tubo amarillo gel 1", "proceso": "PROCESA LOCAL"},
        "TROPONINA T SANGRE": {"tubo": "tubo amarillo gel 1", "proceso": "PROCESA LOCAL"},
        "PROGESTERONA SANGRE": {"tubo": "tubo amarillo gel 2", "proceso": "DERIVA A TEMUCO"},
        "HORMONA LUTEINIZANTE (LH) SANGRE": {"tubo": "tubo amarillo gel 3", "proceso": "DERIVA A VILLARRICA"},
    },
    "Temuco": {
        "GLUCOSA SANGRE": {"tubo": "tubo amarillo gel 1", "proceso": "PROCESA LOCAL"},
        "GAMAGLUTAMIL TRANSFERASA (GGT) SANGRE": {"tubo": "tubo amarillo gel 1", "proceso": "PROCESA LOCAL"},
        "TROPONINA T SANGRE": {"tubo": "tubo amarillo gel 1", "proceso": "PROCESA LOCAL"},
        "PROGESTERONA SANGRE": {"tubo": "tubo amarillo gel 1", "proceso": "PROCESA LOCAL"},
        "HORMONA LUTEINIZANTE (LH) SANGRE": {"tubo": "tubo amarillo gel 1", "proceso": "PROCESA LOCAL"},
    },
}


examenes_sel = st.multiselect("Selecciona examen(es)", EXAMENES)
hospital = st.selectbox("Selecciona hospital", HOSPITALES)
st.divider()

if not examenes_sel:
    st.info("Selecciona al menos un examen")
else:
    tubos = set()
    rows = []
    for ex in examenes_sel:
        info = RULES[hospital].get(ex, {"tubo": "NO DEFINIDO", "proceso": "NO DEFINIDO"})
        tubos.add(info["tubo"])
        rows.append({"Examen": ex, "Tubo": info["tubo"], "Lugar de proceso": info["proceso"]})

    st.markdown("### Tubos a tomar (únicos)")
    for t in sorted(tubos):
        st.write(f"- {t}")

    st.divider()
    st.markdown("### Detalle por examen")
    st.dataframe(pd.DataFrame(rows), use_container_width=True, hide_index=True)

st.divider()
st.caption("Elaborado por TM. Camilo Muñoz, Enero 2026")
