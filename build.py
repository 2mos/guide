import os
import json

relative_path = 'pages'
current_dir = os.path.dirname(os.path.abspath(__file__))
pages_dir = os.path.join(current_dir, relative_path)
template_path = os.path.join(current_dir, 'template.html')
md_files = list()

with open(template_path, 'r') as template_file:
    template_content = template_file.read()

for root, _, files in os.walk(pages_dir):
    for file_name in files:
        file_name = os.path.splitext(file_name)[0]
        new_folder_path = os.path.join(current_dir, file_name)
        os.makedirs(new_folder_path, exist_ok=True)
        updated_template = template_content.replace('{file_name}', file_name)
        html_file_path = f"{new_folder_path}/index.html"
        with open(html_file_path, 'w') as html_file:
            html_file.write(updated_template)
        md_files.append(file_name)

json_file = 'files.json'
with open(json_file, 'w') as f:
    json.dump(md_files, f)



