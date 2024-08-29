# import streamlit as st
# import pandas as pd
# import plotly.express as px
# from streamlit_plotly_events import plotly_events
# import plotly.graph_objects as go
# import numpy as np
# from scipy import stats
# df = pd.read_csv('main_df_subset.csv')
# df = df[(df['skill_name'] != 'Other')]

# state_mapping = {
#     'NJ': 'New Jersey', 'IL': 'Illinois', 'NY': 'New York', 'CA': 'California', 'PA': 'Pennsylvania', 
#     'WI': 'Wisconsin', 'WA': 'Washington', 'NC': 'North Carolina', 'OH': 'Ohio', 'GA': 'Georgia', 
#     'KY': 'Kentucky', 'FL': 'Florida', 'MD': 'Maryland', 'TX': 'Texas', 'VA': 'Virginia', 
#     'MI': 'Michigan', 'SD': 'South Dakota', 'IN': 'Indiana', 'NE': 'Nebraska', 'MO': 'Missouri', 
#     'MA': 'Massachusetts', 'TN': 'Tennessee', 'LA': 'Louisiana', 'DC': 'District of Columbia', 
#     'AR': 'Arkansas', 'OK': 'Oklahoma', 'UT': 'Utah', 'MN': 'Minnesota', 'AZ': 'Arizona', 'CT': 'Connecticut', 
#     'RI': 'Rhode Island', 'ME': 'Maine', 'NH': 'New Hampshire', 'CO': 'Colorado', 'AL': 'Alabama', 
#     'KS': 'Kansas', 'ID': 'Idaho', 'HI': 'Hawaii', 'OR': 'Oregon', 'NV': 'Nevada', 'NM': 'New Mexico', 
#     'VT': 'Vermont', 'IA': 'Iowa', 'SC': 'South Carolina', 'DE': 'Delaware', 'ND': 'North Dakota', 
#     'MS': 'Mississippi', 'WY': 'Wyoming', 'MT': 'Montana', 'AK': 'Alaska'
# }

# # Reverse mapping for filtering purposes
# reverse_state_mapping = {v: k for k, v in state_mapping.items()}

# df_filtered_state = df.copy()
# df_filtered_state['state'] = df_filtered_state['state'].replace(state_mapping)
# df_filtered_state = df_filtered_state[df_filtered_state['state'].isin(state_mapping.values())]

# # Filter necessary columns and exclude 'Not Specified' from 'formatted_experience_level'
# df_filtered_state = df_filtered_state[
#     (df_filtered_state['formatted_experience_level'] != 'Not Specified') &
#     (df_filtered_state['skill_name'] != 'other')
# ][['state', 'skill_name', 'formatted_experience_level']]



# ########################Side Bar#################################

# with st.sidebar:
#     st.sidebar.title("Filters")
#     unique_skill_names = df['skill_name'].dropna().unique()
#     selected_skill_name = st.sidebar.selectbox('Select Skill:', unique_skill_names)
#     unique_states = df_filtered_state['state'].unique()
#     selected_state = st.sidebar.selectbox("Select a State", unique_states)

# filtered_df_skill_state = df[df['skill_name'] == selected_skill_name]
# filtered_df_skill_state = filtered_df_skill_state[filtered_df_skill_state['state'] == selected_state]

# min_salary = filtered_df_skill_state['min_salary'].min()
# avg_salary = filtered_df_skill_state['min_salary'].mean()
# max_salary = filtered_df_skill_state['min_salary'].max()

# st.sidebar.subheader('Salary Statistics')
# st.sidebar.write(f"Minimum Salary: ${min_salary:,.2f}")
# st.sidebar.write(f"Average Salary: ${avg_salary:,.2f}")
# st.sidebar.write(f"Maximum Salary: ${max_salary:,.2f}")
# num_job_postings = filtered_df_skill_state['job_id'].count()
# st.sidebar.subheader('Number of Job Postings')
# st.sidebar.write(f"Total Job Postings: {num_job_postings}")



# ########################MAP PLOT#################################
# filtered_df = df[df['skill_name'] == selected_skill_name]

# state_job_counts = filtered_df.groupby('state')['job_id'].count().reset_index()
# state_job_counts.columns = ['state', 'job_count']


# min_job_count = state_job_counts['job_count'].min()
# max_job_count = state_job_counts['job_count'].max()
# num_bins = 3
# if max_job_count == min_job_count:
#     max_job_count += 1
# color_ranges = pd.cut(state_job_counts['job_count'], bins=num_bins, retbins=True)[1]
# def format_label(value):
#     if value >= 1000:
#         return f'{int(round(value/1000))}K'
#     else:
#         return f'{int(value)}'
    
# labels = [f'{(format_label(color_ranges[i]))} - {(format_label(color_ranges[i+1]))}' for i in range(len(color_ranges) - 1)]
# state_job_counts['color_label'] = pd.cut(state_job_counts['job_count'],
#                                         bins=color_ranges,
#                                         labels=labels,
#                                         include_lowest=True)
# colors = [
#     '#C6CFFF',  
#     '#A6E3E9',  
#     '#DEECFF',  
# ]
# color_map = {label: colors[i] for i, label in enumerate(labels)}

# state_job_counts['color'] = state_job_counts['color_label'].map(color_map)

# ticktext = labels
# tickvals = list(range(len(labels)))

