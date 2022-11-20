def savings(gross_pay, tax_rate, expenses):
    ltx = gross_pay * (1 - tax_rate) // 1  # deduct tax rate from gross pay, round down via floor division
    thp = ltx - expenses  # ltx less expenses

    return thp

def material_waste(total_material, material_units, num_jobs, job_consumption):
    mc = num_jobs * job_consumption  # total materials consumed
    wm = total_material - mc  # total material less mc

    return str(wm) + material_units

def interest(principal, rate, periods):
    si = principal * (rate * periods)  # calculation for simple interest
    fv = principal * si  # obtain final value

    return fv

def body_mass_index(weight, height):
    wm = weight * 0.45359237  # convert pounds to kilograms
    hfi = height[0] * 12  # convert foot to inches
    him = (height[1] + hfi) * 0.0254  # convert inches to meters
    bmi = wm / (him ** 2)  # bmi = kg / (m ^ 2)

    return bmi