# AIOpenScience [![DOI](https://zenodo.org/badge/599211911.svg)](https://zenodo.org/badge/latestdoi/599211911)

**Author**: Alejandro Ruiz Ballester

Esta es la librería para la clase Artificial Intelligence And Open Science In Research Software Engineering

This code analyzes a series of input papers though Grobid and returns a Wordcloud based on the abstract, a list of all the links inside of the paper and a bar graph with the number of figures per paper.

# How to use locally 

In order to use it locally :

1) Open the anaconda3 terminal 
2) Create the conda environment
```bash
conda create --name myenv python=3.10
```
3) Activate the environment 
```bash
conda activate myenv 
```
4) Install all the dependencies located in /docs/requirements.txt using pip
One example:
```bash
pip install PyPDF2 
```
5) Add in the folder ./code/shared all the downloaded PDFs that you want to have analyzed 
6) Get Grobid Docker image and run it in port 8070
```bash
docker pull lfoppiano/grobid:0.7.2
docker run -t --rm -p 8070:8070 lfoppiano/grobid:0.7.2
```
8) Run the code
```bash
python entrega.py
```
# How to use using Docker 
Firstly clone the repository in a folder
1) Add in the folder ./code/shared all the downloaded PDFs that you want to have analyzed 
2) Build the docker image
```bash
docker build -t img_name .
```
Make sure that the dockerfile is located where entrega.py is

3) Get Grobid Docker image and run it in port 8070
```bash
docker pull lfoppiano/grobid:0.7.2
docker run -t --rm -p 8070:8070 lfoppiano/grobid:0.7.2
```
4) Create the volume using the shared folder
```bash
docker volume create shared
```
6) Run the code container 
```bash
docker run --rm -it --network="host" -v ./shared:/shared img_name
```
## References

- GROBID. (2008-2023). Retrieved from https://github.com/kermitt2/grobid
