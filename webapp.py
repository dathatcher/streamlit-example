import streamlit as st
import yaml

def create_config_model(config_data):
    config_model = {}
    for config_item in config_data.get("configuration_items", []):
        item_name = config_item.get("name", "")
        config_model[item_name] = {
            "Type": config_item.get("type", ""),
            "Description": config_item.get("description", ""),
            "Location": config_item.get("location", ""),
            "Owner/Contact": config_item.get("owner_contact", ""),
            "Status": config_item.get("status", ""),
            "Lifecycle Information": config_item.get("lifecycle_information", []),
            "Attributes/Specifications": config_item.get("attributes_specifications", []),
            "Dependencies": config_item.get("dependencies", []),
            "Configuration History": config_item.get("configuration_history", ""),
            "Related Documentation": config_item.get("related_documentation", ""),
            "Security Compliance": config_item.get("security_compliance", {}).get("nist_controls", []),
        }
    return config_model

def display_hierarchy(dependencies, level=0):
    for dependency in dependencies:
        st.text("  " * level + f"- {dependency}")
        if isinstance(dependency, dict):
            display_hierarchy(dependency, level + 1)

def main():
    st.title("Configuration Model Viewer")

    # File Upload
    uploaded_file = st.file_uploader("Upload YAML Configuration File", type=["yaml", "yml"])

    if uploaded_file is not None:
        try:
            config_data = yaml.safe_load(uploaded_file)
            config_model = create_config_model(config_data)

            # Display Configuration Model
            for item_name, item_data in config_model.items():
                st.subheader(f"Configuration Item: {item_name}")
                for field, value in item_data.items():
                    st.text(f"{field}: {value}")

                dependencies = item_data.get("Dependencies", [])
                if dependencies:
                    st.text("Dependencies:")
                    display_hierarchy(dependencies)

                st.markdown("---")

        except yaml.YAMLError as e:
            st.error(f"Error loading YAML file: {e}")

if __name__ == "__main__":
    main()
