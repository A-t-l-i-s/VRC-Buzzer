import sys
sys.path = [".", "lib", "lib.zip", "bin", "bin.zip", "engine.zip"]

import os
import io
import shutil
import zipfile
import requests

from pathlib import Path





if (__name__ == "__main__"):
	owner = "A-t-l-i-s"
	repo = "VRC-Buzzer"

	delDirs = [
		"engine",
		"res/fonts",
		"res/icons",
		"res/parameters",
		"res/plugins",
		"res/styles"
	]


	req = requests.get(
		url = f"https://api.github.com/repos/{owner}/{repo}/releases/latest",
		headers = {
			"Accept": "application/vnd.github+json"
		},
		json = True
	)

	req.raise_for_status()


	# Get data as json
	data = req.json()


	# Get assets
	assets = data.get("assets")

	fileData = io.BytesIO()

	if (isinstance(assets, list)):
		for a in assets:
			if (a["name"] == "Windows.zip"):
				with requests.get(url = a["browser_download_url"], stream = True) as r:
					r.raise_for_status()

					
					s = 0
					
					for c in r.iter_content(chunk_size = 0xffff):
						s += len(c)

						fileData.write(c)

						p = round((s / a["size"]) * 100, 2)
						print(f"Downloading {p}%")



				break



	# Delete old files
	for d in delDirs:
		p = Path(d)

		print(f"Deleting '{p}'")

		if (p.exists()):
			if (p.is_dir()):
				shutil.rmtree(p)

			else:
				os.remove(p)


	# Open buffer as zip file
	file = zipfile.ZipFile(fileData)

	# Get all files inside
	files = file.namelist()
	filesLen = len(files)

	for i, n in enumerate(files):
		p = round((i / filesLen) * 100, 2)
		
		try:
			file.extract(
				n,
				Path(".")
			)

			print(f"Extracted {p}% '{n}'")
		
		except:
			print(f"Failed to extract {p}% '{n}'")


	# Close buffer files
	file.close()
	fileData.close()








