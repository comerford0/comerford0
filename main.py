import yaml
from datetime import UTC, datetime
from pathlib import Path

from jinja2 import Environment, FileSystemLoader


with Path("portfolio.yaml").open(encoding="utf-8") as f:
    data = yaml.safe_load(f)

# Add any extra context if needed
data["current_year"] = datetime.now(tz=UTC).year

for link in data.get("social_links"):
    if not link.get("svg_path"):
        continue
    with Path(link["svg_path"]).open(encoding="utf-8") as svg_file:
        link["svg_data"] = svg_file.read()

# Set up Jinja environment
env = Environment(loader=FileSystemLoader("."), autoescape=True)
index_template = env.get_template("templates/index_template.html")
resume_template = env.get_template("templates/resume_template.html")

# Render the template with the data
html_output = index_template.render(**data)
resume_output = resume_template.render(**data)

# Write the output to an HTML file
with Path("index.html").open("w", encoding="utf-8") as f:
    f.write(html_output)

with Path("resume.html").open("w", encoding="utf-8") as f:
    f.write(resume_output)

print("HTML file generated successfully!")
