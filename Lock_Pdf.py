import pikepdf

old_pdf=pikepdf.Pdf.open("example.pdf")
lock=pikepdf.Permissions(extract=False)

old_pdf.save("test.pdf",
                    encryption=pikepdf.Encryption(
                        user="junead449",
                        owner="Chaudhary junead",
                        allow=lock))
                        #user Variable is used as password that we set to our pdf