python version 3.7.3

install config/requirements.txt

python src/main.py airport_from airport_to departure_date --return

test cases:

    python main.py KEF NCE 2019-08-13
    python main.py KEF NCE 2019-08-13 --return=2019-08-18
    
    python main.py KEF ARN 2019-08-06 --return=2019-08-15
    python main.py KEF BMA 2019-08-06 --return=2019-08-15
    python main.py KEF NYO 2019-08-06 --return=2019-08-15
    
    python main.py MSQ PKV 2019-08-13 --return=2019-08-18
    