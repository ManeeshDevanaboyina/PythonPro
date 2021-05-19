                                                        #Not completed code


import xml.etree.ElementTree as ET

input='''
<mobile>
    <company name="samsung">
        <model1 type="low_end">
            <name>samsung M10</name>
            <specifications>Good Camera</specifications>
        </model1>
        <model2 type="high_end">
            <name>samsung s20</name>
            <specifications>High_Performance</specifications>
     </company x>
     <company name="MI">
        <model1 type="low_end">
            <name>Redmi5s</name>
            <specifications>Good Quality</specifications>
        </model1>
        <model2 type="high_end">
            <name>RedmiShark</name>
            <specifications>Good Quality & High_Performance</specifications>
        </model2>
     </company y>
</mobile>'''

text=ET.fromstring(input)
text.findall(company/model)

#x=text.mobile.findall('company x/company y')
#print(x)
