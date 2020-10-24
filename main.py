import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from email.mime.image import MIMEImage

import sys

import mysql.connector
import requests
from bs4 import BeautifulSoup
import datetime








def sendMail():
    
    try:

        gun = datetime.datetime.now().strftime("%A")

        if gun == "Saturday" or gun == "Sunday":
            hafta = "(Haftasonu)"
        else:
            hafta = ""

        url = "http://bigpara.hurriyet.com.tr/doviz/"

        html = requests.get(url).content
        soup = BeautifulSoup(html, "html.parser")
        # list = soup.find("table",{"class":"table table-white table-market"}).find_all("em")[7]

        dolar_alis = soup.find_all("li",{"class":"cell015"})[3]
        dolar_satis = soup.find_all("li",{"class":"cell015"})[4]

        euro_alis = soup.find_all("li",{"class":"cell015"})[6]
        euro_satis = soup.find_all("li",{"class":"cell015"})[7]

        sterlin_alis =soup.find_all("li",{"class":"cell015"})[9]
        sterlin_satis =soup.find_all("li",{"class":"cell015"})[10]


        altin_url = "http://bigpara.hurriyet.com.tr/altin/"

        html_altin = requests.get(altin_url).content
        soup_altin = BeautifulSoup(html_altin, "html.parser")

        altin_alis = soup_altin.find_all("li",{"class":"cell009"})[4]
        altin_satis = soup_altin.find_all("li",{"class":"cell009"})[5]

        ons_alis = soup_altin.find_all("li",{"class":"cell009"})[12]
        ons_satis = soup_altin.find_all("li",{"class":"cell009"})[13]

        weekday = ["a","b","c","d","e","g","k"]
        weekday[6] = "Pazar"
        weekday[0] = "Pazartesi"
        weekday[1] = "Salı"
        weekday[2] = "Çarşamba"
        weekday[3] = "Perşembe"
        weekday[4] = "Cuma"
        weekday[5] = "Cumartesi"
        day = weekday[datetime.datetime.today().weekday()]
        date1 = datetime.datetime.now().strftime("%x") + " " + day
        
        mail = smtplib.SMTP("smtp.live.com",587)
        mail.ehlo()
        mail.starttls()
        mail.login("Mail", "Password")

        mesaj = MIMEMultipart()
        mesaj["From"] = "From"           # Gönderen
        mesaj["To"] = "To"          # Alıcı
        mesaj["Subject"] = f"Döviz Kurları {hafta} "    # Konusu

        html = """\
        <html>
        <head>

            <title>Russ Email</title>
            <style type="text/css">
             a {color: #d80a3e;}
             body, #header h1, #header h2, p {margin: 0; padding: 0;}
             #main {border: 1px solid #cfcece;}
             img {display: block;}
             #top-message p, #bottom p {color: #3f4042; font-size: 12px;     font-family: Arial, Helvetica, sans-serif; }
             #header h1 {color: #ffffff !important; font-family: "Lucida     Grande", sans-serif; font-size: 24px; margin-bottom:  0!important;     padding-bottom: 0; }
             #header p {color: #ffffff !important; font-family: "Lucida  Grande",   "Lucida Sans", "Lucida Sans Unicode", sans-serif;   font-size: 12px;    }
             h5 {margin: 0 0 0.8em 0;}
               h5 {font-size: 18px; color: #444444 !important;   font-family:    Arial, Helvetica, sans-serif; }
             p {font-size: 12px; color: #444444 !important; font-family:   "Lucida   Grande", "Lucida Sans", "Lucida Sans Unicode",  sans-serif;    line-height: 1.5;}
             #dovizler li{list-style-type:none; text-align: left; font-family: 'Source Sans Pro', sans-serif; padding-left: 16%;font-weight: bold;}
             #alis li{list-style-type:none; text-align: center; font-family: 'Source Sans Pro', sans-serif;color: #808080;}
             li{border-bottom: 1px solid #e7e7e7; padding: 4%;}
             #dolar{border-top: 1px solid #e7e7e7;}
             #satis li{list-style-type:none; text-align: center; font-family: 'Source Sans Pro', sans-serif;color: #808080;}
             td{
               list-style: none;
             }
             li{
              border-bottom:none;



             }
              ul{
                list-style-type:none;
                padding-inline-start: none !important;
              }
              button{
                margin-top: 5px;
                width: 150px;
                background-color: lightblue;
                border: 1px solid #f2f2f2;
                border-radius: 10px;
                
              }
              button:focus{
                outline:none;
              }
              button:hover{
                background-color: rgb(152, 191, 204);
              }
            </style>
         </head>
         <body>
        """
        html2= f"""

               <table id="main" width="600" align="center" cellpadding="0" cellspacing="15" bgcolor="ffffff">
                 <thead >
                    <tr>
                        <td>
                          <table id="header" cellspacing="0" align="center" bgcolor="#8fb3e9">
                            <tr>
                              <td width="600" align="center" height="50"     bgcolor="#036647"><h1 >Döviz Kurları</h1></td>
                            </tr>
                            <tr>
                              <td width="570"  bgcolor="#036647" ><p align="right" font-weight="bold" id="date">{date1}</p></td>
                            </tr>
                          </table>
                        </td>
                      </tr>
                 </thead>


             </table>
             <table id="main" class="table" width="600" align="center" cellpadding="0" cellspacing="15" bgcolor="ffffff" border= 1px solid #cfcece border-collapse="collapse"   border-top="none !important" >
                <thead class="thead-dark">
                  <tr>

                    <th style="padding:3%;" scope="col">DÖVİZ</th>
                    <th scope="col" style="text-align: center;">ALIŞ</th>
                    <th scope="col">SATIŞ</th>
                  </tr>
                </thead>
                <tbody >
                  <tr>


                    <td  style="text-align: center; padding:3%;">Dolar</td>
                    <td style="text-align: center;padding:3%;">{dolar_alis.text}</td>
                    <td  style="text-align: center;padding:3%;">{dolar_satis.text}</td>
                  </tr>
                  <tr>

                    <td  style="text-align: center;padding:3%;">Euro</td>
                    <td style="text-align: center;padding:3%;">{euro_alis.text}</td>
                    <td style="text-align: center;padding:3%;">{euro_satis.text}</td>
                  </tr>
                  <tr>

                    <td style="text-align: center;padding:3%;">Sterlin</td>
                    <td style="text-align: center;padding:3%;">{sterlin_alis.text}</td>
                    <td style="text-align: center;padding:3%;">{sterlin_satis.text}</td>
                  </tr>
                  <tr>

                    <td style="text-align: center; padding:3%;">Gram Altın</td>
                    <td style="text-align: center;padding:3%;">{altin_alis.text}</td>
                    <td style="text-align: center;padding:3%;">{altin_satis.text}</td>
                  </tr>
                  <tr>
                    <td style="text-align: center;padding:3%;">Ons Altın</td>
                    <td style="text-align: center;padding:3%;">{ons_alis.text}</td>
                    <td style="text-align: center;padding:3%;">{ons_satis.text}</td>
                  </tr>

                </tbody>

              </table>
              <table id="bottom" cellpadding="20" cellspacing="0" width="600"   align="center">
                <tr>
                  <td align="center">
                    <p>Altın verileri Kuveyttürk aracılığıyla, diğer döviz verileri ise Hürriyet aracılığıyla sağlanmaktadır.</p>
                    <p><a href="#" >Hürriyet</a> | <a href="http://bigpara.hurriyet.com.tr/doviz/" target="_blank" id="forex">Forex</a> | <a href="https://www.kuveytturk.com.tr/   finans-portali/" target="_blank" id="kuveyt">Kuveyttürk</a></p>
                    <button id="buton" onclick="" type="button">Like it</button>
                  </td>

                </tr>
              </table><!-- top message -->
            </td></tr></table>

         </body>
         </html>
        """
        htmlresult = html + html2
        body_html = MIMEText(htmlresult, "html")  
        mesaj.attach(body_html)


        # fp = open('dist/altinkuru.png', 'rb')
        # msgImage = MIMEImage(fp.read())
        # fp.close()
        # msgImage.add_header('Content-ID', '<image1>')

        # mesaj.attach(msgImage)

        mail.sendmail(mesaj["From"], mesaj["To"], mesaj.as_string())
        print("Mail başarılı bir şekilde gönderildi.")
        mail.close()

 
    except:
        print("Hata:", sys.exc_info()[0])





sendMail()