# fig = px.choropleth(
#     state_job_counts,
#     locations='state',
#     locationmode='USA-states',
#     color='color_label', 
#     scope='usa',
#     color_discrete_map=color_map,  
#     title='Job Postings by State',
#     labels={'job_count': 'Job Count', 'color_label': 'Job Count Range'},  
#     category_orders={"color_label": labels}  
# )
# fig.update_geos(projection_type="albers usa")
# fig.update_traces(
#     hovertemplate='<b>%{location}</b><br>Job Count=%{customdata[0]}<extra></extra>',
#     customdata=state_job_counts[['job_count', 'state']]
# )

# fig.update_layout(coloraxis_colorbar=dict(
#     title="Open Jobs",
#     tickvals=tickvals,
#     ticktext=ticktext,
#     lenmode="pixels", len=300, yanchor="top", y=1,
#     ticks="outside"
# ))

# st.plotly_chart(fig)

# ########################BOX PLOT #######################33
# # def filter_and_plot3(df, selected_skill_name):
# #     df_filtered_state_boxPlot = df[['min_salary', 'max_salary', 'company_size', 'skill_name']]
# #     df_filtered_state_boxPlot = df_filtered_state_boxPlot[df_filtered_state_boxPlot['company_size'] != 'Not Specified']
    
# #     df_filtered_state_boxPlot = df_filtered_state_boxPlot[df_filtered_state_boxPlot['skill_name'].str.contains(selected_skill_name, case=False, na=False)]
    
# #     df_filtered_state_boxPlot['salary'] = df_filtered_state_boxPlot.apply(lambda row: [row['min_salary'], row['max_salary']], axis=1)
# #     df_expanded = df_filtered_state_boxPlot.explode('salary')
    
# #     fig = px.box(df_expanded, x='company_size', y='salary', color='company_size', title=f'Salary Range by Company Size for {selected_skill_name}',
# #                 labels={'company_size': 'Company Size', 'salary': 'Salary'})
    
# #     fig.update_layout(xaxis={'categoryorder':'total ascending'},
# #                     xaxis_title='Company Size',
# #                     yaxis_title='Salary',
# #                     xaxis_tickangle=-45,
# #                     yaxis_range=[0, 600000],
# #                     showlegend=False)  
    
# #     st.plotly_chart(fig)

# # if selected_skill_name:
# #     filter_and_plot3(df, selected_skill_name)
# df['salary'] = df.apply(lambda row: [row['min_salary'], row['max_salary']], axis=1)
# df_expanded = df.explode('salary')
# df_expanded['salary'] = pd.to_numeric(df_expanded['salary'], errors='coerce')
# df_expanded = df_expanded.dropna(subset=['salary'])

# # Convert 'applies' to categorical with 10 unique values
# # Handle non-numeric data and missing values appropriately
# df_expanded['applies'] = pd.to_numeric(df_expanded['applies'], errors='coerce')
# df_expanded = df_expanded.dropna(subset=['applies'])  # Drop rows with NaN applies values

# # Use pd.qcut with 'drop' duplicates option
# df_expanded['applies_category'] = pd.qcut(df_expanded['applies'], q=10, labels=False, duplicates='drop')

# # Sidebar selection for skills
# with st.sidebar:
#     st.sidebar.title("Skills")
#     unique_skill_names = df['skill_name'].dropna().unique()
#     selected_skill_name = st.sidebar.selectbox('Select Skill:', unique_skill_names)

# def filter_and_plot3(df, selected_skill_name):
#     df_filtered = df_expanded[df_expanded['company_size'] != 'Not Specified']
#     df_filtered = df_filtered[df_filtered['skill_name'].str.contains(selected_skill_name, case=False, na=False)]
    
#     # Remove outliers using Z-score
#     df_filtered = df_filtered[(np.abs(stats.zscore(df_filtered['salary'])) < 3)]
    
#     # Create box plot with added feature of applies distribution
#     fig = px.box(df_filtered, x='company_size', y='salary', color='applies_category', title=f'Salary Range by Company Size for {selected_skill_name}',
#                  labels={'company_size': 'Company Size', 'salary': 'Salary', 'applies_category': 'Applies Category'})
    
#     fig.update_layout(xaxis=dict(rangeslider=dict(visible=True), type="linear") ,
#                       xaxis_title='Company Size',
#                       yaxis_title='Salary',
#                       xaxis_tickangle=0,  # Straighten the x-axis labels
#                       yaxis_range=[0, 600000],
#                       showlegend=True)
    
#     # Add violin plot layer for Applies distribution
#     fig2 = px.violin(df_filtered, x='company_size', y='salary', color='applies_category', box=True, points="all")
#     for trace in fig2.data:
#         fig.add_trace(trace)
    
#     st.plotly_chart(fig)

# if selected_skill_name:
#     filter_and_plot3(df, selected_skill_name)
# ########################SNAKEY PLOT#######################33

