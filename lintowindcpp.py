import lxml.etree as etree

class Converter(object):
    """
    """
    
    def __init__(self, source, target):
        """
        
        Arguments:
        - `source`:
        - `target`:
        """
        self._source = open(source)
        self._target = open(target, "w");
    def convert(self):
        doc=etree.parse(self._source);
        root=doc.getroot();
        root.set("Version", "0.770")
        for elem in root:
            elem.set("Target", self.convertPath(elem.get("Target")))

        doc._setroot(root);
        doc.write(self._target, encoding='utf-8', standalone='yes')
        self._target.close();

    def convertPath(self, path):
        path=path.replace("/home/rajat/Music", "E:/songs");
        path=path.replace("/home/rajat/Videos", "E:/movies")
        path=path.replace("/media/windows", "C:")
        path=path.replace("/media/Programs", "D:")
        path=path.replace("/media/All", "E:")
        path=path.replace("/media/win7", "F:")
        path=path.replace("/media/Studies", "G:")
        path=path.replace("/", "\\");
        return path

if __name__ == '__main__':    
    conv=Converter("/home/rajat/.dc++/Queue.xml", "/media/windows/Users/Rajat/AppData/Roaming/DC++/Queue.xml");
    conv.convert();

