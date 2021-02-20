import json

from string import split

import webapp2 

class CP7Handler(webapp2.RequestHandler):

  def get(self):
    try:
      codigo = self.request.get('codigo')
      callback = self.request.get('callback')
      codigo = str(codigo)

      cod1 = open("primeiros.txt")
      first = cod1.readlines()
      cod1.close()

      cod2 = open("segundos.txt")
      second = cod2.readlines()
      cod2.close()

      for i in range(0,len(second)):
        tempa = split(second[i],",")
        testea = tempa[0]
        if (testea==codigo):
          first = []
          second = []
          desc2 = open("descb.txt")
          linha = desc2.readlines()
          desc2.close()
          colunas = split(linha[i],",")
          localidade = colunas[0]
          arteria = colunas[1]
          local = colunas[2]
          troco = colunas[3]
          break
        tempb = split(first[i],",")
        testeb = tempb[0]
        if (testeb==codigo):
          first = []
          second = []          
          desc1 = open("desca.txt")
          linha = desc1.readlines()
          desc1.close()
          colunas = split(linha[i],",")
          localidade = colunas[0]
          arteria = colunas[1]
          local = colunas[2]
          troco = colunas[3]
          break
        
      result = {'cp7': codigo , 'localidade': localidade , 'arteria': arteria , 'local ou zona': local , 'troco': troco}
      self.response.headers['Content-Type'] = 'application/json'
      if callback:
        self.response.out.write(callback + '(' + json.dumps(result) + ')')
      else:
        self.response.out.write(json.dumps(result))
    except:
      result={"status":{"message":"missing or invalid parameter."}}
      self.response.headers['Content-Type'] = 'application/json'
      self.response.out.write(json.dumps(result))

app = webapp2.WSGIApplication([('/cp7', CP7Handler)])

