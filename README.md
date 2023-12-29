# Python Concurrency and Parallelism

This project demonstrates the use of concurrency and parallelism in Python. It consists of three main modules: `concurrency.py`, `parallelism.py`, and `utils.py`, which are all called from `main.py`.

## Getting Started

These instructions will get you a copy of the project up and running on your local machine for development and testing purposes.

### Prerequisites

The project requires the following Python packages:

- numpy==1.21.2
- pandas==1.3.3
- concurrent.futures==3.1.1
- multiprocessing==0.70.11.1
- threading==4.4.2

You can install these packages using pip:

```
pip install -r requirements.txt
```

### Running the Project

To run the project, simply execute the `main.py` script:

```
python main.py
```

## Modules

### main.py

This is the main script that calls functions from the other modules. 

### concurrency.py

This module demonstrates the use of threading for concurrency in Python. It defines a function `some_function` that creates and starts two threads, each of which calls a worker function with a specified delay.

### parallelism.py

This module demonstrates the use of multiprocessing for parallelism in Python. It defines a function `some_function` that creates and starts two processes, each of which calls a worker function with a specified delay.

### utils.py

This module contains utility functions that are used by the other modules.

## Authors

- Your Name

## License

This project is licensed under the MIT License - see the LICENSE.md file for details
