import requests
def testapi():
    soap_address = 'https://malaysiaairlines-rt-stage1.campaign.adobe.com/nl/jsp/soaprouter.jsp'
    req_header = {
        'Content-Type': 'text/xml;charset=UTF-8',
        'SOAPAction': 'nms:rtEvent#PushEvent',
    }
    soap_message = '''<soapenv:Envelope xmlns:soapenv="http://schemas.xmlsoap.org/soap/envelope/" xmlns:urn="urn:nms:rtEvent">
                        <soapenv:Header/>
                        <soapenv:Body>
                            <urn:PushEvent>
                                <urn:sessiontoken>mc/tGBNFTNoTOx1</urn:sessiontoken>
                                <urn:domEvent>
                                    <rtEvent email="kirti.p@anxilla.com" type="payment_confirmation_event" wishedChannel="0">
                                        <ctx>
                                            <confirmationID>#787fjhdfk</confirmationID>
                                        </ctx>
                                    </rtEvent>
                                </urn:domEvent>
                            </urn:PushEvent>
                        </soapenv:Body>
                    </soapenv:Envelope>'''

    # Make the request
    response = requests.post(soap_address, headers=req_header, data=soap_message)
    if response.status_code == 200:
        print(response.content)
    else:
        print(response)
    return '1'

testapi()