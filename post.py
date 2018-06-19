import xml.etree.ElementTree
e = xml.etree.ElementTree.parse('electron.xml').getroot()

for hist1d in e.findall('histogram1d'): ## big loop
    name  = hist1d.get('name')
    title = hist1d.get('title')
    print('histogram1d! name:',name,' title:',title)
    for annotation in hist1d.findall('annotation'): ## this loop is for annotation
        for item in annotation.findall('item'):  
            key   = item.get('key')
            value = item.get('value')
            print('annotation! key:',key,' value',value)
    for axis in hist1d.findall('axis'):   ## this loop is for axis 
        direction    = axis.get('direction')
        numberOfBins = axis.get('numberOfBins')
        bin_min      = axis.get('min')
        bin_max      = axis.get('max')
        print('axis! direction:',direction,' numberofbins:',numberOfBins,' bin_min:',bin_min,' bin_max:',bin_max)
    for data1d in hist1d.findall('data1d'):  ## this loop is for data
        for bin1d in data1d.findall('bin1d'):
            binNum  = bin1d.get('binNum')
            entries = bin1d.get('entries')
            print('data1d! binNum:',binNum,' entries:',entries)

    print('==================end of this hist====================')
    print('======================================================')
