import pubmed_parser as pp
import json
import re
import os


original_dataset_dir = "PMC-dataset"
preprocessed_dataset_dir = "PMC-dataset-preprocessed"
selected_keys = ["full_title", "abstract"]

xml_paths = pp.list_xml_path(original_dataset_dir)
for xml_path in xml_paths:
    paper_dict = pp.parse_pubmed_xml(xml_path)
    selected_data = {key: paper_dict[key] for key in selected_keys}

    xml_file_name = re.search(r"[^/]+(?=\.xml$)", xml_path).group()
    selected_file_path = preprocessed_dataset_dir + "/" + xml_file_name + ".json"
    
    if not os.path.exists(preprocessed_dataset_dir):
        os.makedirs(preprocessed_dataset_dir)
    with open(selected_file_path, "w") as json_file:
        json.dump(selected_data, json_file, indent=4)