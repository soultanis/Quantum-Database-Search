<img src="Sitzungsprotokolle/README-src/Logo-School-of-Engineering.jpg" alt="ZHAW" width="150"/>

# Grover-Algorithmus Qiskit
Dieses Repository dient als Anhang zum eBook "Vom Qubit bis zum Grover-Algorithmus", was ihm Rahmen einer Projektarbeit an der ZHAW School of Engineering durchgeführt wurde. Das Ziel dieser Publikation ist es zu zeigen, wie ein Quantencomputer rechnet und wie es ihm gelingt, effizienter als der klassische Computer zu sein, demonstriert anhand des Grover-Algorithmus. Dabei ist die Publikation in drei Kapitel aufgeteilt:
- Kapitel 1 - Einleitung: Die Einleitung bietet eine grobe Übersicht zum Thema Quantencomputer, wobei versucht wird, mit wenigen und einfachen Sätzen den Quantencomputer zu beschreiben. Ausserdem sind Informationen zum Framework Qiskit von IBM aufzufinden, die für die Implementation benutzt wurde.
- Kapitel 2 - Cbits und Qubits: In diesem Kapitel tauchen wir in die Theorie der Quanteninformatik ein. Angefangen bei den kleinsten Bausteinen, dem Cbit und Qubit, arbeiten wir uns durch bis zu den Schaltungen, damit das fundamentale Verständnis für Algorithmen gelegt ist. Oder anders ausgedrückt: Das Kapitel der linearen Algebra kombiniert mit der Wahrscheinlichkeitstheorie über den Komplexen Zahlen. Viel Mathematik, wenig Lückenfüller-Text.
- Kapitel 3 - Der Grover-Algorithmus: Zum Schluss wird die Theorie in die Praxis umgesetzt. Es wird Schritt für Schritt aufgezeigt, wie der Grover-Algorithmus funktioniert und wie man ihn auf einem echten Quantencomputer von [IBM](https://www.ibm.com/ch-de/?ar=1) mit dem Framework [Qiskit](https://qiskit.org/) ausführt.

## Voraussetzungen
Unter [Qiskit](https://github.com/Qiskit) sind Grundkonzepte sehr gut dokumentiert. Folgende Installationen werden benötigt:
- [Anaconda](https://www.anaconda.com/download/) oder [Python](https://www.python.org/downloads/) und [Jupyter-Notebook](https://github.com/jupyter/notebook)
- [Qiskit](https://github.com/Qiskit/qiskit-tutorial/blob/master/INSTALL.md) __Version 0.6.0__
```
pip install qiskit==0.6.0
```
- [IBM Q Account](https://www.ibm.com/account/reg/us-en/signup?formid=urx-19776&target=https%3A%2F%2Fwww.ibm.com%2Fch-de%2F%3Far%3D1)

## [Jupyter-Notebook](https://github.com/soultanis/Grover-Algorithmus-Qiskit/tree/master/Jupyter-Notebook)
Theorie und Implementation des Grover Algorithmus mit bis zu 4 Qbits (Simulation- und IBMQ-Backend) mit Jupyter-Notebook.

## [src](https://github.com/soultanis/Grover-Algorithmus-Qiskit/tree/master/src)
Implementation des Grover Algorithmus mit bis zu 3 Qbits (Simulation- und IBMQ-Backend) in Python.  

## [Sitzungsprotokolle](https://github.com/soultanis/Grover-Algorithmus-Qiskit/tree/master/Sitzungsprotokolle)
Festgehaltene Sitzungsprotokolle mit Prof. Dr. Kurt Stockinger und Prof. Dr. Ruedi Füchslin.
