import streamlit as st
import math

st.title('Basement Finishing Cost Estimator')

# Function to calculate drywall requirements
def calculate_drywall(length, width, height, panel_length, panel_width, include_ceiling, add_extra):
    wall_area = 2 * height * (length + width)
    ceiling_area = length * width if include_ceiling else 0
    total_area = wall_area + ceiling_area
    if add_extra:
        total_area *= 1.10  # Add 10% extra
    panel_area = panel_length * panel_width
    num_panels = math.ceil(total_area / panel_area)
    return total_area, num_panels

# Function to calculate flooring requirements
def calculate_flooring(length, width, add_extra):
    area = length * width
    if add_extra:
        area *= 1.10  # Add 10% extra
    return area

st.header('Drywall Estimation')

# Drywall Inputs
wall_length = st.number_input('Enter the length of the walls (in feet):', min_value=0.0, value=24.0)
wall_width = st.number_input('Enter the width of the walls (in feet):', min_value=0.0, value=12.0)
wall_height = st.number_input('Enter the height of the walls (in feet):', min_value=0.0, value=8.0)
include_ceiling = st.checkbox('Include ceiling in drywall calculation?', value=True)
drywall_panel_length = st.selectbox('Select drywall panel length (in feet):', [8, 10, 12], index=0)
drywall_panel_width = 4  # Standard width
drywall_cost_method = st.radio('Select drywall cost method:', ('Per Square Foot', 'Per Panel'))
if drywall_cost_method == 'Per Square Foot':
    drywall_cost_per_sqft = st.number_input('Enter the cost per square foot of drywall ($):', min_value=0.0, value=0.50)
else:
    drywall_cost_per_panel = st.number_input(f'Enter the cost per {drywall_panel_width}x{drywall_panel_length} ft panel ($):', min_value=0.0, value=10.0)
add_extra_drywall = st.checkbox('Add 10% extra drywall material for waste?')

# Drywall Calculations
total_drywall_area, num_panels = calculate_drywall(wall_length, wall_width, wall_height, drywall_panel_length, drywall_panel_width, include_ceiling, add_extra_drywall)
if drywall_cost_method == 'Per Square Foot':
    total_drywall_cost = total_drywall_area * drywall_cost_per_sqft
else:
    total_drywall_cost = num_panels * drywall_cost_per_panel

st.subheader('Drywall Results')
st.write(f'Total drywall area: {total_drywall_area:.2f} sq ft')
st.write(f'Number of {drywall_panel_width}x{drywall_panel_length} ft panels needed: {num_panels}')
st.write(f'Total drywall material cost: ${total_drywall_cost:.2f}')

st.header('Flooring Estimation')

# Flooring Inputs
flooring_length = st.number_input('Enter the length of the flooring area (in feet):', min_value=0.0, value=19.0)
flooring_width = st.number_input('Enter the width of the flooring area (in feet):', min_value=0.0, value=14.0)
flooring_cost_method = st.radio('Select flooring cost method:', ('Per Square Foot', 'Per Unit'))
if flooring_cost_method == 'Per Square Foot':
    flooring_cost_per_sqft = st.number_input('Enter the cost per square foot of flooring ($):', min_value=0.0, value=2.00)
else:
    flooring_unit_area = st.number_input('Enter the area covered per flooring unit (in sq ft):', min_value=0.1, value=20.0)
    flooring_cost_per_unit = st.number_input('Enter the cost per flooring unit ($):', min_value=0.0, value=50.0)
add_extra_flooring = st.checkbox('Add 10% extra flooring material for waste?')

# Flooring Calculations
total_flooring_area = calculate_flooring(flooring_length, flooring_width, add_extra_flooring)
if flooring_cost_method == 'Per Square Foot':
    total_flooring_cost = total_flooring_area * flooring_cost_per_sqft
else:
    num_units = math.ceil(total_flooring_area / flooring_unit_area)
    total_flooring_cost = num_units * flooring_cost_per_unit

st.subheader('Flooring Results')
st.write(f'Total flooring area: {total_flooring_area:.2f} sq ft')
if flooring_cost_method == 'Per Unit':
    st.write(f'Number of flooring units needed: {num_units}')
st.write(f'Total flooring material cost: ${total_flooring_cost:.2f}')

# Total Project Cost
total_project_cost = total_drywall_cost + total_flooring_cost
st.header('Total Project Cost')
st.write(f'Total cost for drywall and flooring materials: ${total_project_cost:.2f}')
