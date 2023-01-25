import streamlit as st
import yaml

# Example configuration items
config_items = [
    {"name": "Web Server", "description": "Apache or Nginx"},
    {"name": "Database", "description": "MySQL or PostgreSQL"},
    {"name": "Cache", "description": "Redis or Memcached"}
]

# Example pipeline stages
pipeline_stages = [
    "Plan", "Build", "Deploy to Lower Environments", "Test", "Deploy to Production"
]

# Example pipeline tools
pipeline_tools = {
    "Plan": ["Jira", "Trello"],
    "Build": ["Jenkins", "TravisCI"],
    "Deploy to Lower Environments": ["Ansible", "Chef"],
    "Test": ["JUnit", "TestNG"],
    "Deploy to Production": ["AWS CodeDeploy", "Heroku"]
}

# Example DAST and SAST tools
dast_sast_tools = ["OWASP ZAP", "Burp Suite", "Nessus"]

# Create a selectbox for the configuration items
config_item_select = st.selectbox("Select Configuration Item", [item["name"] for item in config_items])

# Create checkboxes for pipeline stages and tools
selected_stages = st.multiselect("Select Pipeline Stages", pipeline_stages)
pipeline_tools_select = {}
for stage in selected_stages:
    pipeline_tools_select[stage] = st.multiselect(f"Select Tools for {stage}", pipeline_tools[stage])

# Create checkboxes for DAST and SAST tools
dast_sast_tools_select = st.multiselect("Select DAST and SAST Tools", dast_sast_tools)

# Convert the selected configuration items, pipeline, and DAST/SAST tools to YAML
config = {
    "config_items": config_item_select,
    "pipeline": pipeline_tools_select,
    "dast_sast_tools": dast_sast_tools_select
}
yaml_config = yaml.dump(config)

# Display the YAML configuration
st.write("### Configuration:")
st.code(yaml_config, language='yaml')
