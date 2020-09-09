## 2. Defining the Dataset Class ##

class Dataset:
    def __init__(self):
        self.type = 'csv'
        
dataset = Dataset()
print(dataset.type)

## 3. Passing Additional Arguments to the Initializer ##

# Default display code
class Dataset:
    def __init__(self, data):
        self.type = "csv"
        self.data = data
f = open("nfl.csv", 'r')        
f = csv.reader(f)
nfl_data = list(f)
nfl_dataset = Dataset(nfl_data)
dataset_data=nfl_dataset.data

## 4. Adding Additional Behavior ##

class Dataset:
    def __init__(self, data):
        self.data = data
        
    def print_data(self, num_rows):
        print(self.data[:num_rows])
        
nfl_dataset = Dataset(nfl_data)
nfl_dataset.print_data(5)

## 5. Enhancing the Initializer ##

class Dataset:
    def __init__(self, data):
        self.data  =data
        self.header = self.data[0]
        self.data = self.data[1:]
        
nfl_dataset = Dataset(nfl_data)
nfl_header = nfl_dataset.header

## 6. Grabbing Column Data ##

class Dataset:
    def __init__(self, data):
        self.header = data[0]
        self.data = data[1:]
    
    def column(self, label):
        if label not in self.header:
            return None
        
        index = 0
        for idx, element in enumerate(self.header):
            if label == element:
                index = idx
                break
        
        column = []
        for row in self.data:
            column.append(row[index])
        return column

nfl_dataset = Dataset(nfl_data)
year_column = nfl_dataset.column('year')
player_column = nfl_dataset.column('player')
print(nfl_data[0:4])

## 7. Count Unique Method ##

# Default display code
class Dataset:
    def __init__(self, data):
        self.header = data[0]
        self.data = data[1:]
    
    def column(self, label):
        if label not in self.header:
            return None
        
        index = 0
        for idx, element in enumerate(self.header):
            if label == element:
                index = idx
        
        column = []
        for row in self.data:
            column.append(row[index])
        return column
    
    def count_unique(self, label):
        result = self.column(label)
        unique = set(result)
        count = len(unique)
        return count

nfl_dataset = Dataset(nfl_data)
total_years = nfl_dataset.count_unique('year')

## 8. Make Objects Human Readable ##

# Default display code
class Dataset:
    def __init__(self, data):
        self.header = data[0]
        self.data = data[1:]
    
    # Add the special method here
    
    def column(self, label):
        if label not in self.header:
            return None
        
        index = 0
        for idx, element in enumerate(self.header):
            if label == element:
                index = idx
        
        column = []
        for row in self.data:
            column.append(row[index])
        return column
    
        
    def count_unique(self, label):
        unique_results = set(self.column(label))
        count = len(unique_results)
        return count
    
    def __str__(self):
        return str(self.data[:10])

nfl_dataset = Dataset(nfl_data)
print(nfl_dataset)