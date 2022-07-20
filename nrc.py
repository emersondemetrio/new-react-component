#!/usr/bin/python3
import sys
import os
import json
from typing import List


def create_file(path: str, content: str) -> None:
    with open(path, 'w') as f:
        f.write(f"""{content.strip()}\n""")


def ensure_path(path: str) -> None:
    if not os.path.exists(path):
        os.makedirs(path)


def summary(assets: object) -> None:
    print(f"\n> [NRC] New React component: {assets['name']}\n")
    print(f"> Obs.: Path is relative to {os.getcwd()}\n")
    print(f"> Files created at {os.path.realpath(assets['full-path'])}\n")
    print("Results:\n")
    print(json.dumps(assets, indent=4))


def get_export_template(component_file: str) -> str:
    return f"export {{ default }} from './{component_file}';"


def get_component_template(component_name: str, properties: List[str]) -> str:
    prop_types = ""
    prop_values = ""
    pos = -1
    lb = ""
    for p in properties:
        pos += 1
        lb = "\n" if pos != len(properties) - 1 else ""
        prop_types += f"  {p}: string;{lb}"
        prop_values += f"{p}, "

    return f"""
import React, {{ useEffect, useState }} from 'react';
import {{ Box }} from '@drivekyte/web-components';

type {component_name}Props = {{
{prop_types}
}};

const {component_name} = ({{ {prop_values} }}: {component_name}Props) => {{
  const [loading, setLoading] = useState(false);

  console.log('This props', {prop_values if prop_values else '"None"'});

  useEffect(() => {{
    setLoading(!loading);
  }}, [loading]);

  return (
    <Box>
      <div>{component_name}</div>
    </Box>
  );
}};

export default {component_name};"""


def main(full_path: str, properties: List[str]) -> None:
    file_name = full_path.split('/')[-1]
    assets = {
        "export-file": "index",
        "full-path": full_path,
        "file": file_name.lower(),
        "name": file_name.title().replace('-', ''),
    }

    summary(assets)

    ensure_path(full_path)

    create_file(
        f'{full_path}/{assets["export-file"]}.ts',
        get_export_template(assets["file"]))

    create_file(
        f'{full_path}/{assets["file"]}.tsx',
        get_component_template(assets['name'], properties))


if __name__ == "__main__":
    os.system('clear')

    if len(sys.argv) < 2 or not sys.argv[1]:
        print("\n> Error - no name was given\n")
        print('> Usage:\nnrc path/to/component-name\n')
        print('> Example:\nnrc welcome-page\n')
        exit(-1)

    properties = sys.argv[2::] if len(sys.argv) > 2 else []

    main(sys.argv[1], properties)
