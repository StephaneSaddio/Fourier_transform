import FourierDrawing_brd

im_Image = FourierDrawing_brd.image().save_as_df()
df_nicely_formated = biketrauma_brd.format_date(df)
biketrauma_brd.plot_location(biketrauma_brd.get_accident(df))
