# dataGenSDV
Spike SDV

# virtual env creation and activation 
    python -m venv venv
    source venv/bin/activate

# install modules
    pip install -r requirements.txt    

# Validate setup and SDV's working 
    python basic.py

# Generate single table data. Input and output file paths are hardcoded
    python single_table.py

# Generate multiple table relational data. Input and output file paths are hardcoded
    python multi_table.py