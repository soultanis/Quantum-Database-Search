# Python
Eine Implementierung des Grover-Algorithmus mit Qiskit mit bis zu maximal 3 Qubits.

## Übersicht
Um eine Bedienungsanleitung zu erhalten ist `python grover_test.py -h` auszuführen.

### Bedienungsanleitung
#### Erforderliche Argumente
  * `n` die Anzahl der Qubits (mit n max. = 3)
  * `x_star` ist der markierte Zustand (zwischen 0 und 2**n), d.h. der Zustand für den das Orakel 1 zurückgibt. Im Allgemeinen sollte das Orakel als eine Blackbox abstrahiert werden. In diesem Projekt wurde jedoch das Orakel selbst gebaut für 2 bzw. 3 Qubits.
#### Optionale Argumente
* `real` ist True für ein IBMQ-Backend und ist False (default) für das Simulator-Backend. Wenn die Variable auf True gesetzt ist, wird die online Variable automatisch auch auf True gesetzt. Hierfür wird ein IBM Q Token benötigt.
* `online` ist True für ein online IBMQ-Backend und ansonsten False (default).
* `backend_name` ist der Name des Backends, das verwendet wird. Falls die Variable leer gelassen wird, wird eine Standartauswahl genommen. Ist nur für online Backends sinnvoll.
* `--plot` plottet das Histogramm des Resultats.
* `--img_dir IMG_DIR` speichert den Schaltkreis als Bild in das angegebene Verzeichnis ab.
* `-i` gibt nur Informationen über die Schaltung für ein spezifisches Backend ohne es auszuführen.
* `-h` gibt diese Bedienungsanleitung aus.

## Ausführungsbeispiel mit einem IBMQ-Backend
Beispiel eines Experiments mit 3 Qubits, dem markierten Zustand 5 und einem IBMQ-Backend:
- __Als Modul__
``` python
import grover_test as gt

gt.build_and_run(3, [5], real=True, online=True)
```
- __Command line__
``` bash
>python src/grover_test.py 3 5 -r
```
oder wenn spezifisch z.B. auf den ibmq_16_melbourne zugegriffen werden möchte:
``` bash
>python src/grover_test.py 3 5 -r -i -b ibmq_16_melbourne
```
## Ausführungsbeispiel mit einem Simulator-Backend  
Beispiel eines Experiments mit 2 Qubits, dem markierten Zustand 3 und mit dem Simulator-Backend:
- __Als Modul__
``` python
import grover_test as gt

gt.build_and_run(2, [3])
```
- __Command line__
``` bash
>python src/grover_test.py 2 3
```

## Resultate
Die öffentlich zugängigen IBMQ-Backends liefern mit Stand 03.01.2019 nur für n-Qubits mit n < 3 richtige Ergebnisse.
Das Simulator-Backend hingegen liefert auch mit 3 Qubits richtige Ergebnisse und könnte erweitert werden, was jedoch mit grossem Aufwand verbunden ist, da die Anzahl der Gatter extrem Ansteigt.
