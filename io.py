class io(object):
    def __init__(self, arg):
        super(io, self).__init__()
        self.arg = arg

    def createBitFile(filename):
        return open(filename, 'wb')

    def readLine(file):
        return file.readLine()

    def hasLinesLeft(file):
        return file.readLine() == ''

    def closeFile(file):
        file.close()
