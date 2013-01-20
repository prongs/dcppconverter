import lxml.etree as etree
import os

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
	dcppxml=etree.parse(open("/home/"+os.environ['USER']+"/.dc++/DCPlusPlus.xml"))
	self.version=dcppxml.find('Settings/ConfigVersion').text

    def convert(self):
        doc=etree.parse(self._source);
        root=doc.getroot();
        root.set("Version", self.version)
        for elem in root:
            elem.set("Target", self.convertPath(elem.get("Target")))

        doc._setroot(root);
        doc.write(self._target, encoding='utf-8', standalone='yes')
        self._target.close();

    def convertPath(self, path):
        path=path.replace("\\", "/");
        path=path.replace("C:/", "/media/windows/");
        path=path.replace("D:/", "/media/Programs/");
        path=path.replace("E:/", "/media/All/");
        path=path.replace("F:/", "/media/win7/");
        path=path.replace("G:/", "/media/Studies/");
        return path;



if __name__ == '__main__':    
    conv=Converter("/media/windows/Users/Rajat/AppData/Roaming/DC++/Queue.xml", "/home/rajat/.dc++/Queue.xml");
    conv.convert();