# st.title("Sankey Plot for Job Data")
# state_filtered = df_filtered_state[df_filtered_state['state'] == selected_state]
# top_skills = state_filtered['skill_name'].value_counts()
# top_skills = top_skills[top_skills.index != 'other'].head(5).index.tolist()
# state_filtered = state_filtered[state_filtered['skill_name'].isin(top_skills)]
# all_labels = list(set(state_filtered['skill_name']).union(set(state_filtered['formatted_experience_level'])))
# label_to_index = {label: i for i, label in enumerate(all_labels)}
# source = []
# target = []
# value = []
# skills_to_exp = state_filtered.groupby(['skill_name', 'formatted_experience_level']).size().reset_index(name='count')
# for _, row in skills_to_exp.iterrows():
#     source.append(label_to_index[row['skill_name']])
#     target.append(label_to_index[row['formatted_experience_level']])
#     value.append(row['count'])
# skill_colors = ['#E8D3FF', '#C6CFFF', '#A6E3E9', '#DEECFF', '#F3F8FF']
# skill_color_map = {skill: skill_colors[i] for i, skill in enumerate(top_skills)}
# node_colors = []
# for label in all_labels:
#     if label in skill_color_map:
#         node_colors.append(skill_color_map[label])
#     else:
#         node_colors.append("rgba(0, 0, 0, 0.1)")  # Light grey for other nodes
# link_colors = []
# for _, row in skills_to_exp.iterrows():
#     link_colors.append(skill_color_map[row['skill_name']])
# fig = go.Figure(data=[go.Sankey(
#     node=dict(
#         pad=15,
#         thickness=20,
#         line=dict(color="black", width=0.5),
#         label=all_labels,
#         color=node_colors
#     ),
#     link=dict(
#         source=source,
#         target=target,
#         value=value,
#         color=link_colors
#     )
# )])

# fig.update_layout(title_text=f"Sankey Diagram of Job Data for {selected_state}", font_size=10)

# st.plotly_chart(fig)



# ######################## FACET #######################
# # # Filter dataframe by selected state and exclude 'Other'
# # filtered_df_facet = df[(df['state'] == selected_state)]

# # # Determine top 6 skills for the selected state
# # top_skills = filtered_df_facet['skill_name'].value_counts().nlargest(6).index

# # # Assign 'Other' to the skills that are not in top_skills
# # filtered_df_facet['top_skill'] = filtered_df_facet['skill_name'].where(filtered_df_facet['skill_name'].isin(top_skills), 'Other')

# # # Group data by company name, top skill, and calculate mean employee count
# # company_skill_emp = filtered_df_facet.groupby(['company_name', 'top_skill'])['employee_count'].mean().reset_index()

# # # Sort the dataframe by employee_count in descending order within each top_skill
# # company_skill_emp = company_skill_emp.sort_values(by=['top_skill', 'employee_count'], ascending=[True, False])

# # # Create a new dataframe to store only the top 5 companies for each top_skill
# # top_5_companies = pd.DataFrame()
# # category_orders = {}
# # for skill in top_skills:
# #     top_5 = company_skill_emp[company_skill_emp['top_skill'] == skill].nlargest(5, 'employee_count')
# #     top_5_companies = pd.concat([top_5_companies, top_5])
# #     category_orders[skill] = top_5['company_name'].tolist()

# # # Ensure company names are correctly ordered within each facet
# # category_orders_flat = [company for sublist in category_orders.values() for company in sublist]

# # # Create the facet graph
# # fig_facet = px.bar(top_5_companies, 
# #                    x='company_name', 
# #                    y='employee_count', 
# #                    color='top_skill', 
# #                    facet_col='top_skill',
# #                    facet_col_wrap=3,  # Adjust this value to change the number of columns in the facet grid
# #                    title=f'Top 5 Companies by Employee Count for Top Skills in {selected_state}',
# #                    category_orders={'company_name': category_orders_flat, 'top_skill': list(top_skills)})

# # fig_facet.update_xaxes(tickangle=45, title_text='')
# # fig_facet.update_yaxes(matches=None)  # Allow individual y-axes for each facet
# # fig_facet.update_yaxes(title_text='Employee Count', col=1)  # Set 'Employee Count' label only for the leftmost graph in each row
# # fig_facet.update_layout(height=1000, width=1000, showlegend=True)  # Adjust the height and width as needed
# # fig_facet.for_each_annotation(lambda a: a.update(text=a.text.split("=")[-1]))  # Simplify facet titles

# # # Display the facet graph
# # st.plotly_chart(fig_facet)

# # # Display the key for the top companies
# # st.sidebar.subheader(f'Top 5 Companies in {selected_state} for each Top Skill')
# # for skill in top_skills:
# #     st.sidebar.subheader(f'Top Companies for {skill}')
# #     top_companies = top_5_companies[top_5_companies['top_skill'] == skill]['company_name'].unique()
# #     for company in top_companies:
# #         st.sidebar.write(company)


# # ######################## voilent  #######################
# # # Filter dataframe by selected state
# # # Filter dataframe by selected state
# # filtered_df_state = df[df['state'] == selected_state]

# # # Determine top 6 skills for the selected state
# # top_skills = filtered_df_state['skill_name'].value_counts().nlargest(6).index

# # # Assign 'Other' to the skills that are not in top_skills
# # filtered_df_state['top_skill'] = filtered_df_state['skill_name'].where(filtered_df_state['skill_name'].isin(top_skills), 'Other')

# # # Group data by company name, top skill, and calculate mean employee count
# # company_skill_emp = filtered_df_state.groupby(['company_name', 'top_skill'])['employee_count'].mean().reset_index()

# # # Sort the dataframe by employee_count in descending order within each top_skill
# # company_skill_emp = company_skill_emp.sort_values(by=['top_skill', 'employee_count'], ascending=[True, False])

# # # Create a new dataframe to store only the top 5 companies for each top_skill
# # top_5_companies = pd.DataFrame()
# # category_orders = {}
# # for skill in top_skills:
# #     top_5 = company_skill_emp[company_skill_emp['top_skill'] == skill].nlargest(5, 'employee_count')
# #     top_5_companies = pd.concat([top_5_companies, top_5])
# #     category_orders[skill] = top_5['company_name'].tolist()

