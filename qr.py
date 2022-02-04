from textwrap import fill
import qrcode
import image

qr = qrcode.QRCode(
    version= 15, 
    box_size= 10,
    border= 5 
)

data= ""  #pass in the url of your data, or whatever you wish to create a qr code for. 
qr.add_data(data)

qr.make(fit= True)
img = qr.make_image(fill = "black", back_color = "white")
img.save("") #pass in the desired name of the generated qr