import biketrauma_brd

df = biketrauma_brd.Load_db().save_as_df()
df_nicely_formated = biketrauma_brd.format_date(df)
biketrauma_brd.plot_location(biketrauma_brd.get_accident(df))