# # # Dropdown to select a skill
# # selected_skill = st.selectbox("Select Skill", top_skills)

# # # Filter the data for the selected skill
# # selected_skill_data = top_5_companies[top_5_companies['top_skill'] == selected_skill]

# # # Create the bar plot for the selected skill
# # fig = px.bar(selected_skill_data, 
# #              x='company_name', 
# #              y='employee_count', 
# #              color='company_name', 
# #              title=f'Top 5 Companies by Employee Count for {selected_skill} in {selected_state}',
# #              category_orders={'company_name': category_orders[selected_skill]})

# # fig.update_xaxes(tickangle=45, title_text='Company Name')
# # fig.update_yaxes(title_text='Employee Count')

# # # Hide the legend
# # fig.update_layout(showlegend=False)

# # # Display the bar plot
# # st.plotly_chart(fig)

# # # Display the key for the top companies in the sidebar
# # st.sidebar.subheader(f'Top 5 Companies in {selected_state} for {selected_skill}')
# # top_companies = selected_skill_data['company_name'].unique()
# # for company in top_companies:
# #     st.sidebar.write(company)
# ######################## FACET #######################
# # # Filter dataframe by selected state
# # filtered_df_state = df[df['state'] == selected_state]

# # # Determine top 6 skills for the selected state
# # top_skills = filtered_df_state['skill_name'].value_counts().nlargest(6).index

# # # Assign 'Other' to the skills that are not in top_skills
# # filtered_df_state['top_skill'] = filtered_df_state['skill_name'].where(filtered_df_state['skill_name'].isin(top_skills), 'Other')

# # # Group data by company name, top skill, and calculate mean applies and views
# # company_skill_emp = filtered_df_state.groupby(['company_name', 'top_skill']).agg(
# #     avg_applies=('applies', 'mean'),
# #     avg_views=('views', 'mean')
# # ).reset_index()

# # # Sort the dataframe by avg_applies in descending order within each top_skill
# # company_skill_emp = company_skill_emp.sort_values(by=['top_skill', 'avg_applies'], ascending=[True, False])

# # # Create a new dataframe to store only the top 5 companies for each top_skill
# # top_5_companies = pd.DataFrame()
# # category_orders = {}
# # for skill in top_skills:
# #     top_5 = company_skill_emp[company_skill_emp['top_skill'] == skill].nlargest(5, 'avg_applies')
# #     top_5_companies = pd.concat([top_5_companies, top_5])
# #     category_orders[skill] = top_5['company_name'].tolist()

# # # Melt the dataframe to have 'avg_applies' and 'avg_views' as values in a single column
# # top_5_companies_melted = top_5_companies.melt(id_vars=['company_name', 'top_skill'], 
# #                                               value_vars=['avg_applies', 'avg_views'],
# #                                               var_name='metric',
# #                                               value_name='avg_value')

# # # Dropdown to select a skill
# # selected_skill = st.selectbox("Select Skill", top_skills)

# # # Filter the data for the selected skill
# # selected_skill_data = top_5_companies_melted[top_5_companies_melted['top_skill'] == selected_skill]

# # # Create the bar plot for the selected skill
# # fig = px.bar(selected_skill_data, 
# #              x='company_name', 
# #              y='avg_value', 
# #              color='metric', 
# #              barmode='group',
# #              title=f'Average Applies and Views by Company for {selected_skill} in {selected_state}',
# #              category_orders={'company_name': category_orders[selected_skill]})

# # fig.update_xaxes(tickangle=45, title_text='Company Name')
# # fig.update_yaxes(title_text='Average')

# # # Hide the legend
# # fig.update_layout(showlegend=True)

# # # Display the bar plot
# # st.plotly_chart(fig)

# # # Display the key for the top companies in the sidebar
# # st.sidebar.subheader(f'Top 5 Companies in {selected_state} for {selected_skill}')
# # top_companies = selected_skill_data['company_name'].unique()
# # for company in top_companies:
# #     st.sidebar.write(company)
# # filtered_df_skill = df[df['skill_name'] == selected_skill_name]
# # filtered_df = filtered_df_skill[filtered_df_skill['state'] == selected_state]

# # # Exclude 'Not specific' in formatted_experience_level
# # filtered_df = filtered_df[filtered_df['formatted_experience_level'] != 'Not Specified']

# # # Determine unique values of formatted_experience_level for the selected skill and state
# # unique_experience_levels = filtered_df['formatted_experience_level'].dropna().unique()

# # # Group data by company name, formatted_experience_level, and calculate the sum of applies and views
# # company_exp_level_emp = filtered_df.groupby(['company_name', 'formatted_experience_level']).agg(
# #     count_applies=('applies', 'sum'),
# #     count_views=('views', 'sum')
# # ).reset_index()

# # # Sort the dataframe by count_views in descending order within each experience level
# # company_exp_level_emp = company_exp_level_emp.sort_values(by=['formatted_experience_level', 'count_views'], ascending=[True, False])

# # # Create a new dataframe to store only the top 5 companies for each experience level
# # top_5_companies = pd.DataFrame()
# # category_orders = {}
# # for level in unique_experience_levels:
# #     top_5 = company_exp_level_emp[company_exp_level_emp['formatted_experience_level'] == level].nlargest(5, 'count_views')
# #     top_5_companies = pd.concat([top_5_companies, top_5])
# #     category_orders[level] = top_5['company_name'].tolist()

