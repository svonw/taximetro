import streamlit as st
import datetime
import pandas as pd
import os
from trip import Trip
from trip_recorder import save_trips
from hours_calculator import create_calculator

st.set_page_config(page_title="F5 Taximeter", layout="wide")


if 'calculator' not in st.session_state:
    current_hour = datetime.datetime.now().hour
    st.session_state.calculator = create_calculator(current_hour)

st.title("🚕 Taxímetro")
tab1, tab2 = st.tabs(["Taxímetro", "Histórico de Viajes"])

with tab1:


    # Estado actual
    if Trip.trip_activate:
        status = f"🟢 **Viaje activo** - Estado: {Trip.state}"
    else:
        status = "⚪ Sin viaje activo"
    st.markdown(f"### {status}")
    st.divider()

    col1, col2, col3, col4 = st.columns(4)

    with col1:
        if st.button("🚦 START", type="primary", use_container_width=True):
            Trip.start("start")
            st.session_state.just_finished = False
            st.session_state.started = True
            st.rerun()

    with col2:
        # Botón dinámico según el estado
        if Trip.state == "stopped":
            button_label = "▶️ MOVE"
            command = "move"
        else:
            button_label = "⏸️ STOP"
            command = "stop"

        if st.button(button_label, use_container_width=True, disabled=not Trip.trip_activate):
            Trip.stop_move(command)
            st.rerun()

    with col3:
        if st.button("🏁 FINISH", use_container_width=True, disabled=not Trip.trip_activate):
            if Trip.finish("finish"):
                total_fare = st.session_state.calculator.calculate_fare(
                    Trip.stopped_time, Trip.moving_time
                )
                save_trips(Trip.stopped_time, Trip.moving_time, total_fare)
                st.session_state.just_finished = True
                st.rerun()

    with col4:
        if st.button("❌ EXIT", type="secondary", use_container_width=True, disabled=not st.session_state.get('started', False)):
            st.warning("TAXÍMETRO APAGADO")
            st.session_state.started = False
            st.stop()

    st.divider()

    # Mostrar tarifa

    if Trip.trip_activate:
        tarifa_base = st.session_state.calculator.START_RATE
        current_fare = st.session_state.calculator.calculate_fare(
            Trip.stopped_time, Trip.moving_time
        )
        st.markdown(f"###  Tarifa actual: **{current_fare:.2f} €** (Base: {tarifa_base} €)")

    elif st.session_state.get('just_finished', False):
        # Acabamos de finalizar
        df = pd.read_csv("trips_summary.csv")
        last_fare = df.iloc[-1]['Total Fare']
        st.success(f"### ✅ ¡Viaje finalizado! Total: **{last_fare:.2f} €**")
    else:
        st.info("Inicia un viaje para ver la tarifa")


 # Pestaña 2
with tab2:
    st.title("Histórico de Viajes")


    file_path = "trips_summary.csv"

    if os.path.exists(file_path):


            df = pd.read_csv(file_path)

            if not df.empty:
                df['Total Fare'] = df['Total Fare'].apply(lambda x: f"{x:.2f} €")
                st.dataframe(
                    df,
                    use_container_width=True,
                    hide_index=True
                )
            else:
                st.info("No hay viajes registrados aún")
    else:
        st.info("No hay viajes registrados aún")