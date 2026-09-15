from pyscript import document, display

def placeOrder(e):

    prod1 = document.getElementById("LMXM4")
    prod2 = document.getElementById("LMXM3S")
    prod3 = document.getElementById("RBV3")
    prod4 = document.getElementById("CA5400")
    prod5 = document.getElementById("TV380")
    prod6 = document.getElementById("FDT")

    items = ""
    if prod1.checked: items += "Logitech MX Master 4<br>"
    if prod2.checked: items += "Logitech MX Master 3S<br>"
    if prod3.checked: items += "Razer Basilisk V3<br>"
    if prod4.checked: items += "Corsair Air 5400<br>"
    if prod5.checked: items += "Thermaltake View 380<br>"
    if prod6.checked: items += "Fractal Design Terra<br>"

    subtotal = (

    (float(prod1.value) if prod1.checked else 0.0) + 
    (float(prod2.value) if prod2.checked else 0.0) + 
    (float(prod3.value) if prod3.checked else 0.0) + 
    (float(prod4.value) if prod4.checked else 0.0) + 
    (float(prod5.value) if prod5.checked else 0.0) + 
    (float(prod6.value) if prod6.checked else 0.0)

    )

    textOut = f"""
    -------- reciept --------<br>
    {items if items else "no items selected<br>"}
    -------------------------<br>
    subtotal: ₱{subtotal}<br>
    vat: +12%<br>
    -------------------------<br>
    total: ₱{subtotal + (subtotal * 0.12)}
    """
    
    document.getElementById("textOut").innerHTML = textOut