# # # Melt the dataframe to have 'count_applies' and 'count_views' as values in a single column
# # top_5_companies_melted = top_5_companies.melt(id_vars=['company_name', 'formatted_experience_level'], 
# #                                               value_vars=['count_applies', 'count_views'],
# #                                               var_name='metric',
# #                                               value_name='count_value')

# # # Dropdown to select an experience level
# # selected_experience_level = st.selectbox("Select Experience Level", unique_experience_levels)

# # # Filter the data for the selected experience level
# # selected_experience_level_data = top_5_companies_melted[top_5_companies_melted['formatted_experience_level'] == selected_experience_level]

# # # Create the bar plot for the selected experience level
# # fig = px.bar(selected_experience_level_data, 
# #              x='company_name', 
# #              y='count_value', 
# #              color='metric', 
# #              barmode='group',
# #              title=f'Count of Applies and Views by Company for {selected_experience_level} Experience Level in {selected_state} for {selected_skill_name}',
# #              category_orders={'company_name': category_orders[selected_experience_level]})

# # fig.update_xaxes(tickangle=45, title_text='Company Name')
# # fig.update_yaxes(title_text='Count')

# # # Display the bar plot
# # st.plotly_chart(fig)

# # # Display the key for the top companies in the sidebar
# # st.sidebar.subheader(f'Top 5 Companies in {selected_state} for {selected_experience_level} Experience Level')
# # top_companies = selected_experience_level_data['company_name'].unique()
# # for company in top_companies:
# #     st.sidebar.write(company)
# # Exclude 'Not specific' in formatted_experience_level

# # Exclude 'Not specific' in formatted_experience_level


# filtered_df_skill = df[df['skill_name'] == selected_skill_name]
# filtered_df = filtered_df_skill[filtered_df_skill['state'] == selected_state]
# filtered_df = filtered_df[filtered_df['formatted_experience_level'] != 'Not Specified']

# # Aggregate data by company_name and formatted_experience_level for the plot
# company_experience_data = filtered_df.groupby(['company_name', 'formatted_experience_level']).size().reset_index(name='job_count')

# # Get top 5 companies by job count
# top_5_companies = company_experience_data.groupby('company_name')['job_count'].sum().nlargest(5).index
# top_5_data = company_experience_data[company_experience_data['company_name'].isin(top_5_companies)]

# # Sort data by job count
# top_5_data = top_5_data.sort_values('job_count', ascending=False)

# skill_colors = ['#E8D3FF', '#C6CFFF', '#A6E3E9', '#DEECFF', '#F3F8FF']

# color_map = {
#     "Internship": "#E8D3FF",   
#     "Entry level": "#C6CFFF", 
#     "Associate": "#A6E3E9",    
#     "Mid-Senior level": "#DEECFF",  
#     "Director": "#F3F8FF",    
#     "Executive": "#92A9BD",    
# }

# # Create stacked bar chart
# fig3 = px.bar(
#     top_5_data,
#     x='company_name',
#     y='job_count',
#     color='formatted_experience_level',
#     title=f'Top 5 Companies for {selected_skill_name} in {selected_state} by Experience Level',
#     labels={'job_count': 'Job Count', 'company_name': 'Company', 'formatted_experience_level': 'Experience Level'},
#     barmode='stack',
#     color_discrete_map=color_map,  # Apply color map
#     hover_data={'company_name': False}  # Disable company_name in tooltip

# )
# max_job_count = top_5_data['job_count'].max()

# # Add scrollbar functionality to the x-axis
# fig3.update_layout(
#     xaxis=dict(
#         title='Company',
#         tickangle=-45,
#         automargin=True,
#     ),
#     yaxis=dict(
#         title='Job Count',
#         range=[0, max_job_count + 10]  # Limit y-axis to max job count + 10
#     )
# )

# # Display stacked bar chart in Streamlit
# st.title('LinkedIn Job Postings Analysis Dashboard')
# st.header('Top 5 Companies by Job Count and Experience Level')
# st.plotly_chart(fig3, use_container_width=True)


import streamlit as st
import pandas as pd
import plotly.express as px
import plotly.graph_objects as go
import base64

df = pd.read_csv('main_df_subset.csv')

st.set_page_config(
    page_title="Skills Analysis: Job Market Insights",
    page_icon = 'linkedinlogo.gif',
    layout="wide",
    initial_sidebar_state="expanded")

image_path = 'linkedin.png'
with open(image_path, "rb") as image_file:
    encoded_image = base64.b64encode(image_file.read()).decode()

st.markdown(f"""
    <div style='text-align: center; border: 2px solid #0077B5; padding: 10px; border-radius: 10px; background-color: #FAFAFA; margin-bottom: 20px;'>
        <img src="data:image/png;base64,{encoded_image}" width="50" height="50" style="vertical-align: middle; margin-right: 10px;">
        <span style="font-size: 24px; font-weight: bold;">LinkedIn Job Market Dashboard: Skills & Salaries</span>
        <p>Explore key trends in LinkedIn job postings across the USA. This dashboard highlights state-wise distribution of job postings, the relationship between skills and job types, top employers by skill and state, and salary variations by company size and skill. Use the filters to gain insights into the job market dynamics for your selected skill and state.</p>
    </div>
    """, unsafe_allow_html=True)

df = pd.read_csv('main_df_subset.csv')

