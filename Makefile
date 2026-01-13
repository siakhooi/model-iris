info:
download: clean
	mkdir -p target
	cd notebooks && papermill 00_download_dataset.ipynb ../target/00_download_dataset_output.ipynb
clean:
	rm -rf data target

