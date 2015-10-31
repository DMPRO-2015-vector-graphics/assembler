import sys

def getFileToReadFrom():
    if len(sys.argv) >= 2:
        return open(sys.argv[1], 'r')
    else:
        print('Missing file to read')
        sys.exit(2)
def getFileToWrite():
    
    return

def main():
    fileToReadFrom = getFileToReadFrom()

    print(str(sys.argv))
    print('test')

main()