state_mapping = {
    'NJ': 'New Jersey', 'IL': 'Illinois', 'NY': 'New York', 'CA': 'California', 'PA': 'Pennsylvania', 
    'WI': 'Wisconsin', 'WA': 'Washington', 'NC': 'North Carolina', 'OH': 'Ohio', 'GA': 'Georgia', 
    'KY': 'Kentucky', 'FL': 'Florida', 'MD': 'Maryland', 'TX': 'Texas', 'VA': 'Virginia', 
    'MI': 'Michigan', 'SD': 'South Dakota', 'IN': 'Indiana', 'NE': 'Nebraska', 'MO': 'Missouri', 
    'MA': 'Massachusetts', 'TN': 'Tennessee', 'LA': 'Louisiana', 'DC': 'District of Columbia', 
    'AR': 'Arkansas', 'OK': 'Oklahoma', 'UT': 'Utah', 'MN': 'Minnesota', 'AZ': 'Arizona', 'CT': 'Connecticut', 
    'RI': 'Rhode Island', 'ME': 'Maine', 'NH': 'New Hampshire', 'CO': 'Colorado', 'AL': 'Alabama', 
    'KS': 'Kansas', 'ID': 'Idaho', 'HI': 'Hawaii', 'OR': 'Oregon', 'NV': 'Nevada', 'NM': 'New Mexico', 
    'VT': 'Vermont', 'IA': 'Iowa', 'SC': 'South Carolina', 'DE': 'Delaware', 'ND': 'North Dakota', 
    'MS': 'Mississippi', 'WY': 'Wyoming', 'MT': 'Montana', 'AK': 'Alaska'
}

# Reverse mapping for filtering purposes
reverse_state_mapping = {v: k for k, v in state_mapping.items()}

df_filtered_state = df.copy()
df_filtered_state['state'] = df_filtered_state['state'].replace(state_mapping)
df_filtered_state = df_filtered_state[df_filtered_state['state'].isin(state_mapping.values())]
df['state_full_name'] = df['state'].replace(state_mapping)
if 'selected_state' not in st.session_state:
    st.session_state.selected_state = 'CA' 
     
# Company size mapping
company_size_mapping = {
    1.0: '2-50 employees',
    2.0: '51-200 employees',
    3.0: '201-500 employees',
    4.0: '501-1000 employees',
    5.0: '1001-5000 employees',
    6.0: '5001-10,000 employees',
    7.0: '10,001+ employees'
    }
df['company_size_label'] = df['company_size'].map(company_size_mapping)
df['company_size_label'] = pd.Categorical(df['company_size_label'], categories=[
    '2-50 employees', '51-200 employees', '201-500 employees', '501-1000 employees',
    '1001-5000 employees', '5001-10,000 employees', '10,001+ employees'], ordered=True)

########################Side Bar#################################

with st.sidebar:
    st.sidebar.title("Search Filters")
    unique_skill_names = df['skill_name'].dropna().unique()
    selected_skill_name = st.sidebar.selectbox('Select Skill:', unique_skill_names, key='skill_select')
    unique_states = list(state_mapping.keys())
    selected_state_abbreviation = st.sidebar.selectbox(
        "Select a State",
        unique_states,
        index=unique_states.index(st.session_state.selected_state),
        key='state_select'
    )
    st.session_state.selected_state = selected_state_abbreviation
    selected_state_full_name = state_mapping[selected_state_abbreviation]


filtered_df_skill_state = df[(df['skill_name'] == selected_skill_name) & (df['state'] == selected_state_abbreviation)]


if not filtered_df_skill_state.empty:
    min_salary = filtered_df_skill_state['min_salary'].min()
    max_salary = filtered_df_skill_state['max_salary'].max()
    avg_salary = (filtered_df_skill_state['min_salary'] + filtered_df_skill_state['max_salary']).mean() / 2
    st.sidebar.subheader(f'Salary Statistics for {selected_skill_name} in {selected_state_abbreviation}')
    st.sidebar.write(f"Minimum Salary: ${min_salary:,.2f}")
    st.sidebar.write(f"Average Salary: ${avg_salary:,.2f}")
    st.sidebar.write(f"Maximum Salary: ${max_salary:,.2f}")

    num_job_postings = filtered_df_skill_state.shape[0]  
    st.sidebar.subheader(f'Number of Job Postings for {selected_skill_name} in {selected_state_abbreviation}')
    st.sidebar.write(f"Total: {num_job_postings}")  
    top_5_companies = filtered_df_skill_state['company_name'].value_counts().head(5)
    
    st.sidebar.subheader(f'Top Companies in {selected_state_abbreviation} for {selected_skill_name}')
    for company, count in top_5_companies.items():
        st.sidebar.write(f"{company}: {count} job postings")
else:
    state_filtered = df[df['skill_name'] == selected_skill_name]
    min_salary = state_filtered['min_salary'].min()
    max_salary = state_filtered['max_salary'].max()
    avg_salary = (state_filtered['min_salary'] + filtered_df_skill_state['max_salary']).mean() / 2

    st.sidebar.subheader(f'Salary Statistics for {selected_skill_name}')
    st.sidebar.write(f"Minimum Salary: ${min_salary:,.2f}")
    st.sidebar.write(f"Average Salary: ${avg_salary:,.2f}")
    st.sidebar.write(f"Maximum Salary: ${max_salary:,.2f}")

    num_job_postings = state_filtered.shape[0]  
    st.sidebar.subheader(f'Number of Job Postings in {selected_skill_name}')
    st.sidebar.write(f"Total: {num_job_postings}")  
    top_5_companies = state_filtered['company_name'].value_counts().head(5)
    
    st.sidebar.subheader(f'Top Companies in {selected_skill_name}')
    for company, count in top_5_companies.items():
        st.sidebar.write(f"{company}: {count} job postings")

