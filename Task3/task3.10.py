minutes, price, vat_percent = map(float, input().split())

no_vat = minutes * price
vat_amount = no_vat * (vat_percent / 100)
total = no_vat + vat_amount

print(f"без ПДВ: {no_vat:.2f}")
print(f"ПДВ:     {vat_amount:.2f}")
print(f"разом:   {total:.2f}")