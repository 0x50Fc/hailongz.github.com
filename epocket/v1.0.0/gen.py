
import json
import urllib

def getapi(url):
    url = urllib.urlopen(url)
    s = url.read()
    url.close()
    d = json.loads(s)
    return d

def genCatalog(pdiId,to):

    url = "http://services.xingshulin.com/MediaPlatformWirelessServiceForLiterature/MediaPlatformOtherServlet?m=downloadProductCatalogList&pdiId=%d" % pdiId+"&sessionKey=7B37626662646437313665343566343833326465666334353439623762353763317D2C7B313663636338636636646433643661323962356538326530356661383639613339623137336462617D2C7B66616C73657D2C7B307D2C7B307D2C7B33386337653333652D653030342D343638642D383766382D3461643264623938386236387D2C7B34333231393431643634666662323537633763346666383932346138346364317D2C7B323031332D30362D32322030383A33353A33337D2C7B312E332E327D2C7B65706F636B65747D2C7B756E6B6E6F776E7D"

    rs = getapi(url)
    
    items = []
    
    for item in rs["obj"]:
        
        d = {}
        
        d["title"] = item["dirname"]
        
        if "list" in item:
    
            lis = []
            
            for li in item["list"]:
            
                i = {}
            
                i["title"] = li["dirname"]
            
                i["action"] = {"name":"url","url":"product","m": "downloadProductItemDetail","dirID":li["id"],"pdiId":li["productid"]}
            
                lis.append(i)
            
            d["items"] = lis
        
        else:
        
            d["action"] = {"name":"url","url":"product","m": "downloadProductItemDetail","dirID":item["id"],"pdiId":item["productid"]}
        
        items.append(d)

    data = {"view":"TreeView","items":items}
    
    js = json.dumps(data,sort_keys=True,indent=4)
    
    f = file("./"+to+"/catalog.json","w")
    f.write(js)
    f.close()
            
    print "\ngen "+to+" OK\n"


genCatalog(6,"guide")
genCatalog(5,"medical")
genCatalog(3,"check")
genCatalog(4,"vectortable")
genCatalog(2,"caculator")