#########################COL########################
row1_col1, row1_col2 = st.columns(2)

#########################COL 1########################

with row1_col1:
########################MAP PLOT#################################

    filtered_df = df[df['skill_name'] == selected_skill_name]

    state_job_counts = filtered_df.groupby('state')['job_id'].count().reset_index()
    state_job_counts.columns = ['state', 'job_count']

    min_job_count = state_job_counts['job_count'].min()
    max_job_count = state_job_counts['job_count'].max()
    num_bins = 3
    if max_job_count == min_job_count:
        max_job_count += 1
    color_ranges = pd.cut(state_job_counts['job_count'], bins=num_bins, retbins=True)[1]

    def format_label(value):
        if value >= 1000:
            return f'{int(round(value/1000))}K'
        else:
            return f'{int(value)}'
        
    labels = [f'{(format_label(color_ranges[i]))} - {(format_label(color_ranges[i+1]))}' for i in range(len(color_ranges) - 1)]
    state_job_counts['color_label'] = pd.cut(state_job_counts['job_count'],
                                            bins=color_ranges,
                                            labels=labels,
                                            include_lowest=True)
    colors = [ '#deebf7', '#6baed6','#3182bd',
    ]
    color_map = {label: colors[i] for i, label in enumerate(labels)}

    state_job_counts['color'] = state_job_counts['color_label'].map(color_map)

    ticktext = labels
    tickvals = list(range(len(labels)))

    fig = px.choropleth(
        state_job_counts,
        locations='state',
        locationmode='USA-states',
        color='color_label', 
        scope='usa',
        color_discrete_map=color_map,  
        labels={'job_count': 'Job Count', 'color_label': 'Job Count Range'},  
        category_orders={"color_label": labels}  
    )
    fig.update_geos(projection_type="albers usa")
    fig.update_traces(
        hovertemplate='<b>%{location}</b><br>Job Count=%{customdata[0]}<extra></extra>',
        customdata=state_job_counts[['job_count', 'state']]
    )

    fig.update_layout(coloraxis_colorbar=dict(
        title="Open Jobs",
        tickvals=tickvals,
        ticktext=ticktext,
        lenmode="pixels", len=300, yanchor="top", y=1,
        ticks="outside"
    ))
    st.markdown(f'##### Skill Distribution in Job Postings for {selected_skill_name} across the USA')

    st.plotly_chart(fig)

########################SNAKEY PLOT#######################
with row1_col2:
    state_filtered = df[df['state'] == selected_state_abbreviation]
    top_skills = state_filtered['skill_name'].value_counts()
    top_skills = top_skills[top_skills.index != 'other'].head(5).index.tolist()
    state_filtered = state_filtered[state_filtered['skill_name'].isin(top_skills)]
    all_labels = list(set(state_filtered['skill_name']).union(set(state_filtered['formatted_experience_level'])))
    label_to_index = {label: i for i, label in enumerate(all_labels)}
    source = []
    target = []
    value = []
    skills_to_exp = state_filtered.groupby(['skill_name', 'formatted_experience_level']).size().reset_index(name='count')
    for _, row in skills_to_exp.iterrows():
        source.append(label_to_index[row['skill_name']])
        target.append(label_to_index[row['formatted_experience_level']])
        value.append(row['count'])
    skill_colors = ['#D3F4FF', '#B2DFFB', '#B1E8ED', '#C6CBEF', '#CDFFEB']
    skill_color_map = {skill: skill_colors[i] for i, skill in enumerate(top_skills)}
    node_colors = []
    for label in all_labels:
        if label in skill_color_map:
            node_colors.append(skill_color_map[label])
        else:
            node_colors.append("rgba(0, 0, 0, 0.1)")  # Light grey for other nodes
    link_colors = []
    for _, row in skills_to_exp.iterrows():
        link_colors.append(skill_color_map[row['skill_name']])
    fig = go.Figure(data=[go.Sankey(
        node=dict(
            pad=15,
            thickness=20,
            line=dict(color="black", width=0.5),
            label=all_labels,
            color=node_colors
        ),
        link=dict(
            source=source,
            target=target,
            value=value,
            color=link_colors
        )
    )])
    st.markdown(f"##### Skill Distribution in Job Postings for {selected_skill_name} in {selected_state_full_name}")


    st.plotly_chart(fig)


