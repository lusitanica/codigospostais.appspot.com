import json

from string import split

import webapp2 

class CP4Handler(webapp2.RequestHandler):

  def get(self):
    try:
      codigo = self.request.get('codigo')
      callback = self.request.get('callback')
      codigo = str(codigo)

      arquivo = open("cp4.txt")
      cp4 = arquivo.readlines()
      arquivo.close()

      for i in range(0,len(cp4)):
        temp = split(cp4[i],",")
        if (codigo==temp[0]):
          latitude = temp[2]
          longitude = temp[1]
          break
        
      result = {'cp4': codigo , 'latitude': latitude , 'longitude': longitude}
      self.response.headers['Content-Type'] = 'application/json'
      if callback:
        self.response.out.write(callback + '(' + json.dumps(result) + ')')
      else:
        self.response.out.write(json.dumps(result))
    except:
      result={"status":{"message":"missing or invalid parameter."}}
      self.response.headers['Content-Type'] = 'application/json'
      self.response.out.write(json.dumps(result))

app = webapp2.WSGIApplication([('/cp4', CP4Handler)])

