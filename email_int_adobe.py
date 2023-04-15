import xml.etree.ElementTree as ET

email_data=[]
soap_message = '''<soapenv:Envelope xmlns:soapenv="http://schemas.xmlsoap.org/soap/envelope/" xmlns:urn="urn:nms:rtEvent">
                        <soapenv:Header/>
                        <soapenv:Body>
                            <urn:PushEvent>
                                <urn:sessiontoken>mc/tGBNFTNoTOx1</urn:sessiontoken>
                                <urn:domEvent>
                                    <rtEvent email="kirti.p@anxilla.com" type="payment_decline_event" wishedChannel="0">
                                        <ctx>
                                            <bookingReferenceID>#ABC456</bookingReferenceID>
                                            <flights>
                                                <flight>
                                                    <flightNo>MH195</flightNo>
                                                    <from>KUL</from>
                                                    <to>BOM</to>
                                                    <departureDate>11 Jan 2023</departureDate>
                                                </flight>
                                                <flight>
                                                    <flightNo>MH1041</flightNo>
                                                    <from>BOM</from>
                                                    <to>KUL</to>
                                                    <departureDate>12 Jan 2023</departureDate>
                                                </flight>
                                            </flights>
                                        </ctx>
                                    </rtEvent>
                                </urn:domEvent>
                            </urn:PushEvent>
                        </soapenv:Body>
                    </soapenv:Envelope>'''
root = ET.fromstring(soap_message)
# print(root)
# print(ET.dump(root),'yes') # print the root element to check the XML string
# ns = {'urn': 'urn:nms:rtEvent'}
# rt_event = root.find(".//urn:rtEvent", ns) # find rtEvent element using namespace
# if rt_event is not None:
#     rt_event.set("email", "new_email@example.com")
#     soap_message = ET.tostring(root)
# print(soap_message)

rt_event = root.find(".//{urn:nms:rtEvent}rtEvent")
# rt_event = root.find(".//{http://schemas.xmlsoap.org/soap/envelope/}{urn:nms:rtEvent}rtEvent")


print(rt_event)
# rt_event.set("email", "new_email@example.com")
# if rt_event is not None:
#     rt_event.set("email", "new_email@example.com")
#     soap_message = ET.tostring(root)
# print(soap_message)
# def email_int_adobe():
#     pass

# email_int_adobe()