def GetData():
  print('Connect to database')
  print('test')
def Process_data(data):
    def clean_data(data):
        return [x for x in data if x is not None]

    def sort_data(data):
        return sorted(data)

    data = clean_data(data)
    data = sort_data(data)
    print('done')
    return data
