#import qrcode, and image
import qrcode
import image

#set the properties of the qrcode
qr = qrcode.QRCode(
    version= 15,
    box_size= 10,
    border= 5
)

#pass in the data for which you want to create the code

data  = ""
qr.add_data(data)

qr.make(fit= True)
img = qr.make_image(fill = "black", back_color = "white")
qr.make_image(img)
qr.save("") #pass in the name of the generated qr. 