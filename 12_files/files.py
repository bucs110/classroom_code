import json

def main():
    #modes: r-reading, w-writing, a-append
    fd = open("people.json", "r" )
    json_data = fd.read()
    fd.close()
    data = json.loads(json_data)
    data['Name'] = "Six Fingered Man"
    data['Friends'] = ["Bad People"]
    fd = open("people.json", "w" )
    json_data = json.dumps(data)
    print(json_data)
    print(type(json_data))
    fd.write(json_data)
    fd.close()
main()
