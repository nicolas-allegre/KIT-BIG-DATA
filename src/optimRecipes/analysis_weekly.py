"""optimRecipes/analysis_seasonality.py file.

Sub-module Streamlit for page seasonality_weekly.

"""
###############################################################################
# IMPORTS :
# /* Standard includes. */
# /* Extern modules */
import streamlit as st

# /* Intern modules */
from functions import WeeklyAnalysis


###############################################################################
# CLASS :
class weekly_analysis_module:
    """Class to wrap this module functions to interact with webapp.

    This class is used by webapp streamlit for the analysis of weekly user interactions.
    """

    def __init__(self, interactions_df, log_module, cfg):
        """Initialize the class with the data."""
        self.cfg = cfg
        self.interactions_df = interactions_df
        self.log_module = log_module

    def run(self):
        """Build analysis, and print result on a web streamlit page."""
        st.title("📅 Weekly User Interaction Insights")

        st.markdown("""
        ## 👀 Discover Weekly Patterns!

        Get insights into **user engagement** patterns across different days of the week.
        Whether you’re interested in seeing trends over several years or want to focus on a specific year,
        this section has got you covered! 📊

        ### Toggle Your View:
        - **Show Average Interactions**: See an overview of average interactions across all years.
        - **Select a Specific Year**: Dive into the interaction trends of a particular year.

        ---
        """)

        self.log_module.log_info("Starting weekly_analysis_module")
        # Initialize WeeklyAnalysis
        weekly_analysis = WeeklyAnalysis(self.interactions_df)

        # Add a toggle to view the average or a specific year
        view_avg = st.checkbox("📊 Show Average Interactions Across All Years")

        if view_avg:
            st.markdown("""
            ### 🌐 Average Weekly Activity
            Here’s a look at the **average number of interactions** on each day of the week, combining data from all years. This overview highlights **general trends** in user behavior.
            """)
            # Show average interactions across all years
            fig = weekly_analysis.plot_mean_interactions()
            st.pyplot(fig)
        else:
            # Dropdown to select the year
            years_available = sorted(self.interactions_df['year'].unique())
            selected_year = st.selectbox(
                "📅 Select a Year to Explore", options=years_available)

            st.markdown(f"""
            ### 📅 Weekly Activity for {selected_year}
            Explore the daily interaction patterns for **{selected_year}**. See how user activity changes across each day of the week for this particular year.
            """)
            # Automatically update the plot for the selected year
            fig = weekly_analysis.plot_interactions_for_year(selected_year)
            st.pyplot(fig)
