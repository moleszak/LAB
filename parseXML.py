import xml.etree.ElementTree as ET
### parse user.xml file
# Parse the user.xml file
    mytree = ET.parse('user.xml')
    myroot = mytree.getroot()
user = myroot.find('user')
prit(user.find('name').text)
for role in user.findall('roles'):
    print(role.text)
