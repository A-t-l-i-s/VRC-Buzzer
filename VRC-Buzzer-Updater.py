import sys
sys.path = [".", "lib", "lib.zip", "bin", "bin.zip", "engine.zip"]

import os
import shutil
import zipfile
import requests

from pathlib import Path





if (__name__ == "__main__"):
	owner = "A-t-l-i-s"
	repo = "VRC-Buzzer"
	outFile = Path("release.zip")


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

	if (isinstance(assets, list)):
		for a in assets:
			if (a["name"] == "Windows.zip"):
				with requests.get(url = a["browser_download_url"], stream = True) as r:
					r.raise_for_status()

					
					with outFile.open("wb") as f:
						s = 0
						
						for c in r.iter_content(chunk_size = 0xffff):
							s += len(c)

							f.write(c)

							p = round((s / a["size"]) * 100, 2)
							print(f"Downloading {p}%")



				break


	if (outFile.exists() and outFile.is_file()):
		# Delete old files
		print("Removing Old Files...")
		shutil.rmtree("engine")
		shutil.rmtree("res/data")
		shutil.rmtree("res/fonts")
		shutil.rmtree("res/icons")
		shutil.rmtree("res/parameters")
		shutil.rmtree("res/styles")


		file = zipfile.ZipFile(outFile)

		for n in file.namelist():

			try:
				file.extract(
					n,
					Path(".")
				)
				print(f"Extracted '{n}'")
			
			except:
				print(f"Failed to extract '{n}'")


		# Close file
		file.close()


		# Delete file
		os.remove(outFile)








