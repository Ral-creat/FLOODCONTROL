# --------------------
# 3) Data Analysis (Individual Datasets)
# --------------------
elif page == "Comparison & Analysis":
    st.header("3. Flood & Weather Pattern Analysis")

    # --- Weather Dataset Analysis ---
    if st.session_state.weather_df is not None:
        st.subheader("🌤️ Weather Pattern Analysis")
        w = get_df_safe('weather_df')
        wmain = st.session_state.weather_main

        st.write("**Weather Time Series**")
        st.pyplot(plot_series(w, wmain, title=f"Weather Trend: {wmain}", highlight_events=False))

        # Monthly Weather Pattern
        monthly_avg_weather = w.groupby('month')[wmain].mean()
        yearly_avg_weather = w.groupby('year')[wmain].mean()

        st.write("**Average Weather Value per Month**")
        st.pyplot(plot_bar_from_series(monthly_avg_weather, "Average Weather per Month", xlabel="Month", ylabel=f"Avg {wmain}"))

        st.write("**Average Weather Value per Year**")
        st.pyplot(plot_bar_from_series(yearly_avg_weather, "Average Weather per Year", xlabel="Year", ylabel=f"Avg {wmain}"))

        # Summary
        if not monthly_avg_weather.empty:
            top_month_w = monthly_avg_weather.idxmax()
            top_val_w = monthly_avg_weather.max()
            st.info(f"🌡️ Month with highest {wmain}: **{top_month_w}** ({top_val_w:.2f})")
        if not yearly_avg_weather.empty:
            top_year_w = yearly_avg_weather.idxmax()
            top_val_y = yearly_avg_weather.max()
            st.info(f"📆 Year with highest {wmain}: **{top_year_w}** ({top_val_y:.2f})")

    st.markdown("---")

    # --- Flood Dataset Analysis ---
    if st.session_state.flood_df is not None:
        st.subheader("🌊 Flood Pattern Analysis")
        f = get_df_safe('flood_df')
        fmain = st.session_state.flood_main

        st.write("**Flood Water Level Over Time**")
        st.pyplot(plot_series(f, fmain, title=f"Flood Water Level Trend ({fmain})", highlight_events=True))

        # Monthly Flood Pattern
        monthly_occurrence = f.groupby('month')['is_event'].sum()
        monthly_avg_level = f.groupby('month')[fmain].mean()

        st.write("**Monthly Flood Occurrences**")
        st.pyplot(plot_bar_from_series(monthly_occurrence, "Monthly Flood Occurrences", xlabel="Month", ylabel="No. of Flood Events"))

        st.write("**Average Water Level per Month**")
        st.pyplot(plot_bar_from_series(monthly_avg_level, "Average Water Level per Month", xlabel="Month", ylabel="Avg Water Level"))

        # Yearly Flood Pattern
        yearly_occurrence = f.groupby('year')['is_event'].sum()
        yearly_avg_level = f.groupby('year')[fmain].mean()

        st.write("**Yearly Flood Occurrences**")
        st.pyplot(plot_bar_from_series(yearly_occurrence, "Yearly Flood Occurrences", xlabel="Year", ylabel="No. of Flood Events"))

        st.write("**Average Water Level per Year**")
        st.pyplot(plot_bar_from_series(yearly_avg_level, "Average Water Level per Year", xlabel="Year", ylabel="Avg Water Level"))

        # Summary
        st.markdown("### 📊 Flood Insights")
        if not yearly_occurrence.empty:
            top_year = yearly_occurrence.idxmax()
            top_year_count = int(yearly_occurrence.max())
            st.info(f"📅 **Year with most floods:** {top_year} ({top_year_count} events)")
        if not monthly_occurrence.empty:
            top_month = monthly_occurrence.idxmax()
            top_month_count = int(monthly_occurrence.max())
            st.info(f"🗓️ **Month with most floods:** {top_month} ({top_month_count} events)")

        st.success("✅ Flood pattern analysis complete — view trends above.")
