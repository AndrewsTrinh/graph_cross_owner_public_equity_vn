# Demo graph analytics of Vietnamese public listed company
# Data
- Public data of BoD and BoM members crawled from MBS Website
# Installation
Requirement: install `pipenv` for python
```
pip install pipenv
```
- Installing dependency:
```
pipenv install --system
```
- Starting environment
```
pipenv shell
```
- Running file `crawler.py` to crawl latest data
- Runing file `analyze.py` to render the graph
![final result](./img/graph.png)