#########################COL 2########################
row2_col1, row2_col2 = st.columns(2)
######################## BAR CHART #######################
with row2_col2:

    col1, col2 = st.columns([4, 1])
    filtered_df_skill = df[df['skill_name'] == selected_skill_name]

    filtered_df_state = filtered_df_skill[filtered_df_skill['state'] == selected_state_abbreviation]
    unique_companies = filtered_df_state['company_name'].nunique()

    filter_use = "both"
    if filtered_df_state.empty:
        if not filtered_df_skill.empty:
            filtered_df_state = filtered_df_skill
            filter_use = "skill"
        else:
            filtered_df_state = df[df['state'] == selected_state_abbreviation]
            filter_use = "state"
            if filtered_df_state.empty:
                filtered_df_state = df
                filter_use = "Not Both"
                
    if unique_companies ==1:
        if not filtered_df_skill.empty and filtered_df_skill['company_name'].nunique() !=1:
            filtered_df_state = filtered_df_skill
            filter_use = "skill"
        else:
            filtered_df_state = df[df['state'] == selected_state_abbreviation]
            if filtered_df_state['company_name'].nunique() !=1:
                filtered_df_state = df[df['state'] == selected_state_abbreviation]
                filter_use = "state"

    available_work_types = filtered_df_state['formatted_work_type'].unique()
    if 'selected_work_type' not in st.session_state:
        st.session_state.selected_work_type = available_work_types[0] if available_work_types.size > 0 else None

    with col2:
        selected_work_type = st.radio(
            "Select Work Type",
            available_work_types,
            index=0 if st.session_state.selected_work_type is None else available_work_types.tolist().index(st.session_state.selected_work_type)
        )

        st.session_state.selected_work_type = selected_work_type

    selected_work_type = st.session_state.selected_work_type

    with col1:
        filtered_df = filtered_df_state[filtered_df_state['formatted_work_type'].isin([selected_work_type])]
        company_experience_data = filtered_df.groupby(['company_name', 'formatted_experience_level']).size().reset_index(name='job_count')
        top_5_companies = company_experience_data.groupby('company_name')['job_count'].sum().nlargest(5).index
        top_5_data = company_experience_data[company_experience_data['company_name'].isin(top_5_companies)]
        top_5_data = top_5_data.sort_values('job_count', ascending=False)
        color_map = {
            "Internship": "#DAE1E7",
            "Entry level": "#AEDADD",
            "Associate": "#9ecae1",
            "Mid-Senior level": "#6baed6",
            "Director": "#3182bd",
            "Executive": "#08519c"
        }
        fig3 = px.bar(
            top_5_data,
            x='company_name',
            y='job_count',
            color='formatted_experience_level',
            labels={'job_count': 'Job Count', 'company_name': 'Company', 'formatted_experience_level': 'Experience Level'},
            barmode='stack',
            color_discrete_map=color_map,
            category_orders={
                'formatted_experience_level': ["Internship", "Entry level", "Associate", "Mid-Senior level", "Director", "Executive"]
            },
            hover_data={'company_name': False}
        )
        fig3.update_layout(
            xaxis=dict(
                title='Company',
                tickangle=-45,
                automargin=True,
            ),
            yaxis=dict(
                title='Job Count',
                range=[0, top_5_data['job_count'].max() + 10]
            )
        )
        if filter_use is "both":
            st.markdown(f"##### Top Companies for {selected_skill_name} in {selected_state_full_name}:Distribution by Experience Level of {selected_work_type}")
        if filter_use is "skill":
            st.markdown(f"##### Top Companies for {selected_skill_name} :Distribution by Experience Level of {selected_work_type}")
        if filter_use is "state":
            st.markdown(f"##### Top Companies in {selected_state_full_name}: Distribution by Experience Level of {selected_work_type}")
        if filter_use is "Not Both":
            st.markdown(f"##### Top Companies : Distribution by Experience Level of {selected_work_type}")
        st.plotly_chart(fig3, use_container_width=True)

    
########################BOX PLOT #######################
with row2_col1:
    def box_plot(df, selected_skill_name):
        filter_box = df[df['skill_name'] == selected_skill_name]
        filter_box['salary'] = df.apply(lambda row: [row['min_salary'], row['max_salary']], axis=1)
        df_expanded = filter_box.explode('salary')
        df_expanded['salary'] = pd.to_numeric(df_expanded['salary'], errors='coerce')
        df_expanded['applies'] = pd.to_numeric(df_expanded['applies'], errors='coerce')
        df_expanded = df_expanded.dropna(subset=['salary', 'applies'])

        top_company_sizes = df_expanded.groupby('company_size_label')['salary'].max().nlargest(3).index.tolist()
        company_size_sorted = sorted(top_company_sizes, key=lambda x: list(company_size_mapping.values()).index(x))

        df_expanded = df_expanded[df_expanded['company_size_label'].isin(company_size_sorted)]

        applies_description = df_expanded['applies'].describe()
        def categorize_applies(x):
            if x == 0:
                return 'No\nApplications'
            elif x <= applies_description['75%']:
                return 'Average\nApplications'
            else:
                return 'Above Average\nApplications'
        df_expanded['applies_category'] = df_expanded['applies'].apply(categorize_applies)

        fig = px.box(df_expanded, x='company_size_label', y='salary', color='applies_category',
                     labels={'company_size_label': 'Company Size', 'salary': 'Salary', 'applies_category': 'Applies Category'},
                     color_discrete_map={
                         'No\nApplications': '#9ecae1',
                         'Average\nApplications': '#4292c6',
                         'Above Average\nApplications': '#08306b'
                     },
                     category_orders={'company_size_label': company_size_sorted,
                                      'applies_category':  ['No\nApplications', 'Average\nApplications', 'Above Average\nApplications']},
                     points=False)
        fig.update_layout(
            xaxis_title='Company Size',
            yaxis_title='Salary',
            xaxis_tickangle=-45,
            showlegend=True,
            height=600,
            width=800,
            yaxis_range=[0, df_expanded['salary'].max() + 20000]  
        )
        st.markdown(f"##### Salary Distribution by top 3 Company Size for {selected_skill_name}")
        st.plotly_chart(fig)
    if selected_skill_name:
        box_plot(df, selected_skill_name